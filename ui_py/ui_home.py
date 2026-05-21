# -*- coding: utf-8 -*-

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
    Qt,
    QTimer
)

from PySide6.QtGui import (
    QFont,
    QIcon,
    QPixmap
)

from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget
)

# =========================================================
# MAIN UI
# =========================================================

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")

        MainWindow.resize(1024, 600)

        # =========================
        # CENTRAL WIDGET
        # =========================
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.centralwidget.setStyleSheet("""
QWidget#centralwidget{
    background-color:#0D1820;
}

QFrame#topbar{
    background-color:#111F2C;
}

QFrame#menu_frame{
    background-color:#111F2C;
}

QPushButton{
    border:none;
    border-radius:10px;
    background-color:#1A3040;
    color:white;
}

QPushButton:hover{
    background-color:#00C2FF;
}

QPushButton#btn_exit{
    background-color:#1A3040;
    color:red;
    font-weight:bold;
    font-size:18px;
    border-radius:10px;
}

QPushButton#btn_exit:hover{
    background-color:#2A3A4A;
    color:red;
}

QLabel{
    color:white;
}
""")

        MainWindow.setCentralWidget(self.centralwidget)

        # =========================
        # MAIN LAYOUT
        # =========================
        self.vertical_layout = QVBoxLayout(self.centralwidget)

        # =========================
        # TOPBAR
        # =========================
        self.topbar = QFrame()
        self.topbar.setObjectName("topbar")
        self.topbar.setMinimumHeight(60)
        self.topbar.setMaximumHeight(60)

        self.topbar_layout = QHBoxLayout(self.topbar)
        self.topbar_layout.setContentsMargins(10, 5, 10, 5)
        self.topbar_layout.setSpacing(10)

        # MENU (kalau ada)
        self.topbar_layout.addWidget(
            self.btn_menu if hasattr(self, "btn_menu") else QLabel()
        )

        self.topbar_layout.addStretch()

        # =========================
        # UNDO BUTTON
        # =========================
        self.btn_undo = QPushButton("⟲")
        self.btn_undo.setMinimumSize(50, 50)

        self.btn_undo.setStyleSheet("""
QPushButton{
    background-color:#1A3040;
    color:orange;
    font-size:28px;
    font-weight:bold;
    border-radius:10px;
}
QPushButton:hover{
    background-color:#2A3A4A;
}
""")

        # =========================
        # EXIT BUTTON
        # =========================
        self.btn_exit = QPushButton("✕")
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.setMinimumSize(50, 50)

        # CLOSE WINDOW ACTION
        self.btn_exit.clicked.connect(MainWindow.close)

        # =========================
        # ADD TO TOPBAR
        # =========================
        self.topbar_layout.addWidget(self.btn_undo)
        self.topbar_layout.addWidget(self.btn_exit)

        self.vertical_layout.addWidget(self.topbar)

        # =========================
        # MAIN CONTENT
        # =========================
        self.main_layout = QHBoxLayout()
        self.vertical_layout.addLayout(self.main_layout)

        # =========================
        # MENU FRAME
        # =========================
        self.menu_frame = QFrame()
        self.menu_frame.setObjectName("menu_frame")
        self.menu_frame.setMinimumWidth(0)
        self.menu_frame.setMaximumWidth(0)
        self.menu_frame.hide()

        self.menu_layout = QVBoxLayout(self.menu_frame)

        self.menu_title = QLabel("MENU")
        self.menu_title.setAlignment(Qt.AlignCenter)
        self.menu_title.setFont(QFont("Consolas", 18, QFont.Bold))

        self.menu_layout.addWidget(self.menu_title)
        self.menu_layout.addStretch()

        self.main_layout.addWidget(self.menu_frame)

        # =========================
        # STACKED WIDGET
        # =========================
        self.stackedWidget = QStackedWidget()
        self.main_layout.addWidget(self.stackedWidget)

        # =========================
        # HOME PAGE
        # =========================
        self.home = QWidget()
        self.home_layout = QVBoxLayout(self.home)

        self.title_home = QLabel("ECOLAB")
        self.title_home.setAlignment(Qt.AlignCenter)
        self.title_home.setFont(QFont("Consolas", 36, QFont.Bold))
        self.home_layout.addWidget(self.title_home)

        self.subtitle_home = QLabel("HMI PORTABLE")
        self.subtitle_home.setAlignment(Qt.AlignCenter)
        self.subtitle_home.setFont(QFont("Consolas", 20, QFont.Bold))
        self.home_layout.addWidget(self.subtitle_home)

        self.logo_home = QLabel()
        pixmap = QPixmap("assets/ECOLABlogo.png")

        self.logo_home.setPixmap(
            pixmap.scaled(240, 240, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )
        self.logo_home.setAlignment(Qt.AlignCenter)

        self.home_layout.addWidget(self.logo_home)

        self.desc_home = QLabel("Portable Control of Lighting & AC via HMI")
        self.desc_home.setAlignment(Qt.AlignCenter)
        self.desc_home.setFont(QFont("Consolas", 12))
        self.home_layout.addWidget(self.desc_home)

        self.btn_menu_home = QPushButton("MENU")
        self.btn_menu_home.setMinimumSize(260, 70)

        self.btn_menu_home.setStyleSheet("""
QPushButton{
    background-color:#00C2FF;
    color:#0D1820;
    font-size:28px;
    font-weight:bold;
    border-radius:12px;
}
QPushButton:hover{
    background-color:white;
}
""")

        self.home_layout.addWidget(self.btn_menu_home, alignment=Qt.AlignCenter)
        self.home_layout.addStretch()

        self.stackedWidget.addWidget(self.home)

        # =========================
        # LOADING OVERLAY
        # =========================
        self.loading_overlay = QFrame(self.centralwidget)
        self.loading_overlay.setGeometry(0, 0, 1024, 600)

        self.loading_overlay.setStyleSheet("""
QFrame{
    background-color:#0A0F14;
}
QLabel{
    color:#00C2FF;
}
""")

        self.loading_layout = QVBoxLayout(self.loading_overlay)
        self.loading_layout.setAlignment(Qt.AlignCenter)

        self.loading_logo = QLabel()
        pixmap2 = QPixmap("assets/ECOLABlogo.png")

        self.loading_logo.setPixmap(
            pixmap2.scaled(420, 420, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        self.loading_layout.addWidget(self.loading_logo)

        self.loading_text = QLabel("")
        self.loading_text.setFont(QFont("Arial", 60, QFont.Bold))
        self.loading_text.setAlignment(Qt.AlignCenter)
        self.loading_layout.addWidget(self.loading_text)

        self.full_text = "ECOLAB"
        self.current_text = ""
        self.text_index = 0

        self.text_timer = QTimer()
        self.text_timer.timeout.connect(self.update_loading_text)
        self.text_timer.start(70)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    # =========================
    # LOADING ANIMATION
    # =========================
    def update_loading_text(self):
        if self.text_index < len(self.full_text):
            self.current_text += self.full_text[self.text_index]
            self.loading_text.setText(self.current_text)
            self.text_index += 1
        else:
            self.text_timer.stop()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("ECOLAB HMI")