import tkinter as tk
from tkinter import ttk
from tkinter import Menu, messagebox, filedialog, ttk
from config import *
import os

class BaseWindow:
    def __init__(self, root):
        self.root = root
        self.current_frame = None
        self.setup_styles()

    def create_menu(self):
        """Setup the menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.destroy)

        # Override in subclasses for additional menus
    
    # Open an existing project directory
    def open_project(self):
        """Main method to open a project directory."""
        folder_path = self.select_folder()
        if folder_path:
            self.handle_open_project(folder_path)

    def select_folder(self):
        """Prompt user to select a folder."""
        return filedialog.askdirectory(title="Select Folder")

    def handle_open_project(self, folder_path):
        """Handle the folder selection and basic processing."""
        self.path = folder_path
        self.initialize_folder_processing(folder_path)

    def initialize_folder_processing(self, folder_path):
        """Placeholder for subclass-specific processing."""
        pass


    def new_project(self): messagebox.showinfo("New Project", "Feature coming soon!")
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