from tkinter import *
import tkinter as tk
from tkinter import messagebox
hostspath = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1 "
def limpiar():
    txtweb.delete(0,END)
    txtunlockweb.delete(0,END)


def block():

    hostspath = "C:\Windows\System32\drivers\etc\hosts"
    redirect = "127.0.0.1"
    web = txtweb.get()
    with open(hostspath,"r+") as file:
        file.writelines(redirect+" "+web+"\n")
        messagebox.showinfo(message="Succesfull Destroyed",title="Blocked")

    limpiar()

def unlock():
    hostspath = "C:\Windows\System32\drivers\etc\hosts"
    web = txtunlockweb.get()
    with open(hostspath, "r+") as file:
        content = file.readlines()
        i=0
        for elem in content:
            if web in elem:
                del content[i]
                break
            else:
                i+=1
                continue
        file.close()
        new_file = open(hostspath,"w+")
        for elem in content:
            new_file.write(elem)
        new_file.close()
    messagebox.showinfo(message=":( UNDESTROYED",title="Unblock")
    limpiar()

root = Tk()
root.title("Destroyer for me")
root.geometry("150x100")
root.configure(background="black")
txtweb = Entry(root,bg="cadetblue2")
txtweb.pack()

btnweb = Button(root, text="Destroy",command=block,bg="brown3",fg="white")
btnweb.pack()

txtunlockweb = Entry(root,bg="cadetblue3")
txtunlockweb.pack()

btnunlockweb = Button(root, text="UnDestroyed :(",command=unlock,bg="brown2",fg="white")
btnunlockweb.pack()


root.mainloop()