from tkinter import *
import tkinter as tk
from tkcalendar import *
import random

#>>>>definindo algumas classes

clientes = []

def cadastrar():
    global nome, cpf, dataNasc
    clientes.append()

#formatar cpf

def format_cpf(event=None):
    text = ent2.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [2, 5]:
            new_text += text[index] + "."
        elif index == 8:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    ent2.delete(0, "end")
    ent2.insert(0, new_text)

def format_cpfF(event=None):
    text = cpf.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [2, 5]:
            new_text += text[index] + "."
        elif index == 8:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    cpf.delete(0, "end")
    cpf.insert(0, new_text)

#formatar data

def format_data(event=None):
    text = ent2.get().replace("/", "")[:8]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [1, 3]:
            new_text += text[index] + "/"
        else:
            new_text += text[index]

    ent2.delete(0, "end")
    ent2.insert(0, new_text)

#comandos indispensaveis

def home1():
    f2.forget()
    f1.forget()
    f3.forget()
    f4.forget()
    f5.forget()
    f6.forget()
    f7.forget()
    f8.forget()
    f9.forget()
    fc.forget()
    f0.pack()

def abrir():
    f0.forget()
    fc.pack()
    pabelp.pack()
    btp.place(width=296, height=48, x=136, y=275)
    btb.place(width=248, height=69, x=152, y=392)
    btv.place(width=282, height=71, x=145, y=512)
    bb1.place(width=26, height=20, x=854, y=5)

def login():
    f0.forget()
    f1.pack()
    labelv.pack()
    btlo.place(width=152, height=52, x=474, y=536)
    bth.place(width=312, height=101, x=358, y=202)
    btt.place(width=332, height=69, x=443, y=500)
    ent1.place(width=621, height=36, x=170, y=297)
    ent2.place(width=421, height=38, x=144, y=365)
    ent3.place(width=176, height=27, x=273, y=430)
    bb1.place(width=26, height=20, x=854, y=5)

def entrar():
    f1.forget()
    f2.pack()
    label1.pack()
    btd.place(width=224, height=70, x=52, y=235)
    bts.place(width=220, height=68, x=164, y=519)
    labelpp.place(width=186, height=34, x=412, y=709)
    labelpb.place(width=157, height=27, x=855, y=233)
    bb2.place(width=26, height=20, x=854, y=5)

def deposito():
    f2.forget()
    f3.pack()
    label2.pack()
    btdc.place(width=300, height=40, x=400, y=592)
    val.place(width=137, height=36, x=484, y=288)
    bb3.place(width=26, height=20, x=854, y=5)

def saque():
    f2.forget()
    f4.pack()
    label3.pack()
    btds.place(width=243, height=40, x=743, y=297)
    valp.place(width=194, height=33, x=426, y=291)
    bb4.place(width=26, height=20, x=854, y=5)

def trans():
    f2.forget()
    f5.pack()
    label4.pack()
    btdt.place(width=165, height=73, x=394, y=614)
    vao.place(width=142, height=32, x=512, y=284)
    vae.place(width=137, height=26, x=482, y=416)
    bb5.place(width=26, height=20, x=854, y=5)

def histo():
    f2.forget()
    f6.pack()
    label5.pack()
    lus.place(width=489, height=547, x=32, y=126)
    lib.place(width=355, height=225, x=606, y=228)
    bb6.place(width=26, height=20, x=854, y=5)

def cad():
    fc.forget()
    f7.pack()
    label6.pack()
    btnc.place(width=267, height=48, x=432, y=623)
    nome.place(width=604, height=31, x=178, y=358)
    cpf.place(width=402, height=29, x=152, y=425)
    dat.place(width=165, height=19, x=396, y=495)
    bb7.place(width=26, height=20, x=854, y=5)

def ver():
    fc.forget()
    f8.pack()
    label7.pack()
    opt.place(width=83, height=20, x=537, y=244)
    optp.place(width=88, height=28, x=326, y=407)
    bb8.place(width=26, height=20, x=854, y=5)

def conf():
    fc.forget()
    f9.pack()
    label8.pack()
    bb9.place(width=26, height=20, x=854, y=5)

#criação da janela
root=Tk()
root.title('NIX')
root.geometry('400x200+100+500')
root.minsize(width=1023, height=755)
root.maxsize(width=1023, height=755)
root.config(bg=('white'))

#criação dos frames
f0=Frame(root, bg='Black', border=0)
f1=Frame(root, bg='black', border=0)
f2=Frame(root, bg='Black', border=0)
f2=Frame(root, bg='Black', border=0)
f3=Frame(root, bg='Black', border=0)
f4=Frame(root, bg='Black', border=0)
f5=Frame(root, bg='Black', border=0)
f6=Frame(root, bg='Black', border=0)
f7=Frame(root, bg='black', border=0)
f8=Frame(root, bg='Black', border=0)
f9=Frame(root, bg='Black', border=0)
fc=Frame(root, bg='Black', border=0)

#criação dos itens f0 (inicio)

imagep = PhotoImage(file=r"C:\Users\887753\Desktop\Imagens NIX\1.png")
#imagep = PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\1.png")
label=Label(f0, image=imagep)
btn=Button(f0, text='Login Cliente',font='Arial 20', bg='#350252', foreground='White', command=login)
btn2=Button(f0, text='Login Funcionário', font='Arial 28', bg='#350252', foreground='White',command=abrir)

#criação dos itens labell

imagepx = PhotoImage(file=r"C:\Users\887753\Desktop\Imagens NIX\2.png")
#imagepx = PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\2.png")
pabelp=Label(fc, image=imagepx)
btp=Button(fc, text='Verificação', font='Arial 24', bg='#a6033f', foreground='White', command=ver)
btb=Button(fc, text='Criar uma conta', font='Arial 24', bg='#a6033f', foreground='White', command=cad)
btv=Button(fc, text='Configurar Contas', font='Arial 24', bg='#a6033f', foreground='White', command=conf)
bb=Button(fc, text='<', font='Arial 20', bg='#60078c', foreground='White', command=home1)

#criação dos itens f1

imagepp= PhotoImage(file=r"C:\Users\887753\Desktop\Imagens NIX\7.png")
#imagepp= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\7.png")
labelv=Label(f1, image=imagepp)
btlo=Button(f1, text='Entrar', font='Arial 24', bg='#5012c4', foreground='White', command=entrar)
ent1=Entry(f1, font='Arial 22', bg='#5012c4',foreground='White')
ent2=Entry(f1, font='Arial 22', bg='#5012c4', foreground='White')
ent2.bind('<KeyRelease>', format_cpf)
ent3=Entry(f1, font='Arial 22', bg='#5012c4', foreground='White')
bb1=Button(f1, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)

#Criação dos itens f2

imagex= PhotoImage(file=r"C:\Users\887753\Desktop\Imagens NIX\8.png")
#imagex= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\8.png")
label1=Label(f2, image=imagex)
btd=Button(f2, text='Fazer Depósito', font='Arial 24', bg='#d020f7', foreground='White',command=deposito)
bts=Button(f2, text='Fazer um Saque', font='Arial 22', bg='#d020f7', foreground='White', command=saque)
bth=Button(f2, text='Ver Historico\nde\nTransações', font='Arial 24', bg='#d020f7', foreground='White', command=histo)
btt=Button(f2, text='Fazer uma Transferência', font='Arial 22', bg='#d020f7', foreground='White', command=trans)
labelpp=Label(f2, font='Arial 20', bg='#5012c4', foreground='White')
labelpb=Label(f2, font='Arial 20', bg='#5012c4', foreground='White')
bb2=Button(f2, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)


#criação dos itens f3

images= PhotoImage(file=r"C:\Users\887753\Desktop\Imagens NIX\9.png")
#images= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\9.png")
label2=Label(f3, image=images)
val=Entry(f3, font='Arial 16', bg='#f507bd', foreground='White')
btdc=Button(f3, text='Realizar Depósito', font='Arial 22', bg='#ab0eb0', foreground='White')
bb3=Button(f3, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)

#criação dos itens f4

imaged= PhotoImage(file=r"C:\Users\887753\Desktop\Imagens NIX\10.png")
#imaged= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\10.png")
label3=Label(f4, image=imaged)
valp=Entry(f4, font='Arial 16',bg='#f507bd', foreground='White')
btds=Button(f4, text='Realizar Saque', font='Arial 22', bg='#ab0eb0', foreground='White')
bb4=Button(f4, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)

#Criação dos itens f5

imaget= PhotoImage(file=r"C:\Users\887753\Desktop\Imagens NIX\11.png")
#imaget= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\11.png")
label4=Label(f5, image=imaget)
vao=Entry(f5, font='Arial 16',bg='#f507bd', foreground='White')
vae=Entry(f5, font='Arial 16',bg='#f507bd', foreground='White')
btdt=Button(f5, text='Realizar\nTransação', font='Arial 20', bg='#ab0eb0', foreground='White')
bb5=Button(f5, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)

#Criação dos itens f6

imageh= PhotoImage(file=r"C:\Users\887753\Desktop\Imagens NIX\12.png")
#imageh= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\12.png")
label5=Label(f6, image=imageh)
lus=Label(f6, font='Arial 10', background='#561fed')
lib=Entry(f6, font='Arial 10', bg='#561fed')
bb6=Button(f6, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)

#Criação dos itens f7

imagec= PhotoImage(file=r"C:\Users\887753\Desktop\Imagens NIX\nix.png")
#imagec= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\nix.png")
label6=Label(f7, image=imagec)
btnc=Button(f7, text='Criar Conta', font='Arial 20', bg='#ab0eb0', foreground='White')
nome=Entry(f7, font='Arial 20',background='#561fed', foreground='White')
cpf=Entry(f7, font='Arial 20',background='#561fed', foreground='White')
cpf.bind('<KeyRelease>', format_cpfF)
dat=Label(f7, font='Arial 15', background='#561fed', foreground='White')
bb7=Button(f7, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)

#Criação dos itens f8

imagev= PhotoImage(file=r"C:\Users\887753\Desktop\Imagens NIX\4.png")
#imagev= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\4.png")
label7=Label(f8, image=imagev)
list=['0']
olist=['0']
variable = tk.StringVar(f8)
variable.set(list[0])

opt = tk.OptionMenu(f8, variable, *list)
opt.config(text='Gênero', font=('Arial 10'), background='#450be9')

variablep = tk.StringVar(f8)
variablep.set(olist[0])

optp = tk.OptionMenu(f8, variablep, *olist)
optp.config(text='Gênero', font=('Arial 10'), background='#450be3')
bb8=Button(f8, text='<', font='Arial 20', bg='#a6033f', foreground='White',command=home1)

#Criação dos itens f9

imager= PhotoImage(file=r"C:\Users\887753\Desktop\Imagens NIX\5.png")
#imager= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\5.png")
label8=Label(f9, image=imager)
bb9=Button(f9, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)




#verificar os pixels

#data

def Dater():
    global cal
    def getDate():
        date=cal.get_date()
        print(date)
    cal.place(width=267, height=204, x=580, y=407)
    bubub=Button(f7,text='Confirmar Seleção', bg='purple', command=getDate).place(width=168, height=24, x=393, y=491)
cal=Calendar(f7, selectmode='day', date_pattern="dd-mm-y")
bubu=Button(f7, text='Selecione uma Data', command=Dater).place(width=168, height=24, x=393, y=491)
print(Dater())

# Posicionamento

class Poc:
    # Variáveis Globais
    x1 = y1 = 0  # Armazenam a posição inicial de x e y

print('''Botão Esquerdo: 'place' <Clique na posição inicial e arraste até a posição final>
Botão Scroll:   'geometry' <Mostra as medidas para o posicionamento da janela> "geometry"
''')


def inicio_place(arg):
    global x1, y1
    x1 = arg.x
    y1 = arg.y


def fim_place(arg, master):
    global x1, y1
    print(f'Copiado! .place(width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1})')
    master.clipboard_clear()
    master.clipboard_append(f'.place(width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1})')


def para_geometry(master):
    print(f'Copiado! .geometry("{master.geometry()}")')
    master.clipboard_clear()
    master.clipboard_append(f'.geometry("{master.geometry()}")')

#rodando

#======================================================= Check ======================================================

class pessoa:

    def __init__(self, nome, cpf, nascimento):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento

    def dados(self):
        print("\nNome:", self.nome)
        print("CPF:", self.cpf)
        print("Nascimento:", self.nascimento)

# conta
# classe herdada

class conta(pessoa):
    contas = 0

    def __init__(self, nome, cpf, nascimento, numero=0, saldo=0, senha=0,history=[]):
        super().__init__(nome, cpf, nascimento)

        self.numero = numero
        self.saldo = float(saldo)
        self.history = history
        self.history = []
        conta.addconta()
        self.numero = conta.contas
        self.senha = random.randrange(1, 1000)

    def extrato(self):
        print("\nTitular:", self.nome)
        print("Numero:", self.numero)
        print("Senha:", self.senha)
        print("Saldo:", self.saldo)

    def deposito(self, valor):
        self.saldo += valor
        self.history.append("Deposito De {}".format(valor))

    def saque(self, valor):
        self.saldo -= valor
        self.history.append("Saque De {}".format(valor))

    def transferencia(self, quantia, titular):
        self.saldo -= quantia
        cria.lista[titular-1].saldo += quantia
        self.history.append("Transferencia de {} Para a Conta {}".format(quantia,titular))
        cria.lista[titular-1].history.append("Trasferencia de {} por {} ".format(quantia,self.numero))

    def historico(self):
        for contagem in range(len(self.history)):
            print("|- {}".format(self.history[contagem]))

    # add valor +1 pra contagem de total de contas (numero de identificação)
    @classmethod
    def addconta(cls):
        cls.contas += 1


#classe menu
#big classe

class cria:

    #contagem big importante
    #armazena todos os objetoss
    lista = []
    contagem = 0

    # menu

    @classmethod
    def menu(cls):
        while True:
            try:
                print("\n------------------------------------------------------------------------------------")
                print("\n 1 - Criar Cadastro")
                print(" 2 - Acessar Conta")
                print(" 3 - Finalizar Programa")

                inpute = input("\n   ==   ")

                if inpute == "1":
                    cria.criacao()
                elif inpute == "2":
                    cria.login()
                elif inpute == "3":
                    print("\n------------------------------------------------------------------------------------")
                    break
                else:
                    print("\n Input Invalido --")
                    continue
            except:
                print("\n Input Invalido --")
                continue

    # criacao

    @classmethod
    def criacao(cls):

        print("\n------------------------------------------------------------------------------------")

        # Nome
        print("\n Nome __")
        name = str(input("\n   ==   "))
        print("\n //////////////////////////////////////////////////////")

        # CPF
        print("\n CPF __")
        while True:
            while True:
                try:
                    cpf = int(input("\n   ==   "))
                    cpf = str(cpf)
                    break
                except:
                    print("\n Somente Numeros--")
                    continue
            if len(cpf) == 11:
                cpf = ("{}.{}.{}-{}".format(cpf[0:3],cpf[3:6],cpf[6:9],cpf[9:11]))
                break
            else:
                print("\n Cpf Invalido --")
        print("\n //////////////////////////////////////////////////////")

        # Nascimento
        print("\n Nascimento __")
        while True:
            try:
                while True:
                    print("\nDia : ")
                    dia = int(input("\n   ==   "))
                    if dia in range(1, 31):
                        break
                    else:
                        print("\n Dia Invalido")
                while True:
                    print("\nMes : ")
                    mes = int(input("\n   ==   "))
                    if mes in range(1, 13):
                        break
                    else:
                        print("\n Mes Invalido")
                print("\nAno : ")
                ano = int(input("\n   ==   "))
                nascimento = ("{}/{}/{}".format(dia, mes, ano))
                break
            except:
                print("\n Sommente Numeros-- \n Repita Tudo --")

                continue

        cria.create(name,cpf,nascimento)
        cria.acesso(cria.contagem-1)

    # login

    @classmethod
    def login(cls):
        while True:
            print("\n------------------------------------------------------------------------------------")
            print("\nNumero de usuario :")
            while True:
                try:
                    numero = int(input("\n   ==   "))
                    break
                except:
                    print("\n Somente Numeros -- ")
                    continue
            print("\n //////////////////////////////////////////////////////")
            print("\nSenha :")
            while True:
                try:
                    senha = int(input("\n   ==   "))
                    break
                except:
                    print("\n Somente Numeros --")
            try:
                if senha == cria.lista[numero-1].senha:
                    cria.acesso(numero-1)
                    break
            except:
                pass
            print("\nSenha/Usuario Incorreto/Inexistente --")
            break

    # acesso

    @classmethod
    def acesso(cls,id):

        print("\n------------------------------------------------------------------------------------")

        while True:
            print("\n 1 - Dados ")
            print(" 2 - Extrato ")
            print(" 3 - Deposito ")
            print(" 4 - Saque ")
            print(" 5 - Transferençia ")
            print(" 6 - Historico ")
            print(" 7 - Deslogar ")
            while True:
                try:
                    inpute = int(input("\n    ==    "))
                    break
                except:
                    print("\n Somente Numeros -- ")
                    continue
            if inpute == 1:
                cria.dado(id)
            elif inpute == 2:
                cria.extrat(id)
            elif inpute == 3:
                cria.deposit(id)
            elif inpute == 4:
                cria.saq(id)
            elif inpute == 5:
                cria.transfe(id)
            elif inpute == 6:
                cria.histor(id)
            elif inpute == 7:
                break
            else:
                print("\n Numero Invalido --")
                continue

    # dados

    @classmethod
    def dado(cls,id):
                print("\n //////////////////////////////////////////////////////")
                cria.lista[id].dados()
                print("\n //////////////////////////////////////////////////////")

    # extrato

    @classmethod
    def extrat(cls,id):
                print("\n//////////////////////////////////////////////////////")
                cria.lista[id].extrato()
                print("\n //////////////////////////////////////////////////////")

    # deposito

    @classmethod
    def deposit(cls,id):
            print("\n //////////////////////////////////////////////////////")
            while True:
                try:
                    print("\n Quantia : ")
                    quantia = float(input("\n    ==    "))
                    if quantia <= 0:
                        print("\n Input Invalido --")
                        continue
                    else:
                        cria.lista[id].deposito(quantia)
                        print("\n //////////////////////////////////////////////////////")
                        break
                except:
                    print("\n //////////////////////////////////////////////////////")
                    print("\n Input Invalido --\n Tente a Operação Novamente --")
                    print("\n //////////////////////////////////////////////////////")
                    break

    # saque

    @classmethod
    def saq(cls,id):
        print("\n //////////////////////////////////////////////////////")
        if cria.lista[id].saldo > 0:
            while True:
                try:
                    print("\n Quantia : ")
                    quantia = float(input("\n    ==    "))
                    if quantia <= 0:
                        print("\n Input Invalido --")
                        continue
                    else:
                        if cria.lista[id].saldo >= quantia:
                            cria.lista[id].saque(quantia)
                            print("\n //////////////////////////////////////////////////////")
                            break
                        else:
                            print("\n Saldo Insuficiente --")

                except:
                    print("\n //////////////////////////////////////////////////////")
                    print("\n Input Invalido --\n Tente a Operação Novamente --")
                    print("\n //////////////////////////////////////////////////////")
                    break
        else:
            print("\n Saldo Insuficiente --")
            print("\n //////////////////////////////////////////////////////")

    # transferencias

    @classmethod
    def transfe(cls,id):
            if cria.lista[id].saldo > 0:
                print("\n //////////////////////////////////////////////////////")
                print("\n Quantia")
                while True:
                    try:
                        quantia = float(input("\n    ==    "))
                        if quantia >= 1 and quantia <= cria.lista[id].saldo:
                            break
                        else:
                            print("\n Input Invalido -- ")
                            continue
                    except:
                        print("\n Input Invalido --")
                        continue
                print("\n //////////////////////////////////////////////////////")
                print("\n Numero Do Titular")
                while True:
                    try:
                        titular = int(input("\n    ==    "))
                        if titular <= 0 or titular == cria.lista[id].numero:
                            print("\n Input Invalido --")
                            continue
                        else:
                            break
                    except:
                        print("\n Input Invalido --")
                        continue
                try:
                    cria.lista[id].transferencia(quantia,titular)
                except:
                    print("\n Conta Inexistente --")
                    print("\n //////////////////////////////////////////////////////")
            else:
                print("\n //////////////////////////////////////////////////////")
                print("\n Saldo Insuficiente --")
                print("\n //////////////////////////////////////////////////////")

    # historico

    @classmethod
    def histor(cls,id):
            print("\n------------------------------------------------------------------------------------")
            print("\n Historico :")
            print("\n //////////////////////////////////////////////////////")
            cria.lista[id].historico()
            print("\n //////////////////////////////////////////////////////")


    # criacao ++ de conta

    @classmethod
    def create(cls, nombre, cpf, idade):

        global contagem
        global lista

        cria.contagem += 1
        cria.lista.append(cria.contagem)
        cria.lista[cria.contagem - 1] = conta(nombre, cpf, idade)

        #mostralista
        #print("\n Lista : {} \n contagem : {}".format(cria.lista, cria.contagem))


# Run Zone

cria.create("admin1","123.456.789-10","10/10/10")
cria.lista[0].senha = 1
cria.create("admin2","10.987.654.321","01/01/01")
cria.lista[1].senha = 2
cria.menu()
#=========================================== Check ===============================================================

f0.pack()
label.pack()
btn.place(width=183, height=65, x=627, y=225)
btn2.place(width=305, height=73, x=583, y=574)
root.mainloop()