# -*- coding: utf-8 -*-

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt
)

from PySide6.QtGui import (
    QColor,
    QFont,
    QIcon,
    QLinearGradient,
    QPainter,
    QPen
)

from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
     QGraphicsOpacityEffect
)

# =========================================================
# MAIN UI
# =========================================================

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(1024, 600)

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

QFrame#topbar{
    background-color:#111F2C;
    border-bottom:2px solid #00C2FF;
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
        # TOPBAR
        # =====================================================

        self.topbar = QFrame()

        self.topbar.setObjectName(u"topbar")

        self.topbar.setMinimumHeight(60)

        self.topbar_layout = QHBoxLayout(self.topbar)

        # MENU BUTTON
        self.btn_menu = QPushButton("☰")

        self.btn_menu.setObjectName(u"btn_menu")

        self.btn_menu.setMinimumSize(50, 50)

        self.topbar_layout.addWidget(self.btn_menu)

        self.topbar_layout.addStretch()

        # EXIT BUTTON
        self.btn_exit = QPushButton("✕")

        self.btn_exit.setObjectName(u"btn_exit")

        self.btn_exit.setMinimumSize(50, 50)

        self.topbar_layout.addWidget(self.btn_exit)

        # =====================================================
        # MAIN VERTICAL LAYOUT
        # =====================================================

        self.vertical_layout = QVBoxLayout(self.centralwidget)

        self.vertical_layout.addWidget(self.topbar)

        self.main_layout = QHBoxLayout()

        self.vertical_layout.addLayout(self.main_layout)

        # =====================================================
        # MENU FRAME
        # =====================================================

        self.menu_frame = QFrame()

        self.menu_frame.setObjectName(u"menu_frame")

        self.menu_frame.setMinimumWidth(100)
        self.menu_frame.setMaximumWidth(100)

        self.menu_layout = QVBoxLayout(self.menu_frame)

        # HOME BUTTON
        self.btn_home = QPushButton()

        self.btn_home.setObjectName(u"btn_home")

        self.btn_home.setIcon(QIcon("assets/HOME.png"))

        self.btn_home.setIconSize(QSize(40, 40))

        self.btn_home.setCheckable(True)

        self.menu_layout.addWidget(self.btn_home)

        # LAMP BUTTON
        self.btn_lamp = QPushButton()

        self.btn_lamp.setObjectName(u"btn_lamp")

        self.btn_lamp.setIcon(QIcon("assets/LAMP OFF.png"))

        self.btn_lamp.setIconSize(QSize(40, 40))

        self.btn_lamp.setCheckable(True)

        self.menu_layout.addWidget(self.btn_lamp)

        # TEMP BUTTON
        self.btn_temp = QPushButton()

        self.btn_temp.setObjectName(u"btn_temp")

        self.btn_temp.setIcon(QIcon("assets/AC OFF.png"))

        self.btn_temp.setIconSize(QSize(40, 40))

        self.btn_temp.setCheckable(True)

        self.menu_layout.addWidget(self.btn_temp)

        self.menu_layout.addStretch()

        self.main_layout.addWidget(self.menu_frame)

        # =====================================================
        # STACKED WIDGET
        # =====================================================

        self.stackedWidget = QStackedWidget()

        self.main_layout.addWidget(self.stackedWidget)

        # =====================================================
        # HOME PAGE
        # =====================================================

        self.home = QWidget()

        self.home_layout = QVBoxLayout(self.home)

        # TITLE
        self.title_home = QLabel("SELAMAT DATANG")

        title_font = QFont("Consolas", 30)

        title_font.setBold(True)

        self.title_home.setFont(title_font)

        self.title_home.setAlignment(Qt.AlignCenter)

        self.home_layout.addWidget(self.title_home)

        # SUBTITLE
        self.subtitle_home = QLabel("HMI PORTABLE ECOLAB")

        sub_font = QFont("Consolas", 18)

        self.subtitle_home.setFont(sub_font)

        self.subtitle_home.setAlignment(Qt.AlignCenter)

        self.home_layout.addWidget(self.subtitle_home)


        # DESCRIPTION
        self.desc_home = QLabel(
            "Aplikasi ini digunakan untuk mengontrol\n"
            "lampu dan AC secara portable melalui HMI."
        )

        desc_font = QFont("Consolas", 12)

        self.desc_home.setFont(desc_font)

        self.desc_home.setAlignment(Qt.AlignCenter)

        self.home_layout.addWidget(self.desc_home)

        self.home_layout.addStretch()

        # ADD PAGE
        self.stackedWidget.addWidget(self.home)

        # =====================================================
        # TRANSLATE
        # =====================================================
                # =====================================================
        # LOADING OVERLAY
        # =====================================================

        self.loading_overlay = QFrame(self.centralwidget)

        self.loading_overlay.setGeometry(0, 0, 1024, 600)

        self.loading_overlay.setStyleSheet("""
QFrame{
    background-color:#0D1820;
}
QLabel{
    color:#00C2FF;
}
""")

        self.loading_layout = QVBoxLayout(self.loading_overlay)

        self.loading_layout.setAlignment(Qt.AlignCenter)

        # LOGO
        self.loading_logo = QLabel()

        self.loading_logo.setPixmap(
            QIcon("assets/ECOLABlogo.png").pixmap(220, 220)
        )

        self.loading_logo.setAlignment(Qt.AlignCenter)

        self.loading_layout.addWidget(self.loading_logo)

        # TEXT
        self.loading_text = QLabel("INITIALIZING SYSTEM...")

        font = QFont("Consolas", 18)
        font.setBold(True)

        self.loading_text.setFont(font)

        self.loading_text.setAlignment(Qt.AlignCenter)

        self.loading_layout.addWidget(self.loading_text)
        
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # =========================================================
    # RETRANSLATE
    # =========================================================

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow",
                "ECOLAB HMI",
                None
            )
        )