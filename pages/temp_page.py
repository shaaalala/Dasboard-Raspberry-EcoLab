from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

from ui_py.ui_temp import Ui_temp


class TempPage(QWidget):
    def __init__(self, backend):
        super().__init__()

        self.ui = Ui_temp()
        self.ui.setupUi(self)

        self.backend = backend
        self.current_temp = 24

        self.icon_on = QIcon("assets/AC ON.png")
        self.icon_off = QIcon("assets/AC OFF.png")

        self.ui.btn_ac.clicked.connect(self.toggle_ac)
        self.ui.btn_temp_up.clicked.connect(self.temp_up)
        self.ui.btn_temp_down.clicked.connect(self.temp_down)
        self.ui.btn_cool.clicked.connect(lambda: self.set_mode("COOL"))
        self.ui.btn_fan.clicked.connect(lambda: self.set_mode("FAN"))

        # Semua perubahan dari backend dipantulkan lagi ke widget lewat signal-slot Qt.
        self.backend.ac_status_changed.connect(self.update_ac)
        self.backend.temp_changed.connect(self.update_temp)
        self.backend.mode_changed.connect(self.update_mode)
        self.backend.mcu_status_changed.connect(self.update_mcu)

    def toggle_ac(self, checked):
        self.backend.set_ac(checked)

    def temp_up(self):
        self.current_temp += 1
        self.backend.set_temp(self.current_temp)

    def temp_down(self):
        self.current_temp -= 1
        self.backend.set_temp(self.current_temp)

    def set_mode(self, mode):
        self.backend.set_mode(mode)

    def update_ac(self, state):
        # Saat status datang dari MQTT, tombol diubah tanpa memicu aksi user kedua kali.
        self.ui.btn_ac.blockSignals(True)
        self.ui.btn_ac.setChecked(state)
        self.ui.btn_ac.setIcon(self.icon_on if state else self.icon_off)
        self.ui.label_status.setText(f"Status AC: {'ON' if state else 'OFF'}")
        self.ui.btn_ac.blockSignals(False)

    def update_temp(self, value):
        # Halaman ini menyimpan suhu terakhir agar tombol +/- tahu nilai acuan berikutnya.
        self.current_temp = value

    def update_mode(self, mode):
        self.ui.btn_cool.blockSignals(True)
        self.ui.btn_fan.blockSignals(True)

        self.ui.btn_cool.setChecked(mode == "COOL")
        self.ui.btn_fan.setChecked(mode == "FAN")

        self.ui.btn_cool.blockSignals(False)
        self.ui.btn_fan.blockSignals(False)

    def update_mcu(self, online):
        if online:
            self.ui.label_MCUB.setText("MCU B: CONNECTED")
            self.ui.label_MCUB.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.ui.label_MCUB.setText("MCU B: DISCONNECTED")
            self.ui.label_MCUB.setStyleSheet("color: red; font-weight: bold;")
