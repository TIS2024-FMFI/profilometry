import tkinter as tk
import numpy as np
np.set_printoptions(threshold=np.inf)
from tkinter import Menu, messagebox
import cv2 as cv
import os
from config import WINDOW_CONFIG
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from stl import mesh
import trimesh
from scipy.spatial import Delaunay
from pygltflib import  Mesh as GLTFMesh, Node, Scene, Buffer, BufferView, Accessor
from frontend.base_window import BaseWindow


class Model3D(BaseWindow):
    def __init__(self, path, root, actual_project):
        self.root = root
        if actual_project != None:
            self.path = actual_project.project_dir
        else:
            self.path = path
        self.actual_project = actual_project
        if not os.path.exists(self.path):
            self.open_project()  
            self.actual_project = self.current_project 
            # print("open path "+self.path+ "open current project " + self.current_project.project_dir + "open actual project " + self.actual_project.project_dir)            path = self.actual_project.project_dir
        self.create_menu()
        self.setup_window()

    def point_cloud(self):
        """Reads 3D points from points.txt in the specified path and creates pointcloud for further processing."""
        file_path = f"{self.path}/points.txt"       
        # print("point cloud path " +self.path)
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

    def open_project_f(self):
            self.open_project()
            self.actual_project = self.current_project

    def create_menu(self):
        self.menubar = Menu(self.root.root)
        self.root.root.config(menu=self.menubar)

        # File menu
        file_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Project", command=self.new_project)
        file_menu.add_command(label="Open Project", command=self.open_project_f)
        file_menu.add_command(label="Save Project", command=self.save_project)
        export_menu = Menu(file_menu, tearoff=0)
        file_menu.add_cascade(label="Export", menu=export_menu)
        export_menu.add_command(label="STL", command=lambda: self.export_file("stl"))
        export_menu.add_command(label="OBJ", command=lambda: self.export_file("obj"))
        export_menu.add_command(label="GLTF", command=lambda: self.export_file("gltf"))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)

        # Main menu
        main_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Main Menu", menu=main_menu)
        main_menu.add_command(label="Scan Profile", command=self.scan_profile)
        main_menu.add_command(label= "View Scans", command=self.browse_scans)

    def setup_window(self):
        """Sets up the main window with toggle buttons for 3D Points and 3D Object."""
        title = self.path.split("\\")[-1]
        lbl = tk.Label(self.root.root, text="3D model "+title, font=('Arial 14')) 
        lbl.config(bg='white')
        lbl.place(x=550, y=50)

        self.figure = Figure(figsize=(10, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root.current_frame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)

        def show_3d_points():
            """Displays the 3D point cloud."""
            self.figure.clf()  # Clear the figure
            point_cloud = self.point_cloud()
            if point_cloud.size == 0:
                return
            ax = self.figure.add_subplot(111, projection='3d')
            ax.scatter(point_cloud[:, 0], point_cloud[:, 1], point_cloud[:, 2], c='black', s=1)
            ax.set_title("3D Points")
            ax.grid(False)
            ax.set_axis_off()
            self.canvas.draw()

        def show_3d_object():
            """Displays the smooth 3D object."""
            self.figure.clf()  
            point_cloud = self.point_cloud()
            if point_cloud.size == 0:
                return
            tri = Delaunay(point_cloud[:, :2])
            vertices = point_cloud
            faces = tri.simplices
            ax = self.figure.add_subplot(111, projection='3d')
            ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=faces,
                            cmap='viridis', edgecolor='none')
            ax.set_title("3D Object")
            ax.grid(False)
            ax.set_axis_off()
            self.canvas.draw()

        button_frame = tk.Frame(self.root.root, bg='white')
        button_frame.pack(fill='x', side='bottom', pady=10)

        # Back button
        def go_back():
            for widget in self.root.root.winfo_children():
                widget.destroy()

            from frontend.main_window import MainWindow
            MainWindow(self.root.root, self.actual_project)

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
        
        set_button(.13, .8, '3D Points', show_3d_points)
        set_button(.23, .8, '3D Object', show_3d_object)
        show_3d_points()
        set_button(.03,.8, 'Back', go_back)
        
        self.root.root.state('zoomed')  # Maximize the window
        self.root.root.configure(bg='white')
        self.root.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # Handle window close event   

    def export_file(self, format):
        if format in ["stl", "obj", "gltf"]:
            point_cloud = self.point_cloud()
            if point_cloud.size == 0:
                return 
            tri = Delaunay(point_cloud[:, :2])
            vertices = point_cloud
            faces = tri.simplices 
            mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
            mesh.export(f"{self.path}"+format, file_type=format)
            messagebox.showinfo("Exported", f"Model exported as {self.path}"+format)
        else:
            messagebox.showerror("Unsuported format", f"Could not export {self.path} as format {format}")