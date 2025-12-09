from tkinter import *
from PIL import Image, ImageTk
from DynamicFont import usingOurFont, usingOurFontWithHeight
import subprocess
import sys

def nextPage():
    openNextPy()
    landingWindow.after(3000, closeThisPy)

def openNextPy():
    # Launch the next Python file
    subprocess.Popen([sys.executable, "Menu.py"])

def closeThisPy():
    # CLose the current window
    landingWindow.destroy()

yellowPalette = "#CDAE00"
redPalette = "#730C03"
whitePalette = "#FFFFFF"

landingWindow = Tk()

# Manipulating the headbar doesnt matter since we will remove this to achieve kiosk
landingWindow.title("ORDER TYPE")
iconLogo = PhotoImage(file='reso/LOGO.png')
landingWindow.iconphoto(True, iconLogo)

# landingWindow.overrideredirect(True) # remove ang header to look more like a kiosk
landingWindow.resizable(False, False)
landingWindow.geometry("540x960+583+20") # width,height,x,y
landingWindow.config(background=yellowPalette)


# Real Logo center
img = Image.open('reso/realLogo.png')
reImg = img.resize((120,108))
landingLogo = ImageTk.PhotoImage(reImg)
logoLabel = Label(landingWindow, image=landingLogo, bg=yellowPalette)
logoLabel.place(relx=0.5, rely=0.15, anchor='center')

orderTypeText = usingOurFont('ORDER TYPE', 215, 38, whitePalette)
# Create label with the text image
label = Label(landingWindow, image=orderTypeText, bg=yellowPalette)
label.place(relx=0.5, rely=0.33, anchor='center')

languageText = usingOurFont('SELECT YOUR LANGUAGE', 427, 38, whitePalette)
# Create label with the text image
label = Label(landingWindow, image=languageText, bg=yellowPalette)
label.place(relx=0.5, rely=0.74, anchor='center')


# 2 button 1 Frame
DineInImg = Image.open('reso/dineIn.png')
reDineInImg = DineInImg.resize((163,222))
DineIn = ImageTk.PhotoImage(reDineInImg)

TakeOutImg = Image.open('reso/takeOut.png')
reTakeOutImg = TakeOutImg.resize((163,222))
TakeOut = ImageTk.PhotoImage(reTakeOutImg)

# Create a frame inside landingWindow
buttonFrame = Frame(landingWindow, bg=yellowPalette)
buttonFrame.place(relx=0.5, rely=0.5, anchor='center')

# First button
startButton = Button(buttonFrame, image=DineIn, bg=yellowPalette, borderwidth=0, highlightthickness=0, command=nextPage)
startButton.pack(side=LEFT, padx=20)   # spacing between buttons

# Second button
optionButton = Button(buttonFrame, image=TakeOut, bg=yellowPalette, borderwidth=0, highlightthickness=0, command=nextPage)
optionButton.pack(side=LEFT, padx=20)


# 3 button 1 Frame
EnglishImg = Image.open('reso/english.png')
reEnglishImg = EnglishImg.resize((132,70))
English = ImageTk.PhotoImage(reEnglishImg)

TagalogImg = Image.open('reso/tagalog.png')
reTagalogImg = TagalogImg.resize((132,70))
Tagalog = ImageTk.PhotoImage(reTagalogImg)

BisayaImg = Image.open('reso/bisaya.png')
reBisayaImg = BisayaImg.resize((132,70))
Bisaya = ImageTk.PhotoImage(reBisayaImg)

# Create a frame inside landingWindow
buttonFrame1 = Frame(landingWindow, bg=yellowPalette)
buttonFrame1.place(relx=0.5, rely=0.83, anchor='center')

# First button
startButton = Button(buttonFrame1, image=English, bg=yellowPalette, borderwidth=0, highlightthickness=0)
startButton.pack(side=LEFT, padx=10)   # spacing between buttons

# Second button
optionButton = Button(buttonFrame1, image=Tagalog, bg=yellowPalette, borderwidth=0, highlightthickness=0)
optionButton.pack(side=LEFT, padx=10)

# Third button
optionButton = Button(buttonFrame1, image=Bisaya, bg=yellowPalette, borderwidth=0, highlightthickness=0)
optionButton.pack(side=LEFT, padx=10)


landingWindow.mainloop()