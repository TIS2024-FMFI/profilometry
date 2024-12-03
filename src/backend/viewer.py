import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from config import WINDOW_CONFIG
import os
import cv2
import threading

class ViewerWindow:
    def __init__(self, path, root ):
        self.root = root
        self.root.root.minsize(1920, 1080)
        self.root.root.maxsize(1920, 1080)
        self.path = path
        self.all_points_to_img = []
        self.images_to_delete = []
        self.pripona = 'png'  # File extension (e.g., png, jpg)

        if not self.check_needs_generation():  # Check if files need to be processed
            self.add_images()  # Add existing images
            self.setup_window()  # Initialize the main window layout
            self.create_menu()  # Create the menu bar
        else:
            self.use_algorithm_image_by_image()  # Run the algorithm if needed

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
        file_menu.add_command(label="Open Project", command=self.open_project)
        file_menu.add_command(label="Use Algorithm", command=self.use_algorithm_to_images)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)

        # Main menu
        main_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Main Menu", menu=main_menu)
        main_menu.add_command(label="Scan Profile", command=self.scan_profile)
        main_menu.add_command(label= "Show 3D", command = self.show_3d)

    def use_algorithm_to_images(self):
        top = tk.Toplevel(self.root.root)
        top.title("Výber hodnôt algoritmu")
        top.geometry("300x200")

        def close_window(top):
            significant_threshold_pixel = int(significant_threshold_pixel_spinbox.get())
            largest_points_threshold = int(largest_points_threshold_spinbox.get())
            top.destroy()    
            self.use_algorithm_image_by_image(significant_threshold_pixel = significant_threshold_pixel, 
                                              largest_points_threshold = largest_points_threshold)
        
        frame1 = tk.Frame(top)
        frame1.pack(pady=10)

        label1 = tk.Label(frame1, text="Significant threshold pixel:")
        label1.pack(side=tk.LEFT, padx=5)

        significant_threshold_pixel_spinbox = tk.Spinbox(frame1, from_=0, to=255, width=10, textvariable=tk.StringVar(value="80"))
        significant_threshold_pixel_spinbox.pack(side=tk.LEFT)
        
        
        frame2 = tk.Frame(top)
        frame2.pack(pady=10)
        
        label2 = tk.Label(frame2, text="Largest points threshold:")
        label2.pack(side=tk.LEFT, padx=5)
        
        largest_points_threshold_spinbox = tk.Spinbox(frame2, from_=0, to=255, width=10, textvariable=tk.StringVar(value="30"))
        largest_points_threshold_spinbox.pack(side=tk.LEFT)

        close_button = tk.Button(top, text="Apply", command=lambda: close_window(top))
        close_button.pack(pady=10)
        

    def delete_scans(self, num_from, num_to):
        self.all_points_to_img = []
        for i in range(num_from-1, num_to):
            image_path, images_path_alg = self.scrollbar_images[i]
            os.remove(image_path)
            os.remove(images_path_alg)
        
        self.clear_images()
        self.add_to_scrollbar()

    
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
            
        def show2d():
            from finding_line import LineDetection
            ld = LineDetection(self.path , self.path + '_alg', constant=1, extension= self.pripona)
            if len(self.all_points_to_img) > 1:
                ld.all_points = self.all_points_to_img
            else:
                ld.apply_to_folder()
            
            ld.display_all_points()
        
        def delete_input_box1():
            input_window = tk.Toplevel(self.root.root)
            input_window.title("Enter Two Numbers")
            input_window.geometry("300x200")
            
            tk.Label(input_window, text="Enter first number:").pack(pady=5)
            first_number_entry = tk.Entry(input_window)
            first_number_entry.pack(pady=5)
            
            tk.Label(input_window, text="Enter second number:").pack(pady=5)
            second_number_entry = tk.Entry(input_window)
            second_number_entry.pack(pady=5)
            
            
            def process_numbers():
                try:
                    num1 = int(first_number_entry.get())
                    num2 = int(second_number_entry.get())
                    if num1> num2 or num1<=0 or num2<=0 or num1> len(self.scrollbar_images) or num2 > len(self.scrollbar_images):
                        raise ValueError()
                    ans = messagebox.askyesno("Numbers Entered", f"Do you want to delete images from {num1} to  {num2}?")
                    if ans:
                        self.delete_scans(num1, num2)
                        
                    input_window.destroy()
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers!")
            
            tk.Button(input_window, text="Submit", command=process_numbers).pack(pady=10)
        
        def delete_input_box2():
            for i in self.images_to_delete:
                #print(self.scrollbar_images[int(i)-1])
                os.remove(self.scrollbar_images[int(i)-1][0])
                os.remove(self.scrollbar_images[int(i)-1][1])
            
            self.clear_images()
            self.add_to_scrollbar()
            self.images_to_delete = []

        # Highlight button on hover

        def set_button(relx, rely, text, command):
            button  = tk.Button(self.root.root, text=text, font=('Arial 14'), command=command)
            def on_enter(e):
                button.configure(bg='#2980b9')
            
            def on_leave(e):
                button.configure(bg=WINDOW_CONFIG['bg_color'])
                
                
            button.bind('<Enter>', on_enter)
            button.bind('<Leave>', on_leave)
            
            button.place(relx=relx, rely=rely)

        set_button(.013,.8, 'Back', go_back)
        set_button(.1,.8, 'Show2D', show2d)
        set_button(.2,.8, 'Delete Selected', delete_input_box2)
        set_button(.2,.87, 'Delete Interval', delete_input_box1)
        
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
        self.scrollbar_images = []

        for filename in os.listdir(self.path):
            if filename.endswith("." + self.pripona):  # Check for correct file extension
                file_path = os.path.join(self.path, filename)
                if first_image is None:
                    first_image = str(count + 1) + "|" + file_path  # Store first image for preview

                label = tk.Label(self.scrollable_frame, text=str(count + 1) + '. SCAN', font=("Arial 14"))
                

                split_path = file_path.split('\\')
                split_path[0] += '_alg\\'
                processed_image_path = split_path[0] + split_path[1]
                
                self.scrollbar_images.append((file_path, processed_image_path))
                
                label.pack(padx=170, pady=10)
                label.config(bg="white")
                count += 1

                # Highlight label on hover
                def on_hover_enter(event, label):
                    if label['bg'] != 'red':
                        label.config(bg="lightblue")

                def on_hover_leave(event, label):
                    if label['bg'] != 'red':
                        label.config(bg="white")
                    
                def on_right_click(event, label):
                    if label['bg'] == 'red':
                        label.config(bg='white')
                        self.images_to_delete.remove(label['text'].split('.')[0])
                    else:
                        label.config(bg="red")
                        self.images_to_delete.append(label['text'].split('.')[0])
                    

                label.bind("<Enter>", lambda event, label=label: on_hover_enter(event, label))
                label.bind("<Leave>", lambda event, label=label: on_hover_leave(event, label))

                # Set up click event for each label
                label.bind("<Button-1>", lambda event, name=str(count) + '|' + file_path: self.on_item_click(name))
                label.bind("<Button-3>", lambda event, label=label: on_right_click(event, label))
                
                label.bind("<MouseWheel>", self.on_mouse_wheel)
                label.bind("<Button-4>", self.on_mouse_wheel)
                label.bind("<Button-5>", self.on_mouse_wheel)
                
                self.scrollable_frame.bind("<MouseWheel>", self.on_mouse_wheel)
                self.scrollable_frame.bind("<Button-4>", self.on_mouse_wheel)
                self.scrollable_frame.bind("<Button-5>", self.on_mouse_wheel)

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
        self.image_labelPrew.image_path = photo

        self.image_labelAlg.config(image=adjusted_photo_image)
        self.image_labelAlg.image = adjusted_photo_image
        self.image_labelAlg.image_path = processed_image_path
        
        self.image_labelPrew.bind("<Button-1>", lambda event: self.show_fullscreen(event, self.image_labelPrew))
        self.image_labelAlg.bind("<Button-1>", lambda event: self.show_fullscreen(event, self.image_labelAlg))

        def on_hover(event, img):
            img.config(cursor="hand2")
        
        self.image_labelPrew.bind("<Enter>", lambda event: on_hover(event, self.image_labelPrew))
        self.image_labelAlg.bind("<Enter>", lambda event:  on_hover(event, self.image_labelAlg))
            
    
    def show_fullscreen(self, event, type_img):
        img = cv2.imread(type_img.image_path)
        height, width = img.shape[:2]
        new_width = int(width * 0.5)
        new_height = int(height * 0.5)
        new_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
        cv2.imshow("window", new_img)
        cv2.waitKey(0)
       
    
    def on_mouse_wheel(self, event):
        if event.num == 4 or event.delta == 120: 
            self.canvasScrollFrame.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta == -120: 
            self.canvasScrollFrame.yview_scroll(1, "units")
        
     
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

        self.canvasScrollFrame.bind("<MouseWheel>", self.on_mouse_wheel)
        self.canvasScrollFrame.bind("<Button-4>", self.on_mouse_wheel)
        self.canvasScrollFrame.bind("<Button-5>", self.on_mouse_wheel)
        
        # Add labels for preview sections
        self.Scan1Prewlbl = tk.Label(self.root.root, text="Scan 1 Preview", font=('Arial 14'))  # Original preview
        self.Scan1Prewlbl.place(x=700, y=200)

        self.Scan2Prewlbl = tk.Label(self.root.root, text="Scan 1 Adjusted", font=('Arial 14'))  # Adjusted image preview
        self.Scan2Prewlbl.place(x=700, y=550)

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
        self.image_labelAlg.pack(padx=20, pady=40)

        # Populate the scrollbar with image labels
        self.add_to_scrollbar()

        # Adjust the scroll region when the frame is resized
        def on_frame_configure(event):
            self.canvasScrollFrame.config(scrollregion=self.canvasScrollFrame.bbox("all"))

        self.scrollable_frame.bind("<Configure>", on_frame_configure)


    def use_algorithm_image_by_image(self, significant_threshold_pixel = 80, largest_points_threshold=30):
        try:
            for widget in self.root.root.winfo_children():
                widget.destroy()
        except:
            pass
        
        from finding_line import LineDetection
        os.makedirs(self.path + '_alg', exist_ok=True)  # Create directory for processed files
        processor = LineDetection(self.path, self.path + '_alg', 1, extension=self.pripona)
        processor.significant_threshold_pixel = significant_threshold_pixel
        processor.largest_points_threshold = largest_points_threshold
        self.images_to_delete = []
        
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

            self.all_points_to_img = processor.all_points
            progress_window.destroy()

        # Start the processing in a new thread
        thread = threading.Thread(target=process_images)
        thread.start()

        # Check the thread status and update UI when finished
        def check_thread():
            if thread.is_alive():
                self.root.root.after(100, check_thread)
            else:
                self.setup_window()  # Initialize the main window layout
                self.create_menu()  # Create the menu bar
                self.add_images() # Add images to Scrollbar

        check_thread()

    
    # Apply the algorithm to images
    def use_algorithm_batch(self):
        from finding_line import LineDetection
        os.makedirs(self.path + '_alg', exist_ok=True)  # Create directory for processed files
        processor = LineDetection(self.path, self.path + '_alg', 1, extension=self.pripona)
        self.images_to_delete = []
        
        # Apply the algorithm to all files in the folder
        processor.apply_to_folder()
        self.all_points_to_img = processor.all_points

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
        self.all_points_to_img = []
        self.images_to_delete = []
        # Process files if necessary
        error = False
        if not os.path.exists(folder_path_alg) and len(files) != len(files_alg):
            os.makedirs(folder_path_alg, exist_ok=True)
            from finding_line import LineDetection
            processor = LineDetection(folder_path, folder_path_alg, 1, extension=extension)
            processor.apply_to_folder()
            self.all_points_to_img = processor.all_points

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

    def scan_profile(self): 
        for widget in self.root.root.winfo_children():
            widget.destroy()
            
        from frontend.main_window import MainWindow
        w = MainWindow(self.root.root)
        w.handle_scan()

    def show_3d(self):
        for widget in self.root.root.winfo_children():
            widget.destroy()
        
        from frontend.main_window import MainWindow
        w = MainWindow(self.root.root)
        w.handle_3d()
        