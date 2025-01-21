import cv2
from threading import Thread
import tkinter as tk
from tkinter import Menu, messagebox, ttk, filedialog, simpledialog
from PIL import Image, ImageTk
import os
import re
import json
from frontend.base_window import BaseWindow
from backend.finding_line import LineDetection
from config import CALIBRATION
from pygrabber.dshow_graph import FilterGraph

class Scanner(BaseWindow):
    def __init__(self, main_window, actual_project):
        self.main_window = main_window
        self.cap = None
        self.canvas = None
        self.camera_index = self.find_usb_devices_windows()
        self.running = False
        self.actual_project = actual_project
        self.scan_key = "space"  # Default key for scanning
        super().__init__(main_window.root)
        self.counter = 0
        self.shift = None
        self.start_position = None
        


        # Setup menu and initialize interface
        self.create_menu()
        
        # Set window properties
        self.main_window.root.state("zoomed")  # Start maximized
        self.main_window.root.minsize(1280, 720)  # Minimum size
        self.main_window.root.bind("<space>", lambda event: self.scan_profile())  # Bind default key
        self.setup_camera_view()
        self.create_bottom_strip()
        
    
    def new_project_f(self):
        self.new_project()
        self.actual_project = self.current_project
        raw_scans_path = os.path.join(self.actual_project.project_dir, "scans", "raw")
        self.shift = None
        self.start_position = None
        if os.path.isdir(raw_scans_path):
            self.initialize_counter(raw_scans_path) 
        self.display_message_in_bottom_strip_about_scan_position()


    def open_project_f(self):
        self.open_project()
        self.actual_project = self.current_project
        self.initialize_counter(os.path.join(self.actual_project.project_dir, "scans", "raw"))
        self.display_message_in_bottom_strip_about_scan_position()

    def get_movement_parameters(self):
        # Construct the path to the file
        folder_path = os.path.join(self.actual_project.project_dir, "movement_parameters")
        file_path = os.path.join(folder_path, "movement_view1.txt")
        
        # Check if folder and file exist
        if not os.path.exists(folder_path) or not os.path.exists(file_path):
            return False
        
        try:
            # Open and read the file
            with open(file_path, 'r') as file:
                content = file.read().strip()
                
            # Split content by comma and convert to numbers
            values = content.split(',')
            if len(values) != 2:
                return False
                
            # Convert to integers and remove whitespace
            param1 = int(values[0].strip())
            param2 = int(values[1].strip())
            
            return param1, param2
            
        except (ValueError, IOError):
            return False

    def create_menu(self):
        """Create the menu bar."""
        menubar = Menu(self.main_window.root)
        self.main_window.root.config(menu=menubar)

        # File menu
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Start Camera", command=self.start_camera_view)
        file_menu.add_command(label="Stop Camera", command=self.stop_stream)
        file_menu.add_command(label="New Project", command=self.new_project_f)
        file_menu.add_command(label="Open Project", command=self.open_project_f)
        export_menu = Menu(file_menu, tearoff=0)
        file_menu.add_separator()
        file_menu.add_command(label="Back to Main Menu", command=self.back_to_main_menu)
        file_menu.add_command(label="Exit", command=self.exit_application)

        # Capture Menu
        settings = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Settings", menu=settings)
        settings.add_command(label="Choose a Camera", command=self.choose_camera)
        settings.add_command(label="Camera Settings", command=self.open_camera_settings)
        settings.add_command(label="Calibration", command=self.calibration)
        settings.add_command(label="Object shift", command=self.open_object_shift)
        settings.add_command(label="Set Scan Key Bind", command=self.open_scan_key_dialog)

    def find_usb_devices_windows(self):
        devices = FilterGraph().get_input_devices()
        for device_index, device_name in enumerate(devices):
            if device_name == "HD USB Camera":
                return device_index
        return 0

    def create_bottom_strip(self):
        """Add a strip at the bottom with a Scan button and a Back button on the left."""
        bottom_frame = tk.Frame(self.main_window.root, bg="#eeeeee", pady=20)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Back button on the left
        self.back_button = tk.Button(
            bottom_frame, text="Back", command=self.back_to_main_menu, font=("Arial", 12)
        )
        self.back_button.pack(side=tk.LEFT, padx=10)

        # Scan button
        self.scan_button = tk.Button(
            bottom_frame, text="Scan", command=self.scan_profile, font=("Arial", 12)
        )
        self.scan_button.pack(side=tk.LEFT, padx=10)

        # Conditional messages and calibration setup
        self.message_label = tk.Label(bottom_frame, font=("Arial", 10), bg="#eeeeee", fg="#333333")
        self.message_label.pack(side=tk.LEFT, padx=20)

        self.display_message_in_bottom_strip_about_scan_position()

        # Initial tooltip text for the scan button
        tooltip_text = "Space" if not hasattr(self, 'scan_key') or not self.scan_key else self.scan_key
        self.create_tooltip(self.scan_button, tooltip_text)

    def display_message_in_bottom_strip_about_scan_position(self):
        if not hasattr(self, 'actual_project') or not getattr(self, 'actual_project', None):
            # Case: No project loaded or created
            self.message_label.config(
                text="First, open or create a new project to manage scans."
            )
            self.scan_button.config(state=tk.DISABLED)
        else:
            result = self.get_movement_parameters()
            if result:
                self.start_position, self.shift = result
            if not hasattr(self, 'shift') or self.shift is None:
                # Case: Calibration needed
                self.message_label.config(
                    text="Perform calibration to define the movement distance (in hundredths of a millimeter)."
                )
                self.scan_button.config(state=tk.DISABLED)
            else:
                raw_scans_path = os.path.join(self.actual_project.project_dir, "scans", "raw")
                if os.path.isdir(raw_scans_path):
                    self.initialize_counter(raw_scans_path) 
                # Case: Ready to scan
                self.message_label.config(
                    text=f"Scanning scan number {self.counter}, shifted by {self.start_position+((self.counter-1)*self.shift)} hundredths of a millimeter."
                )
                self.scan_button.config(state=tk.NORMAL)

    def create_tooltip(self, widget, text):
        """Create a tooltip using a Label that appears when the mouse hovers over the widget."""
        tooltip = None

        def show_tooltip(event):
            """Show the tooltip when the mouse enters the widget."""
            nonlocal tooltip
            tooltip = tk.Toplevel(self.main_window.root)
            tooltip.wm_overrideredirect(True)
            x = event.x_root + 10
            y = event.y_root - 10
            tooltip.wm_geometry(f"+{x}+{y}")
            
            label = tk.Label(tooltip, text=text, background="yellow", relief="solid", borderwidth=1, font=("Arial", 10))
            label.pack(padx=5, pady=5)

        def hide_tooltip(event):
            """Hide the tooltip when the mouse leaves the widget."""
            if tooltip:
                tooltip.destroy()

        widget.bind("<Enter>", show_tooltip)
        widget.bind("<Leave>", hide_tooltip)

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
                self.main_window.root.bind(f"<{key}>", lambda event: self.scan_profile())
                self.scan_button.config(text=f"Scan")

                # Update the tooltip text dynamically
                tooltip_text = self.scan_key
                self.create_tooltip(self.scan_button, tooltip_text)

                messagebox.showinfo("Key Binding", f"Scan key set to '{key}'.")
                dialog.destroy()
            else:
                messagebox.showerror("Invalid Input", "Please enter a single alphanumeric character.")

        submit_button = tk.Button(dialog, text="Set Key", font=("Arial", 12), command=on_submit)
        submit_button.pack(pady=10)

    def start_camera_view(self):
        """Initialize the camera view."""
        self.cap = cv2.VideoCapture(self.camera_index, cv2.CAP_DSHOW)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Unable to access camera.")
            return

        self.start_stream()

    def choose_camera(self):
        """Open a pop-up window to choose a camera."""
        dialog = tk.Toplevel(self.main_window.root)
        dialog.title("Choose a Camera")
        dialog.geometry("600x500")
        dialog.resizable(False, False)

        label = tk.Label(dialog, text="Detecting cameras, please wait...", font=("Arial", 12))
        label.pack(pady=10)

        camera_list = ttk.Treeview(dialog, columns=("Index", "Name"), show="headings")
        camera_list.heading("Index", text="Index")
        camera_list.heading("Name", text="Name")
        camera_list.column("Index", width=50, anchor="center")
        camera_list.column("Name", width=400, anchor="w")
        camera_list.pack(pady=10, fill=tk.BOTH, expand=True)

        select_button = tk.Button(dialog, text="Select", font=("Arial", 12), state=tk.DISABLED, command=lambda: self.on_camera_select(camera_list, dialog))
        select_button.pack(pady=10)

        def detect_cameras():
            graph = FilterGraph()
            devices = graph.get_input_devices()

            # Populate the Treeview with available cameras
            for index, device_name in enumerate(devices):
                camera_list.insert("", "end", values=(index, device_name))

            # Enable the Select button and update the label
            if devices:
                label.config(text="Select a camera from the list:")
                select_button.config(state=tk.NORMAL)
            else:
                label.config(text="No cameras detected.")

        # Start the detection thread
        Thread(target=detect_cameras, daemon=True).start()

        dialog.transient(self.main_window.root)
        dialog.grab_set()
        self.main_window.root.wait_window(dialog)

    def on_camera_select(self, camera_list, dialog):
        """Handle camera selection."""
        selected = camera_list.focus()
        if not selected:
            messagebox.showerror("Selection Error", "Please select a camera.")
            return

        values = camera_list.item(selected, "values")
        self.camera_index = int(values[0])
        self.start_camera_view()
        messagebox.showinfo("Camera Selected", f"Selected Camera: {values[1]}")
        dialog.destroy()

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
        
        #self.actual_project = self.current_project
        
        # Release the camera
        if self.cap:
            self.cap.release()
        
        # Unbind events
        self.main_window.root.unbind("<Configure>")
        
        # Vymazať všetky widgety
        for widget in self.main_window.root.winfo_children():
            widget.destroy()
        
        # Delete all widgets
        self.main_window.show_main_menu(self.actual_project)

    def exit_application(self):
        """Exit the application."""
        self.stop_stream()
        self.main_window.root.destroy()
          
    def export_file(self, format): messagebox.showinfo("Export", f"Export as {format} coming soon!")

    def scan_profile(self): 
        if not hasattr(self, 'actual_project') or not getattr(self, 'actual_project', None):
            messagebox.showerror("Error", "No project found. Please create or open a project.")
            return
        
        scans_path_basic = os.path.join(self.actual_project.project_dir)
        ld = LineDetection(scans_path_basic, scans_path_basic + '/scans/processed/', 1, extension="png")
        scans_path = os.path.join(scans_path_basic, "scans", "raw")

        # Initialize counter based on existing files
        self.initialize_counter(scans_path)

        try:
            # Zachytenie snímky z kamery
            ret, frame = self.cap.read()
            if not ret:
                messagebox.showerror("Chyba", "Nepodarilo sa zachytiť snímku.")
                return False

            # Uloženie snímky do raw adresára
            filename = f"{self.counter}_scan_{self.start_position+((self.counter-1)*self.shift)}.png"
            filepath = os.path.join(scans_path, filename)
            cv2.imwrite(filepath, frame)
            ld.apply_to_image(scans_path_basic, filename, True)
            ld.write_points_to_file_app()
            self.display_message_in_bottom_strip_about_scan_position()

            return True
        except Exception as e:
            messagebox.showerror("Chyba", f"Chyba pri snímaní: {e}")
            return False
        
    def open_object_shift(self):
        """Opens a popup window for object shift."""
        # Check if project exists
        if not hasattr(self, 'actual_project') or not getattr(self, 'actual_project', None):
            messagebox.showerror("Error", "No project found. Please create or open a project.")
            return

        # Create a popup window
        shift_window = tk.Toplevel(self.main_window.root)
        shift_window.title("Object Shift")
        shift_window.geometry("450x150")

        # Frame for the start position
        frame_start = tk.Frame(shift_window)
        frame_start.pack(pady=(20, 10))

        tk.Label(frame_start, text="Object start position (hundredths of a millimeter):").pack(side=tk.LEFT, padx=5)
        start_value_spinbox = tk.Spinbox(frame_start, from_=0, to=10000, width=10, textvariable=tk.StringVar(value=0))
        start_value_spinbox.pack(side=tk.LEFT)

        # Frame for the shift
        frame_shift = tk.Frame(shift_window)
        frame_shift.pack(pady=10)

        tk.Label(frame_shift, text="Object shift between scans (hundredths of a millimeter):").pack(side=tk.LEFT, padx=5)
        shift_value_spinbox = tk.Spinbox(frame_shift, from_=-360, to=360, width=10, textvariable=tk.StringVar(value=0))
        shift_value_spinbox.pack(side=tk.LEFT)

        # Function to confirm and apply the values
        def apply_shift():
            try:
                # Check if both values are integer
                try:
                    start_position = int(start_value_spinbox.get())
                except:
                    raise ValueError("Start position must be an integer.")
                
                if start_position < 0:
                    raise ValueError("Start position cannot be lower than 0.")
                
                try:
                    shift = int(shift_value_spinbox.get())
                except:
                    raise ValueError("Object shift must be an integer.")
                
                # Save the start_position and shift to a file
                movement_parameters_path = os.path.join(self.actual_project.project_dir, "movement_parameters")
                os.makedirs(movement_parameters_path, exist_ok=True)
                file_path = os.path.join(movement_parameters_path, "movement_view1.txt")
                
                with open(file_path, "w") as file:
                    file.write(f"{start_position}, {shift}")

                self.start_position = start_position
                self.shift = shift

                self.display_message_in_bottom_strip_about_scan_position()

                messagebox.showinfo("Success", f"Object will start from:\n{self.start_position} hundredths of a millimeter\nIt will be repeatedly moved by:\n{self.shift}hundredths of a millimeter", parent=shift_window)
                shift_window.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e), parent=shift_window)
            except Exception:
                # Handle other errors
                messagebox.showerror("Error", "An unknown error occurred. Please check your inputs.", parent=shift_window)

        # Apply button
        apply_button = tk.Button(shift_window, text="Apply", command=apply_shift)
        apply_button.pack(pady=10)

    def initialize_counter(self, scans_path):
        """Initialize the counter to find the smallest missing scan number."""
        if not os.path.exists(scans_path):
            os.makedirs(scans_path)

        # Collect files matching the pattern "N_scan_*.png"
        existing_files = [f for f in os.listdir(scans_path) if re.match(r"\d+_scan_\d+\.png", f)]

        # Extract the first number (N) from filenames like "7_scan_3500.png"
        scanned_numbers = set()
        for file in existing_files:
            match = re.match(r"(\d+)_scan_\d+\.png", file)
            if match:
                scanned_numbers.add(int(match.group(1)))

        # Find the smallest missing number
        smallest_missing = 1
        while smallest_missing in scanned_numbers:
            smallest_missing += 1

        self.counter = smallest_missing

    def open_camera_settings(self):
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Camera could not be opened.")
            return

        # Open the camera settings dialog
        self.cap.set(cv2.CAP_PROP_SETTINGS, 1)

        # Use an invisible loop to keep the app responsive while allowing window closure
        while cv2.getWindowProperty("Camera Preview", cv2.WND_PROP_VISIBLE) >= 1:
            ret, frame = self.cap.read()
            if not ret:
                messagebox.showerror("Error", "Cannot capture video frame.")
                break

            # Display the live feed in the original preview window if needed
            cv2.imshow("Camera Preview", frame)

            # Exit the loop if the user manually closes the window using the "X" button
            if cv2.getWindowProperty("Camera Preview", cv2.WND_PROP_VISIBLE) < 1:
                break

    def calibration(self):
        """Otvorenie kalibračného dialógového okna pre projekt."""
        # Najprv skontrolujeme, či je projekt otvorený
        if not hasattr(self, 'actual_project') or not getattr(self, 'actual_project', None):
            messagebox.showerror("Chyba", "Najprv otvorte alebo vytvorte projekt.")
            return

        # Dialógové okno pre kalibráciu
        calibration_dialog = tk.Toplevel(self.main_window.root)
        calibration_dialog.title("Kalibrácia")
        calibration_dialog.geometry("500x600")
        calibration_dialog.resizable(False, False)

        # Kontrola existujúcej kalibrácie
        calibration_path_basic = os.path.join(self.actual_project.project_dir)
        calibration_path = os.path.join(self.actual_project.project_dir, "calibration")
        
        # Premenné pre kalibráciu
        width_var = tk.StringVar()
        height_var = tk.StringVar()
        scanned_images = []
        
        # Kontrola existujúcej kalibrácie
        def check_existing_calibration():
            calibration_file = os.path.join(calibration_path, "calibration_data.txt")
            if os.path.exists(calibration_file):
                response = messagebox.askyesno(
                    "Existujúca kalibrácia", 
                    "Pre tento pohľad už existuje kalibrácia. Chcete zmazať existujúce skeny a vytvoriť novú kalibráciu?"
                )
                if response:
                    # Zmazanie existujúcich kalibračných súborov
                    self._cleanup_existing_calibration(calibration_path)
                    return True
                return False
            return True

        # Funkcia pre začatie skenovania
        def start_calibration_scan():
            # Validácia rozmerov
            try:
                width = float(width_var.get())
                height = float(height_var.get())
                
                if width <= 0 or height <= 0:
                    messagebox.showerror("Chyba", "Rozmery musia byť kladné čísla.")
                    return
            except ValueError:
                messagebox.showerror("Chyba", "Zadajte platné numerické hodnoty pre šírku a výšku.")
                return

            # Kontrola existujúcej kalibrácie
            if not check_existing_calibration():
                return

            # Vytvorenie adresárov pre kalibráciu
            os.makedirs(os.path.join(calibration_path, "raw"), exist_ok=True)
            os.makedirs(os.path.join(calibration_path, "processed"), exist_ok=True)

            #Inicializácia line detektora (algoritmu na hľadanie čiary)
            ld = LineDetection(calibration_path_basic, calibration_path_basic + '/calibration/processed/', 1, extension="png", raw_path="/calibration/raw/", processed_path = '/calibration/processed/')
            
            # Spustenie skenovania
            self._run_calibration_scan(
                calibration_path, 
                width, 
                height, 
                scanned_images, 
                progress_bar, 
                scan_button, 
                calibration_dialog,
                ld,
                calibration_path_basic
            )

        # Rozloženie widgetov
        tk.Label(calibration_dialog, text="Kalibrácia", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Rámček pre rozmery
        dimension_frame = tk.Frame(calibration_dialog)
        dimension_frame.pack(pady=20)

        tk.Label(dimension_frame, text="Šírka kalibračného objektu (mm):", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(dimension_frame, textvariable=width_var, font=("Arial", 12), width=10).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(dimension_frame, text="Výška kalibračného objektu (mm):", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(dimension_frame, textvariable=height_var, font=("Arial", 12), width=10).grid(row=1, column=1, padx=5, pady=5)

        # Progres bar
        progress_bar = ttk.Progressbar(
            calibration_dialog, 
            orient="horizontal", 
            length=400, 
            mode="determinate", 
            maximum=5
        )
        progress_bar.pack(pady=20)

        # Tlačidlo skenovania
        scan_button = tk.Button(
            calibration_dialog, 
            text="Spustiť kalibráciu", 
            command=start_calibration_scan, 
            font=("Arial", 12)
        )
        scan_button.pack(pady=10)

    def _cleanup_existing_calibration(self, calibration_path):
        """Vyčistenie existujúcich kalibračných súborov."""
        try:
            # Zmazanie raw a processed adresárov
            raw_path = os.path.join(calibration_path, "raw")
            processed_path = os.path.join(calibration_path, "processed")
            calibration_file = os.path.join(calibration_path, "calibration_data.txt")

            # Odstránenie súborov
            for path in [raw_path, processed_path]:
                if os.path.exists(path):
                    for file in os.listdir(path):
                        os.remove(os.path.join(path, file))

            # Odstránenie kalibračného súboru
            if os.path.exists(calibration_file):
                os.remove(calibration_file)
        except Exception as e:
            messagebox.showerror("Chyba", f"Nepodarilo sa vyčistiť existujúcu kalibráciu: {e}")

    def _run_calibration_scan(self, calibration_path, width, height, scanned_images, progress_bar, scan_button, dialog, ld, calibration_path_basic):
        """Spustenie kalibračného skenovania."""
        def capture_calibration_image():
            """Zachytenie jednej kalibračnej snímky."""
            try:
                # Zastavenie aktuálneho streamovania
                #self.stop_stream()

                # Zachytenie snímky z kamery
                ret, frame = self.cap.read()
                if not ret:
                    messagebox.showerror("Chyba", "Nepodarilo sa zachytiť snímku.")
                    return False

                # Uloženie snímky do raw adresára
                filename = f"cal_scan_{len(scanned_images) + 1}.png"
                filepath = os.path.join(calibration_path, "raw", filename)
                cv2.imwrite(filepath, frame)
                ld.apply_to_image(calibration_path_basic, filename, True)
                ld.write_points_to_file_app()

                # Pridanie do zoznamu
                scanned_images.append(filepath)

                # Aktualizácia progress baru
                progress_bar['value'] = len(scanned_images)

                # Reštart streamovania
                #self.start_stream()

                return True
            except Exception as e:
                messagebox.showerror("Chyba", f"Chyba pri snímaní: {e}")
                return False

        def finalize_calibration():
            """Finalizácia kalibračného procesu."""
            if len(scanned_images) == CALIBRATION['count']:
                # Uloženie kalibračných údajov
                calibration_file = os.path.join(calibration_path, "calibration_data.txt")
                avg_distance = 0 ##TO DO
                with open(calibration_file, "w") as f:
                    f.write(f"{width}, {height}, {avg_distance}\n")

                messagebox.showinfo("Kalibrácia", "Kalibrácia úspešne dokončená.")
                dialog.destroy()
                self.open_object_shift()
            else:
                messagebox.showwarning("Nedokončená kalibrácia", f"Je potrebné zachytiť {CALIBRATION['count']} snímok.")

        def on_scan_click():
            """Obsluha kliknutia na skenovanie."""
            if len(scanned_images) < CALIBRATION['count']:
                if capture_calibration_image():
                    if len(scanned_images) == CALIBRATION['count']:
                        scan_button.config(text="Dokončiť kalibráciu", command=finalize_calibration)
            else:
                finalize_calibration()

        # Konfigurácia tlačidla
        scan_button.config(text="Zachytiť snímku", command=on_scan_click)
        
