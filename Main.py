from tkinter import *

# windows = frame/panel
# widgets = components(button,label,image)

window = Tk()
window.geometry("540x820")
window.title("Python - KIOSK")
window.config(background="#CDAE00")

iconLogo = PhotoImage(file='reso/LOGO.png')

window.iconphoto(True, iconLogo)
window.mainloop()