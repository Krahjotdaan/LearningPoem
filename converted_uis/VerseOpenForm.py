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
        VerseOpenForm.resize(450, 800)
        self.centralwidget = QtWidgets.QWidget(VerseOpenForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setContentsMargins(10, 5, 10, 5)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setMaximumSize(QtCore.QSize(48, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setText("")
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_9.addWidget(self.backButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleAndAuthorLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleAndAuthorLabel.sizePolicy().hasHeightForWidth())
        self.titleAndAuthorLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.titleAndAuthorLabel.setFont(font)
        self.titleAndAuthorLabel.setObjectName("titleAndAuthorLabel")
        self.horizontalLayout.addWidget(self.titleAndAuthorLabel)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.sourceVerseText = QtWidgets.QWidget()
        self.sourceVerseText.setObjectName("sourceVerseText")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.sourceVerseText)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.sourceVerseText)
        self.label.setMaximumSize(QtCore.QSize(83, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.strings = QtWidgets.QLineEdit(self.sourceVerseText)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strings.sizePolicy().hasHeightForWidth())
        self.strings.setSizePolicy(sizePolicy)
        self.strings.setObjectName("strings")
        self.horizontalLayout_6.addWidget(self.strings)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.applyButton = QtWidgets.QPushButton(self.sourceVerseText)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applyButton.sizePolicy().hasHeightForWidth())
        self.applyButton.setSizePolicy(sizePolicy)
        self.applyButton.setObjectName("applyButton")
        self.horizontalLayout_5.addWidget(self.applyButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.sourceVerseText)
        self.label_2.setMaximumSize(QtCore.QSize(83, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.quatrains = QtWidgets.QLineEdit(self.sourceVerseText)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quatrains.sizePolicy().hasHeightForWidth())
        self.quatrains.setSizePolicy(sizePolicy)
        self.quatrains.setObjectName("quatrains")
        self.horizontalLayout_7.addWidget(self.quatrains)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.removeFiltersButton = QtWidgets.QPushButton(self.sourceVerseText)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeFiltersButton.sizePolicy().hasHeightForWidth())
        self.removeFiltersButton.setSizePolicy(sizePolicy)
        self.removeFiltersButton.setObjectName("removeFiltersButton")
        self.horizontalLayout_39.addWidget(self.removeFiltersButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_39, 1, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verseText = QtWidgets.QTextBrowser(self.sourceVerseText)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.verseText.setFont(font)
        self.verseText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.verseText.setObjectName("verseText")
        self.verticalLayout_2.addWidget(self.verseText)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 0, 1, 3)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 6)
        self.gridLayout_3.setColumnStretch(2, 3)
        self.gridLayout_3.setRowStretch(0, 3)
        self.gridLayout_3.setRowStretch(1, 3)
        self.gridLayout_3.setRowStretch(2, 51)
        self.tabWidget.addTab(self.sourceVerseText, "")
        self.firstWordOfStrings = QtWidgets.QWidget()
        self.firstWordOfStrings.setObjectName("firstWordOfStrings")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.firstWordOfStrings)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_10 = QtWidgets.QLabel(self.firstWordOfStrings)
        self.label_10.setMaximumSize(QtCore.QSize(83, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_21.addWidget(self.label_10)
        self.gridLayout_2.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.strings_2 = QtWidgets.QLineEdit(self.firstWordOfStrings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strings_2.sizePolicy().hasHeightForWidth())
        self.strings_2.setSizePolicy(sizePolicy)
        self.strings_2.setObjectName("strings_2")
        self.horizontalLayout_20.addWidget(self.strings_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_20, 0, 1, 1, 1)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.applyButton_2 = QtWidgets.QPushButton(self.firstWordOfStrings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applyButton_2.sizePolicy().hasHeightForWidth())
        self.applyButton_2.setSizePolicy(sizePolicy)
        self.applyButton_2.setObjectName("applyButton_2")
        self.horizontalLayout_22.addWidget(self.applyButton_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_22, 0, 2, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_9 = QtWidgets.QLabel(self.firstWordOfStrings)
        self.label_9.setMaximumSize(QtCore.QSize(83, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_19.addWidget(self.label_9)
        self.gridLayout_2.addLayout(self.horizontalLayout_19, 1, 0, 1, 1)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.quatrains_2 = QtWidgets.QLineEdit(self.firstWordOfStrings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quatrains_2.sizePolicy().hasHeightForWidth())
        self.quatrains_2.setSizePolicy(sizePolicy)
        self.quatrains_2.setObjectName("quatrains_2")
        self.horizontalLayout_23.addWidget(self.quatrains_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_23, 1, 1, 1, 1)
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.removeFiltersButton_2 = QtWidgets.QPushButton(self.firstWordOfStrings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeFiltersButton_2.sizePolicy().hasHeightForWidth())
        self.removeFiltersButton_2.setSizePolicy(sizePolicy)
        self.removeFiltersButton_2.setObjectName("removeFiltersButton_2")
        self.horizontalLayout_46.addWidget(self.removeFiltersButton_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_46, 1, 2, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verseText_2 = QtWidgets.QTextBrowser(self.firstWordOfStrings)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.verseText_2.setFont(font)
        self.verseText_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.verseText_2.setObjectName("verseText_2")
        self.verticalLayout_4.addWidget(self.verseText_2)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 2, 0, 1, 3)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 6)
        self.gridLayout_2.setColumnStretch(2, 3)
        self.gridLayout_2.setRowStretch(0, 3)
        self.gridLayout_2.setRowStretch(1, 3)
        self.gridLayout_2.setRowStretch(2, 51)
        self.tabWidget.addTab(self.firstWordOfStrings, "")
        self.firstAndLastWordsOfStrings = QtWidgets.QWidget()
        self.firstAndLastWordsOfStrings.setObjectName("firstAndLastWordsOfStrings")
        self.gridLayout = QtWidgets.QGridLayout(self.firstAndLastWordsOfStrings)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.label_20 = QtWidgets.QLabel(self.firstAndLastWordsOfStrings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMaximumSize(QtCore.QSize(83, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_50.addWidget(self.label_20)
        self.gridLayout.addLayout(self.horizontalLayout_50, 0, 0, 1, 1)
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.strings_3 = QtWidgets.QLineEdit(self.firstAndLastWordsOfStrings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strings_3.sizePolicy().hasHeightForWidth())
        self.strings_3.setSizePolicy(sizePolicy)
        self.strings_3.setObjectName("strings_3")
        self.horizontalLayout_48.addWidget(self.strings_3)
        self.gridLayout.addLayout(self.horizontalLayout_48, 0, 1, 1, 1)
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.applyButton_3 = QtWidgets.QPushButton(self.firstAndLastWordsOfStrings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applyButton_3.sizePolicy().hasHeightForWidth())
        self.applyButton_3.setSizePolicy(sizePolicy)
        self.applyButton_3.setObjectName("applyButton_3")
        self.horizontalLayout_51.addWidget(self.applyButton_3)
        self.gridLayout.addLayout(self.horizontalLayout_51, 0, 2, 1, 1)
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.label_19 = QtWidgets.QLabel(self.firstAndLastWordsOfStrings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMaximumSize(QtCore.QSize(83, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_47.addWidget(self.label_19)
        self.gridLayout.addLayout(self.horizontalLayout_47, 1, 0, 1, 1)
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.quatrains_3 = QtWidgets.QLineEdit(self.firstAndLastWordsOfStrings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quatrains_3.sizePolicy().hasHeightForWidth())
        self.quatrains_3.setSizePolicy(sizePolicy)
        self.quatrains_3.setObjectName("quatrains_3")
        self.horizontalLayout_52.addWidget(self.quatrains_3)
        self.gridLayout.addLayout(self.horizontalLayout_52, 1, 1, 1, 1)
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.removeFiltersButton_3 = QtWidgets.QPushButton(self.firstAndLastWordsOfStrings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeFiltersButton_3.sizePolicy().hasHeightForWidth())
        self.removeFiltersButton_3.setSizePolicy(sizePolicy)
        self.removeFiltersButton_3.setObjectName("removeFiltersButton_3")
        self.horizontalLayout_49.addWidget(self.removeFiltersButton_3)
        self.gridLayout.addLayout(self.horizontalLayout_49, 1, 2, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verseText_3 = QtWidgets.QTextBrowser(self.firstAndLastWordsOfStrings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verseText_3.sizePolicy().hasHeightForWidth())
        self.verseText_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.verseText_3.setFont(font)
        self.verseText_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.verseText_3.setObjectName("verseText_3")
        self.verticalLayout_9.addWidget(self.verseText_3)
        self.gridLayout.addLayout(self.verticalLayout_9, 2, 0, 1, 3)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 6)
        self.gridLayout.setColumnStretch(2, 3)
        self.gridLayout.setRowStretch(0, 3)
        self.gridLayout.setRowStretch(1, 3)
        self.gridLayout.setRowStretch(2, 51)
        self.tabWidget.addTab(self.firstAndLastWordsOfStrings, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout_4.addLayout(self.verticalLayout, 1, 0, 1, 2)
        self.gridLayout_4.setColumnStretch(0, 5)
        self.gridLayout_4.setColumnStretch(1, 34)
        self.gridLayout_4.setRowStretch(0, 5)
        self.gridLayout_4.setRowStretch(1, 63)

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(
            "converted_uis/../resource/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backButton.setIcon(self.icon)
        self.backButton.setIconSize(QtCore.QSize(45, 45))
        self.VERSETEXT = None
        self.VERSETEXT2 = None
        self.VERSETEXT3 = None
        self.vt = None
        self.vt2 = None
        self.vt3 = None
        VerseOpenForm.setCentralWidget(self.centralwidget)
        self.retranslateUi(VerseOpenForm)
        self.tabWidget.setCurrentIndex(0)

        self.applyButton.clicked.connect(VerseOpenForm.apply_button_clicked)
        self.applyButton_2.clicked.connect(VerseOpenForm.apply_button2_clicked)
        self.applyButton_3.clicked.connect(VerseOpenForm.apply_button3_clicked)
        self.removeFiltersButton.clicked.connect(
            VerseOpenForm.remove_filters_clicked)
        self.removeFiltersButton_2.clicked.connect(
            VerseOpenForm.remove_filters2_clicked)
        self.removeFiltersButton_3.clicked.connect(
            VerseOpenForm.remove_filters3_clicked)
        self.backButton.clicked.connect(VerseOpenForm.back_button_clicked)

        VerseOpenForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(VerseOpenForm)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(VerseOpenForm)

    def retranslateUi(self, VerseOpenForm):
        _translate = QtCore.QCoreApplication.translate
        VerseOpenForm.setWindowTitle(_translate("VerseOpenForm", "MainWindow"))
        self.titleAndAuthorLabel.setText(_translate("VerseOpenForm", "<html><head/><body><p>Название и автор</p></body></html>"))
        self.label.setText(_translate("VerseOpenForm", "Строки"))
        self.applyButton.setText(_translate("VerseOpenForm", "Применить"))
        self.label_2.setText(_translate("VerseOpenForm", "Строфы"))
        self.removeFiltersButton.setText(_translate("VerseOpenForm", "Убрать фильтр"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sourceVerseText), _translate("VerseOpenForm", " Исходный "))
        self.label_10.setText(_translate("VerseOpenForm", "Строки"))
        self.applyButton_2.setText(_translate("VerseOpenForm", "Применить"))
        self.label_9.setText(_translate("VerseOpenForm", "Строфы"))
        self.removeFiltersButton_2.setText(_translate("VerseOpenForm", "Убрать фильтр"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.firstWordOfStrings), _translate("VerseOpenForm", "Первое слово"))
        self.label_20.setText(_translate("VerseOpenForm", "Строки"))
        self.applyButton_3.setText(_translate("VerseOpenForm", "Применить"))
        self.label_19.setText(_translate("VerseOpenForm", "Строфы"))
        self.removeFiltersButton_3.setText(_translate("VerseOpenForm", "Убрать фильтр"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.firstAndLastWordsOfStrings), _translate("VerseOpenForm", "Первое и последнее"))
