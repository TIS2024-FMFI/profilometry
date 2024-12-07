import cv2
from threading import Thread
import tkinter as tk
from tkinter import Menu, messagebox
from PIL import Image, ImageTk


class Scanner:
    def __init__(self, main_window):
        self.main_window = main_window
        self.cap = None
        self.canvas = None
        self.camera_index = 0
        self.running = False
        self.scan_key = "space"  # Default key for scanning

        # Setup menu and initialize interface
        self.create_menu()
        
        # Set window properties
        self.main_window.root.state("zoomed")  # Start maximized
        self.main_window.root.minsize(1280, 720)  # Minimum size
        self.main_window.root.bind("<space>", lambda event: self.start_scan())  # Bind default key
        self.setup_camera_view()
        self.create_bottom_strip()

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
        file_menu.add_command(label="Back to Main Menu", command=self.main_window.show_main_menu)
        file_menu.add_command(label="Exit", command=self.exit_application)

        # Main Menu
        main_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Main Menu", menu=main_menu)
        main_menu.add_command(label="Scan Profile", command=self.scan_profile)
        main_menu.add_command(label="Browse Scans", command=self.browse_scans)

        # Capture Menu
        settings = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Settings", menu=settings)
        settings.add_command(label="Choose a Camera", command=self.choose_camera)
        settings.add_command(label="Camera Settings", command=self.open_camera_settings)
        settings.add_command(label="Calibration", command=self.calibration)
        settings.add_command(label="Set Scan Key Bind", command=self.open_scan_key_dialog)

    def create_bottom_strip(self):
        """Add a strip at the bottom with a Scan button."""
        bottom_frame = tk.Frame(self.main_window.root, bg="#eeeeee", pady=20)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.scan_button = tk.Button(
            bottom_frame, text="Scan (Default: Space)", command=self.start_scan, font=("Arial", 12)
        )
        self.scan_button.pack()

    def open_scan_key_dialog(self):
        """Open a custom dialog to set the scan key."""
        dialog = tk.Toplevel(self.main_window.root)
        dialog.title("Set Scan Key Bind")
        dialog.geometry("300x150")
        dialog.resizable(False, False)

        label = tk.Label(dialog, text="Enter a single character for scanning:", font=("Arial", 12))
        label.pack(pady=10)

        entry = tk.Entry(dialog, font=("Arial", 14), width=5, justify="center")
        entry.pack(pady=5)

        def on_submit():
            key = entry.get().strip()
            if len(key) == 1 and key.isalnum():
                self.scan_key = key
                self.main_window.root.bind(f"<{key}>", lambda event: self.start_scan())
                self.scan_button.config(text=f"Scan (Current: {key})")
                messagebox.showinfo("Key Binding", f"Scan key set to '{key}'.")
                dialog.destroy()
            else:
                messagebox.showerror("Invalid Input", "Please enter a single alphanumeric character.")

        submit_button = tk.Button(dialog, text="Set Key", font=("Arial", 12), command=on_submit)
        submit_button.pack(pady=10)
    def start_camera_view(self):
        """Initialize the camera view."""
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Unable to access camera.")
            return

        self.start_stream()

    def setup_camera_view(self):
        """Setup the canvas to display the camera feed."""
        if not self.canvas:
            self.canvas = tk.Canvas(self.main_window.root, bg="black")
            self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        else:
            self.canvas.delete("all")

        # Ensure canvas dynamically resizes with a 16:9 aspect ratio
        self.main_window.root.bind("<Configure>", self.update_canvas_aspect_ratio)

    def update_canvas_aspect_ratio(self, event):
        """Update the canvas size to maintain a 16:9 aspect ratio."""
        if event.widget == self.main_window.root:
            width = event.width
            height = int(width / 16 * 9)
            if height > event.height:
                height = event.height
                width = int(height / 9 * 16)
            self.canvas.config(width=width, height=height)
            self.canvas.place(x=(event.width - width) // 2, y=(event.height - height) // 2)

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

            # Resize frame to maintain a 16:9 aspect ratio
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

    # Dummy placeholder methods for menu items
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
