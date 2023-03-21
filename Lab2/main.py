from tkinter import *
import shelve
import random
import BinatyAttitudes
import LogicalOperations

def Mainread():
    with shelve.open('StoresList.shelf', 'r') as myshelf:
        first_dict = myshelf["first"]
        second_dict = myshelf['second']

        firstDict.update({k: v for k, v in first_dict.items() if k not in firstDict})
        secondDict.update({k: v for k, v in second_dict.items() if k not in secondDict})
        print(firstDict)
        print(secondDict)

def openwin():
    pass


def info():
    G = 24
    N = 1
    variant = (N + G % 60) % 30 + 1
    return variant


def openwin2():
    win = Tk()
    win.title('Вікно 2')
    win.geometry('570x500')

    ChooseFrame = LabelFrame(win, labelanchor="n", font=font)
    ListFrame = LabelFrame(win, labelanchor="n", font=font)
    ChooseFrame.grid(row=0, column=0, padx=9, pady=9, sticky="nsew")
    ListFrame.grid(row=0, column=1, sticky="nsew", pady=9, padx=9)

    def update(val):
        RadioVar.set(val)

    def selected(BoxName):
        index = BoxName.curselection()

        for i in index:
            print(i)
            item = BoxName.get(i)

            if RadioVar.get() == 1:
                FirstList.insert(END, item)
                if Names[item] == "w":
                    firstDict[item] = "w"
                else:
                    firstDict[item] = "m"
            else:
                SecondList.insert(END, item)
                if Names[item] == "w":
                    secondDict[item] = "w"
                else:
                    secondDict[item] = "m"
        print(firstDict)
        print(secondDict)

    def savefromlistbox(nameDict, number):
        with shelve.open('StoresList.shelf') as f:
            f[number] = nameDict

    def readshelve():

        Mainread()
        FirstList.delete(0, END)
        SecondList.delete(0, END)

        for k, i in enumerate(firstDict.keys()):
            FirstList.insert(k, i)
        for k, i in enumerate(secondDict.keys()):
            SecondList.insert(k, i)

    def removefromlist(NameBox, NameDict):
        if NameBox.curselection():
            NameDict.pop(NameBox.get(NameBox.curselection()))
            NameBox.delete(NameBox.curselection())

    # Головний лейбл
    WScroll = Scrollbar(ChooseFrame)
    WList = Listbox(ChooseFrame, font=font2)
    WScroll.config(command=WList.yview)
    WList.config(yscrollcommand=WScroll.set, selectmode='multiple')
    WText = Label(ChooseFrame, text="Жіночі імена:")

    WText.grid(row=0, column=0, sticky="we", columnspan=2)
    WList.grid(row=1, column=0, sticky="NSEW")
    WScroll.grid(row=1, column=1, sticky="ns")

    MList = Listbox(ChooseFrame, font=font2, selectmode='multiple')  #
    MScroll = Scrollbar(ChooseFrame)  # Скролбар для списків
    MScroll.config(command=MList.yview)  #
    MList.config(yscrollcommand=MScroll.set)  #
    MText = Label(ChooseFrame, text="Чоловічі імена:")

    MText.grid(row=2, column=0, columnspan=2, sticky="we")
    MList.grid(row=3, column=0, sticky="NSEW")
    MScroll.grid(row=3, column=1, sticky="ns")

    for k, (i, j) in enumerate(Names.items()):

        if j == "w":
            WList.insert(k, i)
        else:
            MList.insert(k, i)
    # ---------------------------

    # Лейбл вибору

    RadioVar = IntVar()
    SetText = Label(ListFrame, text="Виберіть список до якого додасте ім'я")
    FirstRadio = Radiobutton(ListFrame, text="Перший список", variable=RadioVar, value=1, command=lambda: update(1))
    SecondRadio = Radiobutton(ListFrame, text="Другий список", variable=RadioVar, value=2, command=lambda: update(2))
    FirstScroll = Scrollbar(ListFrame)
    SecondScroll = Scrollbar(ListFrame)

    FirstList = Listbox(ListFrame, yscrollcommand=FirstScroll.set)
    SecondList = Listbox(ListFrame, yscrollcommand=SecondScroll.set)
    FirstScroll.config(command=FirstList.yview)
    SecondScroll.config(command=SecondList.yview())

    FirstSaveButt = Button(ListFrame, text="Зберегти А", height=3, width=25,
                           command=lambda: savefromlistbox(firstDict, "first"),
                           state=NORMAL, font=font2)
    SecondSaveButt = Button(ListFrame, text="Зберегти В", height=3, width=25,
                            command=lambda: savefromlistbox(secondDict, "second"),
                            state=NORMAL, font=font2)

    ReadButt = Button(ListFrame, text="Зчитати з файлу", height=3, width=52, command=readshelve,
                      state=NORMAL, font=font2)
    RemoveFirstButt = Button(ListFrame, text="Видалити з А", height=3, width=25,
                             command=lambda: removefromlist(FirstList, firstDict),
                             state=NORMAL, font=font2)
    RemoveSecondButt = Button(ListFrame, text="Видалити з В", height=3, width=25,
                              command=lambda: removefromlist(SecondList, secondDict),
                              state=NORMAL, font=font2)

    SetText.grid(row=0, column=0, columnspan=4, pady=9, padx=18, sticky="we")
    FirstRadio.grid(row=1, column=0, pady=5, padx=18, sticky="we", columnspan=2)
    SecondRadio.grid(row=1, column=2, pady=5, padx=18, sticky="we", columnspan=2)
    FirstList.grid(row=2, column=0, sticky="nsew")
    SecondList.grid(row=2, column=2, sticky="nsew")
    FirstScroll.grid(row=2, column=1, sticky="ns")
    SecondScroll.grid(row=2, column=3, sticky="ns")
    FirstSaveButt.grid(row=3, column=0, columnspan=2)
    RemoveSecondButt.grid(row=4, column=2, columnspan=2)
    RemoveFirstButt.grid(row=4, column=0, columnspan=2)
    SecondSaveButt.grid(row=3, column=2, columnspan=2)
    ReadButt.grid(row=5, column=0, columnspan=4)

    MList.bind('<Double-Button-1>', lambda event: selected(MList))
    WList.bind('<Double-Button-1>', lambda event: selected(WList))
    MList.bind("<Return>", lambda event: selected(MList))
    WList.bind("<Return>", lambda event: selected(WList))
    # --------------------------------------------

    win.mainloop()


def openwin3():
    global R, S, first, second, WifeHusband, MotherInlaw, last
    R = set()
    S = set()
    win = Tk()
    win.title('Вікно 3')
    win.geometry('1000x600')
    Mainread()
    def fillList():
        for k, i in enumerate(firstDict.keys()):
            AList.insert(k, i)
        for k, i in enumerate(secondDict.keys()):
            BList.insert(k, i)

    ChooseFrame = LabelFrame(win, labelanchor="n", font=font)
    ListFrame = LabelFrame(win, labelanchor="n", font=font)
    ChooseFrame.grid(row=0, column=0, padx=9, pady=9, sticky="nsew")
    ListFrame.grid(row=0, column=1, sticky="nsew", pady=9, padx=9)

    # Лейбл з виведенням множин
    AScroll = Scrollbar(ChooseFrame)
    AList = Listbox(ChooseFrame, font=font2)
    AScroll.config(command=AList.yview)
    AList.config(yscrollcommand=AScroll.set, selectmode="none")
    AText = Label(ChooseFrame, text="Множина А:")

    AText.grid(row=0, column=0, sticky="we", columnspan=2)
    AList.grid(row=1, column=0, sticky="NSEW")
    AScroll.grid(row=1, column=1, sticky="ns")

    BList = Listbox(ChooseFrame, font=font2, selectmode="none")  #
    BScroll = Scrollbar(ChooseFrame)  # Скролбар для списків
    BScroll.config(command=BList.yview)  #
    BList.config(yscrollcommand=BScroll.set)  #
    BText = Label(ChooseFrame, text="Множина В:")

    BText.grid(row=2, column=0, columnspan=2, sticky="we")
    BList.grid(row=3, column=0, sticky="NSEW")
    BScroll.grid(row=3, column=1, sticky="ns")
    fillList()


    # Лейбл графічного зображення

    SetText = Label(ListFrame, text="Графічне зображення відношень R та S ", font=21)
    SetText.grid(row=0, column=0, columnspan=4, pady=9, padx=18, sticky="we")
    women = set()
    men = set()
    MotherAndSon = set()
    WifeHusband, MotherInlaw = BinatyAttitudes.Atitudes(firstDict, secondDict, women, men, MotherAndSon)


    canvas1 = Canvas(ListFrame, width=1000, height=200)
    first = list(firstDict.keys())
    second = list(secondDict.keys())
    dictS1 = dict()
    dictS2 = dict()
    print("======= first then dict ======\n")
    print(first)
    print(firstDict)
    print("======= second, dict ======")
    print(second)
    print(secondDict)

    for i in range(len(first)):
        canvas1.create_text(30 + i * 74, 25, text=str(first[i]), font="Arial 10", anchor=CENTER)
        canvas1.create_oval([25 + i * 74, 32], [35 + i * 74, 42], fill="black")
        dictS1.update({first[i]: [30 + i * 74, 37]})
    last = 0
    for i in range(len(second)):
        last = 30 + i * 74
        canvas1.create_text(last, 175, text=str(second[i]), font="Arial 10", anchor=CENTER)
        canvas1.create_oval([25 + i * 74, 158], [35 + i * 74, 168], fill="black")
        dictS2.update({second[i]: [last, 163]})
    canvas1.config(width=last+30)

    for (i, j) in WifeHusband:
        if i in first and j in second:
            print(i, j)
            canvas1.create_line(dictS1[i], dictS2[j], arrow=LAST)
    canvas1.grid(row=1, column=0, columnspan=2)
    canvas2 = Canvas(ListFrame, width=last+30, height=200)
    dictR1 = dict()
    dictR2 = dict()
    for i in range(len(first)):
        last = 30 + i * 74
        canvas2.create_text(30 + i * 74, 25, text=str(list(first)[i]), font="Arial 10", anchor=CENTER)
        canvas2.create_oval([25 + i * 74, 32], [35 + i * 74, 42], fill="black")
        dictR1.update({first[i]: [30 + i * 74, 37]})
    for i in range(len(second)):
        last = 30 + i * 74
        canvas2.create_text(30 + i * 74, 175, text=str(second[i]), font="Arial 10", anchor=CENTER)
        canvas2.create_oval([25 + i * 74, 158], [35 + i * 74, 168], fill="black")
        dictR2.update({second[i]: [30 + i * 74, 163]})
    for (i, j) in MotherInlaw:
        if i in first and j in second:
            canvas2.create_line(dictR1[i], dictR2[j], arrow=LAST)
    canvas1.config(width=last + 30)
    canvas2.config(width=last+30)
    canvas2.grid(row=3, column=0, columnspan=2)

    win.geometry(f'{last+250}x600')
    win.mainloop()
def openwin4():
    win = Tk()
    win.title('Вікно 4')
    win.geometry(f'{last+30}x300')
    print(last)
    canvas1 = Canvas(win, width=last+30, height=200)
    dick1 = dict()
    dick2 = dict()
    for i in range(len(first)):
        canvas1.create_text(30 + i * 74, 25, text=str(first[i]), font="Arial 10", anchor=CENTER)
        canvas1.create_oval([25 + i * 74, 32], [35 + i * 74, 42], fill="black")
        dick1.update({first[i]: [30 + i * 74, 37]})
    for i in range(len(second)):
        canvas1.create_text(30 + i * 74, 175, text=str(second[i]), font="Arial 10", anchor=CENTER)
        canvas1.create_oval([25 + i * 74, 158], [35 + i * 74, 168], fill="black")
        dick2.update({second[i]: [30 + i * 74, 163]})
    canvas1.grid(row=2, column=0, columnspan=5)

    button1 = Button(win, width=5, text="R ∪ S", command=lambda: LogicalOperations.ownunite(canvas1, first, second, WifeHusband, MotherInlaw, dick1, dick2), font="Arial 14").grid(row=0, column=0, stick="we")
    button2 = Button(win, width=5, text="R ∩ S", command=lambda: LogicalOperations.ownintersect(canvas1, first, second, WifeHusband, MotherInlaw, dick1, dick2), font="Arial 14").grid(row=0, column=1, stick="we")
    button3 = Button(win, width=5, text="R \ S", command=lambda: LogicalOperations.owndiff(canvas1, first, second, WifeHusband, MotherInlaw, dick1, dick2), font="Arial 14").grid(row=0, column=2, stick="we")
    button4 = Button(win, width=5, text="U \ R", command=lambda: LogicalOperations.Udifference(canvas1, first, second, WifeHusband, MotherInlaw, dick1, dick2), font="Arial 14").grid(row=0, column=3, stick="we")
    button4 = Button(win, width=5, text="S^-1", command=lambda: LogicalOperations.inversing(canvas1, first, second, WifeHusband, MotherInlaw, dick1, dick2), font="Arial 14").grid(row=0, column=4, stick="we")

firstDict = {}
secondDict = {}
R = set()
S = set()

Names = {'Олександр': 'm', 'Володимир': 'm', 'Іван': 'm',
         'Михайло': 'm', 'Ярослав': 'm', 'Андрій': 'm',
         'Віктор': 'm', 'Роман': 'm', 'Олег': 'm',
         'Сергій': 'm', 'Денис': 'm', 'Василь': 'm',
         'Юрій': 'm', 'Павло': 'm', 'Тарас': 'm',
         'Оксана': "w", 'Людмила': "w", 'Ірина': "w",
         'Наталія': "w", 'Марія': "w", 'Олена': "w",
         'Тетяна': "w", 'Лариса': "w", 'Євгенія': "w",
         'Анна': "w", 'Юлія': "w", 'Вікторія': "w",
         'Світлана': "w", 'Катерина': "w", 'Іванна': "w"
         }

# --Шрифт та дизайн, константи--
font = ["Helvetica", 10, "bold"]
font2 = ["Calibri", 10]
background = "#ffffff"
buttonHeight = 4
buttonWidth = 32

# ----- Вікно 1 -----
root = Tk()
root.title('Головне вікно')
root.geometry('570x260')
root.resizable(width=False, height=False)

# Створення блоків
infoBox = LabelFrame(root, text='Інформація про студента', labelanchor="n", font=font)
calcBox = LabelFrame(root, text="Обрахунок варіанту", labelanchor='n', font=font)
winBox = LabelFrame(root, text="Навігація", labelanchor="n", font=font)

# Розміщення полів
winBox.grid(row=0, column=3, padx=20, pady=10, sticky="nswe", rowspan=2)
infoBox.grid(row=0, padx=20, pady=10, sticky="we", columnspan=2)
calcBox.grid(row=1, column=0, padx=20, pady=10, sticky="we", columnspan=2)

# Інформація про студента
infoText = Label(infoBox, text="Бережанський\nДанііл\nВадимович\nГрупа - ІО-24, номер - 1".format(info()),
                 font=("Helvetica", 13), justify=LEFT)
infoText.grid(row=1, column=1, padx=10, pady=10, sticky="we")

# Обрахунок варіанту
calcText = Label(calcBox, text="(1 + 24 % 60) % 30 + 1 = {0!s}".format(info()), font=["Calibri", 13])
calcText.grid(row=0, column=0, pady=19, padx=20, sticky="nsew")

# Поле кнопок-вікон
winB2 = Button(winBox, text="Відкрити вікно №2", height=buttonHeight, width=buttonWidth, command=openwin2,
               state=NORMAL, font=font2)
winB3 = Button(winBox, text="Відкрити вікно №3", height=buttonHeight, width=buttonWidth, command=openwin3,
               state=NORMAL, font=font2)
winB4 = Button(winBox, text="Відкрити вікно №4", height=buttonHeight, width=buttonWidth, command=openwin4,
               state=NORMAL, font=font2)

winB2.grid(row=0, column=0, padx=5, pady=1, sticky="nsew")
winB3.grid(row=1, column=0, padx=5, pady=3, sticky="nsew")
winB4.grid(row=2, column=0, padx=5, pady=1, sticky="nsew")

root.mainloop()
