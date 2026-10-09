import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def btn1Click():
    st.insert('end',cmbSubj.get()+'\n')
subList=['English','Calculus','Football']
root = tk.Tk()
root.title("Test Scrolled Text")
root.geometry("500x300+800+200")

cmbSubj= ttk.Combobox(root)
cmbSubj['values']=subList
cmbSubj.place(x=10,y=10)

btn1 = ttk.Button(root,text="ลงทะเบียน",command=btn1Click)
btn1.place(x=200,y=10)
st=ScrolledText(root,width=20,height=5)
st.place(x=300,y=10)

root.mainloop()
