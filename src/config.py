# config.py

# Application Window Configuration
# This section defines the general properties of the main application window.
WINDOW_CONFIG = {
    'title': 'LaserScan Pro',          # Title of the application window
    'width_ratio': 1,                  # Width as a fraction of the screen width
    'height_ratio': 1,                 # Height as a fraction of the screen height
    'min_width': 1280,                 # Minimum width of the application window (in pixels)
    'min_height': 720,                 # Minimum height of the application window (in pixels)
    'bg_color': '#F0F8FF',             # Background color of the window
    'state': 'zoomed',                 # Initial state of the window (e.g., zoomed to fullscreen)
}

# Line Detection Configuration
# These parameters control the behavior of the line detection algorithm.
LINE_DETECTION = {
    'significant_threshold_pixel': 80,  # Minimum pixel intensity to consider as part of the laser line
    'largest_points_threshold': 30,     # Max vertical deviation from the reference line to include a point
    'shift_constant': 0.01,             # Constant used for shifting 3D points in the Z-axis
}

# Button Configuration
# Defines properties for buttons used across the application.
BUTTON_CONFIG = {
    'default_scan_key': 'space',        # Default key binding for triggering a scan
    'bottom_strip_bg': '#eeeeee',       # Background color for the bottom strip in the scanner
    'bottom_strip_pady': 20,            # Padding for the bottom strip
}

# 3D Model Visualization Configuration
# Settings for visualizing 3D models using matplotlib.
MODEL_3D_CONFIG = {
    'figure_size': (8, 6),              # Size of the matplotlib figure (in inches)
    'figure_dpi': 100,                  # Resolution of the figure (dots per inch)
    'axis_labels': {                    # Axis labels for the 3D plot
        'x': 'X Axis',                  # Label for the X-axis
        'y': 'Y Axis',                  # Label for the Y-axis
        'z': 'Z Axis'                   # Label for the Z-axis
    },
}

# Labels and Messages Configuration
# Text and fonts used for labels and error messages in the application.
LABELS_MESSAGES = {
    'viewer_label': 'Viewing Images',                               # Default label for the viewer
    'viewer_label_font': ('Arial', 16),                             # Font for viewer labels
    'error_camera_access': 'Unable to access the camera.',          # Error message for camera issues
    'scan_feature_not_implemented': 'Scanning feature not implemented.',  # Placeholder text
    'info_viewing_images': 'Viewing images in folder: {}',          # Info message for viewer
}

# Camera Configuration
# Default settings for camera access and streaming behavior.
CAMERA_CONFIG = {
    'index': 0,                         # Default camera index (0 for primary camera)
    'stream_delay': 10,                 # Delay (in milliseconds) between frames for streaming
}
