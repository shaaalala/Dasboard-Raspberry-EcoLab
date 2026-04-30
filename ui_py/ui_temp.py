# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'temprNpJuA.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_temp(object):
    def setupUi(self, temp):
        if not temp.objectName():
            temp.setObjectName(u"temp")
        temp.resize(1024, 600)
        temp.setMinimumSize(QSize(1024, 600))
        temp.setMaximumSize(QSize(1024, 600))
        temp.setStyleSheet(u"\n"
"QWidget {\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Tombol umum */\n"
"QPushButton {\n"
"    background-color: #34495e;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2c3e50;\n"
"}\n"
"\n"
"/* Tombol AC aktif */\n"
"QPushButton#btn_ac:checked {\n"
"    background-color: #27ae60;\n"
"}\n"
"   ")
        self.verticalLayout = QVBoxLayout(temp)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.topSpacer)

        self.label_title = QLabel(temp)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setStyleSheet(u"\n"
"color: black;\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"      ")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.frame = QFrame(temp)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_ac = QPushButton(self.frame)
        self.btn_ac.setObjectName(u"btn_ac")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ac.sizePolicy().hasHeightForWidth())
        self.btn_ac.setSizePolicy(sizePolicy)
        self.btn_ac.setMinimumSize(QSize(120, 120))
        self.btn_ac.setMaximumSize(QSize(120, 120))
        self.btn_ac.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #bdc3c7;\n"
"    border-radius: 60px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #27ae60;\n"
"}\n"
"     ")
        icon = QIcon()
        icon.addFile(u"assets/AC OFF.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ac.setIcon(icon)
        self.btn_ac.setIconSize(QSize(60, 60))
        self.btn_ac.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_ac)


        self.verticalLayout.addWidget(self.frame)

        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.label_status = QLabel(temp)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setStyleSheet(u"\n"
"color: #000000;\n"
"background transparan;\n"
"padding: 8px;\n"
"border-radius: 8px;\n"
"font-weight: bold;\n"
"     ")
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.label_status)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_temp_up = QPushButton(temp)
        self.btn_temp_up.setObjectName(u"btn_temp_up")
        sizePolicy.setHeightForWidth(self.btn_temp_up.sizePolicy().hasHeightForWidth())
        self.btn_temp_up.setSizePolicy(sizePolicy)
        self.btn_temp_up.setMinimumSize(QSize(180, 70))

        self.gridLayout.addWidget(self.btn_temp_up, 0, 0, 1, 1)

        self.btn_cool = QPushButton(temp)
        self.btn_cool.setObjectName(u"btn_cool")
        sizePolicy.setHeightForWidth(self.btn_cool.sizePolicy().hasHeightForWidth())
        self.btn_cool.setSizePolicy(sizePolicy)
        self.btn_cool.setMinimumSize(QSize(180, 70))
        self.btn_cool.setCheckable(True)
        self.btn_cool.setAutoExclusive(True)

        self.gridLayout.addWidget(self.btn_cool, 0, 1, 1, 1)

        self.btn_temp_down = QPushButton(temp)
        self.btn_temp_down.setObjectName(u"btn_temp_down")
        sizePolicy.setHeightForWidth(self.btn_temp_down.sizePolicy().hasHeightForWidth())
        self.btn_temp_down.setSizePolicy(sizePolicy)
        self.btn_temp_down.setMinimumSize(QSize(180, 70))

        self.gridLayout.addWidget(self.btn_temp_down, 1, 0, 1, 1)

        self.btn_fan = QPushButton(temp)
        self.btn_fan.setObjectName(u"btn_fan")
        sizePolicy.setHeightForWidth(self.btn_fan.sizePolicy().hasHeightForWidth())
        self.btn_fan.setSizePolicy(sizePolicy)
        self.btn_fan.setMinimumSize(QSize(180, 70))
        self.btn_fan.setCheckable(True)
        self.btn_fan.setAutoExclusive(True)

        self.gridLayout.addWidget(self.btn_fan, 1, 1, 1, 1)


        self.vboxLayout.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.vboxLayout)

        self.label_MCUB = QLabel(temp)
        self.label_MCUB.setObjectName(u"label_MCUB")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_MCUB.setFont(font)
        self.label_MCUB.setStyleSheet(u"\n"
"color: red;\n"
"font-weight: bold;\n"
" ")
        self.label_MCUB.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_MCUB)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.bottomSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.bottomSpacer)


        self.retranslateUi(temp)

        QMetaObject.connectSlotsByName(temp)
    # setupUi

    def retranslateUi(self, temp):
        self.label_title.setText(QCoreApplication.translate("temp", u"CONTROL SUHU", None))
        self.label_status.setText(QCoreApplication.translate("temp", u"Status AC: OFF", None))
        self.btn_temp_up.setText(QCoreApplication.translate("temp", u"Temp +", None))
        self.btn_cool.setText(QCoreApplication.translate("temp", u"COOL", None))
        self.btn_temp_down.setText(QCoreApplication.translate("temp", u"Temp -", None))
        self.btn_fan.setText(QCoreApplication.translate("temp", u"FAN", None))
        self.label_MCUB.setText(QCoreApplication.translate("temp", u"MCU B: DISCONNECTED", None))
        pass
    # retranslateUi

