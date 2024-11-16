#toto?
from wx.lib.calendar import CalDays
import pywintypes
from sympy.matrices.expressions.tests.test_applyfunc import Xk
from openpyxl.chartsheet import custom
from numpy.core.defchararray import isnumeric
print ("RUN")
import base64
import math
import traceback
import tkinter
from tkinter import *
import tkinter.font as tkFont

import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
import PIL.Image
import PIL.ImageTk
import time
import subprocess
import customtkinter
from idlelib.tooltip import Hovertip

import numpy as np
from scipy.signal import savgol_filter
import peakutils
from scipy.interpolate import interp1d,interp2d,griddata
import langsStrings
import sys
import argparse

from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
import csv
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from mpl_toolkits.axisartist.axislines import Subplot
from matplotlib.colors import ListedColormap
import random
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from scipy.signal import find_peaks_cwt
import warnings
from pathlib import Path
import cProfile
from matplotlib.transforms import blended_transform_factory
imdata = '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GDzDomIk6F862mJ+8E03F0Z5nclFmuRkK5Kde8HmqyJ4ATH+FOweWRCRAAAPVGlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNC40LjAtRXhpdjIiPgogPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgeG1sbnM6aXB0Y0V4dD0iaHR0cDovL2lwdGMub3JnL3N0ZC9JcHRjNHhtcEV4dC8yMDA4LTAyLTI5LyIKICAgIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIgogICAgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIKICAgIHhtbG5zOnBsdXM9Imh0dHA6Ly9ucy51c2VwbHVzLm9yZy9sZGYveG1wLzEuMC8iCiAgICB4bWxuczpHSU1QPSJodHRwOi8vd3d3LmdpbXAub3JnL3htcC8iCiAgICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgICB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iCiAgIHhtcE1NOkRvY3VtZW50SUQ9ImdpbXA6ZG9jaWQ6Z2ltcDphMGRlNjBiNS03MjY4LTRkYjItYTU0Mi00OWFiNjg1YmUzNjIiCiAgIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6NWVlYTYxZWUtMDczMS00MmEyLWJjNTktYzkyZmI4ZDkwOGM4IgogICB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6MjdlMTBhMTAtMWQ1MC00MzdkLWJhNmMtNTEwMzIzNzEwZGFhIgogICBHSU1QOkFQST0iMi4wIgogICBHSU1QOlBsYXRmb3JtPSJXaW5kb3dzIgogICBHSU1QOlRpbWVTdGFtcD0iMTYxNTE5NTYwMTYxNzE0OCIKICAgR0lNUDpWZXJzaW9uPSIyLjEwLjgiCiAgIGRjOkZvcm1hdD0iaW1hZ2UvcG5nIgogICB4bXA6Q3JlYXRvclRvb2w9IkdJTVAgMi4xMCI+CiAgIDxpcHRjRXh0OkxvY2F0aW9uQ3JlYXRlZD4KICAgIDxyZGY6QmFnLz4KICAgPC9pcHRjRXh0OkxvY2F0aW9uQ3JlYXRlZD4KICAgPGlwdGNFeHQ6TG9jYXRpb25TaG93bj4KICAgIDxyZGY6QmFnLz4KICAgPC9pcHRjRXh0OkxvY2F0aW9uU2hvd24+CiAgIDxpcHRjRXh0OkFydHdvcmtPck9iamVjdD4KICAgIDxyZGY6QmFnLz4KICAgPC9pcHRjRXh0OkFydHdvcmtPck9iamVjdD4KICAgPGlwdGNFeHQ6UmVnaXN0cnlJZD4KICAgIDxyZGY6QmFnLz4KICAgPC9pcHRjRXh0OlJlZ2lzdHJ5SWQ+CiAgIDx4bXBNTTpIaXN0b3J5PgogICAgPHJkZjpTZXE+CiAgICAgPHJkZjpsaQogICAgICBzdEV2dDphY3Rpb249InNhdmVkIgogICAgICBzdEV2dDpjaGFuZ2VkPSIvIgogICAgICBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOmE2NjEyMzgzLWIzZGYtNDBmNS04NTFlLWUzOTY3NjYwMzA0MCIKICAgICAgc3RFdnQ6c29mdHdhcmVBZ2VudD0iR2ltcCAyLjEwIChXaW5kb3dzKSIKICAgICAgc3RFdnQ6d2hlbj0iMjAyMS0wMy0wOFQwOToyNjo0MSIvPgogICAgPC9yZGY6U2VxPgogICA8L3htcE1NOkhpc3Rvcnk+CiAgIDxwbHVzOkltYWdlU3VwcGxpZXI+CiAgICA8cmRmOlNlcS8+CiAgIDwvcGx1czpJbWFnZVN1cHBsaWVyPgogICA8cGx1czpJbWFnZUNyZWF0b3I+CiAgICA8cmRmOlNlcS8+CiAgIDwvcGx1czpJbWFnZUNyZWF0b3I+CiAgIDxwbHVzOkNvcHlyaWdodE93bmVyPgogICAgPHJkZjpTZXEvPgogICA8L3BsdXM6Q29weXJpZ2h0T3duZXI+CiAgIDxwbHVzOkxpY2Vuc29yPgogICAgPHJkZjpTZXEvPgogICA8L3BsdXM6TGljZW5zb3I+CiAgPC9yZGY6RGVzY3JpcHRpb24+CiA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz77oDXnAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAC4jAAAuIwF4pT92AAAAB3RJTUUH5QMICRop9QcrlgAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAACAASURBVHja7b15mF1Vne/9WXvvs8881XCqKlWZKgMJISFMgSBgVEAg0oI2oqiobctzu/X1dtt9X1+v96G99vW1Wy9qd2NrS19ofcWrYGM7gA00GIZAMEAIkJlUZajx1HDOqTPvab1/nFPDSaoyGTBc1ud5dlJnn73XXnsN3/1bv/Vb+whAolAoFG8CNFUECoVCCZZCoVAowVIoFEqwFAqFQgmWQqFQKMFSKBRKsBQKhUIJlkKhUCjBUigUSrAUCoVCCZZCoVAowVIoFEqwFAqFQgmWQqFQKMFSKBRKsBQKhUIJlkKhUCjBUigUSrAUCoVCCZZCoVAowVIoFEqwFAqFQgmWQqFQKMFSKBRKsBQKhUIJlkKhUNQxTkciT55/IU0v7UNIA/CBNEFM/u0DfMhIAKcrxkTcz1CuQK9dZltpjKfH+uizSm/oTa+Onc/FsSs4J3Ih87WzSIY7CIokMh3AFlBuq5KVOcay46TNfvorPfSV93CgvI39mRewvfxbsrFEF3YjL9tAMZlAGgJ00D2HSE8Pxcd/g5MvqB71RteJX2PDuQmWpTII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'

import json
from threading import Thread

from tkinter.filedialog import askopenfilename,askdirectory
from calibration import Calibration

from openpyxl import Workbook

customtkinter.set_appearance_mode("light")  
customtkinter.set_default_color_theme("green")  

global laaang
import wmi
import re

def returnCameraIndexes():

    global laaang
    global cccaaa

    index = 0
    if(laaang == "EN"):
        l = 1
    else:
        l = 0
    arr = [langsStrings.vyberte_kameru[l]]
    c = wmi.WMI()
    #wql = "Select * From Win32_USBControllerDevice"
    #wql = "SELECT * FROM Win32_PnPEntity WHERE PNPDeviceID LIKE 'USB\\VID_%'"
    wql = "SELECT * FROM Win32_PnPEntity WHERE Service='usbvideo'"
    i = 0
    for item in c.query(wql):
        q = item.Caption
        print(item)
        #quit()
        #if re.findall("Camera",q):
        arr.append(q+":"+str(i))
        i = i + 1
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index, cv2.CAP_MSMF)
        if cap.read()[0]:
            print(cap.getBackendName())

            cap.release()
        index += 1
        i -= 1
    arr.append(langsStrings.refresh[l])
    cccaaa = arr
    return arr

configfile = "configset.txt"
calData = "calData.txt"
with open(calData) as f:
    lines = f.readlines()

calDatas = []
if(len(lines)<3):
    lines = ["0;0.0\n","640;640.0\n","1280;1280.0"]
for i in range(len(lines)):
    calDatas.append(lines[i].replace("\n", "").split(';'))

calDatas = np.array(calDatas)
calDatas = calDatas.astype(np.float)
calDatas = calDatas.tolist()
print(calDatas)

with open(configfile, 'r') as file:
    configtext = (file)
    configdata = json.load(file)

if(int(configdata["debug"])== 0):
    sys.stdout = open(os.devnull, 'w')
    warnings.filterwarnings("ignore")

laaang = configdata["lang"]
def editConfigset(configtext):
    f = open(configfile, 'w')

    f.write(str(configtext))
    f.close()

class App:
    DEFAULT_CALIBRATION = calDatas

    def __init__(self, args, window, window_title, video_source=0,video_source2=1):

        self.move = 0
        self.neg1 = 1
        self.setBG = False

        self.showPXNMval = 0
        self.unitsGraph = 0
        self.autoYgraph = 0
        self.autoYgraph1 = 1
        self.colorGraph = 0

        self.dozoom = 1
        self.refLive = 0

        self.cameras_list = returnCameraIndexes()

        self.window = window
        photo = PhotoImage(file = 'ikona.png')
        self.window.wm_iconphoto(False, photo)

        self.colorcross = tkinter.IntVar()
        self.colorcross.set(1)
        self.window.geometry("1480x960")

        self.window.title(window_title)
        self.video_source = int(configdata["camrgb"])
        self.video_source2 = int(configdata["camspect"])
        self.def_font = tkinter.font.nametofont("TkDefaultFont")
        self.def_font.configure(size=9)
        self.vid = MyVideoCapture(
            args.calibration or App.DEFAULT_CALIBRATION, self.video_source)

        self.point1 = 'x'
        self.point2 = 'x'
        self.point3 = 'x'
        if args.calibration is not None:
            self.point1 = args.calibration[0][0]
            self.point2 = args.calibration[1][0]
            self.point3 = args.calibration[2][0]

        def select_points(event):

            if self.marker1.cget("text") == "Kliknutím vyberte bod!":
                self.marker1.configure(text=event.x)
                self.point1 = int(event.x)
            elif self.marker2.cget("text") == "Kliknutím vyberte bod!":
                self.marker2.configure(text=event.x)
                self.point2 = int(event.x)
            elif self.marker3.cget("text") == "Kliknutím vyberte bod!":
                self.marker3.configure(text=event.x)
                self.point3 = int(event.x)

        def clear_points():

            self.marker1.configure(text="Kliknutím vyberte bod!")
            self.marker2.configure(text="Kliknutím vyberte bod!")
            self.marker3.configure(text="Kliknutím vyberte bod!")
            self.txt1.delete(0, tkinter.END)
            self.txt2.delete(0, tkinter.END)
            self.txt3.delete(0, tkinter.END)
            self.calbutton.configure(
                text="Calibrate",  bg="red")
        def showToolsGraph():
            self.bottom_frame_c.grid(row=2, column=1, padx=0, pady=0)
            self.bTools1.grid_remove()
            self.bTools2.grid(row=1, column=0, pady=20, sticky="nw")
        def hideToolsGraph():
            self.bottom_frame_c.grid_remove()
            self.bTools1.grid(row=1, column=0, pady=20, sticky="nw")
            self.bTools2.grid_remove()

        def showPXNM():
            self.vid.showPXNMval = not self.vid.showPXNMval
            if(self.vid.showPXNMval == True):
                self.bshowPXNM.configure(state="normal")
                self.bshowPXNM2.configure(state="disabled")
            else:
                self.bshowPXNM.configure(state="disabled")
                self.bshowPXNM2.configure(state="normal")

            self.avvv = 0
            if(self.vid.showPXNMval == 0):
                self.vid.unitsGraph = ""
                self.lang =  langvar.get()
                if(self.lang == "EN"):
                    l = 1
                else:
                    l = 0

            else:
                self.vid.unitsGraph = ""
                self.lang =  langvar.get()
                if(self.lang == "EN"):
                    l = 1
                else:
                    l = 0

        def autoY():
            self.vid.autoYgraph1 = not self.vid.autoYgraph1
            self.avvv = 0
        autoY() 
        def colorGraph():
            self.vid.colorGraph = not self.vid.colorGraph
            if(self.vid.colorGraph == 1):
                self.switch_1.configure(state="normal")
            else:
                self.switch_1.configure(state="disabled")
            self.avvv = 0
        def emptyFu():
            print("a")
        def do_zoom(event):
            if event.delta > 0: 
                self.dozoom = 2
                self.canvas1.bind('<ButtonPress-1>', lambda event: self.canvas1.scan_mark(event.x, event.y))
                self.canvas1.bind("<B1-Motion>", lambda event: self.canvas1.scan_dragto(event.x, event.y, gain=1))
            else:
                self.canvas1.xview_moveto(self.origX)
                self.canvas1.yview_moveto(self.origY)
                self.dozoom = 1
                self.canvas1.bind('<ButtonPress-1>',emptyFu)
                self.canvas1.bind("<B1-Motion>",emptyFu)

        def peakwidth(event):
            self.avvv = 0
            self.lang =  langvar.get()
            if(self.lang == "EN"):
                l = 1
            else:
                l = 0

            self.lbpeak.configure(text=langsStrings.sirka_vrcholu[l]+": "+str(int(self.peakwidth.get())))
            setattr(self.vid, 'mindist', event)

        def peakthresh(event):
            self.avvv = 0

            self.lang =  langvar.get()
            if(self.lang == "EN"):
                l = 1
            else:
                l = 0

            self.lbthresh.configure(text=langsStrings.prah[l]+": "+str(int(self.thresh.get())))
            setattr(self.vid, 'thresh', event)
        def turnOnOffRealColor():

            self.avvv = 0
        def turnOnOffPeaks():
            self.avvv = 0
            print("Peaks:", self.offpeak_var.get())
        def savfilter(event):
            self.avvv = 0
            max = 16

            self.lang =  langvar.get()
            if(self.lang == "EN"):
                l = 1
            else:
                l = 0

            self.lbfilt.configure(text=langsStrings.filter[l]+": "+str(int(self.filt.get())))
            setattr(self.vid, 'savpoly', event)
        def choicecrosscolor_cb():

            if(self.colorcross.get() == 1):
                self.vid2.colorcross2 = (255,255,255)
            elif(self.colorcross.get() == 2):
                self.vid2.colorcross2 = (0,0,0)
            elif(self.colorcross.get() == 3):
                self.vid2.colorcross2 = (0,0,255)
            else:
                self.vid2.colorcross2 = (255,255,255)

        def rotate_cb(event):
            self.vid.rotate_deg = self.rotation.get()
            self.vid2.rotate_deg = self.rotation.get()
        def moveline_cb(event):
            self.avvv = 0
            """
            if(self.vid.moveline + self.vid.heightline>719.9):
                self.vid.moveline = 720-self.vid.heightline
                configdata["moveline"] = 720-self.vid.heightline
                self.moveline.set(self.vid.moveline)
            if(self.vid.moveline<=self.vid.heightline):
                self.vid.moveline = self.vid.heightline+1
                configdata["moveline"] = self.vid.heightline+1
                self.moveline.set(self.vid.moveline)
            """
            if(event == "plus"):
                self.moveline.set(configdata["moveline"]-1)
            elif(event == "minus"):
                self.moveline.set(configdata["moveline"]+1)
            self.vid.moveline = self.moveline.get()

            configdata["moveline"] = self.vid.moveline
            self.moveline_v.configure(text = str(720-int(self.vid.moveline)))
            configtext = json.dumps(configdata)
            editConfigset(configtext)

        def moveline2_cb(event):
            if(event == "plus"):
                self.moveline2.set(configdata["moveline2"]-1)
            elif(event == "minus"):
                self.moveline2.set(configdata["moveline2"]+1)
            self.vid.moveline2 = self.moveline2.get()
            self.vid2.moveline2 = self.moveline2.get()
            configdata["moveline2"] = self.vid2.moveline2
            configtext = json.dumps(configdata)
            editConfigset(configtext)
        def moveline3_cb(event):
            if(event == "plus"):
                self.moveline3.set(configdata["moveline3"]-1)
            elif(event == "minus"):
                self.moveline3.set(configdata["moveline3"]+1)
            self.vid.moveline3 = self.moveline3.get()
            self.vid2.moveline3 = self.moveline3.get()
            configdata["moveline3"] = self.vid2.moveline3
            configtext = json.dumps(configdata)
            editConfigset(configtext)

        def moveline4_cb(event):
            if(event == "plus"):
                self.moveline4.set(self.vid.moveline4-1)
            elif(event == "minus"):
                self.moveline4.set(self.vid.moveline4+1)
            self.vid.moveline4 = self.moveline4.get()
            self.vid.moveline4 = self.moveline4.get()
            self.moveline_v4.configure(text=str(int(self.vid.moveline4)))

        def heightline_cb(event):
            """
            if(self.vid.moveline + self.vid.heightline>719.9):
                self.vid.moveline = 720-self.vid.heightline
                configdata["moveline"] = 720-self.vid.heightline
                self.moveline.set(self.vid.moveline)
                moveline_cb(1)

            if(self.vid.moveline<=self.vid.heightline):
                self.vid.moveline = self.vid.heightline+1
                configdata["moveline"] = self.vid.heightline+1
                self.moveline.set(self.vid.moveline)
                moveline_cb(1)
                """
            self.avvv = 0
            if(event == "plus"):
                self.heightline.set(configdata["heightline"]-1)
            elif(event == "minus"):
                self.heightline.set(configdata["heightline"]+1)
            self.vid.heightline = self.heightline.get()
            configdata["heightline"] = self.vid.heightline
            self.moveline_v2.configure(text=str(int(self.vid.heightline)))
            configtext = json.dumps(configdata)
            editConfigset(configtext)
        def heightline_cb2(event):
            if(event == "plus"):
                self.heightline3.set(self.heightline3.get()-1)
            elif(event == "minus"):
                self.heightline3.set(self.heightline3.get()+1)
            self.vid.heightline3 = self.heightline3.get()
            self.moveline_v5.configure(text=str(int(self.vid.heightline3)))

        def openSettingsCam():

            if(self.buttonSetGain.get() == 1):
                self.vid.vid.set(cv2.CAP_PROP_AUTO_EXPOSURE, -1)
                time.sleep(1)
                self.vid.vid.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
            else:
                self.vid.vid.set(15, int(self.setexposure.get()))

            #self.vid.vid.set(cv2.CAP_PROP_SETTINGS, 1)

        def setexposure_cb(event):
            self.buttonSetGain.deselect()
            self.avvv = 0
            if(event == "plus"):
                self.setexposure.set(self.setexposure.get()-1)
            elif(event == "minus"):
                self.setexposure.set(self.setexposure.get()+1)
            self.vid.setexposure = self.setexposure.get()
            self.moveline_v3.configure(text=str(int(self.vid.setexposure)))
            self.vid.vid.set(15, self.vid.setexposure)

        def setgain_cb(event):
            self.avvv = 0
            if(event == "plus"):
                self.setgain.set(self.setgain.get()-1)
            elif(event == "minus"):
                self.setgain.set(self.setgain.get()+1)
            self.vid.setgain = self.setgain.get()
            self.moveline_vG.configure(text=str(int(self.vid.setgain)))
            self.vid.vid.set(14, int(self.vid.setgain))
            print(self.vid.vid.get(14))
        def setexposure2_cb(event):
            if(event == "plus"):
                self.setexposure2.set(self.setexposure2.get()-1)
            elif(event == "minus"):
                self.setexposure2.set(self.setexposure2.get()+1)
            self.vid.setexposure2 = self.setexposure2.get()
            self.vid2.vid2.set(15, self.vid.setexposure2)
        def setbrightness_cb(event):
            self.vid.setbrightness = self.setbrightness.get()
            self.vid.vid.set(10, self.vid.setbrightness)
        def engine(axis,move):
            self.move = self.move + move

            if(self.move<0):
                self.move = 0
            self.bmovemeasure.configure(bg="gray")

        def reLV():
            self.avvv = 0
            print("a")
        def selectFile():

            filename = askopenfilename()

            self.entryfile.insert(0, filename)
            self.entryfile.xview("end")
            self.vid.entryfile_path = filename

            reLV()
            self.buttonfile.grid_remove()
            self.buttonremovefile.grid(row=3,column=3)
            self.vid.stopcamvid = 1
            if(filename):
                self.avvv = 0
            if(self.thread.is_alive() == False):

                self.thread.start()

        def loadCalFile():
            filename = askopenfilename(initialdir=Path.cwd(),filetypes=(("txt files", "*.txt"),("all files", "*.*")))
            with open(filename, 'r') as file:
                calData_new = (file.read())
                new_cal = file.readlines()

            f = open('calData.txt', 'w')
            f.write(calData_new)
            f.close()

            with open(filename, 'r') as file:
                calData_new = (file.read())
                new_cal = file.readlines()

            calData = "calData.txt"
            with open(calData) as f:
                lines = f.readlines()

            calDatas = []
            if(len(lines)<3):
                lines = ["0;0.0\n","640;640.0\n","1280;1280.0"]
            for i in range(len(lines)):
                calDatas.append(lines[i].replace("\n", "").split(';'))

            calDatas = np.array(calDatas)
            calDatas = calDatas.astype(np.float)
            calDatas = calDatas.tolist()
            App.DEFAULT_CALIBRATION = calDatas

            togglesettings()
            self.calibrate()
        def selectFile2():
            removeSelectedFile()
            filename = askopenfilename()

            self.entryfile2.insert(0, filename)
            self.vid.entryfile_path2 = filename

            self.buttonfile2.grid_remove()
            self.buttonremovefile2.grid(row=3,column=3)

        def removeSelectedFile():
            self.vid.stopcamvid = 1

            self.entryfile.delete(0, END)
            self.entryfile.insert(0, "")
            self.vid.entryfile_path = ""
            self.buttonfile.grid(row=3,column=3)
            self.buttonremovefile.grid_remove()
        def selectSpect():
            self.neg1 =  var1.get()
        def deleteRows():
            del self.vid.addRows
            self.avvv = 0
            self.odobratCiary.grid_forget()
            self.pridatCiary.grid(row=8,column=3,rowspan=2)
        def addRows():
            print("pridat")
            self.vid.addRows = 1
            self.vid.pridatCiaryN = int(self.pridatCiaryN.get())
            self.avvv = 0
            self.pridatCiary.grid_forget()#.grid(row=8,column=3,rowspan=2)
            self.odobratCiary.grid(row=8,column=3,rowspan=2)#.grid(row=11,column=3,rowspan=2)
        def selectRefer():
            self.avvv = 0
            self.vid.waspressed = 1
            self.vid.refLive = not self.vid.refLive
            if(self.vid.refLive == 1):

                ret, frame, frame_org = self.vid.get_frame()
                cv2.imwrite("refpic.png",
                                cv2.cvtColor(frame_org, cv2.COLOR_BGR2RGB))
                self.dropFunc2.configure(state="normal")

            self.moveline_v4.configure(text=str(int(configdata["moveline"])))
            self.moveline4.set(configdata["moveline"])
            self.vid.moveline4 = int(configdata["moveline"])
            self.moveline_v5.configure(text=str(int(self.vid.heightline)))
            self.vid.heightline3 = int(self.vid.heightline)
            self.heightline3.set(int(self.vid.heightline))

        def selectLang(first=False):

            self.avvv = 0
            global laaang
            laaang = langvar.get()
            configdata["lang"] = langvar.get()
            configtext = json.dumps(configdata)
            editConfigset(configtext)
            self.lang =  langvar.get()

            if(self.lang == "EN"):
                l = 1
            else:
                l = 0
            global cccaaa

            changeee = []
            changeee.append(langsStrings.vyberte_kameru[l])
            x = 1
            try:
                del(cccaaa[0])
                del(cccaaa[-1])
            except:
                a=1
            try:
                #del(cccaaa[0])
                #del(cccaaa[-1])
                for i in range(len(cccaaa)):
                    changeee.append(cccaaa[i])
            except:
                #print("tu som zastal 10")
                a=1
            changeee.append(langsStrings.refresh[l])

            self.calGraphShow.configure(text=langsStrings.kalibracna_krivka[l])

            self.offpeak.configure(text=langsStrings.zobrazit_vrcholy[l])
            self.drop2.configure(values=changeee)
            self.drop2.set(langsStrings.vyberte_kameru[l])
            self.lbfilt.configure(text=langsStrings.filter[l]+": "+str(int(self.filt.get())))
            self.lmoveline.configure(text=langsStrings.ciara[l])
            self.lmoveline2.configure(text=langsStrings.ciara[l])
            self.lsetexposure.configure(text=langsStrings.expozicia[l])
            self.lsetexposure2.configure(text=langsStrings.expozicia[l])
            self.lheightline3.configure(text=langsStrings.pocet_riadkov[l])
            self.lheightline.configure(text=langsStrings.pocet_riadkov[l])
            self.lcontrolcamera.configure(text=langsStrings.ovladanie_spektrometra[l])
            self.lcontrolcamera2.configure(text=langsStrings.ovladanie_statickeho_spektra[l])
            self.titleofspec.configure(text=langsStrings.nastavenie_spektra[l])
            self.titleofsource.configure(text=langsStrings.zdroj[l])
            self.titleoffile.configure(text=langsStrings.nazov_suboru[l])
            self.titleoffunc.configure(text=langsStrings.operacie[l])
            self.showRef.configure(text=langsStrings.zobrazit_ref[l])
            self.showPrie.configure(text=langsStrings.podiel[l])
            self.showRoz.configure(text=langsStrings.rozdiel[l])
            self.buttonSetGain.configure(text=langsStrings.vysoka_citlivost[l])
            self.lcontroltitle.configure(text=langsStrings.kalibracia_spektrometra[l])
            self.axisXtitle.configure(text=langsStrings.xaxis[l])
            self.bautoYbTitle.configure(text=langsStrings.yaxis[l])
            self.switch_1.configure(text=langsStrings.zapnut_realne_farby[l])
            self.checkselect.configure(text=langsStrings.zobrazit_v_grafe[l])
            self.checkselect2.configure(text=langsStrings.zobrazit_v_grafe[l])
            self.buttonfile.configure(text=langsStrings.vyberte_spektrum[l])
            self.buttonfile2.configure(text=langsStrings.vyberte_spektrum[l])
            self.buttonremovefile.configure(text=langsStrings.vyberte_spektrum2[l])
            self.selectRef.configure(text=langsStrings.referencne_spektrum[l])

            Hovertip(self.lbthresh,langsStrings.prah_tip[l], hover_delay=500)
            Hovertip(self.thresh,langsStrings.prah_tip[l], hover_delay=500)

            Hovertip(self.lbfilt,langsStrings.filter_tip[l], hover_delay=500)
            Hovertip(self.filt,langsStrings.filter_tip[l], hover_delay=500)
            Hovertip(self.buttonSetGain,langsStrings.vysoka_citlivost_tip[l], hover_delay=500)
            Hovertip(self.lmoveline,langsStrings.ciara_tip[l], hover_delay=500)
            Hovertip(self.lmoveline2,langsStrings.ciara_tip[l], hover_delay=500)
            Hovertip(self.lsetexposure,langsStrings.expozicia_tip[l], hover_delay=500)
            Hovertip(self.lsetexposure,langsStrings.expozicia_tip[l], hover_delay=500)
            Hovertip(self.lheightline3,langsStrings.sirka_tip[l], hover_delay=500)
            Hovertip(self.lheightline,langsStrings.sirka_tip[l], hover_delay=500)
            Hovertip(self.moveline,langsStrings.ciara_tip[l], hover_delay=500)
            Hovertip(self.moveline_v4,langsStrings.ciara_tip[l], hover_delay=500)
            Hovertip(self.setexposure,langsStrings.expozicia_tip[l], hover_delay=500)
            Hovertip(self.setexposure,langsStrings.expozicia_tip[l], hover_delay=500)
            Hovertip(self.heightline3,langsStrings.sirka_tip[l], hover_delay=500)
            Hovertip(self.heightline,langsStrings.sirka_tip[l], hover_delay=500)

            Hovertip(self.saturacia,langsStrings.saturacia[l], hover_delay=500)

            Hovertip(self.selectRef,langsStrings.referencne_spektrum_tip[l], hover_delay=500)

            Hovertip(self.canvas0,langsStrings.panel_ziveho_spektra[l], hover_delay=500)
            Hovertip(self.canvascrop,langsStrings.vybrana_cast_spektra[l], hover_delay=500)
            Hovertip(self.buttonfile,langsStrings.nahrajte_spektrum_zo_suboru[l], hover_delay=500)
            Hovertip(self.drop2,langsStrings.vyberte_kameru_spektrometra[l], hover_delay=500)
            Hovertip(self.showRef,langsStrings.zobrazit_v_pozadi_ref[l], hover_delay=500)
            Hovertip(self.showRoz,langsStrings.rozdiel_aktualneho[l], hover_delay=500)
            Hovertip(self.showPrie,langsStrings.podiel_aktualneho[l], hover_delay=500)
            Hovertip(self.lcontrolcamera,langsStrings.nastavit_roi[l], hover_delay=500)
            Hovertip(self.setCalButton,langsStrings.nastavenie_kal_a_ine[l], hover_delay=500)
            Hovertip(self.snapshotbtn,langsStrings.ulozit_graf_tabulku[l], hover_delay=500)
            Hovertip(self.lbpeak,langsStrings.min_vzdialenost_x[l], hover_delay=500)
            Hovertip(self.peakwidth,langsStrings.min_vzdialenost_x[l], hover_delay=500)

            Hovertip(self.axisXtitle,langsStrings.jednotkyosx[l], hover_delay=500)
            Hovertip(self.bshowPXNM,langsStrings.jednotkyosx[l], hover_delay=500)
            Hovertip(self.bshowPXNM2,langsStrings.jednotkyosx[l], hover_delay=500)

            Hovertip(self.bautoYbTitle,langsStrings.zapnut_autoY[l], hover_delay=500)
            Hovertip(self.bautoYb,langsStrings.zapnut_autoY[l], hover_delay=500)

            try:

                self.langlabel.configure(text=langsStrings.jazyk[l])
                self.lbl1.configure(text=langsStrings.px_a_nm[l])
                self.lbl2.configure(text=langsStrings.px_a_nm[l])
                self.lbl3.configure(text=langsStrings.px_a_nm[l])
                self.calbutton.configure(text=langsStrings.kalibracia[l])
            except:
                a=1
            self.setCalButton.configure(text=langsStrings.nastavenia_a_kalibracia[l])

            self.lbpeak.configure(text=langsStrings.sirka_vrcholu[l]+": "+str(int(self.peakwidth.get())))
            self.lbthresh.configure(text=langsStrings.prah[l]+": "+str(int(self.thresh.get())))

            self.stopbtn.configure(text="\u23F8 "+langsStrings.pozastavit[l])
            self.bcolorGraphb.configure(text=langsStrings.farby_v_grafe[l])

            stream = open('save.png', "rb")

            self.snapshotbtn.configure(text="\U0001F4BE "+langsStrings.ulozit[l]+"    ")
            self.options_spek2 = [langsStrings.len_spektrum[l],langsStrings.podiel[l],langsStrings.rozdiel[l]]
            self.clicked2Func.set(self.options_spek2[0])

            if(first == True):
                togglesettings()
        def removeSelectedFile2():

            self.vid.switchPRval = 2
            self.entryfile2.delete(0, END)
            self.entryfile2.insert(0, "")
            self.vid.entryfile_path2 = ""
            self.buttonfile2.grid(row=3,column=3)
            self.buttonremovefile2.grid_remove()
        def startMeasure():
            mmtostepsr = int(float(self.x1ofmeasure.get())/0.094)
            mmtostepsc = int(float(self.y1ofmeasure.get())/0.094)
            self.move = mmtostepsr*mmtostepsc

            thread = Thread(target = snapshot, args = (self.move, ))
            thread.start()

        def stopcam(aa=False):

            self.avvv = 0
            self.lang =  langvar.get()
            if(self.lang == "EN"):
                l = 1
            else:
                l = 0
            if(self.vid.stopcamvid == 1):
                self.vid.stopcamvid = 0
                self.stopbtn.configure(text="\u25B6 "+langsStrings.spustit[l])

            else:
                self.vid.stopcamvid = 1 
                self.stopbtn.configure(text="\u23F8 "+langsStrings.pozastavit[l])

            if(aa == True):

                toolbar.zoom()

        def snapshot(name="me-",fff=1):
            if(self.lang == "EN"):
                l = 1
            else:
                l = 0

            """

            time.sleep(1)

            """

            try:
                if(fff != 1):
                    for i in range(0,9):

                        time.sleep(0.5)
                    for i in range(0,14):

                        time.sleep(0.5)

                    for i in range(0,9):

                        time.sleep(0.5)
                    for i in range(0,22):

                        time.sleep(0.5)

                    time.sleep(0.5)
            except:
                a=1
            try:
                rows = int(float(self.x1ofmeasure.get())/0.1)

                columns = int(float(self.y1ofmeasure.get())/0.1)

            except:
                rows = 0
                columns = 0

            scanmap = []
            scanmap2 = []
            x = rows-1
            y = columns-1
            x1 = 0
            y1 = 0
            even = 1
            checky = 1

            for x1 in range(0,rows):
                row = 0 
                column = 1
                scanmap.append([row,column])
            for x1 in range(0,columns):

                row = 1
                column = 0

                scanmap.append([row,column])
                even = even + 1
                for y1 in range(0,rows):

                    column = 1
                    row = 0
                    if(even%2==1):
                        scanmap2.append([x1,y1])
                        scanmap.append([row,column])
                    else:
                        scanmap2.append([x1,x-y1])

                        scanmap.append([row,-column])

            self.scanmap = scanmap

            self.scanmap2 = scanmap2

            """
            if(self.nameofmeasure.get() != ""):
                if(self.nameofmeasure.get() != "Názov merania"):
                    foldername = self.nameofmeasure.get()
                else:
                    foldername = (datetime.now())
                    foldername = str((datetime.timestamp(foldername))).replace(".", "")
            else:
            """
            def do_Save():
                
                dt = str(datetime.now())
                ts = dt.split(" ")

                ts[1] = name+ts[1].split(".")[0].replace(":", "-")

                foldername = (ts[0])
                foldername = askdirectory()

                mkdirnumber = 0
                """
                while True:
                    try:
                        if(mkdirnumber == 0):

                            os.mkdir(foldername)
                        else:

                            os.mkdir(foldername+"("+str(mkdirnumber)+")")
                            foldername = foldername+"("+str(mkdirnumber)+")"
                        break
                    except:
                        mkdirnumber = int(mkdirnumber) + 1
                """
                try:
                    os.mkdir(foldername)
                except:
                    e=1
                allData = []
                dataX = []
                dataY = []
                dataZ = []
                dataXYZ = []
                dataX2 = []
                dataY2 = []
                dataZ2 = []
                dataXYZ2 = []
                if(rows < 0):
                    count_move_row = 1
                else:
                    count_move_row = -1
                if(columns < 0):
                    count_move_column = 1
                else:
                    count_move_column = -1

                if(len(self.scanmap) == 0):
                    self.scanmap = [[0,0]]
                for i in range(0,len(self.scanmap)):

                    ret, graphdata = self.vid.get_graph()
                    ret2, graphdata2 = self.vid.get_graph2()
                    ret2, framedata, framedata_org = self.vid.get_frame()

                    ret4, framedata4, framedata_org4 = self.vid.get_frame3()

                    try:

                        print(scanmap[i])
                        """
                        if(scanmap[i][0] == 0):
                            if(scanmap[i-1][0] < 0):

                                for i in range(0,14):

                                    time.sleep(0.1)
                            else:
                                for i in range(0,14):

                                    time.sleep(0.1)
                        """

                        """
                        if(scanmap2[i][0] == 0):
                            print("zmena smeru: ")
                            print(scanmap2[i-1][0])

                            if(scanmap2[i-1][0] > 0):

                            elif(scanmap2[i-1][0] < 0):

                        """       

                    except:
                        a= 0

                    if ret:
                        now = str(i)

                        if(self.neg1 == 2):

                            graphdata = graphdata2
                            framedata_org = framedata_org4
                        time.sleep(1)
                        self.fig.savefig(foldername+'/'+ts[1]+ '-G.png', transparent=False)
                        
                        cv2.imwrite(foldername+'/'+ts[1]+'.png',
                                    cv2.cvtColor(framedata_org, cv2.COLOR_BGR2RGB))

                        f = open(foldername+'/'+ts[1]+'.csv', 'w')
                        f.write('px,nm,Intensity,R,G,B\n')
                        print("tu")

                        ggg = 0
                        if(1==2):

                            dataX.append([])
                            dataY.append([])
                            dataZ.append([])
                            dataXYZ.append([])
                        pxx = 1
                        for x in zip(graphdata[1], graphdata[2]):
                            allData.append([i,x[0],x[1]])

                            try:

                                if(type(self.vid.justnm) == int):
                                    if(int(x[0]) == int(self.vid.justnm)):

                                        dataZ.append(x[1])

                                        dataY.append(self.scanmap2[i][0])
                                        dataX.append(self.scanmap2[i][1])

                                else:

                                    dataXYZ.append(x[0])
                                    dataZ.append(x[1])

                                    dataY.append(self.scanmap2[i][0])
                                    dataX.append(self.scanmap2[i][1])

                                ggg = 1
                            except:
                                try:
                                    dataZ[i].append(x[1])

                                    dataY[i].append(self.scanmap2[i][0])
                                    dataX[i].append(self.scanmap2[i][1])

                                except:

                                    a=1
                            #print("to:")
                            #print((graphdata[len(graphdata)-1])[0])            
                            f.write(str(pxx)+','+str(x[0])+','+str(x[1])+','+str((graphdata[len(graphdata)-1])[0][pxx-1][0])+','+str((graphdata[len(graphdata)-1])[0][pxx-1][1])+','+str((graphdata[len(graphdata)-1])[0][pxx-1][2])+'\n')
                            pxx = pxx + 1
                        f.close()
                        while True:
                            try:
                                if (open(foldername+"/"+ts[1]+".csv", "r")):
                                    break
                            except:
                                a=1
                        wb = Workbook()
                        ws = wb.active
                        abcrow = 0
                        newrow = []
                        with open(foldername+"/"+ts[1]+".csv", 'r') as f:
                            for row in csv.reader(f):
                                if(abcrow > 0):
                                    newrow = []
                                    for i in range(len(row)):
                                        newrow.append(float(row[i]))
                                    row = newrow
                                ws.append(row)
                                abcrow = abcrow + 1
                        wb.save(foldername+"/"+ts[1]+".xlsx")
                if(name == "ref-"):
                    self.entryfile22.delete(0,END)
                    self.entryfile22.insert(0, foldername+'/'+ts[1]+'.png')
                    self.entryfile22.xview("end")

                else:
                    foldername = foldername.replace("/", "\\")
                    print(r'explorer /open,"'+foldername+'"')
                    subprocess.Popen(r'explorer /open,"'+foldername+'"')
            def do_Save_click():
                do_Save()
            """
            self.modalcreatefolder = tkinter.Tk()
            self.modalcreatefolder.eval('tk::PlaceWindow . center')
            self.entryfname = customtkinter.CTkEntry(self.modalcreatefolder, width= 125)
            self.entryfname.grid(row=0,column=0)

            saveBut = customtkinter.CTkButton(self.modalcreatefolder, text="Uložiť",command=do_Save_click)
            saveBut.grid(row=0,column=1)
            saveBut.configure(text=langsStrings.ulozit[l])

            """
            do_Save_click()
            def showGraphEnd(dataX1,dataY1,dataZ1):

                fig = plt.figure()
                fig.set_figwidth(8)
                fig.set_figheight(8)

                ax = fig.add_subplot(111, projection='3d')
                ax.locator_params(integer=True)

                z_points = (dataZ1)

                x_points = dataX1

                y_points = dataY1

                colg = rgb = [0,0,0]##self.vid.wavelength_to_rgb(int(350))

                ax.plot(x_points, y_points, z_points)
                ax.set_xlim(left=0)
                ax.set_xlabel('y')
                ax.set_ylabel('x')
                ax.set_zlabel('z')

                global graph_win,canvas
                graph_win = tkinter.Tk()
                canvas = FigureCanvasTkAgg(fig, master=graph_win)
                canvas.get_tk_widget().grid(row=0,column=0)
                global graphslider

                graphslider = customtkinter.CTkSlider(graph_win, from_=350, to=850, orient="horizontal",tickinterval=50,length=900)

                graphslider.grid(row=1, column=0, sticky="nw")

                graphslider.set(350)
                canvas.draw()

                graph_win.mainloop()
            def reloadGraph3(event):
                reloadGraph2()
            def reloadGraph2():

                dataX2 = []
                dataY2 = []
                dataZ2 = []
                global graphslider,canvas,graph_win

                for i in range(len(dataXYZ)):
                    if(int(dataXYZ[i]) == int(graphslider.get())):
                        try:
                            dataX2.append(abs(dataX[i]-max(dataX))/10)
                            dataY2.append(dataY[i]/10)
                            dataZ2.append(dataZ[i])
                        except:
                            print(i)

                colg = rgb = [0,0,0]#self.vid.wavelength_to_rgb(int(graphslider.get()))

                z_points = (dataZ2)

                x_points = dataX2

                y_points = dataY2

                fig = plt.figure()
                fig.set_figwidth(8)
                fig.set_figheight(8)
                ax = fig.add_subplot(111, projection='3d')
                ax.locator_params(integer=True)

                gax = ax.plot(x_points, y_points, z_points)
                ax.set_xlim(left=0)

                ax.set_xlabel('y')
                ax.set_ylabel('x')
                ax.set_zlabel('z')
                canvas.get_tk_widget().grid_remove()
                canvas = FigureCanvasTkAgg(fig, master=graph_win)
                canvas.get_tk_widget().grid(row=0,column=0)

            def reloadGraph():
                try:
                    global graphslider

                except:
                    a=1
                for i in range(len(dataXYZ)):
                    try:
                        if(int(dataXYZ[i]) == 350):
                            dataX2.append(abs(dataX[i]-max(dataX))/10)

                            dataY2.append(int(dataY[i])/10)
                            dataZ2.append(dataZ[i])

                    except:
                        print(i)

            ggg = 1

        def switchPR(event,funcc):

            self.avvv = -10

            self.lang =  langvar.get()
            if(self.lang == "EN"):
                l = 1
            else:
                l = 0

            if(self.showRoz.get() == 1 and funcc == "Rozdiel"):
                try:
                    self.showPrie.deselect()
                except:
                    a=1
                self.vid.switchPRval = 1
                self.neg1 = 1
            elif(self.showPrie.get() == 1 and  funcc == "Priepustnosť"):
                try:
                    self.showRoz.deselect()
                except:
                    a=1
                self.vid.switchPRval = 0
                self.neg1 = 1
            elif(funcc == "Ref"):
                self.vid.showRefVal = 1
            else:
                self.vid.switchPRval = 2
                self.neg1 = 1
            if(self.showRef.get() == 0):
                self.vid.showRefVal = 0

        def showJustNM():

            try:
                self.vid.justnm = int(self.nm1ofmeasure.get())

            except:
                self.vid.justnm = None
        def changeOfCameraRGB(event):
            configdata["camrgb"] = int(self.clicked.get().split(":")[1])
            configtext = json.dumps(configdata)
            editConfigset(configtext)

            self.vid2.vid2.release()

            self.vid2.vid2 = cv2.VideoCapture(0, cv2.CAP_MSMF)
            self.vid2.vid2.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            self.vid2.vid2.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        def changeOfCameraSpectra(event):
            #print("aaaaaaaaaaa1")
            global laaang
            global cccaaa
            index = 0
            if(laaang == "EN"):
                l = 1
            else:
                l = 0
            if(self.drop2.get() == langsStrings.refresh[l]):

                cccaaa = returnCameraIndexes()
                self.drop2.configure(values=cccaaa)
                self.drop2.set(cccaaa[0])
            else:   
                try:
                    try:
                        configdata["camspect"] = int(self.drop2.get().split(":")[1])
                    except:
                        configdata["camspect"] = configdata["camspect"]#int(self.drop2.get().split(":")[1])
                    if(self.thread.is_alive() == False):
                        self.thread.start()

                    configtext = json.dumps(configdata)
                    editConfigset(configtext)
                    self.vid.vid.release()
                    self.vid.vid = cv2.VideoCapture(int(configdata["camspect"]), cv2.CAP_MSMF)
                    self.vid.vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
                    self.vid.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
                    #print("aaaaaaaaaaa")
                except:
                    #configdata["camspect"] = -1
                    a=1

        def showCalGraph(showornot):
            self.avvv = 0
            self.vid.calGraphShow_var = showornot
            print(self.vid.calGraphShow_var)
            if(self.vid.calGraphShow_var == "0"):
                self.fig.delaxes(self.plot1)
                try:
                    self.fig.delaxes(self.plot2)
                except:
                    a=1  
                self.plot1 = self.fig.add_subplot(111)
        def calHalogen(nieco=False):

            self.avvv = 0
            
            if(nieco == False):
                self.vid.halogen_var = self.halogen_var.get()
            #print(self.vid.halogen_var)
            if(self.vid.halogen_var == "0"):
                self.showRef.select()
            else:
                self.showRef.deselect()
        def switchMaxSum():
            self.avvv = 0
            self.vid.SumMax = self.SumMax_var.get()
            """
            if(self.vid.SumMax == "SUM"):
                self.vid.autoYgraph1 = False
            else:
                self.vid.autoYgraph1 = False
            print(self.vid.SumMax)
            """

        def saveKonst():
            try:
                self.vid.RKonst = float(self.REntry.get())
            except: 
                self.vid.RKonst = 1
            try:
                self.vid.GKonst = float(self.GEntry.get())
            except:
                self.vid.GKonst = 1
            try:
                self.vid.BKonst = float(self.BEntry.get())
            except:
                self.vid.BKonst = 1

            self.avvv  = 0
        def calHalogenWrite():
            selectRefer()
            
            self.avvv = 0

            self.vid.calHalnow = 1
            global laaang
            global cccaaa
            index = 0
            if(laaang == "EN"):
                l = 1
            else:
                l = 0
            tkinter.messagebox.showinfo(title=None, message=langsStrings.korekcia_je_vytvorena[l])
            self.modal.lift()
        def setFirstPos():
            engine(-self.move)
        def peakhold():
            if self.peakholdbtn.cget("bg") == 'yellow':
                self.peakholdbtn.configure(
                     bg="red")
                setattr(self.vid, 'holdpeaks', True)  
                self.filt.configure(state="disabled")
            else:
                self.peakholdbtn.configure(
                     bg="yellow")
                setattr(self.vid, 'holdpeaks', False)  
                self.filt.configure(state="active")
        def showMoreSettings():
            
            if(self.labelFunc.winfo_ismapped()):
                self.labelFunc.grid_remove()
                self.RLabel.grid_remove()
                self.GLabel.grid_remove()
                self.BLabel.grid_remove()
                self.REntry.grid_remove()
                self.GEntry.grid_remove()
                self.BEntry.grid_remove()
                self.SumRadio.grid_remove()
                self.MaxRadio.grid_remove()
                self.labelKonst.grid_remove()
                self.kostButton.grid_remove()
                self.korekciaTitle.grid_remove()
                self.halogenConfig.grid_remove()
                self.halogen.grid_remove()
                showCalGraph("1")
            else:
                showCalGraph("0")
                self.labelFunc.grid(row=0,column=3,padx=3,pady=3,columnspan=2,sticky="news")
                self.RLabel.grid(row=3,column=3,sticky="news")
                self.GLabel.grid(row=4,column=3,sticky="news")
                self.BLabel.grid(row=5,column=3,sticky="news")
                self.REntry.grid(row=3,column=4,sticky="w",padx=(0,20))
                self.GEntry.grid(row=4,column=4,sticky="w",padx=(0,20))
                self.BEntry.grid(row=5,column=4,sticky="w",padx=(0,20))
                self.SumRadio.grid(row=1,column=3,sticky="n",padx=(20,0))
                self.MaxRadio.grid(row=1,column=4,sticky="n",padx=(0,20))
                self.labelKonst.grid(row=2,column=3,padx=3,pady=3,columnspan=2,sticky="news")
                self.kostButton.grid(row=6,column=3,columnspan=2,sticky="n",padx=(0,20),pady=(10,0))
                self.korekciaTitle.grid(row=7,column=3,padx=3,pady=3,sticky="n",columnspan=2)
                self.halogenConfig.grid(row=8,column=3,padx=3,pady=3,sticky="w")
                self.halogen.grid(row=8,column=4,padx=3,pady=3,sticky="e")

        def openCalData():
            for i in range(len(self.allpx_input)):
                self.allpx_input[i].delete(0,END)
                self.allnm_input[i].delete(0,END)

        def on_modal_close():
            showCalGraph("0")
            self.modal.destroy()
        def togglesettings(more=False):
            
            try:
                self.modal.destroy()

            except:
                a = 1
            showCalGraph("1")
            self.modal = Toplevel(self.window)
            self.modal.protocol("WM_DELETE_WINDOW", on_modal_close)

            self.modal.title("Settings")

            global laaang
            laaang = langvar.get()
            if(self.lang == "EN"):
                l = 1
            else:
                l = 0

            self.allnm_input = []
            self.allpx_input = []
            self.calTitle = Label(self.modal, text="Kalibračné body",font='Helvetica 10 bold')
            self.calTitle.grid(row=0, column=0, sticky='n',columnspan=3)
            self.calTitle.configure(text=langsStrings.kalibracne_body[l])
            Hovertip(self.calTitle,langsStrings.kalibracne_body_tip[l], hover_delay=500)
            self.calPxTitle = Label(self.modal, text="px")
            self.calPxTitle.grid(row=1, column=1, sticky='w')
            self.calNmTitle = Label(self.modal, text="nm")
            self.calNmTitle.grid(row=1, column=2, sticky='w')

            #print(App.DEFAULT_CALIBRATION)

            new_cal = np.array(App.DEFAULT_CALIBRATION)

            row_sums = new_cal.sum(axis=1)
            order = np.argsort(row_sums)
            App.DEFAULT_CALIBRATION = new_cal[order].tolist()

            if(more == False):
                minmax = len(App.DEFAULT_CALIBRATION)
                if(len(App.DEFAULT_CALIBRATION)<3):
                    minmax = 3
            else:
                minmax = 15
            missig_inputs = minmax-len(App.DEFAULT_CALIBRATION)
            for i in range(minmax):
                if(more == False):
                    if(i<minmax):
                        Label(self.modal, text=langsStrings.px_a_nm[l]+" "+str(i+1)+":").grid(row=i+2, column=0, sticky='w',padx=3,pady=3)
                else:
                    Label(self.modal, text=langsStrings.px_a_nm[l]+" "+str(i+1)+":").grid(row=i+2, column=0, sticky='w',padx=3,pady=3)

            for i in range(minmax):
                self.allpx_input.append(Entry(self.modal, width=10))   
                self.allnm_input.append(Entry( self.modal,  width=10)) 

            def check(event):
                self.tempCal = (self.calibrate(True))
                if(len(self.tempCal)%2 == 0):
                    self.tempCal = np.array(self.tempCal).reshape(int(len(self.tempCal)/2), -1).tolist()
                else:
                    self.tempCal.append(0)
                    self.tempCal = np.array(self.tempCal).reshape(int(len(self.tempCal)/2), -1).tolist()

            for i in range(len(self.allpx_input)):

                self.allpx_input[i].bind('<KeyRelease>',check)
                self.allnm_input[i].bind('<KeyRelease>',check)
                if(more == False):
                    if(i<minmax):
                        self.allpx_input[i].grid(row=i+2, column=1, sticky='w',padx=3,pady=3)
                else:
                    self.allpx_input[i].grid(row=i+2, column=1, sticky='w',padx=3,pady=3)
                try:
                    self.allpx_input[i].delete(0,END)
                    if(App.DEFAULT_CALIBRATION != [[0.0, 0.0], [640.0, 640.0], [1280.0, 1280.0]]):
                        try:
                            self.allpx_input[i].insert(0,int(self.tempCal[i][0]))
                        except:
                            self.allpx_input[i].insert(0,int(App.DEFAULT_CALIBRATION[i][0]))
                except:
                    a=1
                if(more == False):
                    if(i<minmax):
                        self.allnm_input[i].grid(row=i+2, column=2, sticky='w',padx=3,pady=3)
                else:
                    self.allnm_input[i].grid(row=i+2, column=2, sticky='w',padx=3,pady=3)
                try:
                    self.allnm_input[i].delete(0,END)
                    if(App.DEFAULT_CALIBRATION != [[0.0, 0.0], [640.0, 640.0], [1280.0, 1280.0]]):
                        try:
                            self.allnm_input[i].insert(0,round(float(self.tempCal[i][1]),2))
                        except:
                            self.allnm_input[i].insert(0,round(float(App.DEFAULT_CALIBRATION[i][1]),2))
                except:
                    a=1

            if(more == False):
                self.showmoreCal = Button(self.modal, text="Zobraziť viac", command=lambda:togglesettings(True))
                self.showmoreCal.grid(row=i+3, column=0, sticky='w',padx=3,pady=3)
                self.showFormatCal = Label(self.modal, text="###.###")
                self.showmoreCal.configure(text=langsStrings.zobrazit_viac[l])

                self.opencaldata = Button(self.modal, text="Vymazať kal. dáta", command=openCalData)
                self.opencaldata.grid(row=i+4, column=0, sticky='w',padx=3,pady=3)
                i = i + 1
            else:
                self.showmoreCal = Button(self.modal, text="Zobraziť menej", command=lambda:togglesettings(False))
                self.showmoreCal.grid(row=i+3, column=0, sticky='w',padx=3,pady=3)
                self.showFormatCal = Label(self.modal, text="###.###")

                self.showmoreCal.configure(text=langsStrings.zobrazit_menej[l])

                self.opencaldata = Button(self.modal, text="Vymazať kal. dáta", command=openCalData)
                self.opencaldata.grid(row=i+4, column=0, sticky='w',padx=3,pady=3)
                i = i + 1
            i = i + 1
            self.opencaldata.configure(text=langsStrings.vymazat_kal_data[l])
            Hovertip(self.showFormatCal,langsStrings.kal_format_tip[l], hover_delay=500)
            iconLoadCaltoFile=PhotoImage(file="import.png")
            self.calbuttonUpload = customtkinter.CTkButton(self.modal,image=iconLoadCaltoFile, text="Nahrať\nkalibračný súbor", width=6,
                                            bg="red", command=lambda:[loadCalFile()],text_font=(None,9))
            self.calbuttonUpload.configure(text=langsStrings.nahrat_kalibracny_subor[l])
            self.calbuttonUpload.grid(row=i+3, column=0,columnspan=2,padx=3,pady=3,sticky='news')
            self.calbutton = customtkinter.CTkButton(self.modal, text="Kalibrácia", width=6,
                                            bg="red", command=lambda:[self.calibrate()],text_font=(None,9))

            iconSaveCaltoFile=PhotoImage(file="export.png")
            self.calToSavebutton = customtkinter.CTkButton(self.modal,image=iconSaveCaltoFile, text="KALIBROVAŤ ", width=6,
                                            bg="red", command=lambda:[self.calibrate()],text_font=(None,9))
            self.calToSavebutton.grid(row=i+3, column=2,padx=3,pady=3,sticky='news')
            self.calToSavebutton.configure(text=langsStrings.kalibrovat[l])
            self.labelFunc = customtkinter.CTkLabel(self.modal,text="Funkcie",text_font='Helvetica 10 bold')
            self.labelFunc.configure(text=langsStrings.funkcie[l])
            Hovertip(self.calbuttonUpload,langsStrings.nahrat_kalibracny_subor_tip[l], hover_delay=500)
            Hovertip(self.calToSavebutton,langsStrings.kalibrovat_tip[l], hover_delay=500)

            try:
                self.SumMax_var = customtkinter.StringVar(value=self.vid.SumMax)
            except:
                self.SumMax_var = customtkinter.StringVar(value="MAX")
            self.MaxRadio = customtkinter.CTkRadioButton(self.modal,text="MAX(RGB)",command=switchMaxSum,variable=self.SumMax_var, value="MAX",text_font=(None,9))
            self.SumRadio = customtkinter.CTkRadioButton(self.modal,text="SUM(RGB)",command=switchMaxSum,variable=self.SumMax_var, value="SUM",text_font=(None,9))

            self.labelKonst = customtkinter.CTkLabel(self.modal,text="Konštanty")
            self.labelKonst.configure(text=langsStrings.konstanty[l])

            self.RLabel = tkinter.Label(self.modal,text="R:")

            self.REntry = tkinter.Entry(self.modal)
            try:
                self.REntry.delete(0, END)
                self.REntry.insert(0, self.vid.RKonst)
            except:
                self.REntry.delete(0, END)
                self.REntry.insert(0, 1)

            self.GLabel = tkinter.Label(self.modal,text="G:")

            self.GEntry = tkinter.Entry(self.modal)
            try:
                self.GEntry.delete(0, END)
                self.GEntry.insert(0, self.vid.GKonst)
            except:
                self.GEntry.delete(0, END)
                self.GEntry.insert(0, 1)

            self.BLabel = tkinter.Label(self.modal,text="B:")

            self.BEntry = tkinter.Entry(self.modal)
            try:
                self.BEntry.delete(0, END)
                self.BEntry.insert(0, self.vid.BKonst)
            except:
                self.BEntry.delete(0, END)
                self.BEntry.insert(0, 1)

            self.kostButton = customtkinter.CTkButton(self.modal,width=10,text="Uložiť konštanty",command=saveKonst,text_font=(None,9))
            self.kostButton.configure(text=langsStrings.ulozit_konstanty[l])

            self.korekciaTitle = customtkinter.CTkLabel(self.modal,text="Korekcia",text_font='Helvetica 10 bold')
            self.korekciaTitle.configure(text=langsStrings.korekcia[l])

            """
            try:

                self.halogen_var = customtkinter.StringVar(value=self.vid.halogen_var)
            except:
                a=1
                self.halogen_var = customtkinter.StringVar(value=1)
            """
            try:
                dajsem = int(self.halogen.get())

            except:
                #print("nejde")
                self.halogen_var = customtkinter.StringVar(value=0)
            self.halogen = customtkinter.CTkSwitch(self.modal,text="Korekcia",command=calHalogen,variable=self.halogen_var, onvalue=1, offvalue=0,text_font=(None,9))
            self.halogen.configure(text=langsStrings.korekcia[l])
            Hovertip(self.halogen,langsStrings.korekcia_tip[l], hover_delay=500)
            try:
                if(dajsem==1):

                    self.halogen.select()
                    self.vid.halogen_var = "0"
                    self.avvv = 0

            except:
                print("nejde2")
            self.halogenConfig = customtkinter.CTkButton(self.modal,width=10,text="Vytvoriť korekciu",command=calHalogenWrite,text_font=(None,9))
            self.halogenConfig.configure(text=langsStrings.vytvorit_korekciu[l])

            self.langlabel = customtkinter.CTkLabel(self.modal, text="Jazyky",text_font='Helvetica 10 bold')
            self.langlabel.grid(row=i+5, column=0, columnspan=2, sticky="n",padx=3,pady=3)
            self.moreSettingsSwitch = customtkinter.CTkSwitch(self.modal, text="Rozšírené\nnastavenia",text_font='Helvetica 10 bold',command=showMoreSettings)
            self.moreSettingsSwitch.grid(row=i+5, column=2, padx=3,pady=3,rowspan=2)
            self.moreSettingsSwitch.configure(text=langsStrings.rozsirene_nastavenia[l])
            self.langs = ["EN","SK"]
            rowlang = 7
            columnlang = -1

            customtkinter.CTkRadioButton(self.modal,text=self.langs[0],variable=langvar,value = self.langs[0],command= lambda: selectLang(True)).grid(row=(i+6),column=0,padx=3,pady=(3,10))
            customtkinter.CTkRadioButton(self.modal,text=self.langs[1],variable=langvar,value = self.langs[1],command= lambda: selectLang(True)).grid(row=(i+6),column=1,padx=3,pady=(3,10))
            self.langlabel.configure(text=langsStrings.jazyk[l])
            self.calbutton.configure(text=langsStrings.kalibracia[l])
            """
            if(self.control_frame.grid_info() == {}):
                self.control_frame.grid(row=2, column=0, padx=0,pady=(0,10),sticky="news")
            else:
                self.control_frame.grid_remove()
            """
            self.window.after_cancel(after_id)
        with open(calData) as f:
            lines = f.readlines()
        if(len(lines) == 0):

            after_id = self.window.after(5000, togglesettings)

        def switchCam():
            camspect = configdata["camspect"]
            camrgb = configdata["camrgb"]
            configdata["camspect"] = int(camrgb)
            configdata["camrgb"] = int(camspect)
            configtext = json.dumps(configdata)
            editConfigset(configtext)
            self.vid.vid.release()
            self.vid2.vid2.release()
            self.vid.vid = cv2.VideoCapture(int(configdata["camspect"]), cv2.CAP_MSMF)
            self.vid.vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            self.vid.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

            self.vid2.vid2 = cv2.VideoCapture(int(configdata["camrgb"]), cv2.CAP_MSMF)
            self.vid2.vid2.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            self.vid2.vid2.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            self.clicked.set( "kamera:"+ str(int(configdata["camrgb"])) )
            self.clicked2.set( "kamera:"+ str(int(configdata["camspect"])) )
        def resizeWin2(a):
            print("Win2")

            self.window.grid_columnconfigure(1, weight=1)

            self.top_frame.grid_columnconfigure(0, weight=1)

            self.bottom_frame.grid_columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

            dpi = window.winfo_fpixels('1i')

            if(dpi<100):
                self.bottom_frame.grid_rowconfigure(1, weight=1)
            else:   
                self.bottom_frame.grid_rowconfigure((1,6), weight=1)

            self.control_frame_cam4.grid_propagate(0)
            self.control_frame_cam4.grid_columnconfigure((0,1,2,3,4), weight=1)

            self.moveline.configure(height=100)
            self.heightline.configure(height=100)
            self.setexposure.configure(height=100)
            self.moveline4.configure(height=100)
            self.heightline3.configure(height=100)
            self.control_frame_cam.grid_columnconfigure((0,1,2,3,4), weight=1)

            self.cameraframe.grid_propagate(0)
            self.cameraframe.grid_columnconfigure((0,1,2,3,4), weight=1)
            self.cameraframe.grid_rowconfigure((0), weight=1)

            self.control_frame_cam41.grid_propagate(0)
            self.control_frame_cam41.grid_columnconfigure((0,1,2,3,4), weight=1)

        self.get_width_prev = ""
        self.get_height_prev = ""
        def resizeWin_left(event):

            get_width_now = window.winfo_y()
            get_height_now = window.winfo_x()
            if(get_width_now == self.get_width_prev or get_height_now == self.get_height_prev):

                self.bottom_frame.configure(height=(int(window.winfo_height())))
                self.top_frame.configure(height=(int(window.winfo_height())))

                if(self.top_frame.winfo_width()<300):
                    self.top_frame.configure(width=300)
                self.bbox = self.plot1.get_window_extent().transformed(self.fig.dpi_scale_trans.inverted())
                self.dpi = window.winfo_fpixels('1i')

                self.canvascrop.config(width=int((self.bbox.width/(self.dpi/100))*self.dpi))
                self.camcrop.configure(bg_color="black")

            self.get_width_prev = get_width_now
            self.get_height_prev = get_height_now
        def resizeWin(event):

            if(int(window.winfo_width()) !=self.mainwidth_prev):

                percentwidth = 250/1920
                max_width_frame = int(window.winfo_width()/6)
                max_height_frame = int(window.winfo_height()/3)
                dpi = window.winfo_fpixels('1i')

                self.widthC1 = int(window.winfo_width())
                self.heightC1 = int(window.winfo_height()/2.2)

                self.bottom_frame.configure(height=self.heightC1)
                self.bottom_frame.configure(height=self.widthC1)
                if(dpi >110):
                    max_height_frame = 290
                    max_width_frame = int(abs(max_width_frame*(1-((dpi-100)/100))))

                if(max_height_frame>320):
                    max_height_frame = 320

                max_width_frame_s = max_width_frame
                if(window.winfo_width() > 2000):
                    max_width_frame = int(window.winfo_width()/8)
                    max_width_frame_s = max_width_frame
                if(window.winfo_width() < 2000):
                    max_width_frame_s = max_width_frame*1.5
                if(window.winfo_width() < 1400):
                    max_height_frame = 200
                    max_width_frame = int(window.winfo_width()/6)

                    self.canvas0.configure(height=max_height_frame*0.3)
                    self.canvas2.configure(height=max_height_frame*0.3)
                    for widget in self.control_frame_cam.winfo_children():

                        try:
                            widget.configure(font='Helvetica 7 bold')
                        except:
                            a=1

                    for widget in self.control_frame_cam4.winfo_children():

                        try:
                            widget.configure(font='Helvetica 7 bold')
                        except:
                            a=1
                    for widget in self.control_frame_camcal.winfo_children():

                        try:
                            widget.configure(font='Helvetica 7 bold')
                        except:
                            a=1

                if(window.winfo_width() > 1920):    
                    max_width_frame_s = max_width_frame_s*1.1
                else:
                    max_width_frame_s = max_width_frame_s*0.85
                slider_offset = 180
                frame_offset = 10
                self.top_frame.configure(width=max_width_frame)
                self.control_frame_cam.configure(width=max_width_frame)
                self.control_frame_cam4.configure(width=int(max_width_frame*0.85))
                self.control_frame_camcal.configure(width=int(max_width_frame_s))
                self.canvas0.configure(width=max_width_frame)
                self.canvas2.configure(width=max_width_frame)

                self.cameraframe.configure(width=max_width_frame)
                self.control_frame_cam41.configure(width=max_width_frame)

                self.top_frame.configure(height=max_height_frame+frame_offset)

                self.control_frame_cam4.configure(height=max_height_frame)
                self.control_frame_camcal.configure(height=max_height_frame)

                self.cameraframe.configure(height=max_height_frame)
                self.control_frame_cam41.configure(height=max_height_frame)

                self.moveline.configure(height=max_height_frame-slider_offset)
                self.heightline.configure(height=max_height_frame-slider_offset)
                self.setexposure.configure(height=max_height_frame-slider_offset)
                self.moveline4.configure(height=max_height_frame-slider_offset)
                self.heightline3.configure(height=max_height_frame-slider_offset)
            self.mainwidth_prev = int(window.winfo_width())

        self.top_frame = customtkinter.CTkFrame(window)
        self.top_frame.grid(row=0, column=0, sticky='nwse')

        self.bottom_frame = customtkinter.CTkFrame(window)
        self.bottom_frame.grid(row=0, column=1,sticky="nwse")
        self.bottom_frameO = customtkinter.CTkFrame(self.bottom_frame)
        self.bottom_frameO.grid(row=4, column=1,sticky="n",rowspan=3,pady=10)

        self.control_frame_cam1 = customtkinter.CTkFrame(self.top_frame)

        self.decoration = tkinter.Canvas( 
            self.top_frame, width=317, height=178, borderwidth=0, relief="sunken")

        self.setSwitchCamButton = customtkinter.CTkButton(self.top_frame, text="Prepnúť kamery", command=switchCam)

        options = self.cameras_list

        self.clicked = StringVar()

        self.clicked.set( "kamera:"+ str(int(configdata["camrgb"])) )

        self.drop = OptionMenu( self.top_frame , self.clicked , *options, command = changeOfCameraRGB )

        if args.calibration is not None:
            self.marker1.configure(text=str(args.calibration[0][0]))
            self.marker2.configure(text=str(args.calibration[1][0]))
            self.marker3.configure(text=str(args.calibration[2][0]))
            self.txt1.insert(0, str(args.calibration[0][1]))
            self.txt2.insert(0, str(args.calibration[1][1]))
            self.txt3.insert(0, str(args.calibration[2][1]))
            self.calibrate()  

        langvar = tkinter.StringVar()
        self.offpeak_var = tkinter.StringVar(value="off")
        var1 = tkinter.IntVar()
        var2 = tkinter.IntVar()
        var1.set(1)
        var2.set(0)
        langvar.set(configdata["lang"])

        def defBackground():
            self.avvv = 0
            self.switchBackground.configure(state="normal")

            self.vid.getBG = 1
            tkinter.messagebox.showinfo(title=None, message="Pozadie je definované")

        def removeBackground():
            self.avvv = 0

            if(int(self.setBG_var.get()) == 0):
                self.setBG = False
            else:
                self.setBG = True
            self.vid.setBG = self.setBG

            self.avvv = 0
        def checkZoom(event_ax):
            print("zoom")
            print(event_ax.get_xlim())
        def clickOnCamera(eventorigin):
            x = eventorigin.x
            y = eventorigin.y
            self.moveline.set(((y*4))-2)

            moveline_cb(1)
        self.cameraframe = customtkinter.CTkFrame(self.top_frame)
        self.cameraframe.grid(row=0,column=0,sticky="news",pady=10,padx=10)
        self.canvas0 = customtkinter.CTkCanvas(
            self.cameraframe, width=317, height=178, borderwidth=0, relief="sunken")
        self.canvas0.grid(row=1, column=3,columnspan=3, sticky="n",pady=(10,0),padx=(10,10))
        self.canvas0.bind("<Button-1>",clickOnCamera)
        self.titleofspec = customtkinter.CTkLabel(self.cameraframe,text="Nastavenie spektra",text_font='Helvetica 10 bold')
        self.titleofspec.grid(row=0,column=2,sticky="n",pady=(10,0),padx=(10,10),columnspan=3)
        self.titleofsource = customtkinter.CTkLabel(self.cameraframe,text="Zdroj",text_font='Helvetica 10 bold')
        self.titleofsource.grid(row=2,column=2,sticky="n",pady=(5,0),padx=(10,10),columnspan=3)
        self.checkselect = customtkinter.CTkRadioButton(self.cameraframe,text="Zobraziť v grafe",variable=var1,value = 1,command=selectSpect)

        self.options_spek2 = ["Len spektrum","Rozdiel","Podiel","Kombinácia"]

        self.clicked2Func = StringVar()

        self.clicked2Func.set(self.options_spek2)

        self.dropFunc2 = customtkinter.CTkOptionMenu( self.cameraframe , values=self.options_spek2 , command = switchPR,text_font=(None,9) )

        self.dropFunc2.configure(state="disabled")
        self.setBG_var = customtkinter.StringVar(value=True)
        self.switchBackground = customtkinter.CTkSwitch( self.cameraframe, text="Pozadie" ,command=removeBackground,variable=self.setBG_var, onvalue=True, offvalue=False)

        self.defBackground = customtkinter.CTkButton( self.cameraframe, text="Definovať pozadie",command=defBackground )

        self.control_frame_cam = customtkinter.CTkFrame(self.top_frame)
        self.control_frame_cam.grid(row=2, column=0,sticky="news",pady=0,padx=10)
        self.titleoffunc = customtkinter.CTkLabel(self.cameraframe,text="Operácie",text_font='Helvetica 10 bold')
        self.titleoffunc.grid(row=6,column=2,sticky="n",pady=(5,0),padx=(10,10),columnspan=3)
        self.showRef  =  customtkinter.CTkSwitch(self.cameraframe,text="Zobraziť ref. sp.",command = lambda:switchPR(1,"Ref"))
        self.showRef.grid(row=7,column=4,sticky="w",rowspan=2)
        self.showPrie  =  customtkinter.CTkSwitch(self.cameraframe,text="Priepustnosť",command = lambda:switchPR(1,"Priepustnosť"))
        self.showPrie.grid(row=9,column=4,sticky="w",pady=(0,20))
        self.showRoz  =  customtkinter.CTkSwitch(self.cameraframe,text="Rozdiel",command = lambda:switchPR(1,"Rozdiel"))
        self.showRoz.grid(row=10,column=4,sticky="w",pady=(0,20))
        self.selectRef = customtkinter.CTkButton(self.cameraframe,width=30,text="Referenčné spektrum",command=selectRefer,text_font=(None,9))
        self.selectRef.grid(row=7,column=3,pady=10)
        self.pridatCiary = customtkinter.CTkButton(self.cameraframe,width=30,text="Pridať riadky",command=addRows,text_font=(None,9))
        #self.pridatCiary.grid(row=8,column=3,rowspan=2)
        self.odobratCiary = customtkinter.CTkButton(self.cameraframe,width=30,text="Odobrať riadky",command=deleteRows,text_font=(None,9))
        #self.pridatCiary.grid(row=8,column=3,pady=10,rowspan=2)
        self.pridatCiaryN = customtkinter.CTkEntry(self.cameraframe,width=100,text="Každy N-tý",text_font=(None,9))
        #self.pridatCiaryN.grid(row=10,column=3)
        self.pridatCiaryN.insert(0, 50)
        self.buttonfile = customtkinter.CTkButton(self.cameraframe,text="Vyberte spektrum",command=selectFile,text_font=(None,9))
        self.buttonfile.grid(row=3,column=3,padx=10,pady=10)

        self.buttonremovefile = customtkinter.CTkButton(self.cameraframe,text="Pustiť živý obraz",command=removeSelectedFile,text_font=(None,9))

        self.titleoffile = customtkinter.CTkLabel(self.cameraframe,text="Názov súboru:",text_font='Helvetica 10')
        self.titleoffile.grid(row=4,column=3,sticky="w",pady=(0,0))
        self.entryfile = tkinter.Entry(self.cameraframe)
        self.entryfile.grid(row=5,column=3)
        self.entryfile22 = tkinter.Entry(self.cameraframe)

        options2 = self.cameras_list

        self.clicked2 = StringVar()

        self.clicked2.set( "kamera: "+str(int(configdata["camspect"])) )

        self.drop2 = customtkinter.CTkOptionMenu( self.cameraframe , values=options2, command = changeOfCameraSpectra,text_font=(None,9) )
        self.drop2.grid(row=3,column=4,pady=5,padx=10)
        changeOfCameraSpectra(1)
        self.control_frame_cam4 = customtkinter.CTkFrame(self.top_frame)

        self.control_frame_cam41 = customtkinter.CTkFrame(self.top_frame)

        self.control_frame_camcal = customtkinter.CTkFrame(self.top_frame)
        self.control_frame_camcal.grid(row=4, column=0,sticky="news",pady=10,padx=10)
        self.control_frame_camcale = customtkinter.CTkFrame(self.top_frame)

        self.lcontroltitle = customtkinter.CTkLabel(self.control_frame_camcal, text="Kalibrácia spektrometra",text_font='Helvetica 10 bold')
        self.lcontroltitle.grid(row=0, column=0,columnspan=2)
        self.control_frame = customtkinter.CTkFrame(self.control_frame_camcal)
        self.setCalButton = customtkinter.CTkButton(self.control_frame_camcal, text="Nastavenia a kalibrácía", command=togglesettings,width=100)
        self.setCalButton.grid(row=1, column=0,sticky="news",padx=10,pady=10)
        self.calGraphShow_var = customtkinter.StringVar(value=1)
        self.calGraphShow = customtkinter.CTkSwitch(self.control_frame_camcal,text="Kalibračná krivka",command=showCalGraph,variable=self.calGraphShow_var, onvalue=0, offvalue=1,text_font=(None,9))

        self.clrbutton = customtkinter.CTkButton(
            self.control_frame_camcal, text="Vymazať kalibráciu", command=clear_points)
        self.lcontrolcamera2 = customtkinter.CTkLabel(self.control_frame_cam4, text="Ovládanie statického spektra",text_font='Helvetica 10 bold')
        self.lcontrolcamera2.grid(row=0, column=0,columnspan=2)
        self.lmoveline2 = customtkinter.CTkLabel(self.control_frame_cam4, text="Riadok →" )
        self.lmoveline2.grid(row=1, column=0, pady=(0,0), sticky="n")
        self.moveline_v4 = customtkinter.CTkLabel(
            self.control_frame_cam4,text=50
        )

        self.moveline_v4.grid(row=2, column=0, sticky="wn")
        self.bplusmoveline4 = customtkinter.CTkButton(
            self.control_frame_cam4, text="+", command=lambda: moveline4_cb("plus"),width=1
        )
        self.bplusmoveline4.grid(row=3, column=0, padx=37, pady=2)
        self.bminusmoveline4 = customtkinter.CTkButton(
            self.control_frame_cam4, text="-", command=lambda: moveline4_cb("minus"),width=1
        )
        self.bminusmoveline4.grid(row=5, column=0, padx=37, pady=10)

        self.moveline4 = customtkinter.CTkSlider(
            self.control_frame_cam4, from_=358, to=1, orient="vertical", command=moveline4_cb
        )
        self.moveline4.grid(row=4, column=0, padx=13, pady=0, sticky="n")
        self.moveline4.set(50)

        self.lheightline3 = customtkinter.CTkLabel(self.control_frame_cam4, text="Počet riadkov:")
        self.lheightline3.grid(row=1, column=1, pady=0, sticky="n")

        self.moveline_v5 = customtkinter.CTkLabel(
            self.control_frame_cam4,text="1"
        )

        self.moveline_v5.grid(row=2, column=1, sticky="wn")
        self.bplusheightline3 = customtkinter.CTkButton(
            self.control_frame_cam4, text="+", command=lambda: heightline_cb2("minus"),width=1
        )
        self.bplusheightline3.grid(row=3, column=1, padx=10, pady=2)
        self.bminusheightline3 = customtkinter.CTkButton(
            self.control_frame_cam4, text="-", command=lambda: heightline_cb2("plus"),width=1
        )
        self.bminusheightline3.grid(row=5, column=1, padx=0, pady=2)
        self.heightline3 = customtkinter.CTkSlider(
            self.control_frame_cam4, from_=1, to=100, orient="vertical", command=heightline_cb2
        )
        self.heightline3.grid(row=4, column=1, padx=9, pady=0, sticky="n")
        self.heightline3.set(1)

        self.canvas2 = customtkinter.CTkCanvas(
            self.control_frame_cam41, width=317, height=178, borderwidth=0, relief="sunken")
        self.canvas2.grid(row=0, column=0,columnspan=3, sticky="n",pady=(10,0),padx=(10,10))

        self.checkselect2 = customtkinter.CTkRadioButton(self.control_frame_cam41,text="Zobraziť v grafe",variable=var1,value = 2,command=selectSpect)
        self.checkselect2.grid(row=4,column=0,pady=10,columnspan=2)
        self.buttonfile2 = customtkinter.CTkButton(self.control_frame_cam41,text="Vyberte spektrum",command=selectFile2)
        self.buttonfile2.grid(row=3,column=3)
        self.buttonremovefile2 = customtkinter.CTkButton(self.control_frame_cam41,text="Vymazať",command=removeSelectedFile2)
        self.entryfile2 = customtkinter.CTkEntry(self.control_frame_cam41)
        self.entryfile2.grid(row=3,column=0)

        """
        self.options_spek2 = ["Len spektrum","Rozdiel","Podiel","Kombinácia"]

        self.clicked2Func = StringVar()

        self.clicked2Func.set(self.options_spek2)

        self.dropFunc2 = customtkinter.CTkOptionMenu( self.control_frame_cam41 , values=self.options_spek2 , command = switchPR )
        self.dropFunc2.grid(row=2, column=1, padx=0, pady=10)

        self.control_frame_cam = customtkinter.CTkFrame(self.top_frame)
        self.control_frame_cam.grid(row=1, column=0,sticky="news",pady=10,padx=10)
        """

        self.lrotation = customtkinter.CTkLabel(self.control_frame_cam, text="Rotácia:")

        self.rotation = customtkinter.CTkSlider(
            self.control_frame_cam, from_=0, to=360, orient="vertical", command=rotate_cb
        )

        self.rotation.set(0)

        self.lcontrolcamera = customtkinter.CTkLabel(self.control_frame_cam, text="Ovládanie spektrometra", width=20,text_font='Helvetica 10 bold')
        self.lcontrolcamera.grid(row=0, column=0,columnspan=3)
        variable = StringVar(self.control_frame_cam)
        variable.set("one") 

        crosscolorarray = [("Biely kríž", 1),
            ("Čierny kríž", 2),

             ]

        rowradio = 1

        self.lmoveline = customtkinter.CTkLabel(self.control_frame_cam, text="Riadok →")
        self.lmoveline.grid(row=1, column=0)
        self.bplusmoveline = customtkinter.CTkButton(
            self.control_frame_cam, text="+", command= lambda: moveline_cb("plus"),width=1
        )
        self.bplusmoveline.grid(row=3, column=0)
        self.bminusmoveline = customtkinter.CTkButton(
            self.control_frame_cam, text="-", command=lambda: moveline_cb("minus"),width=1
        )
        self.bminusmoveline.grid(row=5, column=0, pady=(5,10))

        self.moveline = customtkinter.CTkSlider(
            self.control_frame_cam, from_=720, to=1, orient="vertical", command=moveline_cb
        )
        self.moveline.grid(row=4, column=0)
        self.moveline_v = customtkinter.CTkLabel(
            self.control_frame_cam,text="100"
        )
        self.moveline_v.configure(text=str(720-int(configdata["moveline"])))
        self.moveline_v.grid(row=2, column=0)
        self.moveline.set(configdata["moveline"])

        self.lheightline = customtkinter.CTkLabel(self.control_frame_cam, text="Počet riadkov:")
        self.lheightline.grid(row=1, column=1)
        self.moveline_v2 = customtkinter.CTkLabel(
            self.control_frame_cam,text="100"
        )
        self.moveline_v2.configure(text=str(int(configdata["heightline"])))
        self.moveline_v2.grid(row=2, column=1, sticky="wn")
        self.bplusheightline = customtkinter.CTkButton(
            self.control_frame_cam, text="+", command=lambda: heightline_cb("minus"),width=1
        )
        self.bplusheightline.grid(row=3, column=1)
        self.bminusheightline = customtkinter.CTkButton(
            self.control_frame_cam, text="-", command=lambda: heightline_cb("plus"),width=1
        )
        self.bminusheightline.grid(row=5, column=1)
        self.heightline = customtkinter.CTkSlider(
            self.control_frame_cam, from_=1, to=100, orient="vertical", command=heightline_cb
        )
        self.heightline.grid(row=4, column=1)
        self.heightline.set(configdata["heightline"])

        self.lsetexposure = customtkinter.CTkLabel(self.control_frame_cam, text="Expozícia:")
        self.lsetexposure.grid(row=1, column=2)
        self.moveline_v3 = customtkinter.CTkLabel(
            self.control_frame_cam,text="-3"
        )

        self.moveline_v3 = customtkinter.CTkLabel(
            self.control_frame_cam,text="-3"
        )

        self.moveline_v3.grid(row=2, column=2, sticky="wn")
        self.bplussetexposure = customtkinter.CTkButton(
            self.control_frame_cam, text="+", command=lambda: setexposure_cb("minus"),width=1
        )
        self.bplussetexposure.grid(row=3, column=2)
        self.bminussetexposure = customtkinter.CTkButton(
            self.control_frame_cam, text="-", command=lambda: setexposure_cb("plus"),width=1
        )
        self.bminussetexposure.grid(row=5, column=2)
        self.setexposure = customtkinter.CTkSlider(
            self.control_frame_cam, from_=-11, to=0, orient="vertical", command=setexposure_cb
        )
        self.setexposure.grid(row=4, column=2)
        self.setexposure.set(-3)

        self.buttonSetGain = customtkinter.CTkSwitch(self.control_frame_cam,text="Vysoká citlivosť",command=openSettingsCam)
        self.buttonSetGain.grid(row=6, column=1,columnspan=2,pady=5)
        """

        self.lsetgain = customtkinter.CTkLabel(self.control_frame_cam, text="Gain:")
        self.lsetgain.grid(row=1, column=3)
        self.moveline_vG = customtkinter.CTkLabel(
            self.control_frame_cam,text="-3"
        )

        self.moveline_vG.grid(row=2, column=3, sticky="wn")
        self.bplussetgain = customtkinter.CTkButton(
            self.control_frame_cam, text="+", command=lambda: setgain_cb("minus"),width=1
        )
        self.bplussetgain.grid(row=3, column=3)
        self.bminussetgain = customtkinter.CTkButton(
            self.control_frame_cam, text="-", command=lambda: setgain_cb("plus"),width=1
        )
        self.bminussetgain.grid(row=5, column=3)
        self.setgain = customtkinter.CTkSlider(
            self.control_frame_cam, from_=-127, to=127, orient="vertical", command=setgain_cb
        )
        self.setgain.grid(row=4, column=3)
        self.setgain.set(-1)

        """

        self.lsetexposure2 = customtkinter.CTkLabel(self.control_frame_cam1, text="Expozícia:")
        self.lsetexposure2.grid(row=1, column=2, pady=10, sticky="n")
        self.bplussetexposure2 = customtkinter.CTkButton(
            self.control_frame_cam1, text="+", command=lambda: setexposure2_cb("plus"),width=1
        )
        self.bplussetexposure2.grid(row=2, column=2, padx=10, pady=2)
        self.bminussetexposure2 = customtkinter.CTkButton(
            self.control_frame_cam1, text="-", command=lambda: setexposure2_cb("minus"),width=1
        )
        self.bminussetexposure2.grid(row=4, column=2, padx=0, pady=2)
        self.setexposure2 = customtkinter.CTkSlider(
            self.control_frame_cam1, from_=-1, to=-7, orient="vertical", command=setexposure2_cb
        )
        self.setexposure2.grid(row=3, column=2, padx=3, pady=0, sticky="nw")
        self.setexposure2.set(-3)

        self.lbrightness = customtkinter.CTkLabel(self.control_frame_cam, text="Jas:")

        self.bplusbrightness = customtkinter.CTkButton(
            self.control_frame_cam, text="+", command=moveline2_cb,width=1
        )

        self.bminusbrightness = customtkinter.CTkButton(
            self.control_frame_cam, text="-", command=moveline2_cb,width=1
        )

        self.setbrightness = customtkinter.CTkSlider(
            self.control_frame_cam, from_=0, to=255, orient="vertical", command=setbrightness_cb
        )

        self.setbrightness.set(0)
        self.widthC1 = (int(window.winfo_width())) 
        self.widthC2 = int(window.winfo_width())
        self.heightC1 = int(window.winfo_height()/2.2)
        self.heightC2 = 60

        self.camcrop = customtkinter.CTkFrame(self.bottom_frame,bg_color="black")
        self.camcrop.grid(row=0, column=0,columnspan=8,padx=(50,0), pady=0,sticky="n")
        self.saturacia = customtkinter.CTkLabel(self.bottom_frame,height=self.heightC2,width=self.heightC2,bg_color="green",text=".")
        self.saturacia.place(relx = 0, rely = 0,anchor="nw")
        self.canvascrop = customtkinter.CTkCanvas(self.camcrop,width=self.bottom_frame.winfo_width(),height=self.heightC2,  borderwidth=0)
        self.canvascrop.grid(row=0, column=0, padx=0, pady=0,sticky="news")

        dpiA = window.winfo_fpixels('1i')
        self.fig = Figure()

        y = 0

        self.plot1 = self.fig.add_subplot(111)

        self.fig.tight_layout(w_pad=0,h_pad=0)
        self.plot1.grid()

        xCal = []
        yCal = []

        for i in (0,1279):
            xCal.append(i)
            yCal.append(-1)

        self.vid.autoYgraph1 = True
        self.vid.colorGraph = False
        self.plot1.margins(x=0)
        self.ggg = self.plot1.plot(xCal,yCal,color="black")[0]
        self.plot1.set_ylim([0, 275])

        self.canvas1 = FigureCanvasTkAgg(self.fig,
                                   master = self.bottom_frame)  

        self.canvas1.get_tk_widget().grid(row=1, column=0,columnspan=8,sticky="news")

        #self.canvas1.draw()

        self.bottom_frame_g = customtkinter.CTkFrame(self.bottom_frame)
        self.bottom_frame_g.grid(row=2,column=0,columnspan=8,sticky="news")
        def on_click(event):

            stopcam()
        def on_click2(event):
            print("clicktu")
        self.toolbar = NavigationToolbar2Tk(self.canvas1,
                                       self.bottom_frame_g)

        self.zoomBut = self.toolbar.children['!checkbutton2']
        self.moveBut = self.toolbar.children['!checkbutton']

        self.toolbar.update()

        self.canvas4 = customtkinter.CTkCanvas(
            self.bottom_frame, width=self.widthC1, height=self.heightC1, borderwidth=0, relief="sunken", cursor="tcross")

        self.bottom_frame_c = customtkinter.CTkFrame(self.bottom_frame)

        self.bTools1 = customtkinter.CTkButton(self.bottom_frame, text="Práca s grafom",command=showToolsGraph)

        self.bTools2 = customtkinter.CTkButton(self.bottom_frame, text="Práca s grafom",command=hideToolsGraph)

        self.lbpeak = customtkinter.CTkLabel(self.bottom_frameO, text="Šírka vrcholu: 100")
        self.lbpeak.grid(row=3, column=0, sticky="n")

        self.peakwidth = customtkinter.CTkSlider(
            self.bottom_frameO, from_=0, to=100, orient="horizontal", command=peakwidth)
        self.peakwidth.grid(row=4, column=0, sticky="n")
        self.peakwidth.set(100)
        peakwidth(100)

        self.lbthresh = customtkinter.CTkLabel(self.bottom_frameO, text="Prah: 20")
        self.lbthresh.grid(row=3, column=1, sticky="n")

        self.thresh = customtkinter.CTkSlider(
            self.bottom_frameO, from_=0, to=100, orient="horizontal", command=peakthresh)
        self.thresh.grid(row=4, column=1, sticky="n")
        self.thresh.set(20)

        self.lbfilt = customtkinter.CTkLabel(self.bottom_frameO, text="Vyhladzovanie vrcholov: 7")
        self.lbfilt.grid(row=3, column=2, sticky="n")

        self.filt = customtkinter.CTkSlider(
            self.bottom_frameO, from_=0, to=20, orient="horizontal", command=savfilter)
        self.filt.grid(row=4, column=2, sticky="n")
        self.filt.set(7)

        self.offpeak = customtkinter.CTkSwitch(master=self.bottom_frameO, text="Zobraziť vrcholy", command=turnOnOffPeaks,
                                     variable=self.offpeak_var, onvalue="on", offvalue="off")
        self.offpeak.grid(row=0, column=0, padx=0, pady=10, sticky="n",columnspan=4)
        self.axisXtitle = customtkinter.CTkLabel(self.bottom_frame,text="Os x",text_font='Helvetica 9 bold')
        self.axisXtitle.grid(row=5, column=2, sticky="n",columnspan=2)
        self.bshowPXNM = customtkinter.CTkButton(self.bottom_frame,width=30, text="        nm        ",command=showPXNM,corner_radius=0)
        self.bshowPXNM.grid(row=6, column=2, sticky="ne")
        self.bshowPXNM.configure(state="disabled")

        self.bshowPXNM2 = customtkinter.CTkButton(self.bottom_frame,width=30, text="        px        ",command=showPXNM,corner_radius=0)
        self.bshowPXNM2.grid(row=6, column=3, sticky="nw")

        self.bautoYbTitle = customtkinter.CTkLabel(self.bottom_frame,text="Os y",text_font='Helvetica 9 bold')
        self.bautoYbTitle.grid(row=5, column=4, sticky="n")
        self.bautoYb = customtkinter.CTkSwitch(self.bottom_frame,command=autoY,text="Auto Y")
        self.bautoYb.grid(row=6, column=4, sticky="n",padx=20)
        self.bautoYb.select()

        self.switch_1 = customtkinter.CTkSwitch(self.bottom_frame, text="Zapnúť reálne farby", onvalue="on", offvalue="off", command=turnOnOffRealColor)
        #self.switch_1.grid(row=6, column=6, sticky="nw")
        self.switch_1.configure(state="disabled")
        self.bcolorGraphb = customtkinter.CTkSwitch(self.bottom_frame, text="Farby v grafe",command=colorGraph)
        self.bcolorGraphb.grid(row=5, column=6, sticky="nw")

        self.stopbtn = customtkinter.CTkButton(
            self.bottom_frame, text="\u23F8"+" Pozastaviť",height=40, command=lambda:stopcam(True),text_font='Helvetica 16 bold')
        self.stopbtn.grid(row=5, column=0, sticky="nw")

        iconSaveSnapShot=PhotoImage(file="save.png")
        stream = open(u'save.png', "rb")

        self.snapshotbtn = customtkinter.CTkButton(
            self.bottom_frame, text="\u1F5AC"+"Uložiť",height=40, command=snapshot,text_font='Helvetica 16 bold')
        self.snapshotbtn.grid(row=6, column=0, sticky="nw") 

        self.bottom2_frame = customtkinter.CTkFrame(window, width=1280, height=255)

        self.ldesc = customtkinter.CTkLabel(
            self.bottom2_frame, text="\
            *Šírka vrcholu -  minimálna vzdialenosť medzi každým detekovaným vrcholom\
            *Prah -  minimálny prah pre detekciu vrcholu\
            *Filter - \
            *Zapamätať vrcholy - zaznamenanie impulzu ", justify="left")

        self.delay = 10

        resizeWin2(1)
        self.window.bind('<Configure>', resizeWin_left)
        self.mainwidth_prev = 0
        try:
            self.thread = Thread(target = self.update)
            if(self.thread.is_alive() == False):

                self.thread.start()

        except ZeroDivisionError:
            print(traceback.format_exc())

        selectLang()

        self.window.mainloop()
    def calibrateToFile(self):
        dt = str(datetime.now())
        ts = dt.split(" ")

        ts[1] = ts[1].split(".")[0].replace(":", "-")

        foldername = "cal-"+(ts[0])
        foldername = foldername+"-"+ts[1]+".txt"
        calDataCustom = foldername
        edit_cal_file = ""
        new_cal = []
        prev_val = 0
        x = 0
        i = 0
        for widget in self.modal.winfo_children():
            try:

                if(i%2 == 0):
                    if(x <15):
                        new_cal.append([float(prev_val),float(widget.get())])
                        edit_cal_file = edit_cal_file+str(prev_val)+";"+str(widget.get())+"\n"
                    x = x + 1
                prev_val = widget.get()
            except:
                a=1
            i = i + 1
        with open(calDataCustom, 'w') as file:
            file.write(edit_cal_file)
        os.startfile(calDataCustom)
    def calibrate(self,temp = False):

        new_cal = []
        i = 0
        x = 0
        prev_val = 0
        edit_cal_file = ""
        countWidget = 0
        for widget in self.modal.winfo_children():
            try:
                print(widget.get())
                print(countWidget)

                if(widget.get() == "0" or widget.get() == "1"):
                    break
                    a=11
                else:
                    getwid = widget.get().replace(",", ".")
                    new_cal.append(float(getwid))

            except:
                a=1
            countWidget +=1
        print(new_cal)
        if(temp == True):
            return new_cal
            """
            try:

                if(i%2 == 0):
                    if(x <15 and int(widget.get()) > 1):

                        new_cal.append([float(prev_val),float(widget.get())])
                        edit_cal_file = edit_cal_file+str(prev_val)+";"+str(widget.get())+"\n"
                    x = x + 1
                prev_val = widget.get()
            except:
                a=1
            i = i + 1
            """

        new_cal = np.array(new_cal).reshape(int(len(new_cal)/2), -1)

        row_sums = new_cal.sum(axis=1)
        order = np.argsort(row_sums)
        new_cal = new_cal[order].tolist()

        for i in range(len(new_cal)):
            edit_cal_file = edit_cal_file+str(int(new_cal[i][0]))+";"+str(new_cal[i][1])+"\n"

        DEFAULT_CALIBRATION = new_cal
        App.DEFAULT_CALIBRATION = new_cal
        with open(calData, 'w') as file:
            file.write(edit_cal_file)

        calibration = new_cal

        self.vid.recalibrate(calibration)
        self.avvv = 0

        """
        calibration = ((float(self.txt1.get()), float(self.marker1.get())),
                       (float(self.txt2.get()), float(self.marker2.get())),
                       (float(self.txt3.get()), float(self.marker3.get()))
                       )

        self.point1 = float(self.marker1.get())
        self.point2 = float(self.marker2.get())
        self.point3 = float(self.marker3.get())
        configdata["calnm1"] = float(self.marker1.get())
        configdata["calnm2"] = float(self.marker2.get())
        configdata["calnm3"] = float(self.marker3.get())
        configdata["calpx1"] = int(self.txt1.get())
        configdata["calpx2"] = int(self.txt2.get())
        configdata["calpx3"] = int(self.txt3.get())
        configtext = json.dumps(configdata)
        editConfigset(configtext)
        self.vid.recalibrate(calibration)

        self.setCalButton.grid(row=1, column=0)
        self.control_frame.grid_remove()
        """

        tkinter.messagebox.showinfo(title=None, message="Kalibrácia je uložená! Do súboru: "+str(Path.cwd())+"\calData.txt")
        self.modal.lift()
    def update(self):
        print("update")

        graphdata_prev = np.array([])

        first = 0
        self.photoprev = ""
        self.photoprev2 = ""
        self.paddingAnot = 8

        def on_xlims_change(event_ax):

            self.paddingAnot = 1.05

            for i, a in enumerate(self.allAnot):
                a.remove()
            self.allAnot = []
            
            for i in range(len(self.xpeaks)):

                if(self.vid.autoYgraph1 == False):
                    yminan, ymaxan = self.plot1.get_ylim()
                    yminan = ymaxan + (ymaxan - yminan)/10 
                    ymaxan = ymaxan + (ymaxan - yminan)/10
                    self.paddingAnot = abs(ymaxan-max(ypeaks))*5#(max(ypeaks)*1.04)-(ymaxan)
                else:
                    self.paddingAnot = (255*1.04)-255
                if(self.paddingAnot < 0.04):
                    self.paddingAnot = 0.05
                #anot = self.plot1.annotate(str(xpeaks[i]), xy=(float(xpeaks[i]),ypeaks[i]),textcoords='data', xytext=(float(xpeaks[i]),ypeaks[i]+self.paddingAnot),backgroundcolor="red")
                #anot = self.plot1.annotate(str(xpeaks[i]), xy=(float(xpeaks[i]),ypeaks[i]),textcoords='data', xytext=(float(xpeaks[i]),ypeaks[i]),backgroundcolor="red")
                #anot = self.plot1.annotate(str(xpeaks[i]), xy=(float(xpeaks[i]),ypeaks[i]),textcoords='data', xytext=(float(xpeaks[i]),ypeaks[i]))
                background_color = "yellow" 
                bbox_props = dict(boxstyle="round", fc=background_color)
                percent_offset = 0.02
                offset_pixels = percent_offset * (self.plot1.get_ylim()[1] - self.plot1.get_ylim()[0])
                anot = self.plot1.annotate(str(xpeaks[i]), xy=(float(xpeaks[i]), ypeaks[i] + offset_pixels), xytext=(0, offset_pixels), textcoords='offset points', backgroundcolor=background_color, bbox=bbox_props, annotation_clip=False)
                
                self.allAnot.append(anot)

        def on_ylims_change(event_ax):

            self.paddingAnot = 1

        self.vid.autoYgraph1 = False
        kazdydruhykrat = 0
        first = 1
        sec = 0
        while True:
            try:
                self.canvas1.draw()
            except:
                a=1
            if 1==1:

                self.plot1.callbacks.connect('xlim_changed', on_xlims_change)
                self.plot1.callbacks.connect('ylim_changed', on_ylims_change)
                self.plot1.callbacks.connect('ylim_changed', on_xlims_change)
                self.plot1.callbacks.connect('xlim_changed', on_ylims_change)

                cal = Calibration(self.vid.calibration)
                cal.Calibrate() 

                try:

                    ret, frame, frame_org = self.vid.get_frame()

                    ret23, frame23, frame_org23 = self.vid.get_frame3()
                    self.zoomBut.config(state="normal")
                    self.moveBut.config(state="normal")
                    if(self.vid.stopcamvid == 1):
                        if(self.vid.entryfile_path == ""):
                            self.avvv = 0
                            self.zoomBut.config(state="disabled")
                            self.moveBut.config(state="disabled")
                        else:
                            self.vid.stopcamvid = 1
                            self.avvv = self.avvv + 1

                    else:
                        self.avvv = self.avvv + 1

                    if(self.avvv<2):

                        if(self.neg1 == 1):
                            try:
                                try:
                                    graphdata = []
                                    print(self.vid.addRows)
                                    print(self.vid.pridatCiaryN)
                                    self.plot1.remove()# = self.fig.add_subplot(111, projection='3d')
                                    self.plot1 = self.fig.add_subplot(111, projection='3d')
                                    self.plot1.view_init(elev=90, azim=-90)
                                    
                                    #self.plot1.mplot3d.proj_type = 'persp'
                                    self.plot1.cla()
                                    #self.plot1.grid()
                                    #self.plot1.margins(x=0,y=0.1)
                                    #self.plot1.gird()
                                    #z = []
                                    zz = 0
                                    for i in range(1,719):
                                        try:
                                            if(i%self.vid.pridatCiaryN==0):
                                                graphdata = (self.vid.get_graph(i))
                                                x = (graphdata[1][1])
                                                y = (graphdata[1][2])
                                                #z = np.zeros(len(x))
                                                self.plot1.step(x,y,zz,linewidth = '0.7')
                                                zz = zz + 1
                                        except:
                                            a=1
                                    #self.plot1.margins(0)
                                    #self.plot1.gird()
                                    #self.plot1.margins(0)
                                    graphdata_prev = self.vid.get_graph()
                                    continue
                                #except:
                                except Exception as e: 
                                    print(e)
                                    print("nepridat")
                                    #if self.plot1.__class__.__name__ == 'Axes3D':
                                    self.plot1.remove()
                                    self.plot1 = self.fig.add_subplot(111)
                                    graphdata = self.vid.get_graph()
                                    graphdata_prev = self.vid.get_graph()
                            except:
                                self.avvv = 0
                                ret, frame, frame_org = self.vid.get_frame()
                                graphdata = self.vid.get_graph()

                            graphdataRef1 = graphdata
                            try:
                                if(self.vid.waspressed == 1):
                                    self.graphdataRef1 = graphdata[1][2]
                                self.vid.waspressed = 0
                            except:
                                a=1
                            print("idem dalej")
                        else:

                            graphdata = self.vid.get_graph2()
                            graphdata2 = graphdata_prev

                        x = (graphdata[1][1])
                        y = (graphdata[1][2])

                        try:

                            np.seterr(invalid='ignore')
                            rozdielY = np.subtract(np.array(self.graphdataRef1),np.array(y)).tolist()

                            podielY = np.nan_to_num(np.array(y), nan=1, neginf=1, posinf=1).tolist()
                            podielY = np.divide(podielY,np.array(self.graphdataRef1))
                            podielY[podielY > 3] = 3
                            podielY = np.nan_to_num(podielY, nan=1, neginf=1, posinf=1).tolist()
                            podielY = [x*100 for x in podielY]

                        except:
                            a=1

                        xpeaks = []
                        ypeaks = []
                        if(self.vid.switchPRval == 0):

                            graphdata[1][3] = self.vid.getpeaks(podielY)
                            y = podielY
                        elif(self.vid.switchPRval == 1):

                            graphdata[1][3] = self.vid.getpeaks(rozdielY)
                            y = rozdielY
                        else:
                            y = np.array(y)

                            y = y.tolist()
                        peaks = (graphdata[1][3]).tolist()

                        if(self.offpeak_var.get() == "off"):
                            peaks = []

                        self.plot1.cla()
                        self.plot1.margins(0)

                        for i in range(len(y)):

                            for j in range(len(peaks)):

                                if((x[i]) == round(cal.GetWaveLenghtByPx((peaks[j])),1)):
                                    if(round(cal.GetWaveLenghtByPx((peaks[j])),1) not in xpeaks):
                                        xpeaks.append(round(cal.GetWaveLenghtByPx((peaks[j])),1))
                                        ypeaks.append(y[i])

                        colcolors = graphdata[1][4]

                        colcolors2 = graphdata[1][len(graphdata)-3]

                        global laaang

                        if(laaang == "SK"):
                            l = 0
                        elif(laaang == "EN"):
                            l = 1

                        if(self.vid.showPXNMval == False):
                            self.plot1.set_xlabel(langsStrings.vlnova_dlzka[l])
                        else:

                            self.plot1.set_xlabel(langsStrings.pixely[l])

                        if(self.vid.switchPRval == 0):

                            self.plot1.set_ylabel(langsStrings.priepustnost[l])
                        else:

                            self.plot1.set_ylabel(langsStrings.intenzita[l])

                        if(self.vid.showPXNMval == True):
                            xpeaks = []
                            ypeaks = []
                            peaks = (graphdata[1][3]).tolist()
                            if(self.offpeak_var.get() == "off"):
                                peaks = []
                            colcolors = []
                            x = []
                            for i in range(0,1280):
                                x.append(i)

                            for i in range(len(y)):

                                colcolors.append(x[i])
                                for j in range(len(peaks)):

                                    if(int(x[i]) == int((int(peaks[j])))):
                                        if(round((int(peaks[j])),1) not in xpeaks):
                                            xpeaks.append(round((int(peaks[j])),1))
                                            ypeaks.append(y[i])

                        self.xpeaks = xpeaks  
                        self.ypeaks = ypeaks  

                        if(max(y) >= 254):
                            self.saturacia.configure(bg_color="red")
                        elif(max(y) < 254):
                            self.saturacia.configure(bg_color="green")  

                        self.plot1.grid()
                        #print(self.vid.calGraphShow_var)
                        if(self.vid.calGraphShow_var == "0"):

                            if(self.vid.switchPRval == 2):

                               self.plot1.step(x,y,color="black", where='pre', label='pre',linewidth = '0.7')
                               #bins = np.linspace(-5, 5, 101)
                               #counts, edges = np.histogram(y, bins=bins)
                               #self.plot1.bar(edges[:-1], counts, width=np.diff(edges), align='edge')#.bar(x,y,color="blue")

                            try:
                                if(self.vid.switchPRval == 1):
                                    self.plot1.step(x,rozdielY,color="black",linewidth = '0.7')
                                    y = rozdielY

                                elif(self.vid.switchPRval == 0):
                                    self.plot1.step(x,podielY,color="black",linewidth = '0.7') 
                                    y = podielY

                            except:
                                a=1
                            try:
                                if(self.vid.showRefVal == 1):

                                    self.plot1.step(x,(self.graphdataRef1),color="orange",linewidth = '0.7')
                                    if(min(self.graphdataRef1) < min(y)):
                                        minY = min(self.graphdataRef1)
                                    else:
                                        minY = min(y)

                                    if(max(self.graphdataRef1) > max(y)):
                                        maxY = max(self.graphdataRef1)
                                    else:
                                        maxY = max(y)

                                    if(self.vid.switchPRval == 1):
                                        if(min(self.graphdataRef1) < min(rozdielY)):
                                            minY = min(self.graphdataRef1)
                                        else:
                                            minY = min(rozdielY)

                                        if(max(self.graphdataRef1) > max(rozdielY)):
                                            maxY = max(self.graphdataRef1)
                                        else:
                                            maxY = max(rozdielY)

                                    if(self.vid.switchPRval == 0):
                                        if(min(self.graphdataRef1) < min(podielY)):
                                            minY = min(self.graphdataRef1)
                                        else:
                                            minY = min(podielY)

                                        if(max(self.graphdataRef1) > max(podielY)):
                                            maxY = max(self.graphdataRef1)
                                        else:
                                            maxY = max(podielY)
                                    margin = maxY*0.15
                                    if(margin>20):
                                        margin = 20
                                    """    
                                    if(int(minY) == 0):
                                        self.plot1.set_ylim([int(minY), int(maxY)+self.paddingAnot])
                                    else:
                                        self.plot1.set_ylim([int(minY)-self.paddingAnot, int(maxY)+self.paddingAnot])
                                    """

                            except Exception as e:

                                a=1

                            if(self.neg1 != 1):
                                x2 = (graphdata2[1][1])
                                y2 = (graphdata2[1][2])

                                if(self.vid.switchPRval == 0):
                                    if(y[1277] == 0):
                                        y[1277] = 1
                                        y[1276] = 1

                            self.allAnot = []
                            allMinZero = []

                            allMin = []
                            for i in range(len(xpeaks)):
                                allMin.append(min(self.plot1.get_ylim()))
                                allMinZero.append(0)

                            if(self.vid.autoYgraph1 == False):
                                self.plot1.vlines(x=xpeaks, ymin=0, ymax=ypeaks, colors='teal', ls='--', lw=1)
                                margin = max(y)*0.15
                                marginm = min(y)*0.15
                                if(margin>20):
                                    margin = 20
                                """    
                                try:
                                    if(self.vid.showRefVal != 1):
                                        if(min(y) == 0):
                                            self.plot1.set_ylim([min(y), max(y)+self.paddingAnot])
                                        else:
                                            self.plot1.set_ylim([min(y)-self.paddingAnot, max(y)+self.paddingAnot])
                                except:     
                                    try:
                                        if(min(y) == 0):
                                            self.plot1.set_ylim([min(y), max(y)+self.paddingAnot])
                                        elif(min(y) < 10):
                                            self.plot1.set_ylim([0, max(y)+self.paddingAnot])
                                        else:
                                            self.plot1.set_ylim([min(y)-self.paddingAnot, max(y)+self.paddingAnot])
                                    except:
                                        a=1
                                """
                            else:
                                
                                self.plot1.vlines(x=xpeaks, ymin=allMinZero, ymax=ypeaks, colors='black', ls='--', lw=1)     
                            for i in range(len(xpeaks)):

                                self.paddingAnot = 8
                                self.maxY100 = 255
                                self.maxYact = max(y)
                                if(self.vid.autoYgraph1 == False):
                                    #print(self.plot1.get_ylim()[0])
                                    #print(self.plot1.get_ylim()[1])
                                    yminan, ymaxan = self.plot1.get_ylim()
                                    yminan = ymaxan + (ymaxan - yminan)/10 
                                    ymaxan = ymaxan + (ymaxan - yminan)/10
                                    self.paddingAnot = abs(ymaxan-max(ypeaks))*5#ymaxan-max(ypeaks)#(max(ypeaks)*1.04)-(ymaxan)
                                    
                                else:
                                    self.paddingAnot = (255*1.04)-255
                                print(self.paddingAnot)
                                if(self.paddingAnot < 0.04):
                                    self.paddingAnot = 0.05
                                elif(self.paddingAnot > 50):
                                    self.paddingAnot = ypeaks[i] * 0.08
                                print("padding: ",self.paddingAnot)
                                #anot = self.plot1.annotate(str(xpeaks[i]), xy=(float(xpeaks[i]),ypeaks[i]),textcoords='data', xytext=(float(xpeaks[i]),ypeaks[i]+self.paddingAnot),backgroundcolor="yellow")
                                background_color = "yellow" 
                                bbox_props = dict(boxstyle="round", fc=background_color)
                                percent_offset = 0.02
                                offset_pixels = percent_offset * (self.plot1.get_ylim()[1] - self.plot1.get_ylim()[0])
                                anot = self.plot1.annotate(str(xpeaks[i]), xy=(float(xpeaks[i]), ypeaks[i] + offset_pixels), xytext=(0, offset_pixels), textcoords='offset points', backgroundcolor=background_color, bbox=bbox_props, annotation_clip=False)
                                #trans = blended_transform_factory(self.plot1.transData, self.plot1.transAxes)
                                #anot = self.plot1.annotate(str(xpeaks[i]), xy=(float(xpeaks[i]), ypeaks[i]), xycoords=trans, xytext=(0,5), backgroundcolor=background_color, bbox=bbox_props)
                                #anot = self.plot1.annotate(str(xpeaks[i]), xy=(float(xpeaks[i]), ypeaks[i]), xycoords=trans, xytext=(0, 1), textcoords='offset points', backgroundcolor=background_color, bbox=bbox_props)
                                self.allAnot.append(anot)
                            y_data = []
                            for line in self.plot1.get_lines():
                                y_data.append(line.get_ydata())
    
                            try:
                                
    
                                if(len(y_data) >1):
                                    if(np.amin(y_data[0]) > np.amin(y_data[1])):
                                        ymingraf = np.amin(y_data[1])
                                    elif(np.amin(y_data[0])<np.amin(y_data[1])):
                                        ymingraf = np.amin(y_data[0])
                                    else:
                                        ymingraf = np.amin(y_data[0])
                                else:
                                    ymingraf = np.amin(y_data[0])
                                if(len(y_data) >1):
                                    if(np.amax(y_data[0]) > np.amax(y_data[1])):
                                        ymaxgraf = np.amax(y_data[0])
                                    elif(np.amax(y_data[0])<np.amax(y_data[1])):
                                        ymaxgraf = np.amax(y_data[1])
                                    else:
                                        ymaxgraf = np.amax(y_data[0])
                                else:
                                    ymaxgraf = np.amax(y_data[0])
                                yrange = ymaxgraf - ymingraf
                                if(yrange == 1):
                                    yrange = 1
                                padding = yrange * 0.1
    
                            except Exception as e:
                                print("Vyskytla sa chyba1:", e)
                            try:
                                if(self.vid.autoYgraph1 == True):
                                    self.plot1.set_ylim([0, 260])
                                else:
                                    self.plot1.set_ylim([ymingraf - padding, ymaxgraf+ padding])
                            except:
                                a=1
                                #print("tu som zastal 2")

                        else:
                            print("tuto")
                            self.plot1.set_xlim([0, 1280])
                            self.plot1.set_xlabel(" ")
                            xCal = []
                            yCal = []

                            for i in range(len(self.vid.calibration)):
                                xCal.append(self.vid.calibration[i][0])
                                yCal.append(self.vid.calibration[i][1])

                            #self.vid.autoYgraph1 = False
                            #self.vid.colorGraph = False
                            model3 = np.poly1d(np.polyfit(xCal, yCal, 3))

                            z = model3(xCal)
                            ch = yCal - model3(xCal)

                            self.fig.delaxes(self.plot1)
                            try:
                                self.fig.delaxes(self.plot2)
                            except:
                                a=1

                            self.plot1 = self.fig.add_subplot(212)
                            self.plot1.set_xlabel("px")
                            self.plot1.set_ylabel("nm")
                            if(xCal != [0.0, 640.0, 1280.0]):
                                self.plot1.plot(xCal,ch,color="black",marker="o")
                            print(abs(max(ch)))
                            if(abs(max(ch))<=0.01):
                                self.plot1.set_ylim([-0.01, 0.01])
                            if(xCal != [0.0, 640.0, 1280.0]):
                                self.plot1.plot([0,1280],[0,0],color="red")
                            self.plot1.set_xlim(left=0,right=1280)
                            self.plot2 = self.fig.add_subplot(211)

                            self.plot2.set_ylabel("nm")
                            self.plot1.title.set_text(langsStrings.kalibracna_odchylka[l])
                            self.plot2.title.set_text(langsStrings.kalibracna_krivka[l])
                            

                            calibration = Calibration(self.vid.calibration) 

                            calibration.Calibrate()
                            
                            if(xCal != [0.0, 640.0, 1280.0]):
                                self.plot2.plot(sorted(xCal),sorted(yCal),"o",color="red")
                                xCal.append(0)
                                yCal.append(calibration.GetWaveLenghtByPx(0))
                                xCal.append(1280)
                                yCal.append(calibration.GetWaveLenghtByPx(1280))
                                # Fit spojitú funkciu tretieho rádu k vašim dátam
                                #print(len(yCal))
                                
                                if(len(yCal) == 3):
                                    coefficients = np.polyfit(xCal, yCal, 2)
                                else:
                                    coefficients = np.polyfit(xCal, yCal, 3)
                                p = np.poly1d(coefficients)
                                
                                # Generovanie hodnôt pre vykreslenie krivky
                                xCal2 = np.linspace(min(xCal), max(xCal), 1280)
                                yCal2 = p(xCal2)
                                self.plot2.plot(sorted(xCal2),sorted(yCal2),color="red")
                                # Create a smooth curve using cubic Bezier interpolation
                                
                                self.plot2.set_xlim(left=0,right=1280)

                        if(self.vid.colorGraph == True and self.vid.calGraphShow_var == "0"):
                            first = 2

                            if(self.switch_1.get() == "on"):
                                colorlist = colcolors2
                            else:
                                colorlist = colcolors

                            try:
                                #1/x[0]
                                print("nm")
                                new_colorlist = []
                                colorlist = []
                                """
                                for i in range (len(x)):
                                    wavelength = cal.GetWaveLenghtByPx(i)
                                    
                                    wavelength = round(wavelength)

                                    rgb = self.vid.wavelength_to_rgb(wavelength,cal.GetWaveLenghtByPx(0),cal.GetWaveLenghtByPx(1279))
                                    colorlist.append(rgb)
                                """
                                #print(colorlist[0])
                                colorlist = self.vid.create_spectral_map(1279,cal.GetWaveLenghtByPx(0),cal.GetWaveLenghtByPx(1279))
                                spectralmap = matplotlib.colors.LinearSegmentedColormap.from_list("spectrum", colorlist)

                            except Exception as e:
                                print("tato chyba")
                                print(e)
                                print("tato chyba koniec")
                                print("px")
                                colorlist = []
                                for i in range (len(x)):
                                    wavelength = i#cal.GetWaveLenghtByPx(i)

                                    wavelength = round(wavelength)

                                    rgb = self.vid.wavelength_to_rgb(wavelength,0,1279)
                                    colorlist.append(rgb)
                                #print(colorlist)
                                colorlist = self.vid.create_spectral_map(1279)
                                spectralmap = matplotlib.colors.LinearSegmentedColormap.from_list("spectrum", colorlist)

                            wavelengths = x
                            spectrum = y

                            y = y
                            X, Y = np.meshgrid(x, y)
                            paddingclim = 150
                            clim = (min(x),max(x))

                            
                            if(self.vid.switchPRval == 0):
                                print("?")

                                self.plot1.fill_between(wavelengths, spectrum,100, color='black',step='pre',zorder=3, facecolor='blue', alpha=0.5)

                            elif(self.vid.switchPRval == 1):
                                self.plot1.fill_between(wavelengths, spectrum, color='black',step='pre',zorder=3, facecolor='blue', alpha=0.5)
                            else:
                            
                                if(self.vid.autoYgraph1 == False):
                                    if(self.vid.switchPRval == 1):
                                        extent = (np.min(wavelengths), np.max(wavelengths), 0, np.max(y))
                                    else:
                                        extent = (np.min(wavelengths), np.max(wavelengths), 0, np.max(y))
                                else:
                                    if(self.vid.switchPRval == 0):
                                        extent = (np.min(wavelengths), np.max(wavelengths), 0, np.max(y))
                                    else:
                                        extent = (np.min(wavelengths), np.max(wavelengths), 0, np.max(y))
    
                                if(self.switch_1.get() == "on"):
                                    
                                    #colors = self.photo3e.getcolors(maxcolors=256)
                                    #palette = [color[1] for color in colors]
                                    #self.photo3e = self.photo3e.re#self.photo3e.crop((int(cal.GetWaveLenghtByPx(1)), 0, int(cal.GetWaveLenghtByPx(1280)), self.photo3e.height))#self.photo3e[:, int(cal.GetWaveLenghtByPx(1)):int(cal.GetWaveLenghtByPx(1280))]
                                    #extent = ((cal.GetWaveLenghtByPx(1)), (cal.GetWaveLenghtByPx(1280)), 0, np.max(y))
                                    # Prevod do numpy pola pre jednoduchšiu manipuláciu
                                    # Prevod do numpy pola pre jednoduchšiu manipuláciu
                                    #photo_array = np.array(self.photo3e)
                                    
                                    # Získanie maximálnej hodnoty RGB zložiek pre každý pixel
                                    #max_rgb = np.max(photo_array, axis=2)
                                    
                                    # Násobenie RGB zložiek konštantou
                                    #normovacia_konstanta = np.max(max_rgb) / 255.0
                                    #photo_array = (photo_array / normovacia_konstanta).astype(np.uint8)
                                    #photo_array = (photo_array * normovacia_konstanta).astype(np.uint8)
                                    # Získanie nového obrazu PIL.Image
                                    #self.photo3e = (photo_array)
                                    
                                    self.plot1.imshow(self.photo3e, clim=clim, extent=extent, aspect='auto')
                                    #self.plot1.fill_between(wavelengths, spectrum, max(spectrum)+1, color='w',step='pre')
                                    #self.plot1.imshow(X, clim=clim, extent=extent, cmap=spectralmap, aspect='auto')
                                else:
                                    self.plot1.imshow(X, clim=clim, extent=extent, cmap=spectralmap, aspect='auto')
                                if(self.vid.switchPRval == 1):
                                    self.plot1.fill_between(wavelengths, spectrum, max(spectrum)+1, color='w',step='pre')
                                elif(self.vid.switchPRval == 0):
                                    self.plot1.fill_between(wavelengths, spectrum, max(spectrum)+1, color='w',step='pre')
                                else:
                                    self.plot1.fill_between(wavelengths, spectrum, max(spectrum)+1, color='w',step='pre')

                        
                        
                        
                    ret2 = False
                    
                    ret24, graphdata24 = self.vid.get_graph2()
                    #quit()
                    if ret24:

                        if(1==1):
                            try:

                                self.photo24 = PIL.Image.fromarray(graphdata24[0])

                                self.photo24 = self.photo24.resize((self.widthC1, self.heightC1), PIL.Image.ANTIALIAS)
                                self.photo24 = PIL.ImageTk.PhotoImage(
                                    image=self.photo24)

                                if(first < 10):
                                    self.image_on_canvas4 = self.canvas4.create_image(
                                        0, 0, image=self.photo24, anchor=tkinter.NW)
                                else:
                                    self.canvas4.itemconfig(self.image_on_canvas4, image = self.photo2)

                                self.canvas4.update()

                            except:
                                a=1
                                #print("tu som zastal 3")
                    if ret23:

                        self.photo23 = PIL.ImageTk.PhotoImage(
                            image=PIL.Image.fromarray(frame23).resize((self.canvas0.winfo_width(), self.canvas0.winfo_height())))

                        if(first < 10):
                            self.image_on_canvas2 = self.canvas2.create_image(
                                0, 0, image=self.photo23, anchor=tkinter.NW)
                        else:

                            self.canvas2.itemconfig(self.image_on_canvas2, image = self.photo23)

                        self.canvas2.update()

                    if ret:

                        frame = PIL.Image.fromarray(frame).resize((self.canvas0.winfo_width(), self.canvas0.winfo_height()))
                        self.photo = PIL.ImageTk.PhotoImage(image=(frame))

                        if(self.vid.isblack == False):
                            self.frameid = self.canvas0.create_image(
                                    0, 0, image=self.photo, anchor=tkinter.NW)

                            self.canvas0.itemconfig(self.frameid, image = self.photo)
                            self.canvas0.image = self.photo

                        if(self.vid.entryfile_path2 != "" and self.neg1 == 2):

                            self.photo3e = PIL.Image.fromarray(frame_org23)
                            self.photo3e123 = self.photo3e
                            width, height = self.photo3e.size
                            self.photo3e  = self.photo3e.crop((0, int(self.vid.moveline2)-int(self.vid.heightline3), int(width), int(self.vid.moveline2)+int(self.vid.heightline3)))
                            self.photo3e = self.photo3e.resize((int(self.camcrop.winfo_width()), (int(self.camcrop.winfo_height()))), PIL.Image.ANTIALIAS)

                        else:
                            self.photo3e = PIL.Image.fromarray(frame_org)
                            width, height = self.photo3e.size

                            self.photo3e  = self.photo3e.crop((0, int(self.vid.moveline)-int(self.vid.heightline), int(width), int(self.vid.moveline)+int(self.vid.heightline)))

                            self.photo3e = self.photo3e.resize((int(self.camcrop.winfo_width()), (int(self.camcrop.winfo_height()))), PIL.Image.ANTIALIAS)

                        self.photo3 = PIL.ImageTk.PhotoImage(
                            image=self.photo3e)

                        self.image_on_canvas2 = self.canvascrop.create_image(
                                    0, 0, image=self.photo3, anchor=tkinter.NW)

                        self.canvascrop.itemconfig(self.image_on_canvas2, image = self.photo3)
                        self.canvascrop.image = self.photo3
                        #print("kreslim")
                        """
                        try:
                            self.canvas1.draw()
                        except Exception as e:
                            print("Vyskytla sa chyba2:", e)
                        """
                        #print(self.canvas1)
                        
                        
                        #self.canvas1.get_tk_widget().update()
                        #print("kreslim koniec")
                except Exception as e:
                    #exc_type, exc_obj, exc_tb = sys.exc_info()
                    #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    #print(exc_type, fname, exc_tb.tb_lineno)
                    #print (e)
                    #print("aaa")
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(f"{exc_type} in {fname} at line {exc_tb.tb_lineno}: {e}")
                    print("aaa")

                first = 10

            kazdydruhykrat = kazdydruhykrat  + 1

class MyVideoCapture:
    def __init__(self, calibration, video_source=0,video_source2=1):
        self.calibration = calibration
        self.colorcross2 = (255,255,255)
        self.canvas1 = ""
        self.switchPRval = 2
        self.justnm = None
        self.refLive = 0
        self.RKonst = 1
        self.GKonst = 1
        self.BKonst = 1
        self.setBG = False

        self.moveline_v = 0
        self.moveline_v2 = 0
        self.moveline_v3 = 0
        self.moveline_vG = 0
        self.moveline_v4 = 0
        self.mindist = 50  
        self.thresh = 20  
        self.savpoly = 7  
        self.intensity = [0] * 1280  
        self.dataIntensity = [0] * 1280
        self.holdpeaks = False
        self.calHalnow = 0

        self.vid = cv2.VideoCapture(int(configdata["camspect"]), cv2.CAP_MSMF)

        self.showPXNMval = 0
        self.unitsGraph = ""
        self.autoYgraph = 0
        self.autoYgraph1 = 1
        self.colorGraph = 0

        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        self.vid.set(15, -3) 

        if not self.vid.isOpened():
            print(ValueError("Unable to open video source", video_source))

        self.vid.release()

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.rotate_deg = 0
        self.moveline4 = 50
        self.moveline = configdata["moveline"]
        self.moveline2 = configdata["moveline2"]
        self.moveline3 = configdata["moveline3"]
        self.crosscolor = (255,255,255)
        self.heightline = configdata["heightline"]
        self.heightline3 = 1
        self.entryfile_path = ""
        self.entryfile_path2 = ""
        self.stopcamvid = 1
        self.halogen_var = 0
        self.SumMax = "MAX"
        self.calGraphShow_var = "0"
        self.justnm = None
        self.docalcalibration = Calibration(self.calibration)
        self.docalcalibration.Calibrate()   
    def recalibrate(self, calibration):
        self.avvv = 0
        self.calibration = calibration

    def get_frame(self):
        self.isblack=False

        if (1==1):

            try:
                cv2.imwrite("temp.png",
                                    cv2.cvtColor(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB), cv2.COLOR_BGR2RGB))
            except:
                #print("tu som zastal 4")
                a=1

            if(self.entryfile_path == ""):

                if(self.stopcamvid == 1):

                    self.ret, self.frame = self.vid.read()
                    try:
                        self.frame = cv2.resize(self.frame, (1280,720), interpolation = cv2.INTER_AREA)
                    except:
                        #print("tu som zastal 5")
                        self.isblack=True
                        self.ret = True
                        self.frame = cv2.imread("Black.png")
                        self.frame = cv2.resize(self.frame, (1280,720), interpolation = cv2.INTER_AREA)

                else:

                    self.frame = self.frame
                    self.frame = cv2.resize(self.frame, (1280,720), interpolation = cv2.INTER_AREA)
                    self.ret = True

            else:

                self.frame = cv2.imread(self.entryfile_path)

                self.frame = cv2.resize(self.frame, (1280,720), interpolation = cv2.INTER_AREA)
                self.ret = True

            frame = self.frame
            ret = self.ret

            if ret:

                frame_org = frame

                frame123 = frame.copy()
                frame1234 = frame.copy()
                self.readline = cv2.line(frame123, (0, int(self.moveline)), (1280, int(self.moveline)), (255, 255, 255), int(self.heightline))
                self.readline22 = cv2.line(frame1234, (0, int(self.moveline)), (1280, int(self.moveline)), (255, 255, 255), int(self.heightline))

                result = cv2.addWeighted(frame123, 0.5, frame, 1 - 0.5, 0)

                return (ret, cv2.cvtColor(result, cv2.COLOR_BGR2RGB), cv2.cvtColor(frame_org, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None, None)
        else:
            ret = False
            return (ret, None, None)

    def get_frame2(self):

        if self.vid2.isOpened():
            ret, frame = self.vid2.read()

            if ret:

                frame_org = frame
                frame = cv2.resize(frame, (320, 180))  

                self.readline2 = cv2.line(frame, (int(self.moveline2/4), 0), (int(self.moveline2/4),320), self.colorcross2)
                self.readline3 = cv2.line(frame, (0, int(self.moveline3/2)), (320, int(self.moveline3/2)), (255, 255, 255), 1)
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), cv2.cvtColor(frame_org, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None, None)
        else:
            return (ret, None, None)

    def get_frame3(self):

        if 1==1:#self.vid.isOpened():

            if(self.refLive == 1):
                self.entryfile_path2 = "refpic.png"
                self.refLive = 0
            if(self.entryfile_path2 != ""):

                self.frame2 = cv2.imread(self.entryfile_path2)
                self.ret2 = True
            else:
                self.frame2 = []
                self.ret2 = False

            frame = self.frame2
            ret = self.ret2

            if ret:

                frame_org = frame
                frame = cv2.resize(frame, (320, 180))  

                return (ret, cv2.cvtColor(frame_org, cv2.COLOR_BGR2RGB), cv2.cvtColor(frame_org, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None, None)
        else:
            ret = False
            return (ret, None, None)
    def create_spectral_map(self,length,min_w,max_w):
        # Definujeme vlnové dĺžky pre farby - fialová, modrá, zelená, žltá, oranžová, červená
        wavelengths = np.linspace(min_w, max_w, length)
        colors = []
    
        for wavelength in wavelengths:
            if min_w <= wavelength <= 440:  # Fialová až modrá
                r = (440 - wavelength) / (440 - min_w)
                g = 0
                b = 1
            elif 440 <= wavelength <= 490:  # Modrá až zelená
                r = 0
                g = (wavelength - 440) / (490 - 440)
                b = 1
            elif 490 <= wavelength <= 560:  # Zelená až žltá
                r = 0
                g = 1
                b = (560 - wavelength) / (560 - 490)
            elif 560 <= wavelength <= 590:  # Žltá až oranžová
                r = (wavelength - 560) / (590 - 560)
                g = 1
                b = 0
            elif 590 <= wavelength <= 620:  # Oranžová až červená
                r = 1
                g = (620 - wavelength) / (620 - 590)
                b = 0
            #else:
            #    r = 1
            #    g = 0
            #    b = 0
            elif 620 <= wavelength <= max_w:  # Červená až čierna
                r = (max_w - wavelength) / (max_w - 620)
                g = 0
                b = 0
            else:  # Mimo viditeľného spektra
                r = 0
                g = 0
                b = 0
            
    
            colors.append([r, g, b])
    
        return np.array(colors)
    def wavelength_to_rgb(self, nm, min_wavelength=380, max_wavelength=780):
        #print(min_wavelength)
        #print(max_wavelength)
        gamma = 1.2
        max_intensity = 255
        factor = 0

        rgb = {"R": 0, "G": 0, "B": 0}
        #min_wavelength=0#self.docalcalibration.GetWaveLenghtByPx(0)
        #max_wavelength=1279#self.docalcalibration.GetWaveLenghtByPx(1279)
        # Check if the wavelength is within the spectrometer's range.
        if nm < min_wavelength or nm > max_wavelength:
            raise ValueError("Wavelength is out of range.")
        
        if min_wavelength <= nm <= (min_wavelength + (max_wavelength - min_wavelength) / 6):
            rgb["R"] = 0.0
            rgb["G"] = 0.0
            rgb["B"] = (nm - min_wavelength) / ((min_wavelength + (max_wavelength - min_wavelength) / 6) - min_wavelength)
        
        elif (min_wavelength + (max_wavelength - min_wavelength) / 6) <= nm <= (min_wavelength + (2 * (max_wavelength - min_wavelength) / 6)):
            rgb["R"] = 0.0
            rgb["G"] = (nm - (min_wavelength + (max_wavelength - min_wavelength) / 6)) / ((min_wavelength + (2 * (max_wavelength - min_wavelength) / 6)) - (min_wavelength + (max_wavelength - min_wavelength) / 6))
            rgb["B"] = 1.0
        elif (min_wavelength + (2 * (max_wavelength - min_wavelength) / 6)) <= nm <= (min_wavelength + (3 * (max_wavelength - min_wavelength) / 6)):
            rgb["R"] = 0.0
            rgb["G"] = 1.0
            rgb["B"] = -(nm - (min_wavelength + (3 * (max_wavelength - min_wavelength) / 6))) / ((min_wavelength + (3 * (max_wavelength - min_wavelength) / 6)) - (min_wavelength + (2 * (max_wavelength - min_wavelength) / 6)))
        elif (min_wavelength + (3 * (max_wavelength - min_wavelength) / 6)) <= nm <= (min_wavelength + (4 * (max_wavelength - min_wavelength) / 6)):
            rgb["R"] = (nm - (min_wavelength + (3 * (max_wavelength - min_wavelength) / 6))) / ((min_wavelength + (4 * (max_wavelength - min_wavelength) / 6)) - (min_wavelength + (3 * (max_wavelength - min_wavelength) / 6)))
            rgb["G"] = 1.0
            rgb["B"] = 0.0
        elif (min_wavelength + (4 * (max_wavelength - min_wavelength) / 6)) <= nm <= (min_wavelength + (5 * (max_wavelength - min_wavelength) / 6)):
            rgb["R"] = 1.0
            rgb["G"] = -(nm - (min_wavelength + (5 * (max_wavelength - min_wavelength) / 6))) / ((min_wavelength + (5 * (max_wavelength - min_wavelength) / 6)) - (min_wavelength + (4 * (max_wavelength - min_wavelength) / 6)))
            rgb["B"] = 0.0
        elif (min_wavelength + (5 * (max_wavelength - min_wavelength) / 6)) <= nm <= max_wavelength:
            rgb["R"] = 1.0 - (nm - (min_wavelength + (5 * (max_wavelength - min_wavelength) / 6))) / ((max_wavelength - (min_wavelength + (5 * (max_wavelength - min_wavelength) / 6))))
            rgb["G"] = 0.0
            rgb["B"] = 0.0
            #rgb["R"] = 1.0
            #rgb["G"] = 0.0
            #rgb["B"] = (nm - (min_wavelength + (5 * (max_wavelength - min_wavelength) / 6))) / ((max_wavelength - (min_wavelength + (5 * (max_wavelength - min_wavelength) / 6))))
        if(min_wavelength!=0):
            
            if 440 <= nm <= 489:
                rgb["R"] = 0.0
                rgb["G"] = (nm - 440) / (490 - 440)
                rgb["B"] = 1.0
            elif 490 <= nm <= 509:
                rgb["R"] = 0.0
                rgb["G"] = 1.0
                rgb["B"] = -(nm - 510) / (510 - 490)
            elif 510 <= nm <= 579:
                rgb["R"] = (nm - 510) / (580 - 510)
                rgb["G"] = 1.0
                rgb["B"] = 0.0
            elif 580 <= nm <= 644:
                rgb["R"] = 1.0
                rgb["G"] = -(nm - 645) / (645 - 580)
                rgb["B"] = 0.0
            elif 645 <= nm <= 780:
                rgb["R"] = 1.0
                rgb["G"] = 0.0
                rgb["B"] = 0.0
        # Calculate the factor.
        
        if min_wavelength <= nm <= (min_wavelength + (max_wavelength - min_wavelength) / 6):
            factor = 0.3 + 0.7 * (nm - min_wavelength) / ((min_wavelength + (max_wavelength - min_wavelength) / 6) - min_wavelength)
        elif (min_wavelength + (max_wavelength - min_wavelength)):
            factor = 1.0
        
        # Apply the gamma correction and clamp the RGB values to the range 0-255.
        if rgb["R"] > 0:
            rgb["R"] = int(max_intensity * ((rgb["R"] * factor) ** gamma))
        else:
            rgb["R"] = 0

        if rgb["G"] > 0:
            rgb["G"] = int(max_intensity * ((rgb["G"] * factor) ** gamma))
        else:
            rgb["G"] = 0

        if rgb["B"] > 0:
            rgb["B"] = int(max_intensity * ((rgb["B"] * factor) ** gamma))
        else:
            rgb["B"] = 0
            
        return (rgb["R"]/255, rgb["G"]/255, rgb["B"]/255)



    def wavelength_to_rgb_new(self,nm, spectrum_width_px=1280):
        gamma = 0.8
        max_intensity = 255
        factor = 0
        #spectrum_width_px = self.docalcalibration.GetWaveLenghtByPx(1279)
        rgb = {"R": 0, "G": 0, "B": 0}
    
        # Rozsahy vlnových dĺžok v pixeloch
        #calibration = Calibration(self.calibration)
        #calibration.Calibrate()   
        min_wavelength_px = self.docalcalibration.GetWaveLenghtByPx(0)
        max_wavelength_px = self.docalcalibration.GetWaveLenghtByPx(1279)
    
        # Prevedie vlnovú dĺžku na pixelový rozsah
        normalized_wavelength_px = (nm - min_wavelength_px) / (max_wavelength_px - min_wavelength_px) * spectrum_width_px
    
        if 0 <= normalized_wavelength_px <= spectrum_width_px:
            if 0 <= normalized_wavelength_px <= (spectrum_width_px / 6):
                rgb["R"] = 1.0
                rgb["G"] = normalized_wavelength_px / (spectrum_width_px / 6)
                rgb["B"] = 0.0
            elif (spectrum_width_px / 6) < normalized_wavelength_px <= (2 * spectrum_width_px / 6):
                rgb["R"] = 1.0 - (normalized_wavelength_px - spectrum_width_px / 6) / (spectrum_width_px / 6)
                rgb["G"] = 1.0
                rgb["B"] = 0.0
            elif (2 * spectrum_width_px / 6) < normalized_wavelength_px <= (3 * spectrum_width_px / 6):
                rgb["R"] = 0.0
                rgb["G"] = 1.0
                rgb["B"] = (normalized_wavelength_px - 2 * spectrum_width_px / 6) / (spectrum_width_px / 6)
            elif (3 * spectrum_width_px / 6) < normalized_wavelength_px <= (4 * spectrum_width_px / 6):
                rgb["R"] = 0.0
                rgb["G"] = 1.0 - (normalized_wavelength_px - 3 * spectrum_width_px / 6) / (spectrum_width_px / 6)
                rgb["B"] = 1.0
            elif (4 * spectrum_width_px / 6) < normalized_wavelength_px <= (5 * spectrum_width_px / 6):
                rgb["R"] = (normalized_wavelength_px - 4 * spectrum_width_px / 6) / (spectrum_width_px / 6)
                rgb["G"] = 0.0
                rgb["B"] = 1.0
            elif (5 * spectrum_width_px / 6) < normalized_wavelength_px <= spectrum_width_px:
                rgb["R"] = 1.0
                rgb["G"] = 0.0
                rgb["B"] = 1.0 - (normalized_wavelength_px - 5 * spectrum_width_px / 6) / (spectrum_width_px / 6)
    
        if 0 <= normalized_wavelength_px <= (spectrum_width_px / 3):
            factor = 0.3 + 0.7 * (normalized_wavelength_px / (spectrum_width_px / 3))
        elif (spectrum_width_px / 3) < normalized_wavelength_px <= spectrum_width_px:
            factor = 1.0
    
        rgb["R"] = int(max_intensity * ((rgb["R"] * factor) ** gamma))
        rgb["G"] = int(max_intensity * ((rgb["G"] * factor) ** gamma))
        rgb["B"] = int(max_intensity * ((rgb["B"] * factor) ** gamma))
    
        return (rgb["R"] / 255, rgb["G"] / 255, rgb["B"] / 255)

    def wavelength_to_rgb_old(self,nm):

        gamma = 0.8
        max_intensity = 255
        factor = 0
    
        rgb = {"R": 0, "G": 0, "B": 0}
        if 380 <= nm <= 439:
            rgb["R"] = -(nm - 440) / (440 - 380)
            rgb["G"] = 0.0
            rgb["B"] = 1.0
        elif 440 <= nm <= 489:
            rgb["R"] = 0.0
            rgb["G"] = (nm - 440) / (490 - 440)
            rgb["B"] = 1.0
        elif 490 <= nm <= 509:
            rgb["R"] = 0.0
            rgb["G"] = 1.0
            rgb["B"] = -(nm - 510) / (510 - 490)
        elif 510 <= nm <= 579:
            rgb["R"] = (nm - 510) / (580 - 510)
            rgb["G"] = 1.0
            rgb["B"] = 0.0
        elif 580 <= nm <= 644:
            rgb["R"] = 1.0
            rgb["G"] = -(nm - 645) / (645 - 580)
            rgb["B"] = 0.0
        elif 645 <= nm <= 780:
            rgb["R"] = 1.0
            rgb["G"] = 0.0
            rgb["B"] = 0.0
    
        if 380 <= nm <= 419:
            factor = 0.3 + 0.7 * (nm - 380) / (420 - 380)
        elif 420 <= nm <= 700:
            factor = 1.0
        elif 701 <= nm <= 780:
            factor = 0.3 + 0.7 * (780 - nm) / (780 - 700)
    
        if rgb["R"] > 0:
            rgb["R"] = int(max_intensity * ((rgb["R"] * factor) ** 1.5))
        else:
            rgb["R"] = 0
    
        if rgb["G"] > 0:
            rgb["G"] = int(max_intensity * ((rgb["G"] * factor) ** gamma))
        else:
            rgb["G"] = 0
    
        if rgb["B"] > 0:
            rgb["B"] = int(max_intensity * ((rgb["B"] * factor) ** 1.5))
        else:
            rgb["B"] = 0
    
        return (rgb["R"]/255, rgb["G"]/255, rgb["B"]/255)
    
    
    def moving_avg(self, x, box_pts):

        box = np.ones(box_pts)/box_pts
        y_smooth = np.convolve(x, box, mode='same')
        return y_smooth

    def get_graph3(self):

        textoffset = 12
        textoffsetX =50
        percintens = 0
        start_time = time.time()
        self.dataaa2 = []
        calibration = Calibration(self.calibration) 

        calibration.Calibrate()

        if self.vid.isOpened():

            ccoolloorrss = []

            frame = self.frame2
            ret = self.ret2
            ccoolloorrss2 = []

            if ret:

                piwidth = 1280

                bwimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rows, cols,aaaa = bwimage.shape

                elapsed_time = time.time() - start_time

                graph = np.zeros([305, piwidth, 3], dtype=np.uint8)
                graph.fill(255)  

                prevposition = 0
                textoffset = 12
                textoffsetX =50
                font = cv2.FONT_HERSHEY_SIMPLEX

                rows = self.moveline4
                if(rows > 720):
                    rows = 720

                self.halfway2 = int(rows)                

                x = 285

                """
                for i in range(piwidth):

                    if(self.showPXNMval == 1):
                        position = i
                    else:
                        position = round(zero)
                    if(i == 0):
                        poszero = position

                    if position != prevposition:  

                        if position % 20 == 0:
                            cv2.line(graph, (i + textoffsetX, 15), (i + textoffsetX, 255),
                                     (200, 200, 200), 1)

                        if position % 50 == 0:

                            cv2.line(graph, (i + textoffsetX, 15), (i + textoffsetX, 285), (0, 0, 0), 1)

                            cv2.putText(graph, str(
                                position)+self.unitsGraph, (i-textoffset + textoffsetX, 300), font, 0.3, (0, 0, 0), 1, 48)
                    zero += nmperpx
                    prevposition = position

                ""
                for i in range(300):
                    if i % 43 == 0:  
                        cv2.line(graph, (50, i), (piwidth, i),
                                 (100, 100, 100), 1)

                """
                """
                for i in range(cols-4):
                    data = bwimage[self.halfway, i]

                    if self.holdpeaks == True:
                        if data > self.intensity[i]:
                            self.intensity[i] = data
                    else:
                        self.intensity[i] = data

                if self.holdpeaks == False:

                    self.intensity = savgol_filter(
                        self.intensity, 17, int(self.savpoly))
                self.intensity = self.intensity.astype(int)

                """
                self.intensityArray = []
                intensityArrayHelp2=[]

                ccoolloorrss2 = []
                allRGB = []
                oddo = list(range(math.ceil((self.halfway2)- (self.heightline3/2)), math.ceil((self.halfway2)+ (self.heightline3/2))))

                if(self.SumMax == "MAX"):
                    get_DataSpec = np.average(np.max(bwimage[oddo].reshape(int(bwimage[oddo].size/3),3),axis=1).reshape(len(oddo),1280),axis=0)
                elif(self.SumMax == "SUM"):
                    get_DataSpec = np.average(np.sum(bwimage[oddo].reshape(int(bwimage[oddo].size/3),3),axis=1).reshape(len(oddo),1280),axis=0)
                else:
                    get_DataSpec = np.average(np.max(bwimage[oddo].reshape(int(bwimage[oddo].size/3),3),axis=1).reshape(len(oddo),1280),axis=0)
                if(0==1):

                    intensityArrayHelp =[]

                    for i in range(cols):
                        if(self.SumMax == "MAX"):
                            if(self.halogen_var == "0"):

                                getmax = max([bwimage[j, i,0],bwimage[j, i,1],bwimage[j, i,2]])
                                data = getmax
                            else:
                                getmax = max([bwimage[j, i,0],bwimage[j, i,1],bwimage[j, i,2]])
                                data = getmax
                        elif(self.SumMax == "SUM"):
                            if(self.halogen_var == "0"):

                                getmax = sum([bwimage[j, i,0],bwimage[j, i,1],bwimage[j, i,2]])
                                data = getmax
                            else:
                                getmax = sum([bwimage[j, i,0],bwimage[j, i,1],bwimage[j, i,2]])
                                data = getmax

                        self.dataaa2.append(data)
                        ccoolloorrss2.append([bwimage[j, i,0]/255,bwimage[j, i,1]/255,bwimage[j, i,2]/255])
                        allRGB.append([bwimage[j, i,0],bwimage[j, i,1],bwimage[j, i,2]])

                        data_new = data

                        if self.holdpeaks == True:
                            if data > self.intensity[i]:

                                intensityArrayHelp.append(data_new)
                        else:

                            intensityArrayHelp.append(data_new)

                    if(self.autoYgraph == 1):
                        new255 = max(intensityArrayHelp)
                        if(self.SumMax == "MAX"):
                            percintens = 1
                        elif(self.SumMax == "SUM"):
                            percintens = 1
                        for xx in range(len(intensityArrayHelp)):
                            intensityArrayHelp2.append(intensityArrayHelp[xx]*percintens)
                        self.intensityArray.append(intensityArrayHelp2)
                    else:
                        self.intensityArray.append(intensityArrayHelp)

                """
                for i in range(0,len(self.intensityArray[0])-1):
                    cellValue = 0
                    for j in range(len(self.intensityArray)-1):

                        cellValue += self.intensityArray[j][i]
                        if len(self.intensityArray) == j-1:
                            self.dataIntensity[i] = cellValue/len(self.intensityArray)

                """

                self.dataIntensity = get_DataSpec

                self.intensity = self.dataIntensity

                if self.holdpeaks == False:

                    try:
                        """
                        self.intensity = savgol_filter(
                            self.intensity, 5, int(float(self.savpoly)))
                        """
                        self.intensity = self.moving_avg(self.intensity,int(float(self.savpoly)))
                    except Exception as e:
                        print(e)
                        print("problem s vyhladenim")
                self.intensity = self.intensity.astype(float)
                self.intensitynewww22 = []
                if(self.SumMax == "MAX"):
                    for i in range(len(self.intensity)):
                        if(self.intensity[i] > 255):
                            self.intensity[i] = 255

                        self.intensitynewww22.append(self.intensity[i])
                elif(self.SumMax == "SUM"):
                    for i in range(len(self.intensity)):

                        self.intensitynewww22.append(self.intensity[i])
                self.intensity = self.intensitynewww22

                if(self.halogen_var == "1"):

                    self.newintensity = []
                    x = np.polyfit(list(range(0,len(self.intensity))),self.intensity,3)

                    if(self.calHalnow == 1):
                        file1 = open("calibHal.txt","w")
                        for i in range(len(self.intensity)):
                            k = x[3] + x[2] * i + x[1] * i * i + x[0] * i * i * i

                            if(self.intensity[i] >0):
                                if(k/self.intensity[i] >0):
                                    self.newintensity.append(k/self.intensity[i])
                                else:
                                    self.newintensity.append(0)
                            else:
                                self.newintensity.append(0)

                        file1.write(';'.join([str(elem) for elem in self.newintensity])) 
                        file1.close()
                        self.calHalnow = 0

                    file1 = open("calibHal.txt","r")
                    self.newintensity = file1.readlines()[0].split(";")

                    file1.close()
                    self.newintensity2 = []
                    for i in range(len(self.newintensity)):
                        try:
                            if( self.intensity[i] != 255):
                                if(int(float(self.newintensity[i])*self.intensity[i]) > 255):
                                    newint = 255
                                else:
                                    newint = int(float(self.newintensity[i])*self.intensity[i])
                            else:
                                newint = 255 
                            self.newintensity2.append(newint)
                        except:
                            #print("tu som zastal 6")
                            aa=123

                    self.intensity = self.newintensity2
                self.wavelengthdata = []
                index = 0

                a = []
                self.intensity2 = self.intensity
                k = 0

                for i in self.intensity:

                    wavelength = calibration.GetWaveLenghtByPx(index)
                    wavelengthdata = round(wavelength,1)
                    wavelength = round(wavelength)
                    self.wavelengthdata.append(wavelengthdata)
                    rgb = 0#self.wavelength_to_rgb(wavelength)
                    ccoolloorrss.append(rgb)
                    r = rgb[0]
                    g = rgb[1]
                    b = rgb[2]

                    index += 1

                a = []

                thresh = int(self.thresh)  
                indexes = peakutils.indexes(
                    np.array(self.intensity), thres=thresh/max(self.intensity), min_dist=self.mindist)

                for i in indexes:

                    height = self.intensity[i]
                    height = 245-height

                    if(self.showPXNMval == 1):
                        wavelength = i
                    else:
                        wavelength = calibration.GetWaveLenghtByPx(i)

                graphdata = []
                graphdata.append(graph)
                graphdata.append(self.wavelengthdata)
                graphdata.append(self.intensity)
                graphdata.append(indexes)
                graphdata.append(ccoolloorrss)
                graphdata.append(allRGB)
                graphdata.append(ccoolloorrss2)
                return (ret, graphdata)
            else:
                return (ret, None)
        else:
            ret = True
            return (ret, None)

    def get_graph(self,pridat=False):

        start_time = time.time()

        calibration = Calibration(self.calibration)
        calibration.Calibrate()       

        if self.vid.isOpened() or self.entryfile_path != "" or self.isblack == True:

            frame = self.frame
            ret = self.ret
            ccoolloorrss = []
            ccoolloorrss2 = []

            if ret:

                piwidth = 1280

                bwimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rows, cols,aaaa = bwimage.shape

                elapsed_time = time.time() - start_time

                graph = np.zeros([305, piwidth, 3], dtype=np.uint8)

                graph.fill(255)  

                pxrange = abs(self.calibration[0][0]-self.calibration[1][0])

                nmrange = abs(self.calibration[0][1]-self.calibration[1][1])

                pxpernm = pxrange/nmrange

                nmperpx = nmrange/pxrange

                zero = self.calibration[0][1]-(self.calibration[0][0]/pxpernm)
                scalezero = zero  
                prevposition = 0
                textoffset = 12
                textoffsetX =50
                font = cv2.FONT_HERSHEY_SIMPLEX

                rows = self.moveline

                if(rows > 720):
                    rows = 720

                self.halfway = int(rows)                

                x = 285

                for i in range(piwidth):
                    if(self.showPXNMval == 1):
                        position = i
                    else:
                        position = round(zero)
                    if(i == 0):
                        poszero = position

                    if position != prevposition:  

                        """
                        if position % 20 == 0:
                            cv2.line(graph, (i + textoffsetX, 15), (i + textoffsetX, 255),
                                     (200, 200, 200), 1)
                        """
                        if position % 50 == 0:

                            cv2.line(graph, (i + textoffsetX, 15), (i + textoffsetX, 285), (0, 0, 0), 1)

                            cv2.putText(graph, str(
                                position)+self.unitsGraph, (i-textoffset + textoffsetX, 300), font, 0.3, (0, 0, 0), 1, 48)
                    zero += nmperpx
                    prevposition = position

                for i in range(300):
                    if i % 43 == 0:  
                        cv2.line(graph, (50, i), (piwidth, i),
                                 (100, 100, 100), 1)

                """
                for i in range(cols-4):
                    data = bwimage[self.halfway, i]

                    if self.holdpeaks == True:
                        if data > self.intensity[i]:
                            self.intensity[i] = data
                    else:
                        self.intensity[i] = data

                if self.holdpeaks == False:

                    self.intensity = savgol_filter(
                        self.intensity, 17, int(self.savpoly))
                self.intensity = self.intensity.astype(int)

                """
                self.intensityArray = []
                intensityArrayHelp2=[]
                percintens = 0
                self.dataaa = []
                ccoolloorrss = []

                allRGB = []
                if(pridat == False):
                    oddo = list(range(math.ceil((self.halfway)- (self.heightline/2)), math.ceil((self.halfway)+ (self.heightline/2))))
                else:
                    self.halfway = pridat
                    oddo = list(range(math.ceil((self.halfway)- (self.heightline/2)), math.ceil((self.halfway)+ (self.heightline/2))))
                
                reshapeArr = bwimage[oddo].reshape(int(bwimage[oddo].size/3),3)
                reshapeArr = reshapeArr.astype(np.float64)
                """
                print("pred: ")
                print(reshapeArr)
                """
                #print(int(self.RKonst))
                #reshapeArr[:, 0] *= int(self.RKonst)
                reshapeArr[:, 0] *= float(self.RKonst)
                reshapeArr[:, 1] *= float(self.GKonst)
                reshapeArr[:, 2] *= float(self.BKonst)
                """
                print("po: ")
                print(reshapeArr)
                """
                rgbtoexport = []
                rgbtoexport.append(reshapeArr)
                if(self.SumMax == "MAX"):
                    get_DataSpec = np.average(np.max(reshapeArr,axis=1).reshape(len(oddo),1280),axis=0)
                    #print("vysledok: ")
                    #print(get_DataSpec)
                    
                elif(self.SumMax == "SUM"):
                    get_DataSpec = np.average(np.sum(reshapeArr,axis=1).reshape(len(oddo),1280),axis=0)
                else:
                    get_DataSpec = np.average(np.max(reshapeArr,axis=1).reshape(len(oddo),1280),axis=0)

                if(0==1):

                    intensityArrayHelp =[]

                    for i in range(cols):

                        if(self.SumMax == "MAX"):
                            if(self.halogen_var == "0"):

                                getmax = max([bwimage[j, i,0]*self.RKonst,bwimage[j, i,1]*self.GKonst,bwimage[j, i,2]*self.BKonst])

                                data = getmax
                            else:
                                getmax = max([bwimage[j, i,0]*self.RKonst,bwimage[j, i,1]*self.GKonst,bwimage[j, i,2]*self.BKonst])
                                data = getmax

                        elif(self.SumMax == "SUM"):
                            if(self.halogen_var == "0"):

                                getmax = sum([bwimage[j, i,0]*self.RKonst,bwimage[j, i,1]*self.GKonst,bwimage[j, i,2]*self.BKonst])

                                data = getmax
                            else:
                                getmax = sum([bwimage[j, i,0]*self.RKonst,bwimage[j, i,1]*self.GKonst,bwimage[j, i,2]*self.BKonst])
                                data = getmax

                        allRGB.append([bwimage[j, i,0],bwimage[j, i,1],bwimage[j, i,2]])

                        self.dataaa.append(data)

                        try:
                            if(self.getBG == 1):
                                self.getBG = 2
                                self.dataBG = []
                            if(self.getBG > 1):

                                self.dataBG.append(data)

                        except:
                            #print("tu som zastal 7")
                            self.dataBG = []
                            a=1

                        if(self.setBG == True):

                            data = data - self.dataBG[i]
                        ccoolloorrss2.append([bwimage[j, i,0]/255,bwimage[j, i,1]/255,bwimage[j, i,2]/255])

                        if self.holdpeaks == True:
                            if data > self.intensity[i]:

                                intensityArrayHelp.append(data)
                        else:

                            intensityArrayHelp.append(data)

                    if(self.autoYgraph == 1):
                        new255 = max(intensityArrayHelp)

                        if(self.SumMax == "MAX"):
                            percintens = 1
                        elif(self.SumMax == "SUM"):
                            percintens = 1

                        for xx in range(len(intensityArrayHelp)):
                            intensityArrayHelp2.append(intensityArrayHelp[xx]*percintens)
                        self.intensityArray.append(intensityArrayHelp2)
                    else:
                        self.intensityArray.append(intensityArrayHelp)

                prevY = 0

                self.dataIntensity = get_DataSpec

                self.intensity = self.dataIntensity

                if self.holdpeaks == False:

                    try:
                        """
                        self.intensity = savgol_filter(
                            self.intensity, 5, int(float(self.savpoly)))
                        """
                        self.intensity = self.moving_avg(self.intensity,int(float(self.savpoly)))
                    except Exception as e:
                        a=1
                        print("problem s vyhladenim 2")
                        print(e)
                self.intensity = self.intensity.astype(float)
                self.intensitynewww = []
                if(self.SumMax == "MAX"):
                    for i in range(len(self.intensity)):
                        if(self.intensity[i] > 255):
                            self.intensity[i] = 255

                        self.intensitynewww.append(self.intensity[i])
                elif(self.SumMax == "SUM"):
                    for i in range(len(self.intensity)):

                        self.intensitynewww.append(self.intensity[i])
                self.intensity = self.intensitynewww
                if(self.halogen_var == "0"):

                    self.newintensity = []
                    x = np.polyfit(list(range(0,len(self.intensity))),self.intensity,3)
                    if(self.calHalnow == 1):
                        file1 = open("calibHal.txt","w")
                        for i in range(len(self.intensity)):
                            k = x[3] + x[2] * i + x[1] * i * i + x[0] * i * i * i

                            if(self.intensity[i] >0):
                                if(k/self.intensity[i] >0):
                                    self.newintensity.append(k/self.intensity[i])
                                else:
                                    self.newintensity.append(0)
                            else:
                                self.newintensity.append(0)

                        file1.write(';'.join([str(elem) for elem in self.newintensity])) 
                        file1.close()
                        self.calHalnow = 0

                    file1 = open("calibHal.txt","r")
                    self.newintensity = file1.readlines()[0].split(";")

                    file1.close()
                    self.newintensity2 = []
                    for i in range(len(self.newintensity)):
                        try:
                            if( self.intensity[i] != 255):
                                if(int(float(self.newintensity[i])*self.intensity[i]) > 255):
                                    newint = 255
                                else:
                                    newint = int(float(self.newintensity[i])*self.intensity[i])
                            else:
                                newint = 255 
                            self.newintensity2.append(newint)
                        except:
                            #print("tu som zastal 8")
                            aaaa=1

                    self.intensity = self.newintensity2

                self.wavelengthdata = []
                index = 0
                a = []

                for i in self.intensity:

                    wavelength = calibration.GetWaveLenghtByPx(index)
                    wavelengthdata = round(wavelength,1)
                    wavelength = round(wavelength)
                    self.wavelengthdata.append(wavelengthdata)
                    rgb = [0,0,0]#self.wavelength_to_rgb(wavelength)
                    ccoolloorrss.append(rgb)
                    r = rgb[0]
                    g = rgb[1]
                    b = rgb[2]

                    if(self.justnm  != None):
                        if(wavelength == self.justnm):
                            """

                            if(self.colorGraph==0):
                                cv2.line(graph, (index + textoffsetX, 285), (index + textoffsetX, 285-i), (r, g, b), 1)

                                cv2.line(graph, (index + textoffsetX, 284-i), (index + textoffsetX, 285-i),
                                         (0, 0, 0), 1, cv2.LINE_AA)
                            else:
                                cv2.line(graph, (index + textoffsetX, 284-i), (index + textoffsetX, 285-i),
                                         (0, 0, 0), 2, cv2.LINE_AA)
                        """
                        a = 1
                    else:

                        if(self.colorGraph==0):
                            """
                            cv2.line(graph, (index + textoffsetX, 285), (index + textoffsetX, 285-i), (r, g, b), 1)

                            cv2.line(graph, (index + textoffsetX, 284-i), (index + textoffsetX, 285-i),
                                     (0, 0, 0), 1, cv2.LINE_AA)
                                     """
                            a.append((index + textoffsetX, 285-i))
                        else:

                            a.append((index + textoffsetX, 285-i))

                    index += 1

                """
                for index, item in enumerate(a): 
                    if index == len(a) -1:
                        break
                    cv2.line(graph, item, a[index + 1], [0, 0, 0], 1) 
                """

                a = []

                thresh = int(self.thresh)  
                indexes = peakutils.indexes(
                    np.array(self.intensity), thres=thresh/max(self.intensity), min_dist=self.mindist)

                for i in indexes:

                    height = self.intensity[i]
                    height = 245-height

                    if(self.showPXNMval == 1):
                        wavelength = i
                    else:
                        wavelength = calibration.GetWaveLenghtByPx(i)

                self.getBG = 0
                graphdata = []
                graphdata.append(graph)
                graphdata.append(self.wavelengthdata)
                graphdata.append(self.intensity)
                graphdata.append(indexes)
                graphdata.append(ccoolloorrss)
                graphdata.append(allRGB)
                graphdata.append(ccoolloorrss2)
                graphdata.append(rgbtoexport)
                return (ret, graphdata)
            else:
                return (ret, None)
        else:
            ret = True
            return (ret, None)
    def get_graph2(self,pridat=False):

        start_time = time.time()

        calibration = Calibration(self.calibration)
        calibration.Calibrate()       

        if self.vid.isOpened() or self.entryfile_path != "" or self.isblack == True:

            frame = self.frame2
            ret = self.ret2
            ccoolloorrss = []
            ccoolloorrss2 = []

            if ret:

                piwidth = 1280

                bwimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rows, cols,aaaa = bwimage.shape

                elapsed_time = time.time() - start_time

                graph = np.zeros([305, piwidth, 3], dtype=np.uint8)

                graph.fill(255)  

                pxrange = abs(self.calibration[0][0]-self.calibration[1][0])

                nmrange = abs(self.calibration[0][1]-self.calibration[1][1])

                pxpernm = pxrange/nmrange

                nmperpx = nmrange/pxrange

                zero = self.calibration[0][1]-(self.calibration[0][0]/pxpernm)
                scalezero = zero  
                prevposition = 0
                textoffset = 12
                textoffsetX =50
                font = cv2.FONT_HERSHEY_SIMPLEX

                rows = self.moveline4

                if(rows > 720):
                    rows = 720

                self.halfway2 = int(rows)                

                x = 285

                for i in range(piwidth):
                    if(self.showPXNMval == 1):
                        position = i
                    else:
                        position = round(zero)
                    if(i == 0):
                        poszero = position

                    if position != prevposition:  

                        """
                        if position % 20 == 0:
                            cv2.line(graph, (i + textoffsetX, 15), (i + textoffsetX, 255),
                                     (200, 200, 200), 1)
                        """
                        if position % 50 == 0:

                            cv2.line(graph, (i + textoffsetX, 15), (i + textoffsetX, 285), (0, 0, 0), 1)

                            cv2.putText(graph, str(
                                position)+self.unitsGraph, (i-textoffset + textoffsetX, 300), font, 0.3, (0, 0, 0), 1, 48)
                    zero += nmperpx
                    prevposition = position

                for i in range(300):
                    if i % 43 == 0:  
                        cv2.line(graph, (50, i), (piwidth, i),
                                 (100, 100, 100), 1)

                """
                for i in range(cols-4):
                    data = bwimage[self.halfway, i]

                    if self.holdpeaks == True:
                        if data > self.intensity[i]:
                            self.intensity[i] = data
                    else:
                        self.intensity[i] = data

                if self.holdpeaks == False:

                    self.intensity = savgol_filter(
                        self.intensity, 17, int(self.savpoly))
                self.intensity = self.intensity.astype(int)

                """
                self.intensityArray = []
                intensityArrayHelp2=[]
                percintens = 0
                self.dataaa = []
                ccoolloorrss = []

                allRGB = []
                if(pridat == False):
                    oddo = list(range(math.ceil((self.halfway2)- (self.heightline3/2)), math.ceil((self.halfway2)+ (self.heightline3/2))))
                else:
                    self.halfway2 = pridat
                    oddo = list(range(math.ceil((self.halfway2)- (self.heightline3/2)), math.ceil((self.halfway2)+ (self.heightline3/2))))
                
                reshapeArr = bwimage[oddo].reshape(int(bwimage[oddo].size/3),3)
                reshapeArr = reshapeArr.astype(np.float64)
                """
                print("pred: ")
                print(reshapeArr)
                """
                #print(int(self.RKonst))
                #reshapeArr[:, 0] *= int(self.RKonst)
                reshapeArr[:, 0] *= float(self.RKonst)
                reshapeArr[:, 1] *= float(self.GKonst)
                reshapeArr[:, 2] *= float(self.BKonst)
                """
                print("po: ")
                print(reshapeArr)
                """
                rgbtoexport = []
                rgbtoexport.append(reshapeArr)
                if(self.SumMax == "MAX"):
                    get_DataSpec = np.average(np.max(reshapeArr,axis=1).reshape(len(oddo),1280),axis=0)
                    #print("vysledok: ")
                    #print(get_DataSpec)
                    
                elif(self.SumMax == "SUM"):
                    get_DataSpec = np.average(np.sum(reshapeArr,axis=1).reshape(len(oddo),1280),axis=0)
                else:
                    get_DataSpec = np.average(np.max(reshapeArr,axis=1).reshape(len(oddo),1280),axis=0)

                if(0==1):

                    intensityArrayHelp =[]

                    for i in range(cols):

                        if(self.SumMax == "MAX"):
                            if(self.halogen_var == "0"):

                                getmax = max([bwimage[j, i,0]*self.RKonst,bwimage[j, i,1]*self.GKonst,bwimage[j, i,2]*self.BKonst])

                                data = getmax
                            else:
                                getmax = max([bwimage[j, i,0]*self.RKonst,bwimage[j, i,1]*self.GKonst,bwimage[j, i,2]*self.BKonst])
                                data = getmax

                        elif(self.SumMax == "SUM"):
                            if(self.halogen_var == "0"):

                                getmax = sum([bwimage[j, i,0]*self.RKonst,bwimage[j, i,1]*self.GKonst,bwimage[j, i,2]*self.BKonst])

                                data = getmax
                            else:
                                getmax = sum([bwimage[j, i,0]*self.RKonst,bwimage[j, i,1]*self.GKonst,bwimage[j, i,2]*self.BKonst])
                                data = getmax

                        allRGB.append([bwimage[j, i,0],bwimage[j, i,1],bwimage[j, i,2]])

                        self.dataaa.append(data)

                        try:
                            if(self.getBG == 1):
                                self.getBG = 2
                                self.dataBG = []
                            if(self.getBG > 1):

                                self.dataBG.append(data)

                        except:
                            #print("tu som zastal 7")
                            self.dataBG = []
                            a=1

                        if(self.setBG == True):

                            data = data - self.dataBG[i]
                        ccoolloorrss2.append([bwimage[j, i,0]/255,bwimage[j, i,1]/255,bwimage[j, i,2]/255])

                        if self.holdpeaks == True:
                            if data > self.intensity[i]:

                                intensityArrayHelp.append(data)
                        else:

                            intensityArrayHelp.append(data)

                    if(self.autoYgraph == 1):
                        new255 = max(intensityArrayHelp)

                        if(self.SumMax == "MAX"):
                            percintens = 1
                        elif(self.SumMax == "SUM"):
                            percintens = 1

                        for xx in range(len(intensityArrayHelp)):
                            intensityArrayHelp2.append(intensityArrayHelp[xx]*percintens)
                        self.intensityArray.append(intensityArrayHelp2)
                    else:
                        self.intensityArray.append(intensityArrayHelp)

                prevY = 0

                self.dataIntensity = get_DataSpec

                self.intensity = self.dataIntensity

                if self.holdpeaks == False:

                    try:
                        """
                        self.intensity = savgol_filter(
                            self.intensity, 5, int(float(self.savpoly)))
                        """
                        self.intensity = self.moving_avg(self.intensity,int(float(self.savpoly)))
                    except Exception as e:
                        a=1
                        print("problem s vyhladenim 2")
                        print(e)
                self.intensity = self.intensity.astype(float)
                self.intensitynewww = []
                if(self.SumMax == "MAX"):
                    for i in range(len(self.intensity)):
                        if(self.intensity[i] > 255):
                            self.intensity[i] = 255

                        self.intensitynewww.append(self.intensity[i])
                elif(self.SumMax == "SUM"):
                    for i in range(len(self.intensity)):

                        self.intensitynewww.append(self.intensity[i])
                self.intensity = self.intensitynewww
                if(self.halogen_var == "0"):

                    self.newintensity = []
                    x = np.polyfit(list(range(0,len(self.intensity))),self.intensity,3)
                    if(self.calHalnow == 1):
                        file1 = open("calibHal.txt","w")
                        for i in range(len(self.intensity)):
                            k = x[3] + x[2] * i + x[1] * i * i + x[0] * i * i * i

                            if(self.intensity[i] >0):
                                if(k/self.intensity[i] >0):
                                    self.newintensity.append(k/self.intensity[i])
                                else:
                                    self.newintensity.append(0)
                            else:
                                self.newintensity.append(0)

                        file1.write(';'.join([str(elem) for elem in self.newintensity])) 
                        file1.close()
                        self.calHalnow = 0

                    file1 = open("calibHal.txt","r")
                    self.newintensity = file1.readlines()[0].split(";")

                    file1.close()
                    self.newintensity2 = []
                    for i in range(len(self.newintensity)):
                        try:
                            if( self.intensity[i] != 255):
                                if(int(float(self.newintensity[i])*self.intensity[i]) > 255):
                                    newint = 255
                                else:
                                    newint = int(float(self.newintensity[i])*self.intensity[i])
                            else:
                                newint = 255 
                            self.newintensity2.append(newint)
                        except:
                            #print("tu som zastal 8")
                            aaaa=1

                    self.intensity = self.newintensity2

                self.wavelengthdata = []
                index = 0
                a = []

                for i in self.intensity:

                    wavelength = calibration.GetWaveLenghtByPx(index)
                    wavelengthdata = round(wavelength,1)
                    wavelength = round(wavelength)
                    self.wavelengthdata.append(wavelengthdata)
                    rgb = [0,0,0]#self.wavelength_to_rgb(wavelength)
                    ccoolloorrss.append(rgb)
                    r = rgb[0]
                    g = rgb[1]
                    b = rgb[2]

                    if(self.justnm  != None):
                        if(wavelength == self.justnm):
                            """

                            if(self.colorGraph==0):
                                cv2.line(graph, (index + textoffsetX, 285), (index + textoffsetX, 285-i), (r, g, b), 1)

                                cv2.line(graph, (index + textoffsetX, 284-i), (index + textoffsetX, 285-i),
                                         (0, 0, 0), 1, cv2.LINE_AA)
                            else:
                                cv2.line(graph, (index + textoffsetX, 284-i), (index + textoffsetX, 285-i),
                                         (0, 0, 0), 2, cv2.LINE_AA)
                        """
                        a = 1
                    else:

                        if(self.colorGraph==0):
                            """
                            cv2.line(graph, (index + textoffsetX, 285), (index + textoffsetX, 285-i), (r, g, b), 1)

                            cv2.line(graph, (index + textoffsetX, 284-i), (index + textoffsetX, 285-i),
                                     (0, 0, 0), 1, cv2.LINE_AA)
                                     """
                            a.append((index + textoffsetX, 285-i))
                        else:

                            a.append((index + textoffsetX, 285-i))

                    index += 1

                """
                for index, item in enumerate(a): 
                    if index == len(a) -1:
                        break
                    cv2.line(graph, item, a[index + 1], [0, 0, 0], 1) 
                """

                a = []

                thresh = int(self.thresh)  
                indexes = peakutils.indexes(
                    np.array(self.intensity), thres=thresh/max(self.intensity), min_dist=self.mindist)

                for i in indexes:

                    height = self.intensity[i]
                    height = 245-height

                    if(self.showPXNMval == 1):
                        wavelength = i
                    else:
                        wavelength = calibration.GetWaveLenghtByPx(i)

                self.getBG = 0
                graphdata = []
                graphdata.append(graph)
                graphdata.append(self.wavelengthdata)
                graphdata.append(self.intensity)
                graphdata.append(indexes)
                graphdata.append(ccoolloorrss)
                graphdata.append(allRGB)
                graphdata.append(ccoolloorrss2)
                graphdata.append(rgbtoexport)
                return (ret, graphdata)
            else:
                return (ret, None)
        else:
            ret = True
            return (ret, None)

    def getpeaks(self,y):
        calibration = Calibration(self.calibration) 

        calibration.Calibrate()
        thresh = int(self.thresh)  
        
        x_abs = np.absolute(np.array(y))
        try:
            indexes = peakutils.indexes(
                x_abs, thres=thresh/max(y), min_dist=self.mindist)
            
        except:
            #print("tu som zastal 9")
            indexes = peakutils.indexes(
                np.array(y), thres=0, min_dist=self.mindist)

        for i in indexes:

            height = self.intensity[i]
            height = 245-height

            if(self.showPXNMval == 1):
                wavelength = i
            else:
                wavelength = calibration.GetWaveLenghtByPx(i)
        return indexes

    def rotate_image(self, image, angle):

        image_center = tuple(np.array(image.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
        result = cv2.warpAffine(
          image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
        return result

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

def arg_parser() -> argparse.ArgumentParser:
    def parse_calibration(s):
        return tuple([tuple(map(int, p.split(':', 1))) for p in s.split(',', 1)])

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--calibration', type=parse_calibration)
    return parser

appka = App(arg_parser().parse_args(), customtkinter.CTk(), "Spectra",int(configdata["camspect"]),int(configdata["camrgb"]))

