from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)


class LoadingScreen(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Loading")

        self.resize(1024, 600)

        self.setStyleSheet("""

        QWidget{
            background-color:black;
        }

        QLabel{
            color:#00C2FF;
        }

        """)

        layout = QVBoxLayout(self)

        layout.setAlignment(Qt.AlignCenter)

        # ============================================
        # LOGO
        # ============================================

        self.logo = QLabel()

        pixmap = QPixmap("assets/ECOLABlogo.png")

        self.logo.setPixmap(
            pixmap.scaled(
                440,
                440,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        self.logo.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.logo)

        # ============================================
        # TEXT
        # ============================================

        self.text = QLabel("")

        font = QFont("LONDON", 25, QFont.Bold)

        self.text.setFont(font)

        self.text.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.text)

        # ============================================
        # ANIMATION TEXT
        # ============================================

        self.full_text = "ECOLAB DASHBOARD"

        self.current_text = ""

        self.index = 0

        self.timer = QTimer()

        self.timer.timeout.connect(self.update_text)

        self.timer.start(80)

    # ============================================
    # TEXT ANIMATION
    # ============================================

    def update_text(self):

        if self.index < len(self.full_text):

            self.current_text += self.full_text[self.index]

            self.text.setText(self.current_text)

            self.index += 1

        else:

            self.timer.stop()