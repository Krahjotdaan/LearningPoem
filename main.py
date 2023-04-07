from PyQt5 import QtWidgets
from converted_uis import MainWindow
import sys

def main():       
    class mainWindow(QtWidgets.QMainWindow):
        def __init__(self):
            super(mainWindow, self).__init__()
            self.ui = MainWindow()
            self.ui.setupUi(self)
    
    
    app = QtWidgets.QApplication([])
    application = mainWindow()
    application.show()
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
