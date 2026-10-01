import random
secret = random.randint(1,10)
round = 0
import tkinter as tk
from tkinter import messagebox, ttk
def btn_clicked(num):
    global round
    round +=1
    entry_var.set(str(num))
    if num > secret:
        messagebox.showwarning("มากไป", f"{round} มากไป")
    elif num < secret:
        messagebox.showwarning("น้อยไป", f"{round} น้อยไป")
    else:
        messagebox.showinfo("ถูกต้อง", f"คำตอบคือ {secret} คุณทายไป {round} รอบ")
root = tk.Tk()
root.title("Entry")
root.geometry("400x350")
entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var, font=("Arial", 14))
entry.place(x=10, y=10, width=380, height=30)
btn1 = ttk.Button(root, text='1', command=lambda: btn_clicked(1)).place(x=10, y=60, width=90, height=40)
btn2 = ttk.Button(root, text='2', command=lambda: btn_clicked(2)).place(x=110, y=60, width=90, height=40)
btn3 = ttk.Button(root, text='3', command=lambda: btn_clicked(3)).place(x=210, y=60, width=90, height=40)
btn4 = ttk.Button(root, text='4', command=lambda: btn_clicked(4)).place(x=10, y=110, width=90, height=40)
btn5 = ttk.Button(root, text='5', command=lambda: btn_clicked(5)).place(x=110, y=110, width=90, height=40)
btn6 = ttk.Button(root, text='6', command=lambda: btn_clicked(6)).place(x=210, y=110, width=90, height=40)
btn7 = ttk.Button(root, text='7', command=lambda: btn_clicked(7)).place(x=10, y=160, width=90, height=40)
btn8 = ttk.Button(root, text='8', command=lambda: btn_clicked(8)).place(x=110, y=160, width=90, height=40)
btn9 = ttk.Button(root, text='9', command=lambda: btn_clicked(9)).place(x=210, y=160, width=90, height=40)
btn0 = ttk.Button(root, text='0', command=lambda: btn_clicked(0)).place(x=110, y=210, width=90, height=40)
root.mainloop()