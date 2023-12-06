from PyQt5.QtWidgets import QApplication, QWidget
import sys
import window

app = QApplication(sys.argv)
main_window = window.Window()
main_window.show()

app.exec()