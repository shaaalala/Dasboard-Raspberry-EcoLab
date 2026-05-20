# -*- coding: utf-8 -*-

################################################################################
## FORM HOME UI
################################################################################

from PySide6.QtCore import (
    QCoreApplication, QMetaObject, QRect,
    QSize, Qt
)

from PySide6.QtGui import (
    QColor, QFont, QIcon,
    QLinearGradient, QPainter,
    QPen
)

from PySide6.QtWidgets import (
    QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget
)


# =========================================================
# CUSTOM TANK WIDGET
# =========================================================

class TankWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.level = 70

        self.setMinimumSize(180, 300)
        self.setMaximumSize(250, 350)

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w = self.width()
        h = self.height()

        # BODY TANK
        painter.setBrush(QColor("#111F2C"))
        painter.setPen(QPen(QColor("#00C2FF"), 3))

        painter.drawRoundedRect(
            50,
            20,
            120,
            250,
            35,
            35
        )

        # WATER HEIGHT
        fill_height = int((self.level / 100) * 250)

        # WATER GRADIENT
        gradient = QLinearGradient(0, 0, 0, h)

        gradient.setColorAt(0, QColor("#00C2FF"))
        gradient.setColorAt(1, QColor("#0066FF"))

        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)

        painter.drawRoundedRect(
            50,
            270 - fill_height,
            120,
            fill_height,
            30,
            30
        )

        # TEXT %
        painter.setPen(QColor("white"))

        font = QFont("Consolas", 16)
        font.setBold(True)

        painter.setFont(font)

        painter.drawText(
            QRect(0, 280, w, 40),
            Qt.AlignCenter,
            f"{self.level}%"
        )


# =========================================================
# MAIN UI
# =========================================================

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(1024, 600)
        MainWindow.setMinimumSize(QSize(1024, 600))
        MainWindow.setMaximumSize(QSize(1024, 600))

        # =====================================================
        # CENTRAL WIDGET
        # =====================================================

        self.centralwidget = QWidget(MainWindow)

        self.centralwidget.setObjectName(u"centralwidget")

        self.centralwidget.setStyleSheet("""

QWidget#centralwidget{
    background-color:#0D1820;
}

QFrame#menu_frame{
    background-color:#111F2C;
    border-right:2px solid #00C2FF;
}

QPushButton{
    border:none;
    border-radius:15px;
    background-color:#1A3040;
    color:white;
    padding:10px;
}

QPushButton:hover{
    background-color:#00C2FF;
}

QPushButton:checked{
    background-color:#0088CC;
}

QLabel{
    color:white;
}

QLabel#title_home{
    color:#00C2FF;
    font-size:38px;
    font-weight:bold;
}

QLabel#subtitle_home{
    font-size:24px;
}

QLabel#desc_home{
    font-size:15px;
}

        """)

        MainWindow.setCentralWidget(self.centralwidget)

        # =====================================================
        # MAIN LAYOUT
        # =====================================================

        self.main_layout = QHBoxLayout(self.centralwidget)

        # =====================================================
        # SIDEBAR
        # =====================================================

        self.menu_frame = QFrame()

        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumWidth(100)
        self.menu_frame.setMaximumWidth(100)

        self.menu_layout = QVBoxLayout(self.menu_frame)

        # HOME BUTTON
        self.btn_home = QPushButton()
        self.btn_home.setIcon(QIcon("assets/HOME.png"))
        self.btn_home.setIconSize(QSize(40, 40))
        self.btn_home.setCheckable(True)

        self.menu_layout.addWidget(self.btn_home)

        # LAMP BUTTON
        self.btn_lamp = QPushButton()
        self.btn_lamp.setIcon(QIcon("assets/LAMP OFF.png"))
        self.btn_lamp.setIconSize(QSize(40, 40))
        self.btn_lamp.setCheckable(True)

        self.menu_layout.addWidget(self.btn_lamp)

        # TEMP BUTTON
        self.btn_temp = QPushButton()
        self.btn_temp.setIcon(QIcon("assets/AC OFF.png"))
        self.btn_temp.setIconSize(QSize(40, 40))
        self.btn_temp.setCheckable(True)

        self.menu_layout.addWidget(self.btn_temp)

        self.menu_layout.addStretch()

        self.main_layout.addWidget(self.menu_frame)

        # =====================================================
        # CONTENT
        # =====================================================

        self.content = QWidget()

        self.content_layout = QVBoxLayout(self.content)

        # TITLE
        self.title_home = QLabel("SELAMAT DATANG")

        title_font = QFont("Consolas", 30)
        title_font.setBold(True)

        self.title_home.setFont(title_font)
        self.title_home.setAlignment(Qt.AlignCenter)

        self.content_layout.addWidget(self.title_home)

        # SUBTITLE
        self.subtitle_home = QLabel("HMI PORTABLE ECOLAB")

        sub_font = QFont("Consolas", 18)

        self.subtitle_home.setFont(sub_font)
        self.subtitle_home.setAlignment(Qt.AlignCenter)

        self.content_layout.addWidget(self.subtitle_home)

        # TANK
        self.tank = TankWidget()

        self.content_layout.addWidget(
            self.tank,
            alignment=Qt.AlignCenter
        )

        # DESCRIPTION
        self.desc_home = QLabel(
            "Aplikasi ini digunakan untuk mengontrol\n"
            "lampu dan AC secara portable melalui HMI."
        )

        desc_font = QFont("Consolas", 12)

        self.desc_home.setFont(desc_font)
        self.desc_home.setAlignment(Qt.AlignCenter)

        self.content_layout.addWidget(self.desc_home)

        self.content_layout.addStretch()

        self.main_layout.addWidget(self.content)

        # =====================================================
        # TRANSLATE
        # =====================================================

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # =========================================================
    # RETRANSLATE
    # =========================================================

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow",
                u"ECOLAB HMI",
                None
            )
        )