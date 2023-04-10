# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/VerseOpenForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VerseOpenForm(object):
    def setupUi(self, VerseOpenForm):
        VerseOpenForm.setObjectName("VerseOpenForm")
        VerseOpenForm.resize(420, 709)
        self.centralwidget = QtWidgets.QWidget(VerseOpenForm)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 10, 341, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleAndAuthorLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titleAndAuthorLabel.setFont(font)
        self.titleAndAuthorLabel.setObjectName("titleAndAuthorLabel")
        self.horizontalLayout.addWidget(self.titleAndAuthorLabel)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 199, 401, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verseText = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.verseText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.verseText.setObjectName("verseText")
        self.gridLayout.addWidget(self.verseText, 0, 0, 1, 1)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 201, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sourceTextCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceTextCheckBox.sizePolicy().hasHeightForWidth())
        self.sourceTextCheckBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sourceTextCheckBox.setFont(font)
        self.sourceTextCheckBox.setTristate(False)
        self.sourceTextCheckBox.setObjectName("sourceTextCheckBox")
        self.horizontalLayout_3.addWidget(self.sourceTextCheckBox)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(210, 70, 201, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.firstWordCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.firstWordCheckBox.setFont(font)
        self.firstWordCheckBox.setObjectName("firstWordCheckBox")
        self.horizontalLayout_4.addWidget(self.firstWordCheckBox)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 110, 201, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.linesNumberCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.linesNumberCheckBox.setFont(font)
        self.linesNumberCheckBox.setObjectName("linesNumberCheckBox")
        self.horizontalLayout_5.addWidget(self.linesNumberCheckBox)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 150, 201, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.quatrainsNumberCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.quatrainsNumberCheckBox.setFont(font)
        self.quatrainsNumberCheckBox.setObjectName("quatrainsNumberCheckBox")
        self.horizontalLayout_6.addWidget(self.quatrainsNumberCheckBox)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(210, 110, 201, 41))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.numbersOfLines = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.numbersOfLines.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.numbersOfLines.setFont(font)
        self.numbersOfLines.setObjectName("numbersOfLines")
        self.horizontalLayout_7.addWidget(self.numbersOfLines)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(210, 150, 201, 41))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.numbersOfQuatrains = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.numbersOfQuatrains.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.numbersOfQuatrains.setFont(font)
        self.numbersOfQuatrains.setObjectName("numbersOfQuatrains")
        self.horizontalLayout_8.addWidget(self.numbersOfQuatrains)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.backButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setText("")
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_9.addWidget(self.backButton)
        VerseOpenForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(VerseOpenForm)
        QtCore.QMetaObject.connectSlotsByName(VerseOpenForm)

        self.backButton.clicked.connect(VerseOpenForm.back_button_clicked)

    def retranslateUi(self, VerseOpenForm):
        _translate = QtCore.QCoreApplication.translate
        VerseOpenForm.setWindowTitle(_translate("VerseOpenForm", "MainWindow"))
        self.titleAndAuthorLabel.setText(_translate("VerseOpenForm", "<html><head/><body><p>Название и автор</p></body></html>"))
        self.sourceTextCheckBox.setText(_translate("VerseOpenForm", "Исходный"))
        self.firstWordCheckBox.setText(_translate("VerseOpenForm", "Первые слова"))
        self.linesNumberCheckBox.setText(_translate("VerseOpenForm", "Номера строк"))
        self.quatrainsNumberCheckBox.setText(_translate("VerseOpenForm", "Четверостишья"))
