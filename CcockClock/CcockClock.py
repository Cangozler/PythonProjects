import tkinter as tk
from time import strftime

def dark_theme():
    frame = tk.Frame(root, bg="#528B8B")
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    lbl_2 = tk.Label(frame, font=('calibri', 40, 'bold'),
                     background='#528B8B', foreground='#528B8B')
    lbl_2.pack(anchor="s")

    def time():
        string = strftime('%I:%M:%S %p')
        lbl_2.config(text=string)
        lbl_2.after(1000, time)
    time()


root = tk.Tk()
root.title("Cock Time")
root.configure(background="#CDC673")
canvas = tk.Canvas(root, height=30, width=342)
canvas.pack()

frame = tk.Frame(root, bg='#68603B')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
lbl = tk.Label(frame, font=('calibri', 40, 'bold'),
                     background='#C5BD96', foreground='#34301D')
lbl.pack(anchor="s")

def time():
    string = strftime('%I:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
time()

menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
root.config(menu=menubar)
root.mainloop()