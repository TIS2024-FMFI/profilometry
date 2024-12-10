import tkinter as tk
import numpy as np
np.set_printoptions(threshold=np.inf)
from tkinter import Menu, messagebox
import cv2 as cv
from config import WINDOW_CONFIG
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from stl import mesh
import trimesh
from pygltflib import GLTF2, Mesh as GLTFMesh, Node, Scene, Buffer, BufferView, Accessor



class Model3D:
    def __init__(self, path, root):
        self.root = root
        self.path = path
        self.create_menu()
        self.setup_window()
        self.show_3d()

    def point_cloud(self):
        file_path = f"{self.path+'_alg'}/points.txt"
        try:
            point_cloud = np.loadtxt(file_path, dtype=int)
            return point_cloud
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            messagebox.showerror("File Not Found", f"Could not find {file_path}")
            return np.empty((0, 3))
        except ValueError:
            print(f"Error: Invalid file format in {file_path}.")
            messagebox.showerror("Invalid File Format", f"{file_path} contains invalid data.")
            return np.empty((0, 3))
    
    def show_3d(self):
        point_cloud = self.point_cloud()
        if point_cloud.size == 0:
            return 
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(point_cloud[:, 0], point_cloud[:, 1], point_cloud[:, 2], c='blue', s=1)
        ax.grid(False)  
        ax.set_axis_off() 
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')
        canvas = FigureCanvasTkAgg(fig, master=self.root.current_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def create_menu(self):
        self.menubar = Menu(self.root.root)
        self.root.root.config(menu=self.menubar)

        # File menu
        file_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Project", command=self.new_project)
        file_menu.add_command(label="Open Project", command=self.open_project)
        file_menu.add_command(label="Save Project", command=self.save_project)
        export_menu = Menu(file_menu, tearoff=0)
        file_menu.add_cascade(label="Export", menu=export_menu)
        export_menu.add_command(label="STL", command=lambda: self.export_file("stl"))
        export_menu.add_command(label="OBJ", command=lambda: self.export_file("obj"))
        export_menu.add_command(label="GLTF", command=lambda: self.export_file("gltf"))
        file_menu.add_separator()
        # file_menu.add_command(label="Back to Main Menu", command=self.main_window.show_main_menu)
        file_menu.add_command(label="Exit", command=self.on_closing)

        # Main menu
        main_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Main Menu", menu=main_menu)
        main_menu.add_command(label="Scan Profile", command=self.scan_profile)
        main_menu.add_command(label= "View Scans", command=self.browse_scans)

    def setup_window(self):
        title = self.path.split('/')[-1]
        lbl = tk.Label(self.root.root, text="3D model "+title, font=('Arial 14')) 
        lbl.config(bg='white')
        lbl.place(x=550, y=50)

        # Back button
        def go_back():
            for widget in self.root.root.winfo_children():
                widget.destroy()

            from frontend.main_window import MainWindow
            MainWindow(self.root.root)

        # Highlight button on hover

        def set_button(relx, rely, text, command):
            button  = tk.Button(self.root.root, text=text, font=('Arial 14'), command=command)
            def on_enter(e):
                button.configure(bg='#2980b9')
            
            def on_leave(e):
                button.configure(bg=WINDOW_CONFIG['bg_color'])
                
                
            button.bind('<Enter>', on_enter)
            button.bind('<Leave>', on_leave)
            
            button.place(relx=relx, rely=rely)

        set_button(.013,.8, 'Back', go_back)
        
        self.root.root.state('zoomed')  # Maximize the window
        self.root.root.configure(bg='white')
        self.root.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # Handle window close event   

     # Placeholder methods for features under development
    
    def new_project(self): 
        messagebox.showinfo("New Project", "Feature coming soon!") 

    def open_project(self): 
        messagebox.showinfo("Open Project", "Feature coming soon!") 

    def save_project(self): 
        messagebox.showinfo("Save Project", "Feature coming soon!")

    def export_file(self, format): 
        point_cloud = self.point_cloud()
        if point_cloud.size == 0:
            messagebox.showerror("Error", "No file to export.")
            return

        output_file = f"{self.path+'_alg'}/exported_model.{format}"

        try:
            if format == "stl":
                self.export_stl(output_file, point_cloud)
            elif format == "obj":
                self.export_obj(output_file, point_cloud)
            elif format == "gltf":
                self.export_gltf(output_file, point_cloud)
            else:
                raise ValueError("Unsupported format.")
            messagebox.showinfo("Export Successful", f"Model exported as {output_file}.")
        except Exception as e:
            messagebox.showerror("Export Failed", f"Failed to export model: {e}")

    def export_stl(self, file_path, point_cloud):
        num_triangles = len(point_cloud) // 3
        triangles = point_cloud[:num_triangles * 3].reshape((num_triangles, 3, 3))
        stl_mesh = mesh.Mesh(np.zeros(triangles.shape[0], dtype=mesh.Mesh.dtype))
        for i, triangle in enumerate(triangles):
            stl_mesh.vectors[i] = triangle
        stl_mesh.save(file_path)

    def export_obj(self, file_path, point_cloud):
        try:
            if point_cloud.size % 3 != 0:
                point_cloud = point_cloud[:-(point_cloud.size % 3)] 
            point_cloud = point_cloud.reshape(-1, 3)
            mesh = trimesh.points.PointCloud(point_cloud)
            mesh.export(filename)
            print(f"Model exported to {filename}")
        except Exception as e:
            print(f"Failed to export model: {e}")

    def export_gltf(self, file_path, point_cloud):
        vertices = point_cloud.astype(np.float32).flatten().tobytes()
        buffer = Buffer(uri="data.bin", byteLength=len(vertices))
        buffer_view = BufferView(buffer=0, byteOffset=0, byteLength=len(vertices), target=34962) 
        accessor = Accessor(
            bufferView=0,
            byteOffset=0,
            componentType=5126, 
            count=len(point_cloud),
            type="VEC3",
            max=[float(x) for x in np.max(point_cloud, axis=0)],
            min=[float(x) for x in np.min(point_cloud, axis=0)],
        )
        gltf_mesh = GLTFMesh(primitives=[{"attributes": {"POSITION": 0}}])
        node = Node(mesh=0)
        scene = Scene(nodes=[0])
        gltf = GLTF2(
            buffers=[buffer],
            bufferViews=[buffer_view],
            accessors=[accessor],
            meshes=[gltf_mesh],
            nodes=[node],
            scenes=[scene],
            scene=0,
        )
        gltf.save(file_path)

    def scan_profile(self): 
        for widget in self.root.root.winfo_children():
            widget.destroy()
        from frontend.main_window import MainWindow
        w = MainWindow(self.root.root)
        w.handle_scan()

    def browse_scans(self):
        for widget in self.root.root.winfo_children():
            widget.destroy() 
        from frontend.main_window import MainWindow
        w = MainWindow(self.root.root)
        w.handle_view()
    
    def on_closing(self):
        self.root.root.destroy()