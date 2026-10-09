import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
def addCombo (event):
    subjList.append(ent1.get())
    cmdSubj["values"] = subjList
    ent1.focus()
    ent1.delete(0,'end')

root = tk.Tk()
root.title("Test Scrolled Text")
root.geometry("500x300+800+200")

ent1=ttk.Entry(root)
ent1.place(x=10,y=10)
ent1.focus()
ent1.bind('<Return>',addCombo)


subjList =[]
cmdSubj=ttk.Combobox(root)
cmdSubj.place(x=250,y=10)
root.mainloop()
