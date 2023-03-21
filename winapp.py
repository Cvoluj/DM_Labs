import tkinter
from tkinter import *
from tkinter import messagebox
from func import *
import re
import random


def info():
    G = 24
    N = 1
    variant = (N + G % 60) % 30 + 1
    return "Група - ІО-24, номер - {0!s} , варіант - {1!s}".format(N, variant)


def cleanfile():
    with open("results.txt", "w") as f:
        f.write("")


def openwin(win_name):
    new_window = tkinter.Toplevel()
    new_window.title(win_name)
    new_window.geometry("300x300")


def winstate(variable):
    winB2.configure(state=variable)
    winB3.configure(state=variable)
    winB4.configure(state=variable)
    winB5.configure(state=variable)


def show_set():
    A_info['text'] = ','.join(map(str, setA))
    B_info['text'] = ','.join(map(str, setB))
    C_info['text'] = ','.join(map(str, setC))
    U_info['text'] = ','.join(map(str, setU))


def inputChoose():
    enU.configure(state=DISABLED)
    enA.configure(state=NORMAL)
    enB.configure(state=NORMAL)
    enC.configure(state=NORMAL)
    calculateButt.configure(state=NORMAL)
    guideText.configure(text="Введіть множини через пробіл або розділові знаки")
    global choose
    choose = 1


def randomChoose():
    enA.configure(state=NORMAL)
    enB.configure(state=NORMAL)
    enC.configure(state=NORMAL)
    enU.configure(state=NORMAL)
    calculateButt.configure(state=NORMAL)
    guideText.configure(text="Введіть потужність множин")
    global choose
    choose = 2


def choosing():
    cleanfile()
    check = False
    global choose, setA, setB, setC, powerA, powerB, powerC, setU
    if choose == 1:
        try:
            setA = set(sorted(map(int, re.split(delimiters, enA.get()))))
            setB = set(sorted(map(int, re.split(delimiters, enB.get()))))
            setC = set(sorted(map(int, re.split(delimiters, enC.get()))))
            maxValue = max(max(setA), max(setB), max(setC))
            minValue = min(min(setA), min(setB), min(setC))
            if maxValue <= 254 and minValue >= 0:
                setU = set(range(minValue, maxValue + 2))
                show_set()
                guideText.configure(text="Множини створено!")
                print(setA)
                print(setB)
                print(setC)
                print(setU)
                winstate(NORMAL)
                return 0
            else:
                messagebox.showwarning('Помилка', 'Одна з множин вийшла за межі 0 - 255')
        except:
            messagebox.showwarning('Помилка', 'Неправильно введені дані')
    else:
        try:
            powerA = int(enA.get())
            powerB = int(enB.get())
            powerC = int(enC.get())
            check = True
        except ValueError:
            messagebox.showwarning('Помилка', 'Неправильно введені дані')
        if check:
            maxValue = max(powerA, powerB, powerC)
            a = enU.get()
            U = a.split(" ")
            if len(U) == 2:
                first = int(U[0])
                second = int(U[1])
                if first > second or ((second - first) < maxValue) or second > 255:
                    messagebox.showwarning('Помилка',
                                           'Одна з множин вийшла за межі 0-255\nабо розмір універсальної замалий')
                else:

                    winstate(NORMAL)
                    setU = set(range(first, second + 1))
                    setA = set(sorted(random.sample(list(setU), powerA)))
                    setB = set(sorted(random.sample(list(setU), powerB)))
                    setC = set(sorted(random.sample(list(setU), powerC)))
                    show_set()
                    guideText.configure(text="Множини створено!")
                    print(setA)
                    print(setB)
                    print(setC)
                    print(setU)

        else:
            messagebox.showwarning('Помилка', 'Неправильно введені дані')


def openwin2():
    global step2
    step2 = 0

    win2 = Tk()
    win2.title("Вікно 2")
    win2.geometry("800x500")
    win2.resizable(width=False, height=False)

    def win2calc():
        global step2
        global result2

        noSetA = differenceU(setA, setU)
        noSetB = differenceU(setB, setU)
        noSetC = differenceU(setC, setU)
        part1 = union(noSetA, union(noSetA, setB))
        part2 = union(noSetA, setC)
        part3 = union(intersect(setB, setC), intersect(setB, noSetC))
        if step2 == 0:
            StepCalc2['text'] += ','.join(map(str, noSetA)) +'\n'
            StepText2['text'] +="\n¬A∪B"
        elif step2 == 1:
            StepCalc2['text'] += ','.join(map(str, union(noSetA, setB))) + '\n'
            StepText2['text'] += "\n¬A∪(¬A∪B)"
        elif step2 == 2:
            StepCalc2['text'] += ','.join(map(str, union(noSetA, union(noSetA, setB)))) + '\n'
            StepText2['text'] += "\n¬A∪C"
        elif step2 == 3:
            StepCalc2['text'] += ','.join(map(str, union(noSetA, setC))) + '\n'
            StepText2['text'] += "\n¬A∪(¬A∪B)∩(¬A∪C)"
        elif step2 == 4:
            StepCalc2['text'] += ','.join(map(str, intersect(part1, part2))) + '\n'
            StepText2['text'] += "\n¬B"
        elif step2 == 5:
            StepCalc2['text'] += ','.join(map(str, noSetB)) + '\n'
            StepText2['text'] += "\n¬A∪(¬A∪B)∩(¬A∪C)∪¬B"
        elif step2 == 6:
            StepCalc2['text'] += ','.join(map(str, union(intersect(part1, part2), noSetB))) + '\n'
            StepText2['text'] += "\n¬C"
        elif step2 == 7:
            StepCalc2['text'] += ','.join(map(str, noSetC)) + '\n'
            StepText2['text'] += "\nB∩¬C"
        elif step2 == 8:
            StepCalc2['text'] += ','.join(map(str, intersect(setB, noSetC))) + '\n'
            StepText2['text'] += "\nB∩C"
        elif step2 == 9:
            StepCalc2['text'] += ','.join(map(str, intersect(setB, setC))) + '\n'
            StepText2['text'] += "\n((B∩C)∪(B∩¬C))"
        elif step2 == 10:
            StepCalc2['text'] += ','.join(map(str, part3)) + '\n'
            StepText2['text'] += "\n¬A∪(¬A∪B)∩(¬A∪C)∪¬B∩((B∩C)∪(B∩¬C))"
        elif step2 == 11:
            final = intersect(union(intersect(part1, part2), noSetB), part3)
            result2 = ','.join(map(str, final))
            StepCalc2['text'] += result2
            SaveButt.configure(state=NORMAL)
        step2 += 1
    def save2():
        with open('results.txt', 'a') as f:
            print(f"D = {result2}", file=f)
        SaveButt.configure(state=DISABLED)

    descritpionBox2 = LabelFrame(win2, labelanchor='n', font=font, bg=background, text="Створені множини")
    A_text2 = Label(descritpionBox2, text="A = ", bg=background, font=("Helvatica", 11))
    B_text2 = Label(descritpionBox2, text="B = ", bg=background, font=("Helvatica", 11))
    C_text2 = Label(descritpionBox2, text="C = ", bg=background, font=("Helvatica", 11))
    U_text2 = Label(descritpionBox2, text="U = ", bg=background, font=("Helvatica", 11))
    A_info2 = Label(descritpionBox2, bg=background, relief="groove", font=("Helvatica", 11), width=80)
    B_info2 = Label(descritpionBox2, bg=background, relief="groove", font=("Helvatica", 11), width=80)
    C_info2 = Label(descritpionBox2, bg=background, relief="groove", font=("Helvatica", 11), width=80)
    U_info2 = Label(descritpionBox2, bg=background, relief="groove", font=("Helvatica", 11), width=80)
    A_info2['text'] = ','.join(map(str, setA))
    B_info2['text'] = ','.join(map(str, setB))
    C_info2['text'] = ','.join(map(str, setC))
    U_info2['text'] = ','.join(map(str, setU))
    descritpionBox2.grid(row=0, column=0, columnspan=4, padx=18, sticky="we")
    A_text2.grid(row=1, column=0)
    B_text2.grid(row=2, column=0)
    C_text2.grid(row=3, column=0)
    U_text2.grid(row=4, column=0)
    A_info2.grid(row=1, column=1)
    B_info2.grid(row=2, column=1)
    C_info2.grid(row=3, column=1)
    U_info2.grid(row=4, column=1)
    D_text2 = Label(descritpionBox2, text="D = ", bg=background, font=("Helvatica", 11))
    D_info2 = Label(descritpionBox2, bg=background, relief="groove", font=("Helvatica", 11), width=80,
                    text="¬A∪(¬A∪B)∩(¬A∪C)∪¬B∩((B∩C)∪(B∩¬C))")
    descritpionBox2.grid(row=0, column=0, columnspan=4, padx=18, sticky="we")
    A_text2.grid(row=1, column=0)
    B_text2.grid(row=2, column=0)
    C_text2.grid(row=3, column=0)
    U_text2.grid(row=4, column=0)
    D_text2.grid(row=5, column=0)
    A_info2.grid(row=1, column=1)
    B_info2.grid(row=2, column=1)
    C_info2.grid(row=3, column=1)
    U_info2.grid(row=4, column=1)
    D_info2.grid(row=5, column=1)
    # кнопки
    ButtonBox = LabelFrame(win2, labelanchor='n', font=font, bg=background)
    ButtonBox.grid(row=1, column=0, columnspan=4, sticky="we", padx=18, pady=5)
    CalculateButt = Button(ButtonBox, text="Виконати крок", height=buttonHeight, command=win2calc, font=font2, width=45)
    SaveButt = Button(ButtonBox, text="Зберегти", height=buttonHeight, command=save2, state=DISABLED, font=font2,
                      width=45)

    CalculateButt.grid(row=0, column=0, padx=30, pady=5, sticky="we", columnspan=2)
    SaveButt.grid(row=0, column=3, padx=30, pady=5, sticky="we", columnspan=2)

    # Крокове рішення
    StepBox2 = LabelFrame(win2, labelanchor='n', font=font, bg=background, text="Покрокове рішення")
    StepBox2.grid(row=2, column=0, columnspan=4, sticky="we", pady=5, padx=18)
    StepText2 = Label(StepBox2, text="¬A", font=("Helvetica", 11), bg=background)
    StepCalc2 = Label(StepBox2, text="", font=("Helvetica", 11), bg=background, relief="groove", width=45)
    StepText2.grid(row=2, column=0, columnspan=2, padx=9, sticky="we", pady=5)
    StepCalc2.grid(row=2, column=2, columnspan=2, padx=9, sticky="we", pady=5)

    win2.mainloop()


def openwin3():
    global step3
    step3 = 0
    win3 = Tk()
    win3.title("Вікно 3")
    win3.geometry("520x300")
    win3.resizable(width=False, height=False)

    def win3calc():
        global step3
        global result3
        if step3 == 0:
            StepCalc3['text'] += ','.join(map(str, differenceU(setA, setU))) +'\n'
            StepText3['text'] +="\n¬A ∪ C"
        elif step3 == 1:
            StepCalc3['text'] += ','.join(map(str, union(differenceU(setA, setU), setC))) + '\n'
            StepText3['text'] += "\n(¬A ∪ C) ∩ B"
        elif step3 == 2:
            result3 = ','.join(map(str, intersect(union(differenceU(setA, setU), setC), setB)))
            StepCalc3['text'] += result3
            SaveButt.configure(state=NORMAL)
        step3 += 1
    def save3():
        with open('results.txt', 'a') as f:
            print(f"D1 = {result3}", file=f)
        SaveButt.configure(state=DISABLED)

    descritpionBox3 = LabelFrame(win3, labelanchor='n', font=font, bg=background, text="Створені множини")
    A_text3 = Label(descritpionBox3, text="A = ", bg=background, font=("Helvatica", 11))
    B_text3 = Label(descritpionBox3, text="B = ", bg=background, font=("Helvatica", 11))
    C_text3 = Label(descritpionBox3, text="C = ", bg=background, font=("Helvatica", 11))
    U_text3 = Label(descritpionBox3, text="U = ", bg=background, font=("Helvatica", 11))
    A_info3 = Label(descritpionBox3, bg=background, relief="groove", font=("Helvatica", 11), width=50)
    B_info3 = Label(descritpionBox3, bg=background, relief="groove", font=("Helvatica", 11), width=50)
    C_info3 = Label(descritpionBox3, bg=background, relief="groove", font=("Helvatica", 11), width=50)
    U_info3 = Label(descritpionBox3, bg=background, relief="groove", font=("Helvatica", 11), width=50)
    A_info3['text'] = ','.join(map(str, setA))
    B_info3['text'] = ','.join(map(str, setB))
    C_info3['text'] = ','.join(map(str, setC))
    U_info3['text'] = ','.join(map(str, setU))
    D_text3 = Label(descritpionBox3, text="D = ", bg=background, font=("Helvatica", 11))
    D_info3 = Label(descritpionBox3, bg=background, relief="groove", font=("Helvatica", 11), width=50, text="(¬A ∪ C) ∩ B")
    descritpionBox3.grid(row=0, column=0, columnspan=4, padx=18, sticky="we")
    A_text3.grid(row=1, column=0)
    B_text3.grid(row=2, column=0)
    C_text3.grid(row=3, column=0)
    U_text3.grid(row=4, column=0)
    D_text3.grid(row=5, column=0)
    A_info3.grid(row=1, column=1)
    B_info3.grid(row=2, column=1)
    C_info3.grid(row=3, column=1)
    U_info3.grid(row=4, column=1)
    D_info3.grid(row=5, column=1)
    # кнопки
    ButtonBox = LabelFrame(win3, labelanchor='n', font=font, bg=background)
    ButtonBox.grid(row=1, column=0, columnspan=4, sticky="we", padx=18, pady=5)
    CalculateButt = Button(ButtonBox, text="Виконати крок", height=buttonHeight, command=win3calc, font=font2, width=28)
    SaveButt = Button(ButtonBox, text="Зберегти", height=buttonHeight, command=save3, state=DISABLED, font=font2,
                      width=28)

    CalculateButt.grid(row=0, column=0, padx=20, pady=5, sticky="we", columnspan=2)
    SaveButt.grid(row=0, column=3, padx=20, pady=5, sticky="we", columnspan=2)


    # Крокове рішення
    StepBox3 = LabelFrame(win3, labelanchor='n', font=font, bg=background, text="Покрокове рішення")
    StepBox3.grid(row=2, column=0, columnspan=4, sticky="we", pady=5, padx=18)
    StepText3 = Label(StepBox3, text="¬A", font=("Helvetica", 11), bg=background)
    StepCalc3 = Label(StepBox3, text="", width=35, font=("Helvetica", 11), bg=background, relief="groove")
    StepText3.grid(row=2, column=0, columnspan=2, padx=18, sticky="we", pady=5)
    StepCalc3.grid(row=2, column=2, columnspan=2, padx=18, sticky="we", pady=5)

    win3.mainloop()

def openwin4():

    win4 = Tk()
    win4.title("Вікно 4")
    win4.geometry("520x300")
    win4.resizable(width=False, height=False)

    def win4calc():
        global result4
        result4 = ','.join(map(str, intersect(differenceU(setC, setU), setA)))
        StepCalc4['text'] = result4
        SaveButt.configure(state=NORMAL)
    def save4():
        with open('results.txt', 'a') as f:
            print(f"Z = {result4}", file=f)
        SaveButt.configure(state=DISABLED)

    descritpionBox4 = LabelFrame(win4, labelanchor='n', font=font, bg=background, text="Створені множини")
    X_text4 = Label(descritpionBox4, text="X = ", bg=background, font=("Helvatica", 11))
    Y_text4 = Label(descritpionBox4, text="Y = ", bg=background, font=("Helvatica", 11))
    X_info4 = Label(descritpionBox4, bg=background, relief="groove", font=("Helvatica", 11), width=50)
    Y_info4 = Label(descritpionBox4, bg=background, relief="groove", font=("Helvatica", 11), width=50)
    X_info4['text'] = ','.join(map(str, differenceU(setC, setU)))
    Y_info4['text'] = ','.join(map(str, setA))
    Z_text4 = Label(descritpionBox4, text="Z = ", bg=background, font=("Helvatica", 11))
    Z_info4 = Label(descritpionBox4, bg=background, relief="groove", font=("Helvatica", 11), width=50,
                    text="X ∩ Y")
    descritpionBox4.grid(row=0, column=0, columnspan=4, padx=18, sticky="we")
    X_text4.grid(row=1, column=0)
    Y_text4.grid(row=2, column=0)
    Z_text4.grid(row=5, column=0)
    X_info4.grid(row=1, column=1)
    Y_info4.grid(row=2, column=1)
    Z_info4.grid(row=5, column=1)

    # кнопки
    ButtonBox = LabelFrame(win4, labelanchor='n', font=font, bg=background)
    ButtonBox.grid(row=1, column=0, columnspan=4, sticky="we", padx=18, pady=5)
    CalculateButt = Button(ButtonBox, text="Виконати крок", height=buttonHeight, command=win4calc, font=font2, width=28)
    SaveButt = Button(ButtonBox, text="Зберегти", height=buttonHeight, command=save4, state=DISABLED, font=font2,
                      width=28)

    CalculateButt.grid(row=0, column=0, padx=20, pady=5, sticky="we", columnspan=2)
    SaveButt.grid(row=0, column=3, padx=20, pady=5, sticky="we", columnspan=2)

    # Крокове рішення
    StepBox4 = LabelFrame(win4, labelanchor='n', font=font, bg=background, text="Покрокове рішення")
    StepBox4.grid(row=2, column=0, columnspan=4, sticky="we", pady=5, padx=18)
    StepText4 = Label(StepBox4, text="X ∩ Y", font=("Helvetica", 11), bg=background)
    StepCalc4 = Label(StepBox4, text="", width=35, font=("Helvetica", 11), bg=background, relief="groove")
    StepText4.grid(row=2, column=0, columnspan=2, padx=18, sticky="we", pady=5)
    StepCalc4.grid(row=2, column=2, columnspan=2, padx=18, sticky="we", pady=5)

    win4.mainloop()


def openwin5():
    global step5
    step5 = 0
    a, b, c, d = set(), set(), set(), set()
    win5 = Tk()
    win5.title("Вікно 5")
    win5.geometry("520x420")
    win5.resizable(width=False, height=False)

    def win5calc():
        global result5
        result5 = ','.join(map(str, (setU - setC).intersection(setA)))
        StepCalc5['text'] = result5
        SaveButt.configure(state=NORMAL)

    def save5():
        with open('results.txt', 'a') as f:
            print(f"Z1 = {result5}", file=f)
        SaveButt.configure(state=DISABLED)
        UploadButt.configure(state=NORMAL)

    def upload():
        global step5, a, b, c, d
        if step5 == 0:
            with open('results.txt', 'r') as f:
                lines = f.readlines()
                a = lines[0][4::]
                b = lines[1][5::]
                c = lines[2][4::]
                d = lines[3][5::]
                A_info5['text'] = str(a).replace("{}", "").replace("\n", "")
                B_info5['text'] = str(b).replace("{}", "").replace("\n", "")
                C_info5['text'] = str(c).replace("{}", "").replace("\n", "")
                U_info5['text'] = str(d).replace("{}", "").replace("\n", "")
        elif step5 == 1:
            if a == b:
                answer1['text'] = "Елементи однакові"

        elif step5 == 2:
            if c == d:
                answer2['text'] = "Елементи однакові"
        step5 += 1

    compareBox = LabelFrame(win5, labelanchor='n', font=font, bg=background, text="Порівняння" )
    descritpionBox5 = LabelFrame(win5, labelanchor='n', font=font, bg=background, text="Створені множини")
    X_text5 = Label(descritpionBox5, text="X = ", bg=background, font=("Helvatica", 11))
    Y_text5 = Label(descritpionBox5, text="Y = ", bg=background, font=("Helvatica", 11))
    X_info5 = Label(descritpionBox5, bg=background, relief="groove", font=("Helvatica", 11), width=50)
    Y_info5 = Label(descritpionBox5, bg=background, relief="groove", font=("Helvatica", 11), width=50)
    X_info5['text'] = ','.join(map(str, differenceU(setC, setU)))
    Y_info5['text'] = ','.join(map(str, setA))
    Z_text5 = Label(descritpionBox5, text="Z = ", bg=background, font=("Helvatica", 11))
    Z_info5 = Label(descritpionBox5, bg=background, relief="groove", font=("Helvatica", 11), width=50,
                    text="X ∩ Y")
    descritpionBox5.grid(row=0, column=0, columnspan=4, padx=18, sticky="we")
    X_text5.grid(row=1, column=0)
    Y_text5.grid(row=2, column=0)
    Z_text5.grid(row=5, column=0)
    X_info5.grid(row=1, column=1)
    Y_info5.grid(row=2, column=1)
    Z_info5.grid(row=5, column=1)

    # кнопки
    ButtonBox = LabelFrame(win5, labelanchor='n', font=font, bg=background)
    ButtonBox.grid(row=1, column=0, columnspan=4, sticky="we", padx=18, pady=5)
    CalculateButt = Button(ButtonBox, text="Вихарувати стандартно", height=buttonHeight, command=win5calc, font=font2, width=28)
    SaveButt = Button(ButtonBox, text="Зберегти", height=buttonHeight, command=save5, state=DISABLED, font=font2, width=28)
    UploadButt = Button(ButtonBox, text="Загрузити та порівняти", height=buttonHeight, command=upload, state=DISABLED, font=font2, width=28*2+7)

    CalculateButt.grid(row=0, column=0, padx=20, pady=5, sticky="we", columnspan=2)
    SaveButt.grid(row=0, column=3, padx=20, pady=5, sticky="we", columnspan=2)
    UploadButt.grid(row=1, column=0, columnspan=4, padx=20, pady=5, sticky="we")
    # Крокове рішення
    StepBox5 = LabelFrame(win5, labelanchor='n', font=font, bg=background, text="Покрокове рішення")
    StepBox5.grid(row=2, column=0, columnspan=4, sticky="we", pady=5, padx=18)
    StepText5 = Label(StepBox5, text="X ∩ Y", font=("Helvetica", 11), bg=background)
    StepCalc5 = Label(StepBox5, text="", width=35, font=("Helvetica", 11), bg=background, relief="groove")
    StepText5.grid(row=2, column=0, columnspan=2, padx=18, sticky="we", pady=5)
    StepCalc5.grid(row=2, column=2, columnspan=2, padx=18, sticky="we", pady=5)

    # Загрузка
    A_text5 = Label(compareBox, text="D =  ", bg=background, font=("Helvatica", 11))
    B_text5 = Label(compareBox, text="D1 = ", bg=background, font=("Helvatica", 11))
    C_text5 = Label(compareBox, text="Z =  ", bg=background, font=("Helvatica", 11))
    U_text5 = Label(compareBox, text="Z1 =  ", bg=background, font=("Helvatica", 11))
    A_info5 = Label(compareBox, bg=background, relief="groove", font=("Helvatica", 11), width=35)
    B_info5 = Label(compareBox, bg=background, relief="groove", font=("Helvatica", 11), width=35)
    C_info5 = Label(compareBox, bg=background, relief="groove", font=("Helvatica", 11), width=35)
    U_info5 = Label(compareBox, bg=background, relief="groove", font=("Helvatica", 11), width=35)


    compareBox.grid(row=3, column=0, columnspan=4, padx=18, sticky="we")
    A_text5.grid(row=1, column=0, pady=3)
    B_text5.grid(row=2, column=0, pady=3)
    C_text5.grid(row=3, column=0, pady=3)
    U_text5.grid(row=4, column=0, pady=3)
    A_info5.grid(row=1, column=1, pady=3)
    B_info5.grid(row=2, column=1, pady=3)
    C_info5.grid(row=3, column=1, pady=3)
    U_info5.grid(row=4, column=1, pady=3)
    answer1 = Label(compareBox, text="", bg=background, font=("Helvatica", 10))
    answer2 = Label(compareBox, text="", bg=background, font=("Helvatica", 10))
    answer1.grid(row=1, column=2, pady=3)
    answer2.grid(row=3, column=2, pady=3)
    win5.mainloop()


cleanfile()
choose = 0
# --Шрифт та дизайн, константи--
font = ["Helvetica", 10, "bold"]
font2 = ["Calibri", 10]
background = "#ffffff"
buttonHeight = 2
delimiters = "[,\[\] ]+"
step3 = 0
step2 = 0
step5 = 0
setA, setB, setC, setU = set(), set(), set(), set()
powerA, powerB, powerC = 0, 0, 0

root = Tk()
root.title('Головне вікно')
root.geometry('560x475')
root.resizable(width=False, height=False)

# Створення блоків
infoBox = LabelFrame(root, text='Інформація про студента', labelanchor="n", font=font)
inputBox = LabelFrame(root, text="Введення множин", labelanchor='n', font=font)
chooseBox = LabelFrame(root, text="Виберіть операцію", labelanchor="n", font=font)
descritpionBox = LabelFrame(root, labelanchor='n', font=font, bg=background)
winBox = LabelFrame(root, text="Навігація", labelanchor="n", font=font)
Boxes = LabelFrame(root)

# Інформація про студента
infoText = Label(infoBox, text="Бережанський\nДанііл\nВадимович\n{0!s}".format(info()), font=("Helvetica", 13),
                 justify=LEFT)
infoBox.grid(row=0, padx=30, pady=10, sticky="we", columnspan=4)
infoText.grid(row=1, column=1, padx=10, pady=10, sticky="we")

# Розміщення полів
inputBox.grid(row=2, column=1, padx=18, pady=5, sticky="we")
chooseBox.grid(row=2, column=2, pady=5, sticky="we")
winBox.grid(row=2, column=3, padx=18, pady=5, sticky="we")
descritpionBox.grid(row=3, column=0, columnspan=4, padx=18, sticky="we")

# Поле вводу та створення множин
enA = Entry(inputBox, width=14, bd=1, state=DISABLED, font=("Garamond", 16), justify=RIGHT, bg=background)
enB = Entry(inputBox, width=14, bd=1, state=DISABLED, font=("Garamond", 16), justify=RIGHT, bg=background)
enC = Entry(inputBox, width=14, bd=1, state=DISABLED, font=("Garamond", 16), justify=RIGHT, bg=background)
enU = Entry(inputBox, width=14, bd=1, state=DISABLED, font=("Garamond", 16), justify=RIGHT, bg=background)
enA_text = Label(inputBox, text='A: ', width=4, bg=background, font=font)
enB_text = Label(inputBox, text='B: ', width=4, bg=background, font=font)
enC_text = Label(inputBox, text='C: ', width=4, bg=background, font=font)
enU_text = Label(inputBox, text='U: ', width=4, bg=background, font=font)

enA_text.grid(row=0, column=0, pady=2)
enB_text.grid(row=1, column=0, pady=2)
enC_text.grid(row=2, column=0, pady=2)
enU_text.grid(row=3, column=0, pady=2)
enA.grid(row=0, column=1, pady=2)
enB.grid(row=1, column=1, pady=2)
enC.grid(row=2, column=1, pady=2)
enU.grid(row=3, column=1, pady=2)

# Поле вибору операції
inputButt = Button(chooseBox, text="Задати власноруч", command=inputChoose, height=buttonHeight, font=font2)
randomButt = Button(chooseBox, text="Згенерувати випадково", command=randomChoose, height=buttonHeight, font=font2)
calculateButt = Button(chooseBox, text="Порахувати!", state=DISABLED, command=choosing, height=buttonHeight, font=font2)

inputButt.grid(row=0, column=0, padx=5, pady=1, sticky="we")
randomButt.grid(row=1, column=0, padx=5, pady=1, sticky="we")
calculateButt.grid(row=2, column=0, padx=5, pady=1, sticky="we")

# Поле кнопок-вікон
winB2 = Button(winBox, text="Відкрити вікно №2", height=buttonHeight, command=openwin2, state=DISABLED, font=font2)
winB3 = Button(winBox, text="Відкрити вікно №3", height=buttonHeight, command=openwin3, state=DISABLED, font=font2)
winB4 = Button(winBox, text="Відкрити вікно №4", height=buttonHeight, command=openwin4,
               state=DISABLED, font=font2)
winB5 = Button(winBox, text="Відкрити вікно №5", height=buttonHeight, command=openwin5,
               state=DISABLED, font=font2)
winB2.grid(row=0, column=0, padx=5, pady=1, sticky="nsew")
winB3.grid(row=1, column=0, padx=5, pady=1, sticky="nsew")
winB4.grid(row=2, column=0, padx=5, pady=1, sticky="nsew")
winB5.grid(row=3, column=0, padx=5, pady=1, sticky="nsew")

# Поле з інструкціями та створеними множинами
guideText = Label(descritpionBox, text="Виберіть операцію, щоб продовжити...", font=("Helvetica", 11), bg=background)
A_text = Label(descritpionBox, text="A = ", bg=background, font=("Helvatica", 11))
B_text = Label(descritpionBox, text="B = ", bg=background, font=("Helvatica", 11))
C_text = Label(descritpionBox, text="C = ", bg=background, font=("Helvatica", 11))
U_text = Label(descritpionBox, text="U = ", bg=background, font=("Helvatica", 11))



A_info = Label(descritpionBox, bg=background, relief="groove", font=("Helvatica", 11), width=50)
B_info = Label(descritpionBox, bg=background, relief="groove", font=("Helvatica", 11), width=50)
C_info = Label(descritpionBox, bg=background, relief="groove", font=("Helvatica", 11), width=50)
U_info = Label(descritpionBox, bg=background, relief="groove", font=("Helvatica", 11), width=50)
A_text.grid(row=1, column=0)
B_text.grid(row=2, column=0)
C_text.grid(row=3, column=0)
U_text.grid(row=4, column=0)
A_info.grid(row=1, column=1)
B_info.grid(row=2, column=1)
C_info.grid(row=3, column=1)
U_info.grid(row=4, column=1)


guideText.grid(row=0, column=0, columnspan=4, sticky="w", padx=35)

root.mainloop()
