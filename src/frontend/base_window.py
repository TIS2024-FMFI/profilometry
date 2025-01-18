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
                self.current_project = Project(project_name, base_dir=os.path.dirname(folder_path))
                self.current_project.open_project()
                self.current_project.create_scan_folders(folder_path+'/scans')
                self.initialize_folder_processing(folder_path)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open project: {e}")

    def initialize_folder_processing(self, folder_path):
        """Placeholder for subclass-specific processing."""
        pass

    def load_last_project(self):
        """Check and load the last opened project."""
        summary_path = LAST_PROJECT_FILE['name']

        # Check if the last project file exists
        if os.path.exists(summary_path):
            try:
                with open(summary_path, 'r') as file:
                    lines = file.readlines()
                    if len(lines) == 2:
                        project_dir = lines[0].strip()
                        project_name = lines[1].strip()

                        if os.path.exists(project_dir):
                            # Create a Project instance with the loaded name and path
                            print(os.path.dirname(project_dir.rstrip(os.path.dirname('/'))))
                            self.current_project = Project(project_name, base_dir=os.path.dirname(project_dir.rstrip(os.path.dirname('/'))))
                            messagebox.showinfo("Info", f"Loaded last project: {self.current_project.project_name}")
                            return self.current_project
                        else:
                            messagebox.showinfo("Info", "No valid last project found. Please create or open a project.")
                            return None
                    else:
                        messagebox.showinfo("Info", "No valid last project found. Please create or open a project.")
                        return None
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load the last project: {e}")
                return None
        else:
            messagebox.showinfo("Info", "No last project found. Please create or open a project.")
            return None

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
    def get_current_project(self):
        return self.current_project