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
        self.camera_index = self.detect_connected_camera()
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
        file_menu.add_command(label="Back to Main Menu", command=self.back_to_main_menu)
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
        print()
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Unable to access camera.")
            return

        self.start_stream()
    def detect_connected_camera(self):
        """Detect if a specific camera is connected, otherwise default to index 0."""
        connected_camera_id = "USB\\VID_32E4&PID_9320&MI_00\\7&29e53795&0&0000"
        for index in range(10):  # Check up to 10 possible cameras
            cap = cv2.VideoCapture(index)
            if cap.isOpened():
                name = f"Camera {index}"  # Placeholder for camera identification logic
                if connected_camera_id in name:  # Replace with actual identification logic if needed
                    cap.release()
                    return index
                cap.release()
        return 0  # Default to the first camera if the specific one isn't found

    def choose_camera(self):
        """Open a pop-up window to choose a camera."""
        dialog = tk.Toplevel(self.main_window.root)
        dialog.title("Choose a Camera")
        dialog.geometry("400x300")
        dialog.resizable(False, False)

        label = tk.Label(dialog, text="Select a camera from the list:", font=("Arial", 12))
        label.pack(pady=10)

        camera_list = ttk.Treeview(dialog, columns=("Index", "Name"), show="headings")
        camera_list.heading("Index", text="Index")
        camera_list.heading("Name", text="Name")
        camera_list.column("Index", width=50, anchor="center")
        camera_list.column("Name", width=300, anchor="w")
        camera_list.pack(pady=10, fill=tk.BOTH, expand=True)

        connected_camera_id = "USB\\VID_32E4&PID_9320&MI_00\\7&29e53795&0&0000"

        # Populate the camera list
        preselect_index = None
        for index in range(10):
            cap = cv2.VideoCapture(index)
            if cap.isOpened():
                name = f"Camera {index}"
                # Add connected camera name if found
                if connected_camera_id in name:
                    name += " (Connected)"
                    preselect_index = index
                camera_list.insert("", "end", values=(index, name))
                cap.release()

        def on_select():
            selected = camera_list.focus()
            if not selected:
                messagebox.showerror("Selection Error", "Please select a camera.")
                return

            values = camera_list.item(selected, "values")
            self.camera_index = int(values[0])
            messagebox.showinfo("Camera Selected", f"Selected Camera: {values[1]}")
            dialog.destroy()

        if preselect_index is not None:
            for child in camera_list.get_children():
                if camera_list.item(child, "values")[0] == str(preselect_index):
                    camera_list.selection_set(child)
                    break

        select_button = tk.Button(dialog, text="Select", font=("Arial", 12), command=on_select)
        select_button.pack(pady=10)

        dialog.transient(self.main_window.root)
        dialog.grab_set()
        self.main_window.root.wait_window(dialog)

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
        """Continuous capture and display of camera images."""
        while self.running:
            try:
                # Check if the canvas still exists
                if not self.canvas or not self.canvas.winfo_exists():
                    break

                ret, frame = self.cap.read()
                if not ret:
                    break

                # Check if the main window is still active
                if not self.main_window.root.winfo_exists():
                    break

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Finding the dimensions of the canvas
                canvas_width = self.canvas.winfo_width()
                canvas_height = self.canvas.winfo_height()

                if canvas_width > 0 and canvas_height > 0:
                    frame = cv2.resize(frame, (canvas_width, canvas_height))

                    # Image conversion to Tkinter format
                    photo = self.convert_frame_to_image(frame)

                    # image display
                    if self.canvas and self.canvas.winfo_exists():
                        self.canvas.create_image(0, 0, anchor="nw", image=photo)
                        self.canvas.image = photo

            except Exception as e:
                print(f"Chyba v streame: {e}")
                break

        # Definite stop
        self.running = False
        if self.cap:
            self.cap.release()

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
    def back_to_main_menu(self):
        """Navigate back to the main menu."""
        # Stop stream
        self.running = False
        
        # Release the camera
        if self.cap:
            self.cap.release()
        
        # Unbind events
        self.main_window.root.unbind("<Configure>")
        
        # Vymazať všetky widgety
        for widget in self.main_window.root.winfo_children():
            widget.destroy()
        
        # Delete all widgets
        self.main_window.show_main_menu()

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
    def open_camera_settings(self): messagebox.showinfo("Camera Settings", "Feature coming soon!")
