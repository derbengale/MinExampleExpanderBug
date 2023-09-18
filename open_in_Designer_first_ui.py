# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'open_in_Designer_first.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

from MadQt.Widgets.expander import Expander

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1140, 864)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.expander_2 = Expander(Form)
        self.expander_2.setObjectName(u"expander_2")
        self.expander_2.setMinimumSize(QSize(300, 0))
        self.expander_2.setMaximumSize(QSize(16777215, 0))
        self.expander_2.setProperty("curve", 34)
        self.expander_2.setProperty("duration", 250)
        self.expander_2.setProperty("period", 0.000000000000000)
        self.expander_2.setProperty("amplitude", 0.000000000000000)
        self.expander_2.setProperty("overshoot", 0.000000000000000)
        self.expander_2.setProperty("expanded", False)
        self.expander_2.setProperty("animateOnHover", False)
        self.expander_2.setProperty("animFrom", QSize(300, 0))
        self.expander_2.setProperty("animTo", QSize(300, 400))
        self.expander_2.setProperty("animateMaxWidth", False)
        self.expander_2.setProperty("animateMinWidth", False)
        self.expander_2.setProperty("animateMaxHeight", True)
        self.expander_2.setProperty("animateMinHeight", True)
        self.gridLayout_2 = QGridLayout(self.expander_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.expander_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u"Daco_4605931.png"))
        self.label_7.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_10 = QLabel(self.expander_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.label_11 = QLabel(self.expander_2)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_5.addWidget(self.label_11)

        self.label_13 = QLabel(self.expander_2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_5.addWidget(self.label_13)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.label_14 = QLabel(self.expander_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.expander_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_2.addWidget(self.checkBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.expander = Expander(Form)
        self.expander.setObjectName(u"expander")
        self.expander.setMinimumSize(QSize(0, 0))
        self.expander.setMaximumSize(QSize(0, 16777215))
        self.expander.setProperty("curve", 34)
        self.expander.setProperty("duration", 250)
        self.expander.setProperty("period", 0.000000000000000)
        self.expander.setProperty("amplitude", 0.000000000000000)
        self.expander.setProperty("overshoot", 0.000000000000000)
        self.expander.setProperty("expanded", False)
        self.expander.setProperty("animateOnHover", False)
        self.expander.setProperty("animFrom", QSize(0, 100))
        self.expander.setProperty("animTo", QSize(300, 100))
        self.gridLayout_3 = QGridLayout(self.expander)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.expander)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u"clipart855284.png"))

        self.verticalLayout_6.addWidget(self.label_8)

        self.label_9 = QLabel(self.expander)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_6.addWidget(self.label_9)

        self.label_12 = QLabel(self.expander)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_6.addWidget(self.label_12)


        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.expander)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(Form)
        self.checkBox.toggled.connect(self.expander.setExpanded)
        self.checkBox_2.toggled.connect(self.expander_2.setExpanded)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_7.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"Once you open the .py file this expander gets resized to the initial width set in this expanders AnimMaxWidth==AnimMinWidth though I deactivated the Setting.", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"After I save this file the Setting does not get saved properly", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Because its behavong this way i can not use it in my program as I want it", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"It is not possible to set  Maximum width to 9999999999 because Expander overwrites this setting at initialization.", None))
        self.label.setText(QCoreApplication.translate("Form", u"This is my main content in here. Thank you for creating nice things for us and making our programs more beautiful :-) Greetings from Germany", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"This is my main content in here. Thank you for creating nice things for us and making our programs more beautiful :-) Greetings from Germany", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"This is my main content in here. Thank you for creating nice things for us and making our programs more beautiful :-) Greetings from Germany", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"This is my main content in here. Thank you for creating nice things for us and making our programs more beautiful :-) Greetings from Germany", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"This is my main content in here. Thank you for creating nice things for us and making our programs more beautiful :-) Greetings from Germany", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"This is my main content in here. Thank you for creating nice things for us and making our programs more beautiful :-) Greetings from Germany", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"Vertical Expander works fine in QtDesigner but not at runtime", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Horizontal Expander works as expected", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"This Expander works fine.", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Im already using it in many places in my program this way.", None))
    # retranslateUi

