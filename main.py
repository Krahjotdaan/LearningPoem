import os
from PyQt5 import QtWidgets
from converted_uis.MainWindow import *
from converted_uis.AboutProgramForm import *
from converted_uis.LibraryForm import *
from converted_uis.MethodologyForm import *
from converted_uis.VerseCreationForm import *
from converted_uis.VerseEditForm import *
from converted_uis.VerseOpenForm import *
from methods.first_word import *
from methods.first_and_last_word import *
from methods.quatrains import *
from methods.lines import *
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

    def apply_button_clicked(self): 
        try:           
            if self.ui.quatrains.text() == "" and self.ui.strings.text() != "":
                tmp = lines(self.ui.vt, self.ui.strings.text())
                self.ui.verseText.setText(tmp)
                self.ui.vt = self.ui.VERSETEXT

            if self.ui.strings.text() == "" and self.ui.quatrains.text() != "":
                tmp = quatrains(self.ui.vt, self.ui.quatrains.text())
                self.ui.verseText.setText(tmp)
                self.ui.vt = self.ui.VERSETEXT

            if self.ui.strings.text() != "" and self.ui.quatrains.text() != "":
                tmp = lines(self.ui.vt, self.ui.strings.text())
                tmp = quatrains(tmp, self.ui.quatrains.text())
                self.ui.verseText.setText(tmp)
                self.ui.vt = self.ui.VERSETEXT

            if self.ui.strings.text() == "" and self.ui.quatrains.text() == "":
                self.ui.verseText.setText(self.ui.vt)
        
        except ValueError:
            pass

    def apply_button2_clicked(self):
        try:
            if self.ui.quatrains_2.text() == "" and self.ui.strings_2.text() != "":
                tmp = lines(self.ui.vt2, self.ui.strings_2.text())
                self.ui.verseText_2.setText(tmp)
                self.ui.vt2 = self.ui.VERSETEXT2

            if self.ui.strings_2.text() == "" and self.ui.quatrains_2.text() != "":
                tmp = quatrains(self.ui.vt2, self.ui.quatrains_2.text())
                self.ui.verseText_2.setText(tmp)
                self.ui.vt2 = self.ui.VERSETEXT2

            if self.ui.strings_2.text() != "" and self.ui.quatrains_2.text() != "":
                tmp = lines(self.ui.vt2, self.ui.strings_2.text())
                tmp = quatrains(tmp, self.ui.quatrains_2.text())
                self.ui.verseText_2.setText(tmp)
                self.ui.vt2 = self.ui.VERSETEXT2

            if self.ui.strings_2.text() == "" and self.ui.quatrains_2.text() == "":
                self.ui.verseText_2.setText(self.ui.vt2)

        except ValueError:
            pass

    def apply_button3_clicked(self):
        try:
            if self.ui.quatrains_3.text() == "" and self.ui.strings_3.text() != "":
                tmp = lines(self.ui.vt3, self.ui.strings_3.text())
                self.ui.verseText_3.setText(tmp)
                self.ui.vt3 = self.ui.VERSETEXT3

            if self.ui.strings_3.text() == "" and self.ui.quatrains_3.text() != "":
                tmp = quatrains(self.ui.vt3, self.ui.quatrains_3.text())
                self.ui.verseText_3.setText(tmp)
                self.ui.vt3 = self.ui.VERSETEXT3

            if self.ui.strings_3.text() != "" and self.ui.quatrains_3.text() != "":
                tmp = lines(self.ui.vt3, self.ui.strings_3.text())
                tmp = quatrains(tmp, self.ui.quatrains_3.text())
                self.ui.verseText_3.setText(tmp)
                self.ui.vt3 = self.ui.VERSETEXT3

            if self.ui.strings_3.text() == "" and self.ui.quatrains_3.text() == "":
                self.ui.verseText_3.setText(self.ui.vt3)

        except ValueError:
            pass

    def remove_filters_clicked(self):
        self.ui.verseText.setText(self.ui.vt)
        self.ui.quatrains.setText("")
        self.ui.strings.setText("")

    def remove_filters2_clicked(self):
        self.ui.verseText_2.setText(self.ui.vt2)
        self.ui.quatrains_2.setText("")
        self.ui.strings_2.setText("")

    def remove_filters3_clicked(self):
        self.ui.verseText_3.setText(self.ui.vt3)
        self.ui.quatrains_3.setText("")
        self.ui.strings_3.setText("")

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
                self.verseOpenWindow.ui.verseText_2.setText(first_word(vrstxt))
                self.verseOpenWindow.ui.verseText_3.setText(first_and_last_word(vrstxt))
                self.verseOpenWindow.ui.VERSETEXT = vrstxt
                self.verseOpenWindow.ui.VERSETEXT2 = first_word(vrstxt)
                self.verseOpenWindow.ui.VERSETEXT3 = first_and_last_word(vrstxt)
                self.verseOpenWindow.ui.vt = vrstxt
                self.verseOpenWindow.ui.vt2 = first_word(vrstxt)
                self.verseOpenWindow.ui.vt3 = first_and_last_word(vrstxt)
                
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
        for verse in self.ui.verses:
            if verse.isChecked() is True:
                os.remove(f"verses/{verse.text()}.txt")
                self.ui.verses.remove(verse)
                self.ui.vbox.removeWidget(verse)
                self.ui.vbox.update()

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
