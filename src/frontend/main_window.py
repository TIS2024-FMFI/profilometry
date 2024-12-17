# main_window.py
import tkinter as tk
from tkinter import ttk
import sys
import os

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
        self.actual_project = actual_project
        self.setup_window()
        self.setup_styles()
        self.show_main_menu()

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
        self.create_logo(logo_frame)

        # Button section
        button_frame = tk.Frame(self.current_frame, bg=WINDOW_CONFIG['bg_color'])
        button_frame.pack(pady=30)

        # Add main menu buttons
        self.create_main_buttons(button_frame)

    def create_logo(self, parent):
        """Create application logo"""
        logo_size = 150
        canvas = tk.Canvas(parent, width=logo_size, height=logo_size,
                           bg=WINDOW_CONFIG['bg_color'], highlightthickness=0)
        canvas.pack()

        # Draw the logo on the canvas
        self._draw_logo(canvas, logo_size)

    def _draw_logo(self, canvas, size):
        """Draw the logo with gradient circles and text"""
        center_x = size / 2
        center_y = size / 2

        # Gradient circle colors
        gradient_colors = ['#E8E8E8', '#E0E0E0', '#D8D8D8', '#D0D0D0', '#C8C8C8',
                           '#C0C0C0', '#B8B8B8', '#B0B0B0', '#A8A8A8', '#A0A0A0']

        # Draw concentric gradient circles
        for i, color in enumerate(gradient_colors):
            canvas.create_oval(10 + i, 10 + i, size - 10 - i, size - 10 - i,
                               fill=color, outline='')

        # Add horizontal lines and a central oval
        canvas.create_line(center_x - 30, center_y, center_x + 30, center_y,
                           fill='#2c3e50', width=3)
        canvas.create_line(center_x - 20, center_y - 20, center_x + 20, center_y - 20,
                           fill='#2c3e50', width=3)
        canvas.create_oval(center_x - 5, center_y - 5, center_x + 5, center_y + 5,
                           fill='#2c3e50')

        # Add text for the logo
        canvas.create_text(center_x + 1, center_y + 40 + 1,
                           text="LaserScan", fill='#7f8c8d',
                           font=('Arial', 12, 'bold'))
        canvas.create_text(center_x, center_y + 40, text="LaserScan",
                           fill='#2c3e50', font=('Arial', 12, 'bold'))

        canvas.create_text(center_x + 25 + 1, center_y - 40 + 1,
                           text="PRO", fill='#7f8c8d', font=('Arial', 8))
        canvas.create_text(center_x + 25, center_y - 40, text="PRO",
                           fill='#2c3e50', font=('Arial', 8))

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
        scanner.start_camera_view()
        
    def handle_view(self):
        """Handle the 'VIEW SCANS' button click"""
        self.clear_window()
        viewer = ViewerWindow('', self, self.actual_project)

    def handle_3d(self):
        """Handle the 'SHOW 3D MODEL' button click"""
        self.clear_window()
        model3d = Model3D('images/gombik_novy',self)
