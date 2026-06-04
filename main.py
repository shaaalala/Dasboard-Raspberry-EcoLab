import os
import sys
from pathlib import Path

from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt, QTimer
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsOpacityEffect
)

from backend.lamp_backend import LampBackend
from backend.mqtt_client import MqttClient
from backend.temp_backend import TempBackend
from config import load_mqtt_config
from pages.lamp_page import LampPage
from pages.temp_page import TempPage
from ui_py.ui_home import Ui_MainWindow
from ui_py.ui_menu import Ui_MenuPage

BASE_DIR = Path(__file__).resolve().parent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)

        # =========================
        # UI HOME
        # =========================
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # =========================
        # MENU PAGE
        # =========================
        self.menu_ui = Ui_MenuPage()
        self.ui.stackedWidget.addWidget(self.menu_ui)

        # =========================
        # MQTT
        # =========================
        self.mqtt_config = load_mqtt_config()
        self.mqtt = MqttClient(
            broker=self.mqtt_config["broker"],
            port=self.mqtt_config["port"],
            username=self.mqtt_config["username"] or None,
            password=self.mqtt_config["password"] or None,
            ca_cert_path=self.mqtt_config["ca_cert_path"],
            use_tls=self.mqtt_config["use_tls"],
        )
        self.mqtt.start()

        # =========================
        # BACKEND
        # =========================
        self.lamp_backend = LampBackend(self.mqtt)
        self.temp_backend = TempBackend(self.mqtt)

        self.lamp_page = LampPage(self.lamp_backend)
        self.temp_page = TempPage(self.temp_backend)

        self.ui.stackedWidget.addWidget(self.lamp_page)
        self.ui.stackedWidget.addWidget(self.temp_page)

        # DEFAULT PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        # =========================
        # SIGNAL HOME
        # =========================
        self.ui.btn_menu_home.clicked.connect(self.show_menu)
        self.ui.btn_exit.clicked.connect(self.close)

        # =========================
        # SIGNAL MENU
        # =========================
        self.menu_ui.btn_lamp.clicked.connect(self.show_lamp)
        self.menu_ui.btn_ac.clicked.connect(self.show_temp)
        self.ui.btn_undo.clicked.connect(self.go_back)
        self.ui.btn_exit.clicked.connect(self.close)

        # =========================
        # LOADING EFFECT
        # =========================
        effect = QGraphicsOpacityEffect()
        self.ui.loading_text.setGraphicsEffect(effect)
        effect.setOpacity(0)

        self.anim = QPropertyAnimation(effect, b"opacity")
        self.anim.setDuration(3000)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.start()

        QTimer.singleShot(3500, self.ui.loading_overlay.hide)

        # DRAG WINDOW
        self.dragPos = None

    # =========================
    # NAVIGATION
    # =========================
    def show_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

    def show_menu(self):
        self.ui.stackedWidget.setCurrentWidget(self.menu_ui)

    def show_lamp(self):
        self.ui.stackedWidget.setCurrentWidget(self.lamp_page)

    def show_temp(self):
        self.ui.stackedWidget.setCurrentWidget(self.temp_page)

    def go_back(self):

        current = self.ui.stackedWidget.currentWidget()

        if current == self.lamp_page:
            self.show_menu()

        elif current == self.temp_page:
            self.show_menu()

        elif current == self.menu_ui:
            self.show_home()

        else:
            self.show_home()
    # =========================
    # DRAG WINDOW
    # =========================
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.dragPos:
            delta = event.globalPosition().toPoint() - self.dragPos
            self.move(self.pos() + delta)
            self.dragPos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.dragPos = None


if __name__ == "__main__":

    os.chdir(BASE_DIR)

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    QTimer.singleShot(100, window.ui.loading_overlay.show)
    QTimer.singleShot(100, window.ui.loading_overlay.raise_)

    sys.exit(app.exec())