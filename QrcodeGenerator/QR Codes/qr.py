from tkinter import *
import qrcode
import os
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
window = Tk()
window.title("QR CODE GENERATOR")
window.configure(background="#E38B17")
window.geometry('320x100')
try:
	window.wm_iconbitmap('gtss.ico')
except:
	pass
lb  = Label(window, bg="#E85D04", fg="white", text="Link or text:")
lb.grid(column=0 , row=0)
lb = Label(window,  text="")
txt = Entry(window, bg="#F48C06", fg="white",width=55)
txt.grid(column=0, row=1)

def clicked():
    img = qrcode.make(txt)
    type(img)  
    img.save("QRcodes.png")
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr = qrcode.QRCode()
qr.add_data(txt)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")


def save():
    dir_name = filedialog.askdirectory()
    os.chdir(dir_name)
    
    
    
btn = Button(window, text="Create", bg="#E85D04", fg="white",command=clicked)
btn.grid(column=0, row=6)
    
btn1 =Button(window, text ='Save', bg="#E85D04", fg="white",command = save)
btn1.grid(column=0, row=7)
window.mainloop()