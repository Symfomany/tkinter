#!/usr/bin/env python

from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Spinbox widget")
o = ttk.Combobox(root, values=["ligne 1", "ligne 2", "ligne 3", "ligne 4"])
o.pack()

li = Listbox()
li.config (width = 10, height = 5)
pos = 0   # un entier, "end" ou tkinter.END pour insérer ce mot à la fin
li.insert(pos, "première ligne")
li.insert(pos, "seconde ligne")
li.insert(pos, "troisième ligne")
li.pack()
root.mainloop()