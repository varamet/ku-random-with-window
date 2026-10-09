import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
def delTopline ():
    st.delete('1.0','2.0')

def clear() :
    st.delete('1.0','end')

root = tk.Tk()
root.title("Test Scrolled Text")
root.geometry("300x300+100+200")

st = ScrolledText(root,widt=20, height = 5) 
st.place(x=10, y=10)
st.insert('1.0','Line1 col0 \n') 
st.insert('1.0','Line2 col0 \n') 
st.insert('1.0','Line3 col0 \n') 
st.insert('1.0','Line4 col0 \n') 
st.insert('1.0','Line5 col0 \n')

btn1 = ttk.Button(root,text='del1',command=delTopline)
btn1.place(x=200, y=10)
btn2 = ttk.Button(root,text='clear',command=clear)
btn2.place(x=200, y=50)

root.mainloop()