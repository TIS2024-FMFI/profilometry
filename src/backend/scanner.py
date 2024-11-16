# scanner.py
import cv2
from threading import Thread
import tkinter as tk
from tkinter import Menu, simpledialog


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
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_application)

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