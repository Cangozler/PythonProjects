from tkinter import *
from tkinter import filedialog
import tkinter
from pytube import YouTube
from tkinter import filedialog
import os
from PIL import ImageTk, Image  
#Youtube downloader#
def explore_files():
	files = [('video_files', '*.mp4*'), ]
	file = filedialog.asksaveasfilename(filetypes=files, defaultextension=files)
	download(file)

def download(path):

	url = entry.get()
	youtube = YouTube(url)
	stream = youtube.streams.first()
	stream.download(path)

def main():
	global entry
	root = Tk()
	root.geometry('500x200')
	root.resizable(False, False)
	root.title('Can gözler Youtube Dowloader')
	root.configure(background="green")
	frame = Frame(root, bg='gray')
	
	label = Label(frame,
		text='Link gir/URL: ',
		font=('Times', 20, 'underline'),
        bg="gray"
	)

	entry = Entry(frame,
		width=34,
		font=('Times', 20),
		bd=3,
		fg='blue'
	)

	exitButton = Button(frame,
		text='cık/exit',
		width=12, 
		bd=3,
		fg='white',
		bg='red',
		font=('Times', 15, 'bold'),
		command=root.quit
	)

	downloadButton = Button(frame,
		text='İndir/Download',
		width=12, 
		bd=3,
		fg='white',
		bg='LightGreen',
		font=('Times', 15, 'bold'),
		command=explore_files
	)

	frame.pack(padx=10)


	label.grid(row=0, column=0, pady=2)
	entry.grid(row=1, column=0, columnspan=2, pady=20)
	exitButton.grid(row=2, column=0, pady=2)
	downloadButton.grid(row=2,column=1)

	
	root.mainloop()	

main()
