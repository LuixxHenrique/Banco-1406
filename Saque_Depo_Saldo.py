from tkinter import *

root = Tk()


def voltar():
    return

def saldo():
    saldo=deposito()
    print("O seu saldo é:", saldo())

def deposito(dep):
    clear()
    montante=0.0
    dep=0.0
    dep=float(input("Quantia a ser depositada:"))
    clear()
    if (dep > 0):
        print (" |",montante)
        print ("+|",dep)
        montante=montante+dep
        print ("____________")
        print (" |",montante,"\n\n")
    else:
        print("Quantia inválida")
    voltar()
    return montante

frame = Frame(root)
frame.pack(side="top", expand=True, fill="both")
bt1 = Button(root, text='Saque', font='Arial 28')

root.mainloop()