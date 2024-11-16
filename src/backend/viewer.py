import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from config import WINDOW_CONFIG
import os

class ViewerWindow:
    def __init__(self, path):
        self.root = tk.Toplevel()
        self.path = path
        self.pripona = 'png'
        self.setup_window()
        self.pridaj_obrazky()
        self.create_menu()
        
    def create_menu(self):
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

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
        
        file_menu.entryconfig("New Project", state = "disabled")
        file_menu.entryconfig("Save Project", state = "disabled")

        # Main Menu
        main_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Main Menu", menu=main_menu)
        main_menu.add_command(label="Scan Profile", command=self.scan_profile)
        main_menu.add_command(label="Browse Scans", command=self.browse_scans)

        # Capture Menu
        capture_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Capture", menu=capture_menu)
        capture_menu.add_command(label="Calibration", command=self.calibration)
        
        capture_menu.entryconfig("Calibration", state = "disabled")
        
    def setup_window(self):
        
        lbl = tk.Label(self.root, text = "Zoznam scanov", font=('Arial 14'))
        lbl.config(bg='white')
        lbl.place(x=200, y=150) 
        
        def vypni():
            self.root.destroy()
        
        button = tk.Button(self.root, text = "Back", font=('Arial 14'), command= vypni)
        
        def on_enter(e):
            button.configure(bg='#2980b9')
        
        def on_leave(e):
            button.configure(bg=WINDOW_CONFIG['bg_color'])
        
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
        
        button.place(relx=.15, rely=.8)
        
        self.root.state('zoomed')
        self.root.configure(bg='white')
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def on_closing(self):
        self.root.destroy()
        
    
    def clear_images(self):
    # This method will clear the content of the scrollable_frame before adding new content
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
    
    def pridaj_do_scrollbaru(self):
        prvyObr = None
        
        cnt = 0
        for filename in os.listdir(self.path):
            if filename.endswith("."+self.pripona):
                file_path = os.path.join(self.path, filename)
                if prvyObr == None:
                    prvyObr = str(cnt+1)+"|"+file_path
                
                label = tk.Label(self.scrollable_frame, text=str(cnt+1)+'. '+file_path, font=("Arial 14"))
                label.pack(padx=10, pady= 10)
                label.config(bg="white")
                cnt+=1
                
                def on_hover_enter(event, label):
                    label.config(bg="lightblue")

                def on_hover_leave(event, label):
                    label.config(bg="white")

                label.bind("<Enter>", lambda event, label=label: on_hover_enter(event, label))
                label.bind("<Leave>", lambda event, label=label: on_hover_leave(event, label))
                
                label.bind("<Button-1>", lambda event, name=str(cnt)+'|'+file_path: self.on_item_click(name))
                
        if prvyObr:
            self.on_item_click(prvyObr)
    
    def on_item_click(self,photo):
            print(f"Klikol si na obrazok: {photo}")
            cnt, photo = photo.split('|')
            
            rozd = photo.split('\\')
            rozd[0]+='_alg\\'
            imageStr = rozd[0] + rozd[1]
            
            self.Scan1Prewlbl.config(text = "Scan"+cnt+"Preview")
            self.Scan2Prewlbl.config(text = "Scan"+cnt+"Adjusted")
            
            image = Image.open(photo)
            image2 = Image.open(imageStr)
    
            image = image.resize((300, 300))
            photo_image = ImageTk.PhotoImage(image)
            
            image2 = image2.resize((300, 300))
            photo_image2 = ImageTk.PhotoImage(image2)
            
            self.image_labelPrew.config(image=photo_image)
            self.image_labelPrew.image = photo_image
            
            self.image_labelAlg.config(image=photo_image2)
            self.image_labelAlg.image = photo_image2
        
    
    def pridaj_obrazky(self):
        self.scrollFrame = tk.Frame(self.root, height=400, width=500)

        self.canvasScrollFrame = tk.Canvas(self.scrollFrame, height=400, width=500)

        scrollbar = tk.Scrollbar(self.scrollFrame, orient="vertical", command=self.canvasScrollFrame.yview)
        self.canvasScrollFrame.config(yscrollcommand=scrollbar.set)
        self.canvasScrollFrame.config(bg='white')
        self.scrollFrame.config(bg = 'white')
        scrollbar.config(bg = 'white')
        
        self.scrollable_frame = tk.Frame(self.canvasScrollFrame)
        self.scrollable_frame.config(bg = 'white')

        self.Scan1Prewlbl = tk.Label(self.root, text = "Scan1Preview", font=('Arial 14'))
        self.Scan1Prewlbl.place(x=700, y=200) 
        
        self.Scan2Prewlbl = tk.Label(self.root, text = "Scan1Adjusted", font=('Arial 14'))
        self.Scan2Prewlbl.place(x=700, y=500) 

        self.canvasScrollFrame.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        scrollbar.pack(side="right", fill="y")
        self.canvasScrollFrame.pack(side="left", fill="both", expand=True)
        
        self.scrollFrame.pack(side="left" ,padx=20, pady=0)   

        self.image_labelPrew = tk.Label(self.root)
        self.image_labelPrew.pack(padx=20, pady=40)
        
        self.image_labelAlg = tk.Label(self.root)
        self.image_labelAlg.pack(padx=20, pady=20) 

        self.pridaj_do_scrollbaru()
        
        def on_frame_configure(event):
            self.canvasScrollFrame.config(scrollregion=self.canvasScrollFrame.bbox("all"))

        self.scrollFrame.bind("<Configure>", on_frame_configure)
    
    def new_project(self): messagebox.showinfo("New Project", "Feature coming soon!")
    
    def use_algorithm(self):
        from finding_line import HladanieCiary
        os.makedirs(self.path+'_alg', exist_ok=True)
        h = HladanieCiary(self.path, self.path+'_alg',1 ,pripona=self.pripona)
        h.aplikuj_na_subor(1)
        
    
    def open_project(self): 
        folder_path = filedialog.askdirectory(title="Vyberte priečinok")
        folder_path_alg = folder_path + '_alg'
        
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
        if files:
            first_file = files[0]
            koncovka = first_file.split('.')[-1]
        
        self.pripona = koncovka
        
        if not os.path.exists(folder_path_alg):
            os.makedirs(folder_path_alg, exist_ok=True)
            from finding_line import HladanieCiary
            h = HladanieCiary(folder_path, folder_path_alg,1 ,pripona=koncovka)
            h.aplikuj_na_subor(1)
            
        self.path = folder_path
        self.clear_images()

        self.pridaj_do_scrollbaru()

        
        
    def save_project(self): messagebox.showinfo("Save Project", "Feature coming soon!")
    def export_file(self, format): messagebox.showinfo("Export", f"Export as {format} coming soon!")
    def scan_profile(self): messagebox.showinfo("Scan Profile", "Feature coming soon!")
    def browse_scans(self): messagebox.showinfo("Browse Scans", "Feature coming soon!")
    def calibration(self): messagebox.showinfo("Calibration", "Feature coming soon!")
    def start_scan(self): messagebox.showinfo("Start Scan", "Feature coming soon!")
    def stop_scan(self): messagebox.showinfo("Stop Scan", "Feature coming soon!")
    def save_scan(self): messagebox.showinfo("Save Scan", "Feature coming soon!")          
        
def start_viewer():
    root = tk.Tk()
    root.withdraw()
    ViewerWindow('images/vrtulka')
    root.mainloop()