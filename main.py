from PyQt5.QtWidgets import QMainWindow, QApplication
from converted_uis.MainWindow import Ui_MainWindow
import sys


def main():

    class Application(QMainWindow, Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)

    app = QApplication(sys.argv)
    main_window = Application()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
