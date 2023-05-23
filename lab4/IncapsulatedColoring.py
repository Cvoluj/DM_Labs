import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix
        self.num_nodes = len(adjacency_matrix)
        self.degree_array = [0] * self.num_nodes
        self.sort_array = list(range(self.num_nodes))
        self.color_array = [0] * self.num_nodes
        self.graph = nx.Graph()
        self.color_map = []

        self.process_graph()
        self.colorize_nodes()
        self.draw_graph()

    def process_graph(self):
        print("==Матрица Смежности==")
        for row in self.adjacency_matrix:
            print(row)
        print("====")
        print("Отладка".center(50))

        for i in range(self.num_nodes):
            self.degree_array[i] = sum(self.adjacency_matrix[i])

        self.sort_nodes()
        print("SortNodes res:", self.sort_array)
        print("Degree Array res:", self.degree_array)

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
                print(str(self.color_array) + "- Итерация: ", n)

        for i in range(self.num_nodes):
            self.color_map.append(self.color_array[i])

        colorized = [[i, self.color_array[i]] for i in range(self.num_nodes)]
        print("======Результат: [вершина, цвет]======")
        print(colorized)
        print("\nSortArr:", self.sort_array)
        print("Degree Array:", self.degree_array)
        print("Color Array:", self.color_array)

    def color_node(self, node):
        for j in range(self.num_nodes):
            if self.adjacency_matrix[j][node] == 0 and self.color_array[j] == 0 and self.check_dop(j):
                self.color_array[j] = self.current_color

    def draw_graph(self):
        for i in range(self.num_nodes):
            self.graph.add_node(i)

        edges = []
        for i in range(self.num_nodes):
            for j in range(i+1, self.num_nodes):
                if self.adjacency_matrix[i][j] == 1:
                    edges.append((i+1, j+1))
        print(self.color_map)
        self.graph.add_edges_from(edges)
        self.graph.remove_node(0)
        nx.draw(self.graph, node_color=self.color_map, with_labels=True, font_color='white')
        plt.axis('off')
        plt.show()

            # Usage

A =[[0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

graph = Graph(A)

