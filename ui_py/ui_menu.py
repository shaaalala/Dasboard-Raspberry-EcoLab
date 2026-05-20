from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame
)

from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QHBoxLayout
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt

class Ui_MenuPage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("menu_page")

        self.setStyleSheet("""
QWidget{
    background-color:transparent;
    color:white;
}

QFrame#card{
    background-color:#111F2C;
    border-radius:18px;
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

QPushButton#icon_btn{
    background-color:#1A3040;
    border-radius:10px;
}
""")

        self.layout = QVBoxLayout(self)

        # =========================
        # TOP BUTTONS (UNDO + EXIT)
        # =========================
        top = QHBoxLayout()

        self.btn_undo = QPushButton("↶")
        self.btn_undo.setMinimumSize(45, 45)
        self.btn_undo.setObjectName("icon_btn")

        self.btn_exit = QPushButton("✕")
        self.btn_exit.setMinimumSize(45, 45)
        self.btn_exit.setObjectName("icon_btn")

        top.addWidget(self.btn_undo)
        top.addStretch()
        top.addWidget(self.btn_exit)

        self.layout.addLayout(top)

        # =========================
        # CARDS AREA
        # =========================
        cards = QHBoxLayout()

        # -------------------------
        # CARD 1 - LIGHTING
        # -------------------------
        self.card_lamp = QFrame()
        self.card_lamp.setObjectName("card")

        lamp_layout = QVBoxLayout(self.card_lamp)

        self.img_lamp = QLabel()
        self.img_lamp.setAlignment(Qt.AlignCenter)
        self.img_lamp.setPixmap(
            QPixmap("assets/LAMP ON.png").scaled(160, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        self.txt_lamp = QLabel("LIGHTING")
        self.txt_lamp.setAlignment(Qt.AlignCenter)
        self.txt_lamp.setFont(QFont("Consolas", 18, QFont.Bold))

        self.btn_lamp = QPushButton("OPEN")
        self.btn_lamp.setMinimumHeight(60)

        lamp_layout.addWidget(self.img_lamp)
        lamp_layout.addWidget(self.txt_lamp)
        lamp_layout.addWidget(self.btn_lamp)

        # -------------------------
        # CARD 2 - AC
        # -------------------------
        self.card_ac = QFrame()
        self.card_ac.setObjectName("card")

        ac_layout = QVBoxLayout(self.card_ac)

        self.img_ac = QLabel()
        self.img_ac.setAlignment(Qt.AlignCenter)
        self.img_ac.setPixmap(
            QPixmap("assets/AC OFF.png").scaled(160, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        self.txt_ac = QLabel("AC")
        self.txt_ac.setAlignment(Qt.AlignCenter)
        self.txt_ac.setFont(QFont("Consolas", 18, QFont.Bold))

        self.btn_ac = QPushButton("OPEN")
        self.btn_ac.setMinimumHeight(60)

        ac_layout.addWidget(self.img_ac)
        ac_layout.addWidget(self.txt_ac)
        ac_layout.addWidget(self.btn_ac)

        # add to row
        cards.addStretch()
        cards.addWidget(self.card_lamp)
        cards.addSpacing(30)
        cards.addWidget(self.card_ac)
        cards.addStretch()

        self.layout.addLayout(cards)

        self.layout.addStretch()