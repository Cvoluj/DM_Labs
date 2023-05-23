from tkinter import *
import csv
import networkx as nx
import matplotlib.pyplot as plt

class Check:
    def __init__(self, row, column):
        self.check = Entry(edgesBox, width=3, font=font)
        self.check.grid(row=row, column=column)
        self.check.bind("<Button-1>", self.limiter)
        self.check.bind("<Return>", self.addEdge)
        self.check.insert(END, "0")

    def get(self):
        return self.check.get()

    def limiter(self, event):
        if self.check.get() == "10":
            self.check.delete(0, END)
            self.check.insert(END, "0")
        elif self.check.get():
            if self.check.get().isdigit():
                n = int(self.check.get())
            else:
                n = -1
            self.check.delete(0, END)
            self.check.insert(END, str(n+1))



    def addEdge(self, second):
        vertex1 = int(firstSideEntry.get())
        vertex2 = int(secondSideEntry.get())
        if [vertex1, vertex2] not in edges and vertex2 != 0 and vertex1 != 0:
            edges.append([vertex1, vertex2])
            firstList.insert(firstList.size(), f"({vertex1}, {vertex2})")
        else:
            pass
        print(edges)


def addEdge():
    vertex1 = int(firstSideEntry.get())
    vertex2 = int(secondSideEntry.get())
    if [vertex1, vertex2] not in edges and vertex2 != 0 and vertex1 != 0:
        edges.append([vertex1, vertex2])
        firstList.insert(END, f"({vertex1}, {vertex2})")
    print(edges)


def saveInFile(filename, edges):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in edges:
            writer.writerow(row)

    print(f'{len(edges)} rows saved to {filename}.')


def readFromFile(filename):
    global edges
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        edges = []
        for row in reader:
            edges.append(list(map(int, row)))
        print(edges)
    firstList.delete(0, END)
    addEdgeFromRead()


def addEdgeFromRead():
    for row in edges:
        firstList.insert(END, f"({row[0]}, {row[1]})")


def formMatrixs():
    global edges, rect_size, matrixOfSum, matrixOfInd, nodesList
    nodes = set()
    matrixOfSum = []

    for i in edges:
        nodes.add(i[0])
        nodes.add(i[1])
        print(nodes)
    nodesList = sorted(list(nodes))
    sumMatrix = Canvas(sumBox, width=len(nodes) * rect_size, height=len(nodes) * rect_size)
    sumMatrix.grid(row=1, column=1)
    rowLabels = Canvas(sumBox, width=rect_size, height=len(nodes) * rect_size)
    rowLabels.grid(row=1, column=0)
    colLabels = Canvas(sumBox, width=len(nodes) * rect_size, height=rect_size)
    colLabels.grid(row=0, column=1)

    for i, node1 in enumerate(nodesList, start=0):
        row = []
        rowLabels.create_text(rect_size / 2, i * rect_size + rect_size / 2, text=str(node1))
        for j, node2 in enumerate(nodesList, start=0):
            colLabels.create_text(j * rect_size + rect_size / 2, rect_size / 2, text=str(node2))
            if [node1, node2] in edges:
                print(node1, node2)
                text = "1"
                row.append(1)
            else:
                text = "0"
                row.append(0)
            sumMatrix.create_rectangle(j * rect_size, i * rect_size, (j + 1) * rect_size, (i + 1) * rect_size,
                                       fill="white")
            sumMatrix.create_text(j * rect_size + rect_size / 2, i * rect_size + rect_size / 2, text=text)
        matrixOfSum.append(row)
    formGraph.configure(state=NORMAL)
    print("Матриця сумісності:")
    print(matrixOfSum)

    indMatrix = Canvas(incidentBox, width=len(edges) * rect_size, height=len(nodes) * rect_size)
    indMatrix.grid(row=1, column=1)
    indRowLabels = Canvas(incidentBox, width=rect_size, height=len(nodes) * rect_size)
    indRowLabels.grid(row=1, column=0)
    indColLabels = Canvas(incidentBox, width=len(edges) * rect_size, height=rect_size)
    indColLabels.grid(row=0, column=1)

    for i, node in enumerate(nodesList):
        row = []
        indRowLabels.create_text(rect_size / 2, i * rect_size + rect_size / 2, text=str(node))
        for j, edge in enumerate(edges):
            indColLabels.create_text(j * rect_size + rect_size / 2, rect_size / 2, text=f"a{j+1}")
            indMatrix.create_rectangle(j * rect_size, i * rect_size, (j + 1) * rect_size, (i + 1) * rect_size,
                                       fill="white")
            if node == edge[0] and node == edge[1]:
                row.append(2)

                text ='±1'
            elif node == edge[0]:
                text = '+1'
                row.append(1)
            elif node == edge[1]:
                text = '-1'
                row.append(-1)
            else:
                text = '0'
                row.append(0)
            indMatrix.create_text(j * rect_size + rect_size / 2, i * rect_size + rect_size / 2, text=text)
        matrixOfInd.append(row)
    print("Матриця інцидентності")
    for i in matrixOfInd:
        print(i)


def formGraphx():
    global nodesList
    G1 = nx.DiGraph()
    for i, node in enumerate(nodesList):
        for j in range(0, len(matrixOfSum)):
            if matrixOfSum[i][j] == 1:
                G1.add_edge(node, j + 1)

    # create graph from matrixOfInd
    G2 = nx.DiGraph()

    matrix_transpose = list(map(list, zip(*matrixOfInd)))
    for i in range(0, len(matrix_transpose)):
        checkOrient = False
        isStart = False
        isFinish = False
        nodeRemebeber = 0
        edge = [0, 0]
        for j, node in enumerate(nodesList):
            value = matrix_transpose[i][j]
            if value == 2:
                G2.add_edge(node, node)
                nodeCheck = node
                checkOrient = True
            if value == 1:
                edge[0] = node
            if value == -1:
                edge[1] = node
            if checkOrient:
                if edge[0] != 0:
                    G2.add_edge(edge[0], nodeRemebeber)
                    checkOrient = False
                if edge[1] != 0:
                    G2.add_edge(nodeRemebeber, edge[1])
                    checkOrient = False
            if edge[0] != 0 and edge[1] != 0:
                G2.add_edge(edge[0], edge[1])





    # plot graphs
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    nx.draw(G1, ax=ax1, with_labels=True)

    ax1.set_title('Граф матриці суміжності')

    nx.draw(G2, ax=ax2, with_labels=True)
    ax2.set_title('Граф матриці інцидентності')

    plt.show()


def info():
    I = (2401 % 10) + 1
    return I

def variant():
    win = Tk()
    win.title('Інформація про студента')
    win.geometry('250x200')
    myInfo = LabelFrame(win)
    infoText = Label(myInfo, text="Бережанський\nДанііл\nВадимович\nГрупа - ІО-24, номер - 1",
                     font=("Helvetica", 13), justify=LEFT)
    infoText.grid(row=0, column=0, padx=10, sticky="nsew")
    myInfo.grid(row=0, column=0, padx=20, pady=10, sticky="we")
    calcVariant = LabelFrame(win, text="Обрахунок варіанту", labelanchor="n", font=font2)
    calcText = Label(calcVariant, text="(2401 % 10) + 1 = {0!s}".format(info()), font=["Helvetica", 13])
    calcText.grid(row=0, column=0, padx=10, sticky="we")
    calcVariant.grid(row=1, column=0, padx=20, pady=10, sticky="nswe")
    win.mainloop()


# --Шрифт та дизайн, константи--
font = ["Helvetica", 10, "bold"]
font2 = ["Calibri", 10]
background = "#ffffff"
buttonHeight = 2
buttonWidth = 16
rect_size = 27

# ----- Вікно 1 -----
root = Tk()
root.title('Головне вікно')
root.geometry('900x1280')
root.resizable(width=False, height=False)

# Створення блоків
buttonBox = LabelFrame(root, labelanchor="n",text="Меню", font=font)
edgesBox = LabelFrame(root, text="Введення ребер", labelanchor='n', font=font)
incidentBox = LabelFrame(root, text="Матриця інцидентності", labelanchor="n", font=font)
sumBox = LabelFrame(root, text="Матриця суміжності", labelanchor="n", font=font)
buttonBox.grid(row=0, column=0, columnspan=3,padx=20, pady=10, sticky="nswe")
edgesBox.grid(row=1, column=0, rowspan=2, padx=20, pady=20, sticky="nsew")
incidentBox.grid(row=3, columnspan=3, column=0, pady=10, padx=20, sticky="nsew")
sumBox.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky="nsew" )

# Поле кнопок-вікон
formMatrix = Button(buttonBox, text="Сформувати матриці", height=buttonHeight, width=buttonWidth, command=formMatrixs,
               state=NORMAL, font=font2)
saveFile = Button(buttonBox, text="Зберегти у файл", height=buttonHeight, width=buttonWidth,
                  command=lambda: saveInFile(filename1, edges),state=NORMAL, font=font2)
readFile = Button(buttonBox, text="Зчитати з файлу", height=buttonHeight, width=buttonWidth,
                  command=lambda: readFromFile(filename1), state=NORMAL, font=font2)
studentInfo = Button(buttonBox, text="Інформація про студента", height= buttonHeight, width=buttonWidth+6, command=variant,
                     state=NORMAL, font=font2)
formGraph = Button(buttonBox, text="Сформувати графи", height=buttonHeight, width=buttonWidth, command=formGraphx,
               state=DISABLED, font=font2)
formMatrix.grid(row=0, column=0, padx=3, pady=3)
saveFile.grid(row=0, column=2, padx=3, pady=3)
readFile.grid(row=0, column=3, padx=3, pady=3)
studentInfo.grid(row=0, column=4, padx=3, pady=3)
formGraph.grid(row= 0, column=1, padx=3, pady=3)

# --------Введення ребер---------
filename1 = 'edges.csv'
addEdgeButton = Button(edgesBox, font=font2, text="Додати ребро", height=2, width=buttonWidth, command=addEdge,
                       state=NORMAL)
addEdgeButton.grid(row=2, column=0, columnspan=3)
scroll = Scrollbar(edgesBox)
scroll.grid(row=1, column=3, sticky="ns")
firstList = Listbox(edgesBox, yscrollcommand=scroll.set)
scroll.config(command=firstList.yview)
firstList.grid(row=1, column=0,columnspan=3, sticky="nswe")

firstSideLabel = Label(edgesBox, text="1 вершина", font=font2)
secondSideLabel = Label(edgesBox, text="2 вершина", font=font2)
firstSideEntry = Check(0, 1)
secondSideEntry = Check(0, 3)

firstSideLabel.grid(row=0, column=0)
secondSideLabel.grid(row=0, column=2)
edges = []
matrixOfSum = []
matrixOfInd = []


root.mainloop()
