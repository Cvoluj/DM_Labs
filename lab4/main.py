from tkinter import *
import csv
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

## Константи
font = ["Helvetica", 10, "bold"]
font2 = ["Calibri", 10]
background = "#ffffff"
buttonHeight = 2
buttonWidth = 16
rect_size = 27
edges = []
matrix_of_sum = []
filename1 = 'edges.csv'


class Check:
    instances = []

    def __init__(self, row, column, edgesBox):
        Check.instances.append(self)
        self.check = Entry(edgesBox, width=3, font=font)
        self.check.grid(row=row, column=column)
        self.check.bind("<Button-1>", self.limiter)
        self.check.bind("<Return>", self.get_all_instances_add_edge)
        self.check.insert(END, "0")

    def get(self):
        return self.check.get()

    def get_all(event=None):
        return [instance.get() for instance in Check.instances]

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

    @staticmethod
    def get_all_instances_add_edge(self, event=None):
        add_edge()


class Graph:
    def __init__(self, adjacency_matrix, graph_label):
        self.adjacency_matrix = adjacency_matrix
        self.num_nodes = len(adjacency_matrix)
        self.degree_array = [0] * self.num_nodes
        self.sort_array = list(range(self.num_nodes))
        self.color_array = [0] * self.num_nodes
        self.graph = nx.Graph()
        self.color_map = []
        self.graph_label = graph_label

        self.process_graph()
        self.colorize_nodes()
        self.draw_graph()

    def process_graph(self):
        print("Матриця суміжності")
        for row in self.adjacency_matrix:
            print(row)
        print("======")
        print("Відлагодження".center(50))

        for i in range(self.num_nodes):
            self.degree_array[i] = sum(self.adjacency_matrix[i])

        self.sort_nodes()
        print("Відсортований:", self.sort_array)
        print("За спаданням:", self.degree_array)

    def sort_nodes(self):
        for k in range(self.num_nodes):
            max_loc = self.degree_array[k]
            c = k
            for i in range(k + 1, self.num_nodes):
                if self.degree_array[i] > max_loc:
                    c = i
            self.degree_array[c], self.degree_array[k] = self.degree_array[k], self.degree_array[c]
            self.sort_array[c], self.sort_array[k] = self.sort_array[k], self.sort_array[c]

    def check_dop(self, node):
        for j in range(self.num_nodes):
            if self.adjacency_matrix[j][node] == 1 and self.color_array[j] == self.current_color:
                return False
        return True

    def colorize_nodes(self):
        self.current_color = 1
        for n in range(self.num_nodes):
            if self.color_array[self.sort_array[n]] == 0:
                self.color_array[self.sort_array[n]] = self.current_color
                self.color_node(self.sort_array[n])
                self.current_color += 1
                print(str(self.color_array) + "- Крок: ", n)

        for i in range(self.num_nodes):
            self.color_map.append(self.color_array[i])

        colorized = [[i+1, self.color_array[i]] for i in range(self.num_nodes)]
        print("======Результат: [вершина, колір]======")
        print(colorized)
        print("\nВідсортований:", self.sort_array)
        print("За спаданням:", self.degree_array)
        print("Кольоровий:", self.color_array)

    def color_node(self, node):
        for j in range(self.num_nodes):
            if self.adjacency_matrix[j][node] == 0 and self.color_array[j] == 0 and self.check_dop(j):
                self.color_array[j] = self.current_color

    def draw_graph(self):
        self.graph.clear()
        for i in range(self.num_nodes):
            self.graph.add_node(i)

        edges_coloring = []
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                if self.adjacency_matrix[i][j] == 1:
                    edges_coloring.append((i+1, j+1))
        print(edges_coloring)
        self.graph.add_edges_from(edges_coloring)
        figure = plt.Figure(figsize=(4, 3))
        ax = figure.add_subplot(111)
        pos = nx.spring_layout(self.graph)
        self.graph.remove_node(0)
        node_colors = [f"C{i}" for i in self.color_array]
        nx.draw(self.graph, pos, with_labels=True, node_color=node_colors, font_color='white', ax=ax)

        canvas = FigureCanvasTkAgg(figure, master=graphLabel)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)



def variant_window():
    win = Tk()
    win.title('Інформація про студента')
    win.geometry('250x200')
    myInfo = LabelFrame(win)
    infoText = Label(myInfo, text="Бережанський\nДанііл\nВадимович\nГрупа - ІО-24, номер - 1",
                     font=("Helvetica", 13), justify=LEFT)
    infoText.grid(row=0, column=0, padx=10, sticky="nsew")
    myInfo.grid(row=0, column=0, padx=20, pady=10, sticky="we")
    calcVariant = LabelFrame(win, text="Обрахунок варіанту", labelanchor="n", font=font2)
    calcText = Label(calcVariant, text="(2401 % 10) + 1 = {0!s}".format((2401 % 10) + 1), font=["Helvetica", 13])
    calcText.grid(row=0, column=0, padx=10, sticky="we")
    calcVariant.grid(row=1, column=0, padx=20, pady=10, sticky="nswe")
    win.mainloop()


def save_file(filename, edges):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in edges:
            writer.writerow(row)

    print(f'{len(edges)} rows saved to {filename}.')


def read_file(filename):
    global edges
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        edges = []
        for row in reader:
            edges.append(list(map(int, row)))
    firstList.delete(0, END)
    for row in edges:
        firstList.insert(END, f"({row[0]}, {row[1]})")
    print(edges)


def add_edge():
    vertex_list = Check.get_all()
    vertex1 = int(vertex_list[0])
    vertex2 = int(vertex_list[1])

    if [vertex1, vertex2] not in edges and vertex2 != 0 and vertex1 != 0:
        edges.append([vertex1, vertex2])
        firstList.insert(firstList.size(), f"({vertex1}, {vertex2})")
    else:
        pass
    print(edges)


def form_matrix():
    global matrix_of_sum
    nodes = set()
    matrix_of_sum = []

    for i in edges:
        nodes.add(i[0])
        nodes.add(i[1])
        print(nodes)
    nodesList = sorted(list(nodes))
    sumMatrix = Canvas(sumLabel, width=len(nodes) * rect_size, height=len(nodes) * rect_size)
    sumMatrix.grid(row=1, column=1)
    rowLabels = Canvas(sumLabel, width=rect_size, height=len(nodes) * rect_size)
    rowLabels.grid(row=1, column=0)
    colLabels = Canvas(sumLabel, width=len(nodes) * rect_size, height=rect_size)
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
        matrix_of_sum.append(row)
    formGraph.configure(state=NORMAL)
    print("Матриця сумісності:")
    print(matrix_of_sum)


def color_graph():
    global graphLabel
    graphLabel.destroy()
    graph_label_create()
    Graph(matrix_of_sum, graphLabel)


def button_label():
    global formGraph
    buttonLabel = LabelFrame(root, labelanchor="n", text="Меню", font=font)
    buttonLabel.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky="nswe")
    formMatrix = Button(buttonLabel, text="Сформувати матрицю", height=buttonHeight, width=buttonWidth+2,
                        command=form_matrix,
                        state=NORMAL, font=font2)
    saveFile = Button(buttonLabel, text="Зберегти у файл", height=buttonHeight, width=buttonWidth,
                      command=lambda: save_file(filename1, edges), state=NORMAL, font=font2)
    readFile = Button(buttonLabel, text="Зчитати з файлу", height=buttonHeight, width=buttonWidth,
                      command=lambda: read_file(filename1), state=NORMAL, font=font2)
    studentInfo = Button(buttonLabel, text="Інформація про студента", height=buttonHeight, width=buttonWidth + 6,
                         command=variant_window,
                         state=NORMAL, font=font2)
    formGraph = Button(buttonLabel, text="Розфабрувати граф", height=buttonHeight, width=buttonWidth, command=color_graph,
                       state=DISABLED, font=font2)

    formMatrix.grid(row=0, column=0, padx=3, pady=3)
    saveFile.grid(row=0, column=2, padx=3, pady=3)
    readFile.grid(row=0, column=3, padx=3, pady=3)
    studentInfo.grid(row=0, column=4, padx=3, pady=3)
    formGraph.grid(row=0, column=1, padx=3, pady=3)


def edges_entry_label():
    global firstList
    edgesLabel = LabelFrame(root, text="Введення ребер", labelanchor='n', font=font)
    edgesLabel.grid(row=1, column=0, rowspan=2, padx=20, pady=20, sticky="nsew")
    Check(0, 1, edgesLabel)
    Check(0, 3, edgesLabel)
    scroll = Scrollbar(edgesLabel)
    scroll.grid(row=1, column=3, sticky="ns")
    firstList = Listbox(edgesLabel, yscrollcommand=scroll.set)
    scroll.config(command=firstList.yview)
    firstList.grid(row=1, column=0, columnspan=3, sticky="nswe")
    firstSideLabel = Label(edgesLabel, text="1 вершина", font=font2)
    secondSideLabel = Label(edgesLabel, text="2 вершина", font=font2)
    addEdgeButton = Button(edgesLabel, font=font2, text="Додати ребро", height=2, width=buttonWidth,
                           command=add_edge,
                           state=NORMAL)
    addEdgeButton.grid(row=2, column=0, columnspan=3)
    firstSideLabel.grid(row=0, column=0)
    secondSideLabel.grid(row=0, column=2)


def matrix_sum_label():
    global sumLabel
    sumLabel = LabelFrame(root, text="Матриця суміжності", labelanchor="n", font=font)
    sumLabel.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky="nsew")


def graph_label_create():
    global graphLabel
    graphLabel = LabelFrame(root, text="Розфабрований граф", labelanchor="n", font=font)
    graphLabel.grid(row=3, columnspan=3, column=0, pady=10, padx=20, sticky="nsew")


root = Tk()
root.title('Головне вікно')
root.geometry('1200x1280')

root.resizable(width=False, height=False)
button_label()
edges_entry_label()
matrix_sum_label()
graph_label_create()

root.mainloop()
