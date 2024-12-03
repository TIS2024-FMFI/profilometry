import tkinter as tk
import numpy as np
np.set_printoptions(threshold=np.inf)
from tkinter import Menu, messagebox
import cv2 as cv
from config import WINDOW_CONFIG
# import matplotlib.pyplot as plt
# from scipy.spatial import Delaunay
# import trimesh
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection



class Model3D:
    def __init__(self, path, root):
        self.root = root
        self.path = path
        from finding_line import LineDetection
        self.all_points = LineDetection.get_all_points()
        self.create_menu()
        self.setup_window()

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
        lbl = tk.Label(self.root.root, text="3D model", font=('Arial 14')) 
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

    # def vytvor_jeden_zoznam(self,z):
    #     the_zoznam = self.all_points[0]
    #     for zoznam in self.all_points:
    #         if(len(the_zoznam) == 0):
    #             if(len(zoznam) > 1):
    #                 the_zoznam = zoznam
    #         if(len(zoznam) > 1):
    #             the_zoznam = np.concatenate((the_zoznam, zoznam), axis=0)
    #     print(the_zoznam)
    #     return the_zoznam
    
    # def vytvor_poly_siet(self):
    #     zoznam = self.vytvor_jeden_zoznam()
    #     if(len(zoznam) > 1):
    #         tri = Delaunay(zoznam[:,:2])
    #         faces = tri.simplices #indexy trojuholnikov
    #         mesh = trimesh.Trimesh(vertices=zoznam, faces=faces)
    #         mesh.export('output_mesh.obj')
    #         print('Exported to output_mesh.obj')
    #         fig = plt.figure()
    #         ax = fig.add_subplot(111, projection='3d')
    #         ax.add_collection3d(
    #             Poly3DCollection(mesh.triangles, facecolors='skyblue', linewidths=1, edgecolors='black'))
    #         ax.set_xlim([zoznam[:, 0].min(), zoznam[:, 0].max()])
    #         ax.set_ylim([zoznam[:, 1].min(), zoznam[:, 1].max()])
    #         ax.set_zlim([zoznam[:, 2].min(), zoznam[:, 2].max()])
    #         plt.show()
    
     # Placeholder methods for features under development
    
    def new_project(self): 
        messagebox.showinfo("New Project", "Feature coming soon!") 

    def open_project(self): 
        messagebox.showinfo("Open Project", "Feature coming soon!") 

    def save_project(self): 
        messagebox.showinfo("Save Project", "Feature coming soon!")

    def export_file(self, format): 
        messagebox.showinfo("Export", f"Export as {format} coming soon!")

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