import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def copyAll():
    theText = st.get('1.0','end')
    st2.delete('1.0','end')
    st2.insert('1.0',theText)

def copyText():
    theText = st.selection_get()
    st2.insert('1.0',theText)
root = tk.Tk()
root.title("Test Scrolled Text")
root.geometry("300x300+100+200")

st = ScrolledText(root,widt=20, height = 5) 
st.place(x=10, y=10)

st2 = ScrolledText(root,widt=20, height = 5) 
st2.place(x=10, y=110)


btn1 = ttk.Button(root,text='copyAll',command=copyAll)
btn2 = ttk.Button(root,text='copyText',command=copyText)
btn2.place(x=200, y=50)

root.mainloop()