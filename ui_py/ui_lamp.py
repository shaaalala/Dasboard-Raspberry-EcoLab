# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lamp.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 600)
        Form.setMaximumSize(QSize(1024, 600))
        Form.setStyleSheet(u"\n"
"QWidget {\n"
"    background: transparent;\n"
"}\n"
"QToolButton {\n"
"    background-color: #7f8c8d;\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"    font-size: 14px;\n"
"}\n"
"QToolButton:checked {\n"
"    background-color: #f39c12;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: #626567;\n"
"}\n"
"   ")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lampLayout = QHBoxLayout()
        self.lampLayout.setSpacing(30)
        self.lampLayout.setObjectName(u"lampLayout")
        self.lamp1 = QToolButton(Form)
        self.lamp1.setObjectName(u"lamp1")
        self.lamp1.setMinimumSize(QSize(150, 175))
        icon = QIcon()
        icon.addFile(u"assets/LAMP OFF.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lamp1.setIcon(icon)
        self.lamp1.setIconSize(QSize(70, 70))
        self.lamp1.setCheckable(True)
        self.lamp1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.lampLayout.addWidget(self.lamp1)

        self.lamp2 = QToolButton(Form)
        self.lamp2.setObjectName(u"lamp2")
        self.lamp2.setMinimumSize(QSize(150, 175))
        self.lamp2.setIcon(icon)
        self.lamp2.setIconSize(QSize(70, 70))
        self.lamp2.setCheckable(True)
        self.lamp2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.lampLayout.addWidget(self.lamp2)

        self.lamp3 = QToolButton(Form)
        self.lamp3.setObjectName(u"lamp3")
        self.lamp3.setMinimumSize(QSize(150, 175))
        self.lamp3.setIcon(icon)
        self.lamp3.setIconSize(QSize(70, 70))
        self.lamp3.setCheckable(True)
        self.lamp3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.lampLayout.addWidget(self.lamp3)

        self.lamp4 = QToolButton(Form)
        self.lamp4.setObjectName(u"lamp4")
        self.lamp4.setMinimumSize(QSize(150, 175))
        self.lamp4.setIcon(icon)
        self.lamp4.setIconSize(QSize(70, 70))
        self.lamp4.setCheckable(True)
        self.lamp4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.lampLayout.addWidget(self.lamp4)

        self.lamp5 = QToolButton(Form)
        self.lamp5.setObjectName(u"lamp5")
        self.lamp5.setMinimumSize(QSize(150, 175))
        self.lamp5.setIcon(icon)
        self.lamp5.setIconSize(QSize(70, 70))
        self.lamp5.setCheckable(True)
        self.lamp5.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.lamp5.setAutoRaise(False)

        self.lampLayout.addWidget(self.lamp5)


        self.verticalLayout.addLayout(self.lampLayout)

        self.label_MCUA = QLabel(Form)
        self.label_MCUA.setObjectName(u"label_MCUA")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_MCUA.setFont(font)
        self.label_MCUA.setStyleSheet(u"\n"
"color: red;\n"
"font-weight: bold;\n"
"   ")
        self.label_MCUA.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_MCUA)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.lamp1.setText(QCoreApplication.translate("Form", u"Lamp 1\n"
"OFF", None))
        self.lamp2.setText(QCoreApplication.translate("Form", u"Lamp 2\n"
"OFF", None))
        self.lamp3.setText(QCoreApplication.translate("Form", u"Lamp 3\n"
"OFF", None))
        self.lamp4.setText(QCoreApplication.translate("Form", u"Lamp 4\n"
"OFF", None))
        self.lamp5.setText(QCoreApplication.translate("Form", u"Lamp 5\n"
"OFF", None))
        self.label_MCUA.setText(QCoreApplication.translate("Form", u"MCU A: DISCONNECTED", None))
        pass
    # retranslateUi

