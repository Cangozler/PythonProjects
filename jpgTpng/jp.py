import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.title('Image Killer')

canv1 = tk.Canvas(root, width=301, height=251, bg='aquamarine4', relief='raised')
canv1.pack()

label = tk.Label(root, text='Image Killer Tool', bg='cadetblue',fg='white')
label.config(font=('helvetica', 20))
canv1.create_window(151, 61, window=label)


def getPNGFile():
    global İmage
    import_file_path = filedialog.askopenfilename()
    İmage = Image.open(import_file_path)


browseButton_PNGFile = tk.Button(text=" Import Victim ", 
command=getPNGFile, 
bg='aqua', 
fg='black',
font=('helvetica', 12, 'bold'))
canv1.create_window(151, 131, window=browseButton_PNGFile)


def convertToJPGFile():
    global İmage
    global rgb
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    rgb = İmage.convert('RGB')
    rgb.save(export_file_path)


def convertToPNGFile():
    global İmage
    global rgba
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    rgba = İmage.convert('RGBA')
    rgba.save(export_file_path)


saveAsButton_JPGFile = tk.Button(text='Kill to JPG & Save',
 command=convertToJPGFile,
 bg='aqua',
 fg='black',
 font=('helvetica', 12, 'bold'))
canv1.create_window(151, 181, window=saveAsButton_JPGFile)

saveAsButton_PNGFile = tk.Button(text='Kill to PNG & Save', 
 command=convertToPNGFile,
 bg='aqua',
 fg='black',
 font=('helvetica', 12, 'bold'))
canv1.create_window(151, 220, window=saveAsButton_PNGFile)

root.mainloop()

#⣿⣿⣿⣿⠋⢩⢹⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#⣿⣿⣿⡧⣦⠄⢧⡙⢿⣟⢁⣿⣿⣿C⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⢿
#⣿⣿⣿⣷⣶⣶⣦⡈⠂⠄⠸⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉⠰⢠⣼
#⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⢒⣂⠄⠙⢿⣿⣿⡿⠛⢛⣻⣿⣿⡟⢁⣠⣴⣶⣶
#⣿⣿⣿⣿⣿⣿⣿⠇⢇⡄⣆⣤⣀⣦⡄⢈⣉⣛⣭⡀⠙⠭⡛⠿⣿⣻⣿⣿⣿⣿
#⣿⣿⣿⣿⣿⣿⣿⠄⠄⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⣶⣷⡾⣼⣿⠈⠉⠄⠄⠈
#⣿⣿⣿⣿⣿⣿⡇⠄⠄⢿⣿⣿⣿⣥⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠄⠄⠄⠄
#⣿⣿⣿⣿⡿⠋⠄⠄⠄⢸⣿⡿⠿⠄⠈⠛⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠄⠄⠄
#⣿⣿⣿⠟⠁⠄⠄⠄⠄⠄⢠⣄⣀⡲⢦⣤⣼⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄
#⠛⠋⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣟⠻⠿⣿⣿⣿⣷⣾⣿⣿⣿⣿⢿⣿⣿⡇⠄⠄
#⠄⠄⠄a⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⣷⣶⣾⣿⣿⣿⣿⣿⣿⠟⢡⣿⣿⣿⡟⠄⠄
#⣦⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣉⣹⣿⣿⣿⣿⠟⠁⣰⣿⣿⣿⣿⡇⠄⠄
#⣿⣧⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠉⠙⠛⠉⠁⢀⣼⣿⣿⣿N⣿⡟⠄⠄⠄  
