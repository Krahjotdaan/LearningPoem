# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/LibraryForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LibraryForm(object):
    def setupUi(self, LibraryForm):
        LibraryForm.setObjectName("LibraryForm")
        LibraryForm.resize(450, 800)
        self.centralwidget = QtWidgets.QWidget(LibraryForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(10, 5, 10, 5)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
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
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout_8.addLayout(self.horizontalLayout)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 10)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 382, 547))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openButton.sizePolicy().hasHeightForWidth())
        self.openButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.openButton.setFont(font)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout_3.addWidget(self.openButton)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.editButton.setFont(font)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_4.addWidget(self.editButton)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_2.addWidget(self.deleteButton)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)
        self.gridLayout_2.setRowStretch(0, 5)
        self.gridLayout_2.setRowStretch(1, 51)
        self.gridLayout_2.setRowStretch(2, 6)

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(
            "converted_uis/../resource/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backButton.setIcon(self.icon)
        self.backButton.setIconSize(QtCore.QSize(45, 45))

        s = 0
        self.vbox = QtWidgets.QVBoxLayout()
        self.groupBox = QtWidgets.QWidget()
        self.verses = []
        for filename in os.listdir('converted_uis/../verses'):
            if filename.endswith(".txt"):
                verseRadioButton = QtWidgets.QRadioButton()
                name = os.path.basename(filename)
                name = os.path.splitext(name)[0]
                verseRadioButton.setText(str(name))
                self.vbox.addWidget(verseRadioButton)
                self.verses.append(verseRadioButton)
                font = QtGui.QFont()
                font.setPointSize(14)
                verseRadioButton.setFont(font)
                verseRadioButton.resize(370, 40)
                verseRadioButton.move(10, s * 40)
                s += 1

        self.vbox.addStretch(1)
        self.groupBox.setLayout(self.vbox)
        self.scrollArea.setWidget(self.groupBox)

        self.openButton.clicked.connect(LibraryForm.open_button_clicked)
        self.editButton.clicked.connect(LibraryForm.edit_button_clicked)
        self.deleteButton.clicked.connect(LibraryForm.delete_button_clicked)
        self.backButton.clicked.connect(LibraryForm.back_button_clicked)
        
        LibraryForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(LibraryForm)
        QtCore.QMetaObject.connectSlotsByName(LibraryForm)

    def retranslateUi(self, LibraryForm):
        _translate = QtCore.QCoreApplication.translate
        LibraryForm.setWindowTitle(_translate("LibraryForm", "MainWindow"))
        self.label.setText(_translate("LibraryForm", "<html><head/><body><p><span style=\" font-size:20pt;\">Библиотека</span></p></body></html>"))
        self.openButton.setText(_translate("LibraryForm", "Открыть"))
        self.editButton.setText(_translate("LibraryForm", "Изменить"))
        self.deleteButton.setText(_translate("LibraryForm", "Удалить"))
