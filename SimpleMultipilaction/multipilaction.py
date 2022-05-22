from tkinter import *
from turtle import bgcolor

def show_table():
    
	num = int(entry.get())
	str1=' Table of ' + str(num) + '\n-----------------\n'
	for i in range(1,11):
		str1 = str1 + " " + str(num) + " x " + str(i) + " = " + str(num*i) + "\n"

	output_label.configure(text = str1, justify=LEFT)
	
root = Tk()
root.configure(background="#5F9EA0")
root.title("Multiplication Table GUI")

message_label = Label(text= ' Enter a number to \ndisplay its Table ' ,
fg='cadetblue1',
bg='cadetblue4',
font=( ' Verdana ' , 12))

output_label = Label(font=( ' Verdana ' , 12),
                    fg='white',
                    bg='cadetblue4',)

entry = Entry(font=( ' Verdana ' , 12), 
             width=6,
             fg='cadetblue1',
             bg='cadetblue4',)
calc_button = Button(
                    text= ' Show  Table ', 
                    fg='cadetblue1', 
                    bg='cadetblue4',
                    font=( ' Verdana ', 12), 
                    command=show_table)

message_label.grid(row=0, column=0,padx=10, pady=10)
entry.grid(row=0, column=1,padx=10, pady=10, ipady=10)
calc_button.grid(row=1, column=0,padx=10, pady=10)
output_label.grid(row=1, column=1, columnspan=3,padx=10, pady=10)
mainloop()