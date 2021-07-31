import tkinter as tk
from PIL import Image,ImageTk
import random

dice=[r"C:/Users/filoz/Desktop/CKB_bot/roll/Images/D1.png",
r"C:/Users/filoz/Desktop/CKB_bot/roll/Images/D2.png",
r"C:/Users/filoz/Desktop/CKB_bot/roll/Images/D3.png",
r"C:/Users/filoz/Desktop/CKB_bot/roll/Images/D4.png",
r"C:/Users/filoz/Desktop/CKB_bot/roll/Images/D5.png",
r"C:/Users/filoz/Desktop/CKB_bot/roll/Images/D6.png"]

root=tk.Tk()
root.title("Dickroll")
root.geometry("200x200")
root.configure(background='ghostwhite')

img = ImageTk.PhotoImage(Image.open(random.choice(dice)))
imgLab=tk.Label(root,image=img)
imgLab.image=img
imgLab.pack()

def roll():
    img = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    imgLab.configure(image=img)
    imgLab.image = img

button = tk.Button(root, text='Roll u crazy bitch', bg='red3',fg='white', command=roll)
button.pack()

root.mainloop()

#⣿⣿⣿⣿⠋⢩⢹⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#⣿⣿⣿⡧⣦⠄⢧⡙⢿⣟⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⢿
#⣿⣿⣿⣷⣶⣶⣦⡈⠂⠄⠸⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉⠰⢠⣼
#⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⢒⣂⠄⠙⢿⣿⣿⡿⠛⢛⣻⣿⣿⡟⢁⣠⣴⣶⣶
#⣿⣿⣿⣿⣿⣿⣿⠇⢇⡄⣆⣤⣀⣦⡄⢈⣉⣛⣭⡀⠙⠭⡛⠿⣿⣻⣿⣿⣿⣿
#⣿⣿⣿⣿⣿⣿⣿⠄⠄⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⣶⣷⡾⣼⣿⠈⠉⠄⠄⠈
#⣿⣿⣿⣿⣿⣿⡇⠄⠄⢿⣿⣿⣿⣥⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠄⠄⠄⠄
#⣿⣿⣿⣿⡿⠋⠄⠄⠄⢸⣿⡿⠿⠄⠈⠛⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠄⠄⠄
#⣿⣿⣿⠟⠁⠄⠄⠄⠄⠄⢠⣄⣀⡲⢦⣤⣼⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄
#⠛⠋⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣟⠻⠿⣿⣿⣿⣷⣾⣿⣿⣿⣿⢿⣿⣿⡇⠄⠄
#⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⣷⣶⣾⣿⣿⣿⣿⣿⣿⠟⢡⣿⣿⣿⡟⠄⠄
#⣦⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣉⣹⣿⣿⣿⣿⠟⠁⣰⣿⣿⣿⣿⡇⠄⠄
#⣿⣧⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠉⠙⠛⠉⠁⢀⣼⣿⣿⣿⣿⡟⠄⠄⠄  
