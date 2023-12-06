import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

import tap_access

# Main Window
class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        self.list = QListWidget()
        self.list_button = QPushButton("Get Tables")
        self.list_button.clicked.connect(self.get_tables)

        root_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.toolbar)
        left_layout.addWidget(self.canvas)
        left_layout.addWidget(self.button)

        root_layout.addLayout(left_layout)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.list)
        right_layout.addWidget(self.list_button)

        root_layout.addLayout(right_layout)


        # setting layout to the main window
        self.setLayout(root_layout)


    def get_tables(self):
        tables = tap_access.get_available_tables()
        for table in tables:
            self.list.addItem(table["table_name"])


    def plot(self):
        data = tap_access.get_planetary_data("select ra,dec from ps where default_flag = 1 and pl_controv_flag = 0 order by ra,dec desc")
        self.figure.clear()

        ax = self.figure.add_subplot()
        ax.set_xlabel("dec")
        ax.set_ylabel("ra")

        ax.plot(data["dec"], data["ra"], 'r.')
        self.canvas.draw()

