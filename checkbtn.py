import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def chkClicked():
    st.delete('1.0','end')
    thetext=f"{varChk1.get()} {varChk2.get()} {varChk3.get()}"
    st.insert('1.0',varChk1.get())
root = tk.Tk()
root.title("Test Scrolled Text")
root.geometry("500x300+800+200")

def rdoClicked():
    st2.delete('1.0','end')
    thetext=f"{varSize.get()} {varTop.get()}"
    st2.insert('1.0',thetext)

varChk1=tk.StringVar()

chk1=ttk.Checkbutton(root,text='หมูแดง', onvalue='ใส่หมูแดง',offvalue='',variable=varChk1,command=chkClicked)
chk1.place(x=10,y=10)
varChk1.set('ใส่หมูแดง')

varChk2=tk.StringVar()
chk2=ttk.Checkbutton(root,text='หมูกรอบ', onvalue='ใส่หมูกรอบ',offvalue='',variable=varChk2,command=chkClicked)
chk2.place(x=10,y=50)
varChk2.set('ใส่หมูกรอบ')

varChk3=tk.StringVar()
chk3=ttk.Checkbutton(root,text='กุนเชียง', onvalue='ใส่กุนเชียง',offvalue='',variable=varChk3,command=chkClicked)
chk3.place(x=10,y=90)
varChk3.set('ใส่กุนเชียง')

st=ScrolledText(root,width=20,height=5)
st.place(x=200,y=10)

varSize=tk.StringVar()
rdo1=ttk.Radiobutton(root,text='ธรรมดา',variable=varSize,value='จานธรรมดา',command=rdoClicked)
rdo1.place(x=10,y=150)

rdo2=ttk.Radiobutton(root,text='พิเศษ',variable=varSize,value='จานพิเศษ',command=rdoClicked)
rdo2.place(x=110,y=150)

varTop=tk.StringVar()
rdo3=ttk.Radiobutton(root,text='ราดน้ำ',variable=varTop,value='ไม่ต้องราดน้ำ',command=rdoClicked)
rdo3.place(x=10,y=200)

rdo4=ttk.Radiobutton(root,text='ไม่ราดน้ำ',variable=varTop,value='ราดน้ำด้วย',command=rdoClicked)
rdo4.place(x=110,y=200)

st2=ScrolledText(root,width=20,height=5)
st2.place(x=200,y=150)

root.mainloop()