import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from config import WINDOW_CONFIG
import os
import threading

class ViewerWindow:
    def __init__(self, path, root ):
        self.root = root
        self.path = path
        self.pripona = 'png'  # File extension (e.g., png, jpg)
        self.setup_window()  # Initialize the main window layout
        self.create_menu()  # Create the menu bar
        if not self.check_needs_generation():  # Check if files need to be processed
            self.add_images()  # Add existing images
        else:
            self.use_algorithm(batch=False)  # Run the algorithm if needed

    # Check if the algorithm needs to generate processed files
    def check_needs_generation(self):
        files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        try:
            files_alg = [f for f in os.listdir(self.path + "_alg") if os.path.isfile(os.path.join(self.path + "_alg", f))]
        except:
            files_alg = []
            
        # If processed files exist and match the count of originals, no generation is needed
        if len(files_alg) > 0 and len(files) == len(files_alg):
            return False

        return True

    # Create the application menu bar
    def create_menu(self):
        self.menubar = tk.Menu(self.root.root)
        self.root.root.config(menu=self.menubar)

        # File menu
        file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Project", command=self.new_project)
        file_menu.add_command(label="Open Project", command=self.open_project)
        file_menu.add_command(label="Use Algorithm", command=self.use_algorithm)
        file_menu.add_command(label="Save Project", command=self.save_project)
        export_menu = tk.Menu(file_menu, tearoff=0)
        file_menu.add_cascade(label="Export", menu=export_menu)
        export_menu.add_command(label="STL", command=lambda: self.export_file("stl"))
        export_menu.add_command(label="OBJ", command=lambda: self.export_file("obj"))
        export_menu.add_command(label="GLTF", command=lambda: self.export_file("gltf"))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)

        # Disable unavailable menu options
        file_menu.entryconfig("New Project", state="disabled")
        file_menu.entryconfig("Save Project", state="disabled")

        # Main menu
        main_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Main Menu", menu=main_menu)
        main_menu.add_command(label="Scan Profile", command=self.scan_profile)
        main_menu.add_command(label="Browse Scans", command=self.browse_scans)

        # Capture menu
        capture_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Capture", menu=capture_menu)
        capture_menu.add_command(label="Calibration", command=self.calibration)
        
        # Disable unavailable capture options
        capture_menu.entryconfig("Calibration", state="disabled")

    # Set up the main window
    def setup_window(self):
        lbl = tk.Label(self.root.root, text="Scan List", font=('Arial 14')) 
        lbl.config(bg='white')
        lbl.place(x=200, y=150)

        # Back button
        def go_back():
            for widget in self.root.root.winfo_children():
                widget.destroy()

            from frontend.main_window import MainWindow
            MainWindow(self.root.root)

        button = tk.Button(self.root.root, text="Back", font=('Arial 14'), command=go_back)

        # Highlight button on hover
        def on_enter(e):
            button.configure(bg='#2980b9')

        def on_leave(e):
            button.configure(bg=WINDOW_CONFIG['bg_color'])

        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
        
        button.place(relx=.15, rely=.8)

        self.root.root.state('zoomed')  # Maximize the window
        self.root.root.configure(bg='white')
        self.root.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # Handle window close event

    # Handle window closing
    def on_closing(self):
        self.root.root.destroy()

    # Clear all images from the scrollable frame
    def clear_images(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

    # Add images to the scrollbar
    def add_to_scrollbar(self):
        first_image = None
        count = 0

        for filename in os.listdir(self.path):
            if filename.endswith("." + self.pripona):  # Check for correct file extension
                file_path = os.path.join(self.path, filename)
                if first_image is None:
                    first_image = str(count + 1) + "|" + file_path  # Store first image for preview

                label = tk.Label(self.scrollable_frame, text=str(count + 1) + '. ' + file_path, font=("Arial 14"))
                label.pack(padx=10, pady=10)
                label.config(bg="white")
                count += 1

                # Highlight label on hover
                def on_hover_enter(event, label):
                    label.config(bg="lightblue")

                def on_hover_leave(event, label):
                    label.config(bg="white")

                label.bind("<Enter>", lambda event, label=label: on_hover_enter(event, label))
                label.bind("<Leave>", lambda event, label=label: on_hover_leave(event, label))

                # Set up click event for each label
                label.bind("<Button-1>", lambda event, name=str(count) + '|' + file_path: self.on_item_click(name))

        if first_image:
            self.on_item_click(first_image)

    # Display preview and adjusted images on item click
    def on_item_click(self, photo):
        count, photo = photo.split('|')

        split_path = photo.split('\\')
        split_path[0] += '_alg\\'
        processed_image_path = split_path[0] + split_path[1]

        # Update labels for preview and adjusted images
        self.Scan1Prewlbl.config(text="Scan " + count + " Preview")
        self.Scan2Prewlbl.config(text="Scan " + count + " Adjusted")

        # Load and resize the original and adjusted images
        original_image = Image.open(photo).resize((300, 300))
        adjusted_image = Image.open(processed_image_path).resize((300, 300))
        original_photo_image = ImageTk.PhotoImage(original_image)
        adjusted_photo_image = ImageTk.PhotoImage(adjusted_image)

        # Update image labels
        self.image_labelPrew.config(image=original_photo_image)
        self.image_labelPrew.image = original_photo_image

        self.image_labelAlg.config(image=adjusted_photo_image)
        self.image_labelAlg.image = adjusted_photo_image
        
        # Add images to the UI and set up the scrollable frame
    def add_images(self):
        self.scrollFrame = tk.Frame(self.root.root, height=400, width=500)
        self.canvasScrollFrame = tk.Canvas(self.scrollFrame, height=400, width=500)

        # Add scrollbar to the frame
        self.scrollbar = tk.Scrollbar(self.scrollFrame, orient="vertical", command=self.canvasScrollFrame.yview)
        self.canvasScrollFrame.config(yscrollcommand=self.scrollbar.set)
        self.canvasScrollFrame.config(bg='white')
        self.scrollFrame.config(bg='white')
        self.scrollbar.config(bg='white')

        # Create a scrollable frame within the canvas
        self.scrollable_frame = tk.Frame(self.canvasScrollFrame)
        self.scrollable_frame.config(bg='white')

        # Add labels for preview sections
        self.Scan1Prewlbl = tk.Label(self.root.root, text="Scan 1 Preview", font=('Arial 14'))  # Original preview
        self.Scan1Prewlbl.place(x=700, y=200)

        self.Scan2Prewlbl = tk.Label(self.root.root, text="Scan 1 Adjusted", font=('Arial 14'))  # Adjusted image preview
        self.Scan2Prewlbl.place(x=700, y=500)

        # Place scrollable frame inside the canvas
        self.canvasScrollFrame.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Pack the scrollbar and canvas
        self.scrollbar.pack(side="right", fill="y")
        self.canvasScrollFrame.pack(side="left", fill="both", expand=True)
        self.scrollFrame.pack(side="left", padx=20, pady=0)

        # Add placeholders for preview images
        self.image_labelPrew = tk.Label(self.root.root)
        self.image_labelPrew.pack(padx=20, pady=40)

        self.image_labelAlg = tk.Label(self.root.root)
        self.image_labelAlg.pack(padx=20, pady=20)

        # Populate the scrollbar with image labels
        self.add_to_scrollbar()

        # Adjust the scroll region when the frame is resized
        def on_frame_configure(event):
            self.canvasScrollFrame.config(scrollregion=self.canvasScrollFrame.bbox("all"))

        self.scrollable_frame.bind("<Configure>", on_frame_configure)

    # Apply the algorithm to images
    def use_algorithm(self, batch=True):
        from finding_line import LineDetection
        os.makedirs(self.path + '_alg', exist_ok=True)  # Create directory for processed files
        processor = LineDetection(self.path, self.path + '_alg', 1, extension=self.pripona)

        if batch:
            # Apply the algorithm to all files in the folder
            processor.apply_to_folder()
        else:
            files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]

            # Create a progress window for batch processing
            progress_window = tk.Toplevel(self.root.root)
            progress_window.title("Processing Images")
            progress_window.geometry("400x150")
            tk.Label(progress_window, text="Processing images, please wait...", font=("Arial", 12)).pack(pady=10)

            # Progress bar for batch processing
            progress_var = tk.DoubleVar()
            progress_bar = ttk.Progressbar(progress_window, maximum=len(files), variable=progress_var)
            progress_bar.pack(padx=20, pady=20, fill="x")

            # Function to process images in a separate thread
            def process_images():
                for i, image_file in enumerate(files):
                    output_file = os.path.join(self.path, image_file)
                    try:
                        processor.apply_to_image(output_file)
                    except Exception as e:
                        print(f"Error processing {image_file}: {e}")
                        continue

                    # Update progress bar
                    progress_var.set(i + 1)
                    progress_window.update_idletasks()

                progress_window.destroy()

            # Start the processing in a new thread
            thread = threading.Thread(target=process_images)
            thread.start()

            # Check the thread status and update UI when finished
            def check_thread():
                if thread.is_alive():
                    self.root.root.after(100, check_thread)
                else:
                    self.add_images()

            check_thread()

    # Open an existing project directory
    def open_project(self):
        folder_path = filedialog.askdirectory(title="Select Folder")
        folder_path_alg = folder_path + '_alg'

        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        try:
            if not os.path.exists(folder_path_alg):
                files_alg = [f for f in os.listdir(folder_path_alg) if os.path.isfile(os.path.join(folder_path_alg, f))]
        except:
            files_alg = []

        # Determine file extension from the first file
        if files:
            first_file = files[0]
            extension = first_file.split('.')[-1]

        self.pripona = extension

        # Process files if necessary
        error = False
        if not os.path.exists(folder_path_alg) and len(files) != len(files_alg):
            os.makedirs(folder_path_alg, exist_ok=True)
            from finding_line import LineDetection
            processor = LineDetection(folder_path, folder_path_alg, 1, extension=extension)
            processor.apply_to_folder()

            files_alg = [f for f in os.listdir(folder_path_alg) if os.path.isfile(os.path.join(folder_path_alg, f))]
            if len(files) != len(files_alg):
                error = True

        if not error:
            self.path = folder_path
            self.clear_images()
            self.add_to_scrollbar()
        else:
            messagebox.showerror("Processing Error", "An error occurred during processing. Images cannot be displayed.")

    # Placeholder methods for features under development
    def new_project(self): 
        messagebox.showinfo("New Project", "Feature coming soon!") 

    def save_project(self): 
        messagebox.showinfo("Save Project", "Feature coming soon!")

    def export_file(self, format): 
        messagebox.showinfo("Export", f"Export as {format} coming soon!")

    def scan_profile(self): 
        messagebox.showinfo("Scan Profile", "Feature coming soon!")

    def browse_scans(self): 
        messagebox.showinfo("Browse Scans", "Feature coming soon!")

    def calibration(self): 
        messagebox.showinfo("Calibration", "Feature coming soon!")

    def start_scan(self): 
        messagebox.showinfo("Start Scan", "Feature coming soon!")

    def stop_scan(self): 
        messagebox.showinfo("Stop Scan", "Feature coming soon!")

    def save_scan(self): 
        messagebox.showinfo("Save Scan", "Feature coming soon!")
