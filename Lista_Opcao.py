import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("Banco NIX")
root.geometry('700x500')
root.minsize(width=200, height=200)
root.minsize(width=200, height=200)
root.maxsize(width=350, height=200)

# Lista
options_list = ["Contas", "Contas Abertas"]

value_inside = tkinter.StringVar(root)

value_inside.set("Selecione uma opcao")

question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
question_menu.pack()

def print_answers():
    print("Opcao selecionada: {}".format(value_inside.get()))
    return None

submit_button = tkinter.Button(root, text='Confirmar', command=print_answers)
submit_button.pack()

exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()


root.mainloop()