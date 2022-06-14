from tkinter import *

root = Tk()

root.geometry('400x200+100+500')
root.minsize(width=680, height=400)
root.minsize(width=680, height=400)
root.maxsize(width=680, height=400)

# Tamanhos dos botões(Button)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# widgets
label1 = Label(root, font='Arial 28')
bt1 = Button(root, text='Saque', font='Arial 28')
bt2 = Button(root, text='Deposito', font='Arial 28')
bt3 = Button(root, text='Transferencia', font='Arial 28')
bt4 = Button(root, text='Extrato', font='Arial 28')

# layout
bt1.grid(row=1, column=0)
bt2.grid(row=1, column=1)
bt3.grid(row=1, column=2)
bt4.grid(row=1, column=3)
label1.grid(row=0, column=1)

root.mainloop()
