from tkinter import *
import os
from pymysql import *
from tkinter import messagebox as msg


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Registro")
    register_screen.geometry("600x450")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Por favor digite o que se pede", bg="red").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Nome de Usuario * ")

    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    contactnumber_lable = Label(register_screen, text="Numero de Contato * ")
    contactnumber_lable.pack()
    contactnumber_entry = Entry(register_screen)
    contactnumber_entry.pack()
    mothername_lable = Label(register_screen, text="Nome da Mae * ")
    mothername_lable.pack()
    mothername_entry = Entry(register_screen)
    mothername_entry.pack()
    dateofbirth_lable = Label(register_screen, text="Data de Nascimento(YYYY-MM-DD ) * ")
    dateofbirth_lable.pack()
    dateofbirth_entry = Entry(register_screen)
    dateofbirth_entry.pack()
    CPF_lable = Label(register_screen, text="CPF * ")
    CPF_lable.pack()
    CPF_entry = Entry(register_screen)
    CPF_entry.pack()


    password_lable = Label(register_screen, text="Senha * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Registro", width=10, height=1, bg="red", command=register_user).pack()

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("700x250")
    Label(login_screen, text="Por favor digite o que se pede para logar").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Nome de Usuario * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Senha * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(register_screen, text="Registrado com Sucesso!", fg="green", font=("calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Sucesso")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Logado com Sucesso").pack()
    Button(login_success_screen, text="OK", command=menu).pack()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Sucesso")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Senha Invalida ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Sucesso")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="Usuario nao Encontrado").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def deposit():
    global n1
    global a1
    global if1
    global am1
    global deposit_screen
    deposit_screen = Toplevel(main_screen)
    deposit_screen.title("Deposito")
    deposit_screen.geometry("700x250")
    Label(deposit_screen, text="Por favor digite o que se pede para logar").pack()
    Label(deposit_screen, text="").pack()

    name_lable = Label(deposit_screen, text="nome * ")
    name_lable.pack()
    n1 = Entry(deposit_screen)
    n1.pack()

    account_lable = Label(deposit_screen, text="Numero da Conta * ")
    account_lable.pack()
    a1 = Entry(deposit_screen)
    a1.pack()

    amount_lable = Label(deposit_screen, text="Quantia * ")
    amount_lable.pack()
    am1 = Entry(deposit_screen)
    am1.pack()

    Label(deposit_screen, text="").pack()
    Button(deposit_screen, text="Deposito", width=10, height=1, bg="red", command=save).pack()
    Label(deposit_screen, text="").pack()
    Button(deposit_screen, text="Inicio", height="2", width="10", fg='black', bg='orange', command=main_menu).pack()
    Label(deposit_screen, text="").pack(side='left')


def main_menu():
    deposit_screen.destroy()


def save():
    con = connect(db='so', user='root', passwd='system', host='localhost')
    cur = con.cursor()

    nome = n1.get()
    conta = int(a1.get())
    quantia = int(am1.get())
    i = cur.execute("insert into emp3 values(%s,'%d',%d, %d)" % (nome, conta, quantia))
    if i >= 1:
        con.commit()
        msg.showinfo('Informacao', 'Informacao Salva')
        a1.delete(0, 'end')
        n1.delete(0, 'end')
        am1.delete(0, 'end')

    con.close()


def withdraw():
    global withdraw_screen
    withdraw_screen = Toplevel(main_screen)
    withdraw_screen.title("Saque")
    withdraw_screen.geometry("700x250")
    Label(withdraw_screen, text="Por favor digite o que se pede para logar").pack()
    Label(withdraw_screen, text="").pack()

    name_lable = Label(withdraw_screen, text="nome * ")
    name_lable.pack()
    n1 = Entry(withdraw_screen)
    n1.pack()

    account_lable = Label(withdraw_screen, text="Numero da Conta * ")
    account_lable.pack()
    a1 = Entry(withdraw_screen)
    a1.pack()

    amount_lable = Label(withdraw_screen, text="Quantia * ")
    amount_lable.pack()
    am1 = Entry(withdraw_screen)
    am1.pack()
    Label(withdraw_screen, text="").pack()
    Button(withdraw_screen, text="Sacar", width=10, height=1, bg="red", command=save).pack()
    Label(withdraw_screen, text="").pack()
    Button(withdraw_screen, text="Inicio", height="2", width="10", fg='black', bg='orange', command=main_menu1).pack()
    Label(withdraw_screen, text="").pack(side='left')


def main_menu1():
    withdraw_screen.destroy()


def menu():
    global menu_screen
    menu_screen = Toplevel(main_screen)
    menu_screen.title("menu")
    menu_screen.geometry("700x250")
    Label(menu_screen, text="Selecione O Que Deseja", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Deposito", height="2", width="30", fg='black', bg='violet', command=deposit).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Saque", height="2", width="30", fg='black', bg='orange', command=withdraw).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Balanco", height="2", width="30", fg='black', bg='orange', command=balance).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Transferencia", height="2", width="30", fg='black', bg='orange').pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="logout", height="2", width="10", fg='black', bg='orange', command=logout2).pack()
    Label(menu_screen, text="").pack(side='left')


def logout2():
    menu_screen.destroy()


def balance():
    global balance_screen
    balance_screen = Toplevel(main_screen)
    balance_screen.title("balanco")
    withdraw_screen.geometry("300x250")
    Label(withdraw_screen, text="Por favor digite o que se pede para logar").pack()
    Label(withdraw_screen, text="").pack()


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("700x250")
    main_screen.title("Conta Login")
    Label(text="Oque deseja realizar?", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="5", width="50", fg='black', bg='green', font=("Arial Bold", 10), command=login).pack()
    Label(text="").pack()
    Button(text="Registro", height="5", width="50", fg='black', bg='#3366ff', font=("Arial Bold", 10),
           command=register).pack()
    Label(text="").pack()
    Button(text="Deposito", height="5", width="50", fg='black', bg='violet', font=("Arial Bold", 10),
           command=deposit).pack()
    Label(text="").pack()
    Button(text="Sacar", height="5", width="50", fg='black', bg='orange', font=("Arial Bold", 10),
           command=withdraw).pack()
    Label(text="").pack()

    main_screen.mainloop()


main_account_screen()