import tkinter as tk
from tkinter import ttk
from tkinter import Menu, messagebox, filedialog, ttk
from config import *
import os
from src.backend.project import Project

class BaseWindow:
    def __init__(self, root):
        self.root = root
        self.current_project = None
        self.current_frame = None

    def create_menu(self):
        """Setup the menu bar."""
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Project", command=self.new_project)
        file_menu.add_command(label="Open Project", command=self.open_project)
        file_menu.add_command(label="Exit", command=self.root.destroy)

        # Override in subclasses for additional menus
    
    def new_project(self):
        """Create a new project."""
        project_name = tk.simpledialog.askstring("Project Name", "Enter the new project name:")
        if project_name:
            try:
                self.current_project = Project(project_name)
                self.current_project.set_dir()
                self.current_project.create_project()
                messagebox.showinfo("Success", f"Project '{project_name}' created successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create project: {e}")

    # Open an existing project directory
    def open_project(self):
        """Main method to open a project directory."""
        folder_path = filedialog.askdirectory(title="Select Folder")
        if folder_path:
            try:
                project_name = os.path.basename(folder_path)
                self.current_project = Project(project_name, base_path=os.path.dirname(folder_path))
                self.current_project.open_project(folder_path)
                self.initialize_folder_processing(folder_path)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open project: {e}")

    def initialize_folder_processing(self, folder_path):
        """Placeholder for subclass-specific processing."""
        pass

    def save_project(self): messagebox.showinfo("Save Project", "Feature coming soon!")

    def export_file(self, format): messagebox.showinfo("Export", f"Export as {format} coming soon!")

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

    # Handle window closing
    def on_closing(self):
        self.root.root.destroy()