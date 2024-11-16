import tkinter as tk
from tkinter import ttk
from config import WINDOW_CONFIG

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.setup_styles()
        self.create_widgets()
        
    def setup_styles(self):
        """Nastavenie štýlov pre aplikáciu"""
        style = ttk.Style()
        style.configure('Custom.TButton',
                       padding=(20, 15),  # Increased padding
                       font=('Arial', 12, 'bold'),  # Bolder, larger font
                       width=25)
        
        # Add hover effect style
        style.map('Custom.TButton',
                 background=[('active', '#2980b9')],
                 foreground=[('active', 'black')])
        
    def setup_window(self):
        """Nastavenie základných vlastností okna"""
        self.root.title(WINDOW_CONFIG['title'])
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        window_width = int(screen_width * WINDOW_CONFIG['width_ratio'])
        window_height = int(screen_height * WINDOW_CONFIG['height_ratio'])
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.configure(bg=WINDOW_CONFIG['bg_color'])
        
    def create_widgets(self):
        """Vytvorenie všetkých widgetov v hlavnom okne"""
        # Main container to center everything
        main_container = tk.Frame(self.root, bg=WINDOW_CONFIG['bg_color'])
        main_container.place(relx=0.5, rely=0.5, anchor='center')
        
        # Frame pre logo
        logo_frame = tk.Frame(main_container, bg=WINDOW_CONFIG['bg_color'])
        logo_frame.pack(pady=(0, 50))  # Add bottom padding
        
        # Logo
        self.create_logo(logo_frame)
        
        # Frame pre tlačidlá - now horizontal
        button_frame = tk.Frame(main_container, bg=WINDOW_CONFIG['bg_color'])
        button_frame.pack(pady=30)
        
        # Tlačidlá
        self.create_main_buttons(button_frame)
            
    def create_logo(self, parent):
        """Vytvorenie loga aplikácie"""
        logo_size = 150
        canvas = tk.Canvas(parent, width=logo_size, height=logo_size, 
                         bg=WINDOW_CONFIG['bg_color'], highlightthickness=0)
        canvas.pack()
        
        # Logo kresba
        self._draw_logo(canvas, logo_size)
        
    def _draw_logo(self, canvas, size):
        """Kreslenie loga"""
        center_x = size / 2
        center_y = size / 2
        
        # Kruh pozadia s gradient efektom
        gradient_colors = ['#E8E8E8', '#E0E0E0', '#D8D8D8', '#D0D0D0', '#C8C8C8',
                         '#C0C0C0', '#B8B8B8', '#B0B0B0', '#A8A8A8', '#A0A0A0']
        
        for i, color in enumerate(gradient_colors):
            canvas.create_oval(10 + i, 10 + i, size-10 - i, size-10 - i, 
                             fill=color, outline='')
        
        # Základné čiary loga
        canvas.create_line(center_x-30, center_y, center_x+30, center_y, 
                         fill='#2c3e50', width=3)
        canvas.create_line(center_x-20, center_y-20, center_x+20, center_y-20, 
                         fill='#2c3e50', width=3)
        canvas.create_oval(center_x-5, center_y-5, center_x+5, center_y+5, 
                         fill='#2c3e50')
        
        # Text with shadow effect
        shadow_offset = 1
        canvas.create_text(center_x + shadow_offset, center_y+40 + shadow_offset, 
                         text="LaserScan", fill='#7f8c8d',
                         font=('Arial', 12, 'bold'))
        canvas.create_text(center_x, center_y+40, text="LaserScan", 
                         fill='#2c3e50', font=('Arial', 12, 'bold'))
        
        canvas.create_text(center_x+25 + shadow_offset, center_y-40 + shadow_offset, 
                         text="PRO", fill='#7f8c8d', font=('Arial', 8))
        canvas.create_text(center_x+25, center_y-40, text="PRO", 
                         fill='#2c3e50', font=('Arial', 8))
    
    def create_main_buttons(self, parent):
        """Vytvorenie hlavných tlačidiel"""
        buttons = [
            ("SKENOVANIE OBRAZU", self.handle_scan),
            ("PREZERANIE SKENOV", self.handle_view),
            ("ZOBRAZENIE 3D MODELU", self.handle_3d)
        ]
        
        # Create buttons horizontally
        for text, command in buttons:
            button = self.create_styled_button(parent, text, command)
            button.pack(side=tk.LEFT, padx=15)  # Pack horizontally with spacing
            
    def create_styled_button(self, parent, text, command):
        """Vytvorenie štylizovaného tlačidla s vizuálnymi efektmi"""
        # Create a frame for the button to add shadow effect
        button_frame = tk.Frame(parent, bg=WINDOW_CONFIG['bg_color'])
        
        button = ttk.Button(button_frame, text=text, command=command, 
                          style='Custom.TButton')
        
        # Bind hover events for shadow effect
        def on_enter(e):
            button_frame.configure(bg='#2980b9')
        
        def on_leave(e):
            button_frame.configure(bg=WINDOW_CONFIG['bg_color'])
        
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
        
        button.pack(padx=2, pady=2)  # Small padding for shadow effect
        return button_frame

    # Event handlers remain the same
    def handle_scan(self):
        """Handler pre tlačidlo skenovania"""
        from backend.scanner import start_scanner
        start_scanner()
        
    def handle_view(self):
        """Handler pre tlačidlo prezerania"""
        from backend.viewer import start_viewer
        start_viewer()
        
    def handle_3d(self):
        """Handler pre tlačidlo 3D zobrazenia"""
        from backend.model_3d import start_3d_view
        start_3d_view()