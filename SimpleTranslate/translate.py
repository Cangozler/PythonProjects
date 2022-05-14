from cProfile import label
from tkinter import *
from turtle import left
import googletrans
from matplotlib.pyplot import grid
import textblob
from tkinter import ttk, messagebox



root = Tk()
root.title('Simple Trans')
root.geometry("700x300")
root.configure(background="#CDC673")

def translate_it():
	translated_text.delete(1.0, END)
	try:
		for key, value in languages.items():
			if (value == original_combo.get()):
				from_language_key = key
		for key, value in languages.items():
			if (value == translated_combo.get()):
				to_language_key = key

		words = textblob.TextBlob(original_text.get(1.0, END))
		words = words.translate(from_lang=from_language_key , to=to_language_key)
		translated_text.insert(10.0, words)
	except Exception as e:
		messagebox.showerror("Translator", e)
def clear():
	original_text.delete(1.0, END)
	translated_text.delete(1.0, END)

languages = googletrans.LANGUAGES
language_list = list(languages.values())

original_text = Text(root, height=10, width=20)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="I can translate!", font=("Helvetica", 12), command=translate_it)
translate_button.grid(row=1, column=1, padx=1)

translated_text = Text(root, height=10, width=20)
translated_text.grid(row=0, column=2, pady=0, padx=1)


translated_combo = ttk.Combobox(root, width=8, value=language_list)
translated_combo.current(20)
translated_combo.grid(row=0, pady=0, padx=0, ipadx=100, sticky=(W,N), column=2)

original_combo = ttk.Combobox(root, width=8, value=language_list)
original_combo.current(21)
original_combo.grid(row=0, pady=0, padx=0, ipadx=100, sticky=(W,N), column=0)


clear_button = Button(root, text="I can Clear", command=clear)
clear_button.grid(row=5, sticky=(S), pady=20, column=1)
root.mainloop()