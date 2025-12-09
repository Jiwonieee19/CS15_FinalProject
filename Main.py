from tkinter import *
from PIL import Image, ImageTk
from DynamicFont import usingOurFont
import subprocess
import sys

# windows = frame/panel
# widgets = components(button,label,image)

def openStartPy():
    # Launch the next Python file
    subprocess.Popen([sys.executable, "Start.py"])

def closeThisPy():
    # CLose the current window
    landingWindow.destroy()

yellowPalette = "#CDAE00"
redPalette = "#730C03"
whitePalette = "#FFFFFF"

landingWindow = Tk()

# Manipulating the headbar doesnt matter since we will remove this to achieve kiosk
landingWindow.title("Python - KIOSK")
iconLogo = PhotoImage(file='reso/LOGO.png')
landingWindow.iconphoto(True, iconLogo)

# landingWindow.overrideredirect(True) # remove ang header to look more like a kiosk
landingWindow.resizable(False, False)
landingWindow.geometry("540x960+583+20") # width,height,x,y
landingWindow.config(background=yellowPalette)

# Resizing the Image base sakong gusto
img = Image.open('reso/landingLogo.png')
reImg = img.resize((221,229))
landingLogo = ImageTk.PhotoImage(reImg)
logoLabel = Label(landingWindow, image=landingLogo, bg=yellowPalette)
logoLabel.place(relx=0.5, rely=0.3, anchor='center')

text_photo = usingOurFont('"Where Noodles hug the Soul."', 340, 24, whitePalette)
# Create label with the text image
label = Label(landingWindow, image=text_photo, bg=yellowPalette)
label.place(relx=0.5, rely=0.59, anchor='center')

landingWindow.after(2500, openStartPy)
landingWindow.after(6000, closeThisPy)
landingWindow.mainloop()