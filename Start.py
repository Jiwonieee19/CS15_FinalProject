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
    subprocess.Popen([sys.executable, "OrderType.py"])

def closeThisPy():
    # CLose the current window
    landingWindow.destroy()

yellowPalette = "#CDAE00"
redPalette = "#730C03"
whitePalette = "#FFFFFF"

landingWindow = Tk()

# Manipulating the headbar doesnt matter since we will remove this to achieve kiosk
landingWindow.title("START")
iconLogo = PhotoImage(file='reso/LOGO.png')
landingWindow.iconphoto(True, iconLogo)

# landingWindow.overrideredirect(True) # remove ang header to look more like a kiosk
landingWindow.resizable(False, False)
landingWindow.geometry("540x960+583+20") # width,height,x,y
landingWindow.config(background=yellowPalette)

# # Ads/Promo
# AdImg = Image.open('reso/1stAd.png')
# reAdImg = AdImg.resize((486,738))
# FinalAdImg = ImageTk.PhotoImage(reAdImg)
# adLabel = Label(landingWindow, image=FinalAdImg, bg=yellowPalette)
# adLabel.place(relx=0.06, rely=0.02, anchor='nw')



# Ads/Promo
ads = ['reso/1stAd.png', 'reso/2ndAd.png', 'reso/3rdAd.png']

# Preload the images ONCE
preloaded_ads = []
for a in ads:
    img = Image.open(a).resize((486, 738))
    preloaded_ads.append(ImageTk.PhotoImage(img))

ad_index = 0

adLabel = Label(landingWindow, bg=yellowPalette)
adLabel.place(relx=0.06, rely=0.02, anchor='nw')

def rotate_ad():
    global ad_index
    adLabel.config(image=preloaded_ads[ad_index])
    ad_index = (ad_index + 1) % len(preloaded_ads)
    landingWindow.after(2500, rotate_ad)

rotate_ad()



# Real Logo top left
img = Image.open('reso/realLogo.png')
reImg = img.resize((120,108))
landingLogo = ImageTk.PhotoImage(reImg)
logoLabel = Label(landingWindow, image=landingLogo, bg=yellowPalette)
logoLabel.place(relx=0.02, rely=0, anchor='nw')

text_photo = usingOurFontWithHeight('TOP TO START', 492, 141, 50, whitePalette, 90, 30)
# Create label with the text image
startButton = Button(landingWindow, image=text_photo, bg=redPalette, borderwidth=0, highlightthickness=0, command=nextPage)
startButton.place(relx=0.5, rely=0.895, anchor='center')

landingWindow.mainloop()