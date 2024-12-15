# config.py

# Window configuration
WINDOW_CONFIG = {
    'title': 'LaserScan Pro',  # Title of the main application window
    'width_ratio': 1,          # Ratio of the window width to the screen width
    'height_ratio': 1,         # Ratio of the window height to the screen height
    'bg_color': '#F0F8FF'      # Background color of the application window
}

# Button configuration
BUTTON_CONFIG = {
    'width': 20,               # Width of buttons in characters
    'padding': 10,             # Padding around buttons
    'font': ('Arial', 11)      # Font style for buttons
}

LINE_DETECTION = {
    'significant_threshold_pixel': 80,  # Minimum intensity to consider a pixel significant
    'largest_points_threshold': 30      # Maximum allowed deviation from the reference line
}