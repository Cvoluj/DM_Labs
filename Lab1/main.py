import tkinter
from tkinter import *
from tkinter import messagebox
from func import *
hei = 5

choose = 0

def build():
    button1.grid(row=1, column=5, sticky="nsew", rowspan=2, columnspan=2)
    button2.grid(row=3, column=5, sticky="nsew", rowspan=2, columnspan=2)
    button3.grid(row=5, column=5, sticky="nsew", rowspan=2, columnspan=2)
    button4.grid(row=7, column=5, sticky="nsew", rowspan=2, columnspan=2)
    label1.grid(row=1, column=1, columnspan=3, rowspan=2)
    enA.grid(row=2, column=2)
    enB.grid(row=3, column=2)
    enC.grid(row=4, column=2)
    enU.grid(row=5, column=2)
    labA.grid(row=2, column=1, sticky="nsew")
    labB.grid(row=3, column=1, sticky="nsew")
    labC.grid(row=4, column=1, sticky="nsew")
    labU.grid(row=5, column=1, sticky="nsew")
    guide.grid(row=8, column=1, sticky="nsew", columnspan=2)
    regular.grid(row=3, column=3, sticky="nsew", rowspan=2)
    create.grid(row=7, column=3, sticky="nsew", rowspan=2)
    rand.grid(row=5, column=3, sticky="nsew", rowspan=2)#

def openwin(win_name):
    new_window = tkinter.Toplevel()
    new_window.title(win_name)
    new_window.geometry("300x300")


def regularopt():
    enU.configure(state=DISABLED)
    enA.configure(state=NORMAL)
    enB.configure(state=NORMAL)
    enC.configure(state=NORMAL)
    guide.configure(text="Введіть множини \n(через пробіл або розділові знаки)")
    create.configure(state=NORMAL)
    global choose
    choose = 1


def randopt():
    enA.configure(state=NORMAL)
    enB.configure(state=NORMAL)
    enC.configure(state=NORMAL)
    enU.configure(state=NORMAL)
    create.configure(state=NORMAL)
    guide.configure(text="Введіть потужності множин\nінтервал для універсальної множини\n "
                         "(через пробіл або розділові знаки)")
    global choose
    choose = 2


def choosing():
    check = False
    global choose
    if choose == 1:
        try:
            setA = int(set(enA.get().split(r"[,:;\s]")))
            setB = int(set(enB.get().split(r"[,:;\s]")))
            setC = int(set(enC.get().split(r"[,:;\s]")))
            maxValue = max(max(setA), max(setB), max(setC))
            minValue = min(min(setA), min(setB), min(setC))
            if maxValue <= 255 and minValue >= 0:
                normalway()
                button1.configure(state=NORMAL)
                button2.configure(state=NORMAL)
                button3.configure(state=NORMAL)
                button4.configure(state=NORMAL)
                return 0
            else:
                messagebox.showwarning('Помилка', 'Неправельно введені дані')
        except:
            messagebox.showwarning('Помилка', 'Неправельно введені дані')
    else:
        try:
            powerA = int(enA.get())
            powerB = int(enB.get())
            powerC = int(enC.get())
            check = True
        except ValueError:
            messagebox.showwarning('Помилка', 'Неправельно введені дані')
        if check:
            maxValue = max(powerA, powerB, powerC)
            a = enU.get()
            U = a.split(" ")
            if len(U) == 2:
                first = int(U[0])
                second = int(U[1])
                if first > second or ((second - first) < maxValue) or second > 255:
                    messagebox.showwarning('Помилка', 'Неправельно введені дані')
                else:
                    randomway()
                    button1.configure(state=NORMAL)
                    button2.configure(state=NORMAL)
                    button3.configure(state=NORMAL)
                    button4.configure(state=NORMAL)
            else:
                messagebox.showwarning('Помилка', 'Неправельно введені дані')


root = Tk()

root.title("Головне вікно")
root.geometry("400x400")
root.resizable(width=True, height=True)

G = 24
N = 1
variant = (N + G % 60) % 30+1
text1 = "Група - ІО-24, номер - {0!s} , варіант - {1!s}".format(N, variant)

label1 = Label(root, text="Бережанський\nДанііл\nВадимович\n{0!s}".format(text1), font=("Helvetica", 14), justify=LEFT)




button1 = Button(root, text="Відкрити вікно №2", height=hei, command=lambda: openwin("Вікно 2"), state=DISABLED, justify=RIGHT)
button2 = Button(root, text="Відкрити вікно №3", height=hei, command=lambda: openwin("Вікно 3"), state=DISABLED, justify=RIGHT)
button3 = Button(root, text="Відкрити вікно №4", height=hei, command=lambda: openwin("Вікно 4"), state=DISABLED, justify=RIGHT)
button4 = Button(root, text="Відкрити вікно №5", height=hei, command=lambda: openwin("Вікно 5"), state=DISABLED, justify=RIGHT)
regular = Button(root, text="Задати власноруч", height=hei, command=regularopt)

rand = Button(root, text="Згенерувати випадково", height=hei, command=randopt)
create = Button(root, text="Порахувати!", height=hei,state=DISABLED, command=choosing)
guide = Label(root, text="", height=1, justify=LEFT)


enA = Entry(root, width=14, bd=1, state=DISABLED, font=("Garamond", 16), justify=RIGHT)
enB = Entry(root, width=14, bd=1, state=DISABLED, font=("Garamond", 16), justify=RIGHT)
enC = Entry(root, width=14, bd=1, state=DISABLED, font=("Garamond", 16), justify=RIGHT)
enU = Entry(root, width=14, bd=1, state=DISABLED, font=("Garamond", 16), justify=RIGHT)

labA = Label(root, text="A:", justify=LEFT)
labB = Label(root, text="B:", justify=LEFT)
labC = Label(root, text="C:", justify=LEFT)
labU = Label(root, text="U:", justify=LEFT)
build()

root.mainloop()
