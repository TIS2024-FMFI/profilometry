# main_window.py
import tkinter as tk
from tkinter import ttk
import sys
import os
import cv2
from PIL import Image, ImageDraw, ImageTk

# Add the parent directory to the system path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import WINDOW_CONFIG
from frontend.scanner import Scanner
from frontend.viewer import ViewerWindow
from frontend.model_3d import Model3D
from frontend.base_window import BaseWindow

class MainWindow(BaseWindow):
    def __init__(self, root, actual_project = None):
        self.root = root
        self.current_frame = None

        self.setup_window()
        self.setup_styles()
        self.show_main_menu()
        self.initialize_camera()

        self.actual_project = actual_project or self.load_last_project()

    def setup_styles(self):
        """Setup custom styles for the buttons in the application"""
        style = ttk.Style()
        style.configure('Custom.TButton',
                        padding=(20, 15),
                        font=('Arial', 12, 'bold'),
                        width=25)

        # Style mapping for button hover effects
        style.map('Custom.TButton',
                  background=[('active', '#2980b9')],
                  foreground=[('active', 'black')])

    def initialize_camera(self):
        """Initialize the camera and reset its settings to default."""
        try:
            self.cap = cv2.VideoCapture(0)
            if self.cap.isOpened():
                # Reset camera settings to default values
                self.cap.set(cv2.CAP_PROP_BRIGHTNESS, -1)  # Default brightness
                self.cap.set(cv2.CAP_PROP_CONTRAST, -1)    # Default contrast
                self.cap.set(cv2.CAP_PROP_SATURATION, -1) # Default saturation
                self.cap.set(cv2.CAP_PROP_GAIN, -1)       # Default gain (if applicable)
                print("Camera initialized with original default settings.")
            else:
                print("Failed to access the camera.")
        except Exception as e:
            print(f"Error initializing camera: {e}")

    def setup_window(self):
        """Setup basic window properties such as size, title, and background"""
        self.root.title(WINDOW_CONFIG['title'])
        self.root.state('zoomed')  # Maximize the window
        self.root.resizable(True, True)

        # Get screen dimensions and calculate window size and position
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = int(screen_width * WINDOW_CONFIG['width_ratio'])
        window_height = int(screen_height * WINDOW_CONFIG['height_ratio'])

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the window geometry and background color
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.configure(bg=WINDOW_CONFIG['bg_color'])

    def clear_window(self):
        """Clear current frame content from the window"""
        if self.current_frame:
            self.current_frame.destroy()
            self.current_frame = None

        # Create a new blank frame after clearing the window
        self.current_frame = tk.Frame(self.root, bg=WINDOW_CONFIG['bg_color'])
        self.current_frame.pack(expand=True, fill='none')

    def show_main_menu(self, actual_project = None):
        """Display the main menu interface with logo and buttons"""
        self.clear_window()
        self.actual_project = actual_project
        # Main menu frame
        self.current_frame = tk.Frame(self.root, bg=WINDOW_CONFIG['bg_color'])
        self.current_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Logo section
        logo_frame = tk.Frame(self.current_frame, bg=WINDOW_CONFIG['bg_color'])
        logo_frame.pack(pady=(0, 50))

        # Add the logo
        logo_img = self.create_logo(logo_frame)
        self.root.wm_iconphoto(False, logo_img)

        # Button section
        button_frame = tk.Frame(self.current_frame, bg=WINDOW_CONFIG['bg_color'])
        button_frame.pack(pady=30)

        # Add main menu buttons
        self.create_main_buttons(button_frame)

    def create_logo(self, parent):
        logo_size = 150
        canvas = tk.Canvas(parent, width=logo_size * 1.4, height=logo_size * 1.4,
                           bg='#E8E8E8', highlightthickness=0)
        canvas.pack()

        return self.draw_logo(canvas, logo_size * 1.4)

    def draw_logo(self, canvas, size):
        center_x = size / 2
        center_y = size / 2

        image = Image.new("RGBA", (int(size), int(size)), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        base_color = '#FF8A3C'
        components_color = "#1E2E3F"
        draw.ellipse([1, 1, size-1, size-1], fill=base_color)
    
        draw.line((center_x - 70, center_y, center_x + 70, center_y), fill=components_color, width=10)
        draw.line((center_x - 55, center_y - 40, center_x + 55, center_y - 40), fill=components_color, width=10)
        r = 12
        draw.ellipse((center_x - r, center_y - r, center_x + r, center_y + r), fill=components_color, outline=(0, 0, 0, 255), width=2)

        logo_img = ImageTk.PhotoImage(image)
        canvas.create_image(size // 2, size // 2, anchor=tk.CENTER, image=logo_img)
        canvas.image = logo_img

        canvas.create_text(center_x, center_y + 50, text="LaserScan",
                        fill=components_color, font=('Arial', 20, 'bold'))

        canvas.configure(bg=WINDOW_CONFIG['bg_color'])

        return logo_img

    def create_main_buttons(self, parent):
        """Create the main menu buttons with respective actions"""
        buttons = [
            ("SCAN IMAGE", self.handle_scan),
            ("VIEW SCANS", self.handle_view),
            ("SHOW 3D MODEL", self.handle_3d)
        ]

        # Create and pack buttons
        for text, command in buttons:
            button = self.create_styled_button(parent, text, command)
            button.pack(side=tk.LEFT, padx=15)

    def create_styled_button(self, parent, text, command):
        """Create a styled button with hover effects"""
        button_frame = tk.Frame(parent, bg=WINDOW_CONFIG['bg_color'])

        # Create the button with custom style
        button = ttk.Button(button_frame, text=text, command=command,
                            style='Custom.TButton')

        # Add hover effects
        def on_enter(e):
            button_frame.configure(bg='#2980b9')

        def on_leave(e):
            button_frame.configure(bg=WINDOW_CONFIG['bg_color'])

        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)

        button.pack(padx=2, pady=2)
        return button_frame

    def handle_scan(self):
        """Handle the 'SCAN IMAGE' button click"""
        self.clear_window()
        scanner = Scanner(self, self.actual_project)
        self.root.title(WINDOW_CONFIG['title'] + ' - Scan Image')
        scanner.start_camera_view()
        
    def handle_view(self):
        """Handle the 'VIEW SCANS' button click"""
        self.clear_window()
        self.root.title(WINDOW_CONFIG['title'] + ' - View Scans')
        viewer = ViewerWindow('', self, self.actual_project)

    def handle_3d(self):
        """Handle the 'SHOW 3D MODEL' button click"""
        self.root.title(WINDOW_CONFIG['title'] + ' - Show 3D Model')
        self.clear_window()
        model3d = Model3D('', self, self.actual_project)
