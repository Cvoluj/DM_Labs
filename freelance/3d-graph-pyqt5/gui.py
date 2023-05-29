from sys import argv
from calculations3d import get_plot_values

from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QVBoxLayout, QFormLayout, QMessageBox, QGridLayout
from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111, projection='3d')
        super(MplCanvas, self).__init__(fig)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        layout = QHBoxLayout()

        # Plot layout -----------------------------------------
        plot_layout = QVBoxLayout()
        self.plot = MplCanvas(self, width=5, height=4, dpi=100)
        toolbar = NavigationToolbar(self.plot, self)

        plot_layout.addWidget(self.plot)
        plot_layout.addWidget(toolbar)

        # Settings layout -----------------------------------------
        settings_layout = QGridLayout()

        metal_layout = QVBoxLayout()
        self.metal_gb = QGroupBox("Метал")
        self.metal_gb.setMaximumHeight(120)
        self.metal_rb = (QRadioButton("Сталь"), QRadioButton("Мідь"), QRadioButton("Алюміній"))
        self.metal_rb[0].setChecked(True)
        [metal_layout.addWidget(rb, alignment=Qt.AlignTop) for rb in self.metal_rb]
        self.metal_gb.setLayout(metal_layout)

        constants_layout = QFormLayout()
        self.delta0_edit = QLineEdit()
        self.Bi_edit = QLineEdit()
        self.H_0_edit = QLineEdit()
        self.h_edit = QLineEdit()
        self.d_edit = QLineEdit()
        self.n_edit = QLineEdit()
        self.delta0_edit.setMinimumWidth(150)
        self.Bi_edit.setMinimumWidth(150)
        self.H_0_edit.setMinimumWidth(150)
        self.h_edit.setMinimumWidth(150)
        self.d_edit.setMinimumWidth(150)
        self.n_edit.setMinimumWidth(150)

        # Стандартні значення
        self.delta0_edit.setText("1")
        self.Bi_edit.setText("0.3")
        self.H_0_edit.setText("1.0")
        self.h_edit.setText("2")
        self.d_edit.setText("2")
        self.n_edit.setText("100")

        constants_layout.addRow(QLabel("delta0"), self.delta0_edit)
        constants_layout.addRow(QLabel("Bi"), self.Bi_edit)
        constants_layout.addRow(QLabel("H_0"), self.H_0_edit)
        constants_layout.addRow(QLabel("h"), self.h_edit)
        constants_layout.addRow(QLabel("d"), self.d_edit)
        constants_layout.addRow(QLabel("n"), self.n_edit)

        plot_button = QPushButton("Нарисувати графік")
        plot_button.clicked.connect(self.draw_graph)
        settings_layout.addWidget(self.metal_gb, 1, 1, 1, 2)
        settings_layout.addLayout(constants_layout, 2, 1)
        settings_layout.addWidget(plot_button, 5, 1, 1, 2, alignment=Qt.AlignTop)
        layout.addLayout(plot_layout, stretch=6)
        layout.addLayout(settings_layout, stretch=1)

        self.setLayout(layout)
        self.resize(900, 600)
        self.setWindowTitle("3d графік")
        self.show()

    def show_error(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Помилка!")
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setIcon(QMessageBox.Critical)

        msg.exec_()

    def get_checked_rb(self):
        for rb in self.metal_rb:
            if rb.isChecked():
                return rb

    def draw_graph(self):
        metal = self.get_checked_rb()

        delta0 = self.delta0_edit.text()
        Bi = self.Bi_edit.text()
        H_0 = self.H_0_edit.text()
        h = self.h_edit.text()
        d = self.d_edit.text()
        n = self.n_edit.text()

        arguments = (delta0, Bi, H_0, h, d, n)

        float_arguments = []

        # Валідація значень аргументів
        if metal is None:
            self.show_error("Виберіть метал!")
            return
        else:
            metal = metal.text()

        for arg in arguments:
            try:
                float_arguments.append(float(arg))
            except ValueError:
                self.show_error(f"Некоректне значення числового аргументу: {arg}")
                return

        X1, X2, Z = get_plot_values(metal, *float_arguments)
        print(Z)
        self.plot.axes.cla()

        self.plot.axes.set_xlabel('x1')
        self.plot.axes.set_ylabel('x3')
        self.plot.axes.set_zlabel('T')
        self.plot.axes.set_title('3D plot of T(x1, x2, F0)')
        self.plot.axes.plot_trisurf(X1.flatten(), X2.flatten(), Z.flatten(), cmap='viridis', edgecolor='none')
        self.plot.draw()


app = QApplication(argv)
w = MainWindow()
app.exec_()
