from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Banco NIX")
root.geometry('700x500')
root.minsize(width=350, height=250)
root.minsize(width=350, height=250)
root.maxsize(width=450, height=400)

def format_cpf(event=None):
    text = entry.get().replace(".", "").replace("-", "")[:11]
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

    entry.delete(0, "end")
    entry.insert(0, new_text)

entry = Entry(root, font=("Arial", 20))
entry.bind("<KeyRelease>", format_cpf)

def mainF():
    global cal
    def getDate():
        date=cal.get_date()
        print(date)
    cal.pack(pady=20, padx=20)
    butt=Button(root,text="Date Getter", bg="cyan",command=getDate).pack()
cal=Calendar(root,selectmode="day", date_pattern="dd-mm-y")
but=Button(root,text="Pick Date",command=mainF).pack()

entry.pack()

root.mainloop()