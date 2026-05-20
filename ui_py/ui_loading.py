from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QFrame


class LoadingScreen(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Loading")
        self.resize(1024, 600)

        # ============================================
        # OVERLAY (ABSOLUTE, NO LAYOUT)
        # ============================================

        self.loading_overlay = QFrame(self)
        self.loading_overlay.setGeometry(0, 0, self.width(), self.height())
        self.loading_overlay.setAttribute(Qt.WA_StyledBackground, True)
        self.loading_overlay.raise_()

        self.loading_overlay.setStyleSheet("""
            QFrame{
                background-color:black;
            }
            QLabel{
                color:#00C2FF;
                background:transparent;
            }
        """)

        # ============================================
        # LOGO
        # ============================================

        self.logo = QLabel(self.loading_overlay)

        pixmap = QPixmap("assets/ECOLABlogo.png")

        self.logo.setPixmap(
            pixmap.scaled(
                600,
                600,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        self.logo.setAlignment(Qt.AlignCenter)

        self.logo.setGeometry(
            int(self.width()/2 - 300),
            80,
            600,
            600
        )

        # ============================================
        # TEXT
        # ============================================

        self.text = QLabel(self.loading_overlay)

        font = QFont("LONDON", 80, QFont.Bold)
        self.text.setFont(font)

        self.text.setAlignment(Qt.AlignCenter)

        self.text.setGeometry(
            0,
            420,
            self.width(),
            120
        )

        # ============================================
        # ANIMATION
        # ============================================

        self.full_text = "ECOLAB"
        self.current_text = ""
        self.index = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_text)
        self.timer.start(80)

    # ============================================
    # FORCE FULLSCREEN FIX
    # ============================================

    def resizeEvent(self, event):

        self.loading_overlay.setGeometry(0, 0, self.width(), self.height())

        self.logo.setGeometry(
            int(self.width()/2 - 300),
            80,
            600,
            600
        )

        self.text.setGeometry(
            0,
            420,
            self.width(),
            120
        )

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