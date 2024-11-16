# main_window.py
import tkinter as tk
from tkinter import ttk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import WINDOW_CONFIG
from backend.scanner import Scanner

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.current_frame = None
        self.setup_window()
        self.setup_styles()
        self.show_main_menu()
        
    def setup_styles(self):
        """Setup styles for the application"""
        style = ttk.Style()
        style.configure('Custom.TButton',
                       padding=(20, 15),
                       font=('Arial', 12, 'bold'),
                       width=25)
        
        style.map('Custom.TButton',
                 background=[('active', '#2980b9')],
                 foreground=[('active', 'black')])
        
    def setup_window(self):
        """Setup basic window properties"""
        self.root.title(WINDOW_CONFIG['title'])
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        window_width = int(screen_width * WINDOW_CONFIG['width_ratio'])
        window_height = int(screen_height * WINDOW_CONFIG['height_ratio'])
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.configure(bg=WINDOW_CONFIG['bg_color'])

    def clear_window(self):
        """Clear current contents of the window"""
        if self.current_frame:
            self.current_frame.destroy()
            self.current_frame = None
        # Create a new frame after clearing
        self.current_frame = tk.Frame(self.root, bg=WINDOW_CONFIG['bg_color'])
        self.current_frame.pack(expand=True, fill='none')

    def show_main_menu(self):
        """Show the main menu interface"""
        self.clear_window()
        
        # Create main menu frame
        self.current_frame = tk.Frame(self.root, bg=WINDOW_CONFIG['bg_color'])
        self.current_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Logo frame
        logo_frame = tk.Frame(self.current_frame, bg=WINDOW_CONFIG['bg_color'])
        logo_frame.pack(pady=(0, 50))
        
        # Create logo
        self.create_logo(logo_frame)
        
        # Button frame
        button_frame = tk.Frame(self.current_frame, bg=WINDOW_CONFIG['bg_color'])
        button_frame.pack(pady=30)
        
        # Create main buttons
        self.create_main_buttons(button_frame)

    def create_logo(self, parent):
        """Create application logo"""
        logo_size = 150
        canvas = tk.Canvas(parent, width=logo_size, height=logo_size, 
                         bg=WINDOW_CONFIG['bg_color'], highlightthickness=0)
        canvas.pack()
        
        self._draw_logo(canvas, logo_size)
        
    def _draw_logo(self, canvas, size):
        """Draw the logo"""
        center_x = size / 2
        center_y = size / 2
        
        gradient_colors = ['#E8E8E8', '#E0E0E0', '#D8D8D8', '#D0D0D0', '#C8C8C8',
                         '#C0C0C0', '#B8B8B8', '#B0B0B0', '#A8A8A8', '#A0A0A0']
        
        for i, color in enumerate(gradient_colors):
            canvas.create_oval(10 + i, 10 + i, size-10 - i, size-10 - i, 
                             fill=color, outline='')
        
        canvas.create_line(center_x-30, center_y, center_x+30, center_y, 
                         fill='#2c3e50', width=3)
        canvas.create_line(center_x-20, center_y-20, center_x+20, center_y-20, 
                         fill='#2c3e50', width=3)
        canvas.create_oval(center_x-5, center_y-5, center_x+5, center_y+5, 
                         fill='#2c3e50')
        
        canvas.create_text(center_x + 1, center_y+40 + 1, 
                         text="LaserScan", fill='#7f8c8d',
                         font=('Arial', 12, 'bold'))
        canvas.create_text(center_x, center_y+40, text="LaserScan", 
                         fill='#2c3e50', font=('Arial', 12, 'bold'))
        
        canvas.create_text(center_x+25 + 1, center_y-40 + 1, 
                         text="PRO", fill='#7f8c8d', font=('Arial', 8))
        canvas.create_text(center_x+25, center_y-40, text="PRO", 
                         fill='#2c3e50', font=('Arial', 8))
    
    def create_main_buttons(self, parent):
        """Create main menu buttons"""
        buttons = [
            ("SCAN IMAGE", self.handle_scan),
            ("VIEW SCANS", self.handle_view),
            ("SHOW 3D MODEL", self.handle_3d)
        ]
        
        for text, command in buttons:
            button = self.create_styled_button(parent, text, command)
            button.pack(side=tk.LEFT, padx=15)
            
    def create_styled_button(self, parent, text, command):
        """Create a styled button with visual effects"""
        button_frame = tk.Frame(parent, bg=WINDOW_CONFIG['bg_color'])
        
        button = ttk.Button(button_frame, text=text, command=command, 
                          style='Custom.TButton')
        
        def on_enter(e):
            button_frame.configure(bg='#2980b9')
        
        def on_leave(e):
            button_frame.configure(bg=WINDOW_CONFIG['bg_color'])
        
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
        
        button.pack(padx=2, pady=2)
        return button_frame

    def handle_scan(self):
        """Handle scan button click"""
        self.clear_window()
        scanner = Scanner(self)
        scanner.start_camera_view()
       
        
    def handle_view(self):
        """Handle view button click"""
        from backend.viewer import start_viewer
        start_viewer()
        
    def handle_3d(self):
        """Handle 3D view button click"""
        from backend.model_3d import start_3d_view
        start_3d_view()