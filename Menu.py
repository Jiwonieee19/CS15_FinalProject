from tkinter import *
from PIL import Image, ImageTk
from DynamicFont import *
import customtkinter as ctk
import subprocess
import sys

def nextPage():
    openNextPy()
    landingWindow.after(3000, closeThisPy)

def returnPage():
    openPastPy()
    landingWindow.after(3000, closeThisPy)

def openNextPy():
    # Launch the next Python file
    subprocess.Popen([sys.executable, "Menu.py"])

def openPastPy():
    # Launch the next Python file
    subprocess.Popen([sys.executable, "OrderType.py"])

def closeThisPy():
    # CLose the current window
    landingWindow.destroy()

yellowPalette = "#CDAE00"
redPalette = "#730C03"
whitePalette = "#FFFFFF"

landingWindow = Tk()

# Manipulating the headbar doesnt matter since we will remove this to achieve kiosk
landingWindow.title("MAIN MENU")
iconLogo = PhotoImage(file='reso/LOGO.png')
landingWindow.iconphoto(True, iconLogo)

# landingWindow.overrideredirect(True) # remove ang header to look more like a kiosk
landingWindow.resizable(False, False)
landingWindow.geometry("540x960+583+20") # width,height,x,y
landingWindow.config(background=yellowPalette)

text_photo = usingOurFontWithPadding('RETURN', 92, 25, whitePalette)
# return button
returnButton = ctk.CTkButton(landingWindow, width=200, height=50, image=text_photo, text="", corner_radius=10, fg_color=redPalette, command=returnPage)
returnButton.place(relx=0.25, rely=0.07, anchor='center')

# Real Logo top right
img = Image.open('reso/realLogo.png')
reImg = img.resize((120,108))
landingLogo = ImageTk.PhotoImage(reImg)
logoLabel = Label(landingWindow, image=landingLogo, bg=yellowPalette)
logoLabel.place(relx=0.85, rely=0, anchor='n')


# top red bg
topBg = ctk.CTkFrame(landingWindow, width=475, height=570, corner_radius=10, fg_color=redPalette)
topBg.place(relx=0.5, rely=0.44, anchor='center')

ramenText = usingOurFont('RAMEN SECTION', 280, 38, whitePalette)
# Create label with the text image
label = Label(landingWindow, image=ramenText, bg=redPalette)
label.place(relx=0.35, rely=0.18, anchor='center')

# mid red bg
topBg = ctk.CTkFrame(landingWindow, width=475, height=150, corner_radius=10, fg_color=redPalette)
topBg.place(relx=0.5, rely=0.83, anchor='center')

myorderText = usingOurFont('MY ORDER:', 280, 38, whitePalette)
# Create label with the text image
label = Label(landingWindow, image=myorderText, bg=redPalette)
label.place(relx=0.35, rely=0.78, anchor='center')


text_photo = usingOurFontWithPadding('CANCEL', 92, 25, whitePalette)
# cancel button
cancelButton = ctk.CTkButton(landingWindow, width=150, height=50, image=text_photo, text="", corner_radius=10, fg_color=redPalette)
cancelButton.place(relx=0.2, rely=0.95, anchor='center')

text_photo = usingOurFontWithPadding('VIEW', 58, 25, whitePalette)
# view button
viewButton = ctk.CTkButton(landingWindow, width=150, height=50, image=text_photo, text="", corner_radius=10, fg_color=redPalette)
viewButton.place(relx=0.5, rely=0.95, anchor='center')

text_photo = usingOurFontWithPadding('PROCEED', 106, 25, whitePalette)
# proceed button
proceedButton = ctk.CTkButton(landingWindow, width=150, height=50, image=text_photo, text="", corner_radius=10, fg_color='#27ae16')
proceedButton.place(relx=0.8, rely=0.95, anchor='center')

landingWindow.mainloop()