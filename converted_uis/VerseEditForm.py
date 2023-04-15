# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/VerseEditForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VerseEditForm(object):
    def setupUi(self, VerseEditForm):
        VerseEditForm.setObjectName("VerseEditForm")
        VerseEditForm.resize(420, 700)
        self.centralwidget = QtWidgets.QWidget(VerseEditForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 5, 10, 5)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setMaximumSize(QtCore.QSize(48, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setText("")
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_9.addWidget(self.backButton)
        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.author = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.author.setFont(font)
        self.author.setObjectName("author")
        self.verticalLayout_4.addWidget(self.author)
        self.gridLayout.addLayout(self.verticalLayout_4, 2, 2, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verse_text = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.verse_text.setFont(font)
        self.verse_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.verse_text.setObjectName("verse_text")
        self.verticalLayout_7.addWidget(self.verse_text)
        self.gridLayout.addLayout(self.verticalLayout_7, 3, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editVerseButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editVerseButton.sizePolicy().hasHeightForWidth())
        self.editVerseButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.editVerseButton.setFont(font)
        self.editVerseButton.setObjectName("newVerseButton")
        self.horizontalLayout.addWidget(self.editVerseButton)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 3)
        self.gridLayout.setRowStretch(0, 3)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 27)
        self.gridLayout.setRowStretch(4, 4)

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(
            "converted_uis/../resource/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backButton.setIcon(self.icon)
        self.backButton.setIconSize(QtCore.QSize(45, 45))
        VerseEditForm.setCentralWidget(self.centralwidget)
        self.filetitle = ""

        VerseEditForm.setCentralWidget(self.centralwidget)

        self.editVerseButton.clicked.connect(VerseEditForm.edit_button_clicked)
        self.backButton.clicked.connect(VerseEditForm.back_button_clicked)

        self.retranslateUi(VerseEditForm)
        QtCore.QMetaObject.connectSlotsByName(VerseEditForm)

    def retranslateUi(self, VerseEditForm):
        _translate = QtCore.QCoreApplication.translate
        VerseEditForm.setWindowTitle(_translate("VerseEditForm", "MainWindow"))
        self.label_6.setText(_translate("VerseEditForm", "Редактирование"))
        self.label.setText(_translate("VerseEditForm", "<html><head/><body><p><span style=\" font-size:18pt;\">Название:</span></p></body></html>"))
        self.label_2.setText(_translate("VerseEditForm", "<html><head/><body><p><span style=\" font-size:18pt;\">Автор:</span></p></body></html>"))
        self.editVerseButton.setText(_translate("VerseEditForm", "Изменить"))
