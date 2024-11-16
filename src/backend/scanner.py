# scanner.py - Working in progress
import cv2
from threading import Thread
import tkinter as tk
from tkinter import Menu, simpledialog
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class Scanner:
    def __init__(self, main_window):
        self.main_window = main_window
        self.cap = None
        self.canvas = None
        self.camera_index = 0
        self.running = False

        # Setup menu and initialize interface
        self.create_menu()
        self.main_window.root.geometry("1440x810")
        self.main_window.root.minsize(640, 480)

    def create_menu(self):
        """Create the menu bar."""
        menubar = Menu(self.main_window.root)
        self.main_window.root.config(menu=menubar)

        # File menu
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Start Camera", command=self.start_camera_view)
        file_menu.add_command(label="Stop Camera", command=self.stop_stream)
        file_menu.add_command(label="New Project", command=self.new_project)
        file_menu.add_command(label="Open Project", command=self.open_project)
        file_menu.add_command(label="Save Project", command=self.save_project)
        export_menu = Menu(file_menu, tearoff=0)
        file_menu.add_cascade(label="Export", menu=export_menu)
        export_menu.add_command(label="STL", command=lambda: self.export_file("stl"))
        export_menu.add_command(label="OBJ", command=lambda: self.export_file("obj"))
        export_menu.add_command(label="GLTF", command=lambda: self.export_file("gltf"))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_application)

        # Main Menu
        main_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Main Menu", menu=main_menu)
        main_menu.add_command(label="Scan Profile", command=self.scan_profile)
        main_menu.add_command(label="Browse Scans", command=self.browse_scans)
        # Capture Menu
        capture_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Capture", menu=capture_menu)
        capture_menu.add_command(label="Choose a Camera", command=self.choose_camera)
        capture_menu.add_command(label="Camera Settings", command=self.open_camera_settings)  # Renamed method
        capture_menu.add_command(label="Calibration", command=self.calibration)

    def start_camera_view(self):
        """Initialize the camera view."""
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            print("Unable to access camera.")
            return

        self.setup_camera_view()
        self.start_stream()

    def setup_camera_view(self):
        """Setup the canvas to display the camera feed."""
        if not self.canvas:
            self.canvas = tk.Canvas(self.main_window.current_frame, bg="black")
            self.canvas.pack(fill=tk.BOTH, expand=True)  # Expand canvas to fill the whole window
        else:
            self.canvas.delete("all")

        # Ensure canvas dynamically resizes with the window
        self.main_window.current_frame.bind("<Configure>", self.update_canvas_size)

    def update_canvas_size(self, event):
        """Update the canvas size to match the resized window."""
        self.canvas.config(width=event.width, height=event.height)

    def start_stream(self):
        """Start streaming the camera feed."""
        self.running = True
        Thread(target=self.stream, daemon=True).start()

    def stream(self):
        """Continuously capture and display frames from the camera."""
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Resize frame to fit the canvas dimensions
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()

            if canvas_width > 0 and canvas_height > 0:
                frame = cv2.resize(frame, (canvas_width, canvas_height))

                # Convert frame to a format Tkinter can use
                photo = self.convert_frame_to_image(frame)

                # Display the image on the canvas
                self.canvas.create_image(0, 0, anchor="nw", image=photo)
                self.canvas.image = photo

    def convert_frame_to_image(self, frame):
        """Convert OpenCV frame to a format usable by Tkinter."""
        from PIL import Image, ImageTk
        img = Image.fromarray(frame)
        return ImageTk.PhotoImage(image=img)

    def stop_stream(self):
        """Stop streaming and release the camera."""
        self.running = False
        if self.cap:
            self.cap.release()
        if self.canvas:
            self.canvas.delete("all")

    def exit_application(self):
        """Exit the application."""
        self.stop_stream()
        self.main_window.root.destroy()
    def new_project(self): messagebox.showinfo("New Project", "Feature coming soon!")
    def open_project(self): messagebox.showinfo("Open Project", "Feature coming soon!")
    def save_project(self): messagebox.showinfo("Save Project", "Feature coming soon!")
    def export_file(self, format): messagebox.showinfo("Export", f"Export as {format} coming soon!")
    def scan_profile(self): messagebox.showinfo("Scan Profile", "Feature coming soon!")
    def browse_scans(self): messagebox.showinfo("Browse Scans", "Feature coming soon!")
    def calibration(self): messagebox.showinfo("Calibration", "Feature coming soon!")
    def start_scan(self): messagebox.showinfo("Start Scan", "Feature coming soon!")
    def stop_scan(self): messagebox.showinfo("Stop Scan", "Feature coming soon!")
    def save_scan(self): messagebox.showinfo("Save Scan", "Feature coming soon!")
    def choose_camera(self): messagebox.showinfo("Choose Camera", "Feature coming soon!")
    def open_camera_settings(self): messagebox.showinfo("Camera Settings", "Feature coming soon!")
