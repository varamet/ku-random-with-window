import tkinter as tk
from tkinter import ttk,messagebox,Label
from tkinter.scrolledtext import ScrolledText

# Function Insert ScrollText
def orderFood ():
    stFood.insert('1.0',cmbfood.get()+'\n')

# Function Clear ScrollText
def clearOrder():
    stFood.delete('1.0','end')


# Function แสดงรายละเอียดและการจ่ายเงิน
def changeItem ():
    stItem.delete('1.0','end')
    thetext=f"{varW.get()} {varB.get()} {varS.get()} \n {varPay.get()}"
    stItem.insert('1.0',thetext)

# Main Program
root = tk.Tk()
root.title("Food Order")
root.geometry('600x400+200+100')

# สร้าง ComboBox
foodlist=['ข้าวขาหมู','ข้าวหมูแดง','ข้าวมันไก่']
cmbfood= ttk.Combobox(root)
cmbfood['values']=foodlist
cmbfood.place(x=10,y=10)

# สร้างปุ่มบันทึกรายการอาหาร
btn_order =ttk.Button(root,text="บันทึกรายการ",command=orderFood)
btn_order.place(x=180,y=10)

# สร้างปุ่มล้างรายการอาหาร
btn_clear =ttk.Button(root,text="ล้างรายการ",command=clearOrder)
btn_clear.place(x=180,y=60)


# สร้าง ScrolledText รายการอาหาร
stFood=ScrolledText(root,width=30,height=10)
stFood.place(x=300,y=10)

# สร้าง Checkbox รายละเอียด
varW=tk.StringVar()
ckw=ttk.Checkbutton(root,text="อุ่น",variable=varW,onvalue='อุุ่น',offvalue='',command=changeItem)
ckw.place(x=10,y=210)

varB=tk.StringVar()
ckw=ttk.Checkbutton(root,text="ใส่ถุง",variable=varB,onvalue='ใส่ถุง',offvalue='',command=changeItem)
ckw.place(x=60,y=210)

varS=tk.StringVar()
ckw=ttk.Checkbutton(root,text="ช้อนส้อม",variable=varS,onvalue='ช้อนส้อม',offvalue='',command=changeItem)
ckw.place(x=110,y=210)


# สร้าง Radio การจ่ายเงิน
varPay=tk.StringVar()
rdC=ttk.Radiobutton(root,text="จ่ายเงินสด",variable=varPay,value="เงินสด")
rdC.place(x=10,y=250)
rdT=ttk.Radiobutton(root,text="จ่ายเงินโอน",variable=varPay,value="จ่ายเงินโอน")
rdT.place(x=110,y=250)

# สร้าง ScrolledText รายละเอียด
stItem=ScrolledText(root,width=30,height=5)
stItem.place(x=300,y=210)

tk.mainloop()
