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
        ld = LineDetection(path, path+ '_alg', 1, 'png')
        self.all_points = ld.get_all_points()
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