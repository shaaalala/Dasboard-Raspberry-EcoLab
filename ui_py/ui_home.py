# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMinimumSize(QSize(1024, 600))
        MainWindow.setMaximumSize(QSize(1024, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"\n"
"/* BACKGROUND */\n"
"QWidget#centralwidget {\n"
"    background-image: url(\"assets/bg.png\");\n"
"    background-position: center;\n"
"}\n"
"\n"
"/* CARD */\n"
"QFrame#card_weather,\n"
"QFrame#card_power,\n"
"QFrame#card_solar,\n"
"QFrame#card_temp_room,\n"
"QFrame#card_temp_out,\n"
"QFrame#card_wind {\n"
"    background-color: rgba(0,0,0,70);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QFrame#card_weather:hover,\n"
"QFrame#card_power:hover,\n"
"QFrame#card_solar:hover,\n"
"QFrame#card_temp_room:hover,\n"
"QFrame#card_temp_out:hover,\n"
"QFrame#card_wind:hover {\n"
"    background-color: rgba(0,0,0,120);\n"
"}\n"
"\n"
"/* CHILD FRAME */\n"
"QFrame QFrame {\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TEXT */\n"
"QLabel {\n"
"    color: white;\n"
"}\n"
"\n"
"    ")
        self.vboxLayout = QVBoxLayout(self.centralwidget)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.topbar = QFrame(self.centralwidget)
        self.topbar.setObjectName(u"topbar")
        self.topbar.setMinimumSize(QSize(0, 60))
        self.topbar.setStyleSheet(u"\n"
"QFrame#topbar {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QLabel#label_title {\n"
"    color: white;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"       ")
        self.hboxLayout = QHBoxLayout(self.topbar)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.btn_menu = QPushButton(self.topbar)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(50, 50))
        self.btn_menu.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgba(255,255,255,60);\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255,255,255,120);\n"
"}\n"
"          ")

        self.hboxLayout.addWidget(self.btn_menu)

        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.spacerItem)

        self.btn_exit = QPushButton(self.topbar)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(50, 50))
        self.btn_exit.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgba(231, 76, 60, 180);\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(192, 57, 43, 220);\n"
"}\n"
"          ")

        self.hboxLayout.addWidget(self.btn_exit)


        self.vboxLayout.addWidget(self.topbar)

        self.body_frame = QFrame(self.centralwidget)
        self.body_frame.setObjectName(u"body_frame")
        self.hboxLayout1 = QHBoxLayout(self.body_frame)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.menu_frame = QFrame(self.body_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMaximumSize(QSize(0, 16777215))
        self.menu_frame.setStyleSheet(u"\n"
"QFrame#menu_frame {\n"
"    background-color: rgba(44,62,80,200);\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgba(255,255,255,150);\n"
"}\n"
"          ")
        self.vboxLayout1 = QVBoxLayout(self.menu_frame)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.btn_home = QPushButton(self.menu_frame)
        self.btn_home.setObjectName(u"btn_home")
        icon = QIcon()
        icon.addFile(u"assets/HOME.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(50, 50))
        self.btn_home.setCheckable(True)
        self.btn_home.setAutoExclusive(True)

        self.vboxLayout1.addWidget(self.btn_home)

        self.btn_lamp = QPushButton(self.menu_frame)
        self.btn_lamp.setObjectName(u"btn_lamp")
        icon1 = QIcon()
        icon1.addFile(u"assets/LAMP OFF.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_lamp.setIcon(icon1)
        self.btn_lamp.setIconSize(QSize(50, 50))
        self.btn_lamp.setCheckable(True)
        self.btn_lamp.setAutoExclusive(True)

        self.vboxLayout1.addWidget(self.btn_lamp)

        self.btn_temp = QPushButton(self.menu_frame)
        self.btn_temp.setObjectName(u"btn_temp")
        icon2 = QIcon()
        icon2.addFile(u"assets/AC OFF.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_temp.setIcon(icon2)
        self.btn_temp.setIconSize(QSize(50, 50))
        self.btn_temp.setCheckable(True)
        self.btn_temp.setAutoExclusive(True)

        self.vboxLayout1.addWidget(self.btn_temp)

        self.spacerItem1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout1.addItem(self.spacerItem1)


        self.hboxLayout1.addWidget(self.menu_frame)

        self.stackedWidget = QStackedWidget(self.body_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"\n"
"QLabel {\n"
"    color: black;\n"
"}\n"
"  ")
        self.vboxLayout2 = QVBoxLayout(self.home)
        self.vboxLayout2.setSpacing(20)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout2.addItem(self.verticalSpacer)

        self.title_home = QLabel(self.home)
        self.title_home.setObjectName(u"title_home")
        font = QFont()
        font.setFamilies([u"ItalicC"])
        font.setPointSize(35)
        font.setBold(True)
        self.title_home.setFont(font)
        self.title_home.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout2.addWidget(self.title_home)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout2.addItem(self.verticalSpacer_2)

        self.subtitle_home = QLabel(self.home)
        self.subtitle_home.setObjectName(u"subtitle_home")
        font1 = QFont()
        font1.setPointSize(30)
        self.subtitle_home.setFont(font1)
        self.subtitle_home.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout2.addWidget(self.subtitle_home)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout2.addItem(self.verticalSpacer_3)

        self.desc_home = QLabel(self.home)
        self.desc_home.setObjectName(u"desc_home")
        self.desc_home.setMaximumSize(QSize(985, 16777215))
        font2 = QFont()
        font2.setPointSize(16)
        self.desc_home.setFont(font2)
        self.desc_home.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.desc_home.setWordWrap(True)

        self.vboxLayout2.addWidget(self.desc_home)

        self.footer_home = QLabel(self.home)
        self.footer_home.setObjectName(u"footer_home")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setItalic(True)
        self.footer_home.setFont(font3)
        self.footer_home.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout2.addWidget(self.footer_home)

        self.stackedWidget.addWidget(self.home)

        self.hboxLayout1.addWidget(self.stackedWidget)


        self.vboxLayout.addWidget(self.body_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ECOLAB HMI", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"\u2630", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"\u2715", None))
#if QT_CONFIG(tooltip)
        self.btn_home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_lamp.setToolTip(QCoreApplication.translate("MainWindow", u"Control Lamp", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_temp.setToolTip(QCoreApplication.translate("MainWindow", u"Control AC", None))
#endif // QT_CONFIG(tooltip)
        self.title_home.setText(QCoreApplication.translate("MainWindow", u"Selamat Datang", None))
        self.subtitle_home.setText(QCoreApplication.translate("MainWindow", u"HMI Portable ECOLAB", None))
        self.desc_home.setText(QCoreApplication.translate("MainWindow", u"\n"
"Aplikasi ini digunakan untuk mengontrol lampu dan AC secara portable melalui HMI, sehingga meningkatkan fleksibilitas dan mobilitas pengguna.\n"
"     ", None))
        self.footer_home.setText(QCoreApplication.translate("MainWindow", u"Proyek Praktek Mandiri Lintas Disiplin \u2022 2026", None))
    # retranslateUi

