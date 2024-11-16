from tkinter import *
from tkinter import ttk, messagebox
import cv2
from PIL import Image, ImageTk
import threading
import time
import platform

# Check if winsound is available
if platform.system() == "Windows":
    import winsound

class ScannerWindow:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Profilometer Scanner")
        self.camera = None
        self.camera_index = None
        self.is_capturing = False
        self.camera_settings_dict = {}  # Renamed to avoid conflict
        self.setup_window()
        self.create_menu()
        self.create_camera_view()

    def setup_window(self):
        self.root.state('zoomed')
        self.root.configure(bg='black')
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_menu(self):
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        # File Menu
        file_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Project", command=self.new_project)
        file_menu.add_command(label="Open Project", command=self.open_project)
        file_menu.add_command(label="Save Project", command=self.save_project)
        export_menu = Menu(file_menu, tearoff=0)
        file_menu.add_cascade(label="Export", menu=export_menu)
        export_menu.add_command(label="STL", command=lambda: self.export_file("stl"))
        export_menu.add_command(label="OBJ", command=lambda: self.export_file("obj"))
        export_menu.add_command(label="GLTF", command=lambda: self.export_file("gltf"))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)

        # Main Menu
        main_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Main Menu", menu=main_menu)
        main_menu.add_command(label="Scan Profile", command=self.scan_profile)
        main_menu.add_command(label="Browse Scans", command=self.browse_scans)

        # Capture Menu
        capture_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Capture", menu=capture_menu)
        capture_menu.add_command(label="Choose a Camera", command=self.choose_camera)
        capture_menu.add_command(label="Camera Settings", command=self.open_camera_settings)  # Renamed method
        capture_menu.add_command(label="Calibration", command=self.calibration)

    def create_camera_view(self):
        self.camera_frame = Frame(self.root, bg='black')
        self.camera_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

        self.camera_label = Label(self.camera_frame, bg='black')
        self.camera_label.pack(expand=True, fill=BOTH)

        self.control_frame = Frame(self.root, bg='#333333')
        self.control_frame.pack(fill=X, padx=20, pady=(0, 20))

        ttk.Button(self.control_frame, text="Start Scan", command=self.start_scan).pack(side=LEFT, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Stop", command=self.stop_scan).pack(side=LEFT, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Save Scan", command=self.save_scan).pack(side=LEFT, padx=5, pady=5)

    def show_confirmation(self, message):
        confirm_window = Toplevel(self.root)
        confirm_window.title("Confirmation")
        confirm_window.geometry("300x100")
        confirm_window.configure(bg='white')

        label = Label(confirm_window, text=message, bg='white', fg='green', font=("Helvetica", 14))
        label.pack(pady=20)

        if platform.system() == "Windows":
            winsound.Beep(1000, 500)

        confirm_window.after(10000, confirm_window.destroy)

    def choose_camera(self):
        camera_window = Toplevel(self.root)
        camera_window.title("Choose Camera")
        camera_window.geometry("300x400")
        camera_window.transient(self.root)
        camera_window.grab_set()

        list_frame = Frame(camera_window)
        list_frame.pack(expand=True, fill=BOTH, padx=10, pady=10)

        scrollbar = Scrollbar(list_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        camera_listbox = Listbox(list_frame)
        camera_listbox.pack(expand=True, fill=BOTH)

        camera_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=camera_listbox.yview)

        available_cameras = self.scan_cameras()
        for i, camera_name in available_cameras.items():
            camera_listbox.insert(END, f"Camera {i}: {camera_name}")

        def select_camera():
            selection = camera_listbox.curselection()
            if selection:
                selected_index = int(selection[0])
                self.connect_camera(selected_index)
                camera_window.destroy()

        ttk.Button(camera_window, text="Select Camera", command=select_camera).pack(pady=10)

    def scan_cameras(self):
        available_cameras = {}
        max_cameras = 5

        for i in range(max_cameras):
            cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
            if cap.isOpened():
                ret, _ = cap.read()
                if ret:
                    available_cameras[i] = f"Camera Device {i}"
                cap.release()

        return available_cameras

    def connect_camera(self, camera_index):
        if self.camera is not None:
            self.disconnect_camera()

        self.camera = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
        if self.camera.isOpened():
            self.camera_index = camera_index
            self.is_capturing = True
            threading.Thread(target=self.update_camera_feed, daemon=True).start()
            self.show_confirmation(f"Connected to Camera {camera_index}")
        else:
            messagebox.showerror("Error", "Failed to connect to camera")

    def disconnect_camera(self):
        self.is_capturing = False
        if self.camera is not None:
            self.camera.release()
            self.camera = None
        self.camera_label.config(image='')

    def update_camera_feed(self):
        if not self.is_capturing:
            return

        if self.camera and self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_rgb = cv2.resize(frame_rgb, (self.camera_label.winfo_width(), self.camera_label.winfo_height()))

                image = Image.fromarray(frame_rgb)
                photo = ImageTk.PhotoImage(image=image)
                self.camera_label.config(image=photo)
                self.camera_label.image = photo

        self.root.after(30, self.update_camera_feed)

    def open_camera_settings(self):
        if self.camera is None:
            messagebox.showerror("Error", "Please connect a camera first")
            return
        settings_window = Toplevel(self.root)
        settings_window.title("Camera Settings")

    def on_closing(self):
        self.disconnect_camera()
        self.root.destroy()

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

def start_scanner():
    root = Tk()
    root.withdraw()  # Hide the root window
    ScannerWindow()
    root.mainloop()

start_scanner()
