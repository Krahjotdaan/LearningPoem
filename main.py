from PyQt5 import QtWidgets
from converted_uis.MainWindow import *
from converted_uis.AboutProgramForm import *
from converted_uis.LibraryForm import *
from converted_uis.MethodologyForm import *
from converted_uis.VerseCreationForm import *
from converted_uis.VerseEditForm import *
from converted_uis.VerseOpenForm import *
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def new_verse_button_clicked(self):
        self.close()
        self.verseCreationWindow = VerseCreationWindow()
        self.verseCreationWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.verseCreationWindow.show()

    def library_button_clicked(self):
        self.close()
        self.libraryWindow = LibraryWindow()
        self.libraryWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.libraryWindow.show()

    def methodology_button_clicked(self):
        self.close()
        self.methodologyWindow = MethodologyWindow()
        self.methodologyWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.methodologyWindow.show()

    def about_programm_button_clicked(self):
        self.close()
        self.aboutProgramWindow = AboutProgramWindow()
        self.aboutProgramWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.aboutProgramWindow.show()

    def exit_button_clicked(self):
        sys.exit()


class VerseCreationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(VerseCreationWindow, self).__init__()
        self.ui = Ui_VerseCreationForm()
        self.ui.setupUi(self)

    def add_verse_button_clicked(self):
        if self.ui.title.text() is not None and self.ui.author.text() is not None \
            and self.ui.verse_text.toPlainText() is not None:
            fileTitle = str(self.ui.title.text()) + ', ' + str(self.ui.author.text())
            with open(f"verses/{fileTitle}.txt", "w") as fl:
                fl.write(self.ui.verse_text.toPlainText())

            self.ui.title.setText("")
            self.ui.author.setText("")
            self.ui.verse_text.setText("")

    def back_button_clicked(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.mainWindow.show()
        

class VerseEditWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(VerseEditWindow, self).__init__()
        self.ui = Ui_VerseEditForm()
        self.ui.setupUi(self)   
        print(str(self.ui.title.text()) + ', ' + str(self.ui.author.text()))

    def edit_button_clicked(self):
        if self.ui.title.text() is not None and self.ui.author.text() is not None and \
            self.ui.verse_text.toPlainText() is not None:
            newFileTitle = str(self.ui.title.text()) + ', ' + str(self.ui.author.text())
            os.rename(f"verses/{self.ui.filetitle}.txt", f"verses/{newFileTitle}.txt")
            with open(f"verses/{newFileTitle}.txt", "w") as fl:
                fl.write(self.ui.verse_text.toPlainText())
                
                
        self.close()
        self.mainWindow = LibraryWindow()
        self.mainWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.mainWindow.show()

    def back_button_clicked(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.mainWindow.show()


class VerseOpenWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(VerseOpenWindow, self).__init__()
        self.ui = Ui_VerseOpenForm()
        self.ui.setupUi(self)

    def back_button_clicked(self):
        self.close()
        self.mainWindow = LibraryWindow()
        self.mainWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.mainWindow.show()


class LibraryWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LibraryWindow, self).__init__()
        self.ui = Ui_LibraryForm()
        self.ui.setupUi(self)

    def open_button_clicked(self):
        for verse in self.ui.verses:
            if verse.isChecked() is True:
                self.close()
                self.verseOpenWindow = VerseOpenWindow()
                self.verseOpenWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)             
                with open(f"verses/{verse.text()}.txt", "r") as fl:
                    versetext = fl.read()
                
                versetext = list(filter(None, versetext.split('\n')))
                vrstxt = ""
                for i in range(len(versetext)):
                    vrstxt += str(versetext[i])
                    vrstxt += '\n'
                    if (i + 1) % 4 == 0 and i != 0:
                        vrstxt += '\n'

                self.verseOpenWindow.ui.titleAndAuthorLabel.setText(verse.text())
                self.verseOpenWindow.ui.verseText.setText(vrstxt)
                
                self.verseOpenWindow.show()
                
    def edit_button_clicked(self):
        for verse in self.ui.verses:
            if verse.isChecked() is True:
                self.close()
                self.verseEditWindow = VerseEditWindow()
                self.verseEditWindow.setAttribute(
                    QtCore.Qt.WA_DeleteOnClose, True)
                with open(f"verses/{verse.text()}.txt", "r") as fl:
                    versetext = fl.read()

                versetext = list(filter(None, versetext.split('\n')))
                vrstxt = ""
                for i in range(len(versetext)):
                    vrstxt += str(versetext[i])
                    vrstxt += '\n'
                    if (i + 1) % 4 == 0 and i != 0:
                        vrstxt += '\n'

                title_and_author = list(verse.text().split(', '))
                self.verseEditWindow.ui.title.setText(title_and_author[0])
                self.verseEditWindow.ui.author.setText(title_and_author[1])
                self.verseEditWindow.ui.verse_text.setText(vrstxt)
                self.verseEditWindow.ui.filetitle = verse.text()
                self.verseEditWindow.show()

    def delete_button_clicked(self):
        pass

    def back_button_clicked(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.mainWindow.show()


class MethodologyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MethodologyWindow, self).__init__()
        self.ui = Ui_MethodologyForm()
        self.ui.setupUi(self)

    def back_button_clicked(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.mainWindow.show()


class AboutProgramWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AboutProgramWindow, self).__init__()
        self.ui = Ui_AboutProgramForm()
        self.ui.setupUi(self)

    def back_button_clicked(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.mainWindow.show()


def main():       
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    application.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
