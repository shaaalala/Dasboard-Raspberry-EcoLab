import os
import sys
from pathlib import Path

from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from backend.lamp_backend import LampBackend
from backend.mqtt_client import MqttClient
from backend.temp_backend import TempBackend
from config import load_mqtt_config
from pages.lamp_page import LampPage
from pages.temp_page import TempPage
from ui_py.ui_home import Ui_MainWindow
from backend.wifi_backend import WifiBackend

BASE_DIR = Path(__file__).resolve().parent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load profile MQTT aktif lalu buat 1 client yang dipakai semua page.
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

        # Backend menangani logika MQTT dan state untuk masing-masing fitur.
        self.lamp_backend = LampBackend(self.mqtt)
        self.temp_backend = TempBackend(self.mqtt)

        self.lamp_page = LampPage(self.lamp_backend)
        self.temp_page = TempPage(self.temp_backend)

        # Page custom ditambahkan ke stackedWidget setelah halaman home bawaan UI.
        self.ui.stackedWidget.addWidget(self.lamp_page)
        self.ui.stackedWidget.addWidget(self.temp_page)

        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.btn_home.setChecked(True)

        self.ui.btn_home.clicked.connect(self.show_home)
        self.ui.btn_lamp.clicked.connect(self.show_lamp)
        self.ui.btn_temp.clicked.connect(self.show_temp)

        self.ui.btn_menu.clicked.connect(self.toggle_menu)
        self.menu_expanded = False

        self.ui.btn_exit.clicked.connect(self.close)
        self.dragPos = None

    def show_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

    def show_lamp(self):
        self.ui.stackedWidget.setCurrentWidget(self.lamp_page)

    def show_temp(self):
        self.ui.stackedWidget.setCurrentWidget(self.temp_page)

    def toggle_menu(self):
        start_width = self.ui.menu_frame.width()
        end_width = 220 if not self.menu_expanded else 0

        # Sidebar dibuka dan ditutup dengan animasi lebar maksimum.
        self.animation = QPropertyAnimation(self.ui.menu_frame, b"maximumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(start_width)
        self.animation.setEndValue(end_width)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

        self.menu_expanded = not self.menu_expanded

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
    # Paksa working directory ke folder project agar semua path relatif tetap valid.
    os.chdir(BASE_DIR)
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
