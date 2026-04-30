# pages/lamp_page.py
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from ui_py.ui_lamp import Ui_Form


class LampPage(QWidget):
    def __init__(self, backend=None):
        super().__init__()

        # =========================
        # UI
        # =========================
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.backend = backend

        # =========================
        # ICON
        # =========================
        self.icon_off = QIcon("assets/LAMP OFF.png")
        self.icon_on = QIcon("assets/LAMP ON.png")

        # =========================
        # BUTTON LIST
        # =========================
        self.buttons = [
            self.ui.lamp1,
            self.ui.lamp2,
            self.ui.lamp3,
            self.ui.lamp4,
            self.ui.lamp5
        ]

        # =========================
        # INIT BUTTON
        # =========================
        for i, btn in enumerate(self.buttons, start=1):
            btn.setChecked(False)
            btn.setIcon(self.icon_off)
            btn.setText(f"Lamp {i}\nOFF")

            btn.clicked.connect(
                # idx=i diperlukan agar setiap lambda menyimpan nomor lampu yang benar.
                lambda checked, idx=i: self.toggle_lamp(idx, checked)
            )

        # =========================
        # CONNECT BACKEND
        # =========================
        if self.backend:
            self.backend.lamp_changed.connect(self.update_lamp)
            self.backend.mcu_status.connect(self.update_mcu_status)

        # INIT MCU STATUS
        self.update_mcu_status(False)

    # =========================
    # BUTTON ACTION
    # =========================
    def toggle_lamp(self, idx, state):
        if self.backend:
            # Page hanya meneruskan aksi user; keputusan publish ada di backend.
            self.backend.publish(idx, state)

    # =========================
    # UPDATE FROM MQTT
    # =========================
    def update_lamp(self, lamp_index, state):
        btn = self.buttons[lamp_index - 1]

        # blockSignals mencegah update dari MQTT memicu clicked() lagi dan membuat loop.
        btn.blockSignals(True)

        btn.setChecked(state)
        btn.setIcon(self.icon_on if state else self.icon_off)

        status_text = "ON" if state else "OFF"
        btn.setText(f"Lamp {lamp_index}\n{status_text}")

        btn.blockSignals(False)

    # =========================
    # MCU STATUS
    # =========================
    def update_mcu_status(self, connected):
        if connected:
            self.ui.label_MCUA.setText("MCU A: CONNECTED")
            self.ui.label_MCUA.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.ui.label_MCUA.setText("MCU A: DISCONNECTED")
            self.ui.label_MCUA.setStyleSheet("color: red; font-weight: bold;")
