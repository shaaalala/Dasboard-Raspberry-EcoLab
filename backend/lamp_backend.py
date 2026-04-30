from PySide6.QtCore import QObject, Signal


class LampBackend(QObject):
    # lamp_changed membawa dua data sekaligus: nomor lampu dan status ON/OFF.
    lamp_changed = Signal(int, bool)
    mcu_status = Signal(bool)

    BASE_TOPIC = "ecolab/mcuA/lamp"
    STATUS_TOPIC = "ecolab/mcuA/status"

    def __init__(self, mqtt_client, logger=None):
        super().__init__()
        self.mqtt = mqtt_client
        self.logger = logger
        # Menyimpan status lamp terakhir yang diterima dari MQTT.
        self.states = {}
        self.online = False

        self._subscribe_topics()

    def _log(self, message):
        if self.logger:
            self.logger(message)
        else:
            print(message)

    def _subscribe_topics(self):
        # Satu callback dipakai untuk semua status lamp berdasarkan nomor topic.
        for index in range(1, 6):
            self.mqtt.subscribe(f"{self.BASE_TOPIC}{index}/status", self._on_lamp_status)
        self.mqtt.subscribe(self.STATUS_TOPIC, self._on_mcu_status)

    def publish(self, lamp_index, state):
        # Setiap lampu punya topic control sendiri, misalnya lamp1/control, lamp2/control, dst.
        topic = f"{self.BASE_TOPIC}{lamp_index}/control"
        payload = "ON" if state else "OFF"
        self.mqtt.publish(topic, payload)
        self._log(f"[LAMP] {topic} -> {payload}")

    def _on_lamp_status(self, client, userdata, msg):
        try:
            # Nomor lampu diekstrak dari nama topic, bukan dari payload.
            lamp_index = int(msg.topic.split("lamp")[1].split("/")[0])
        except (IndexError, ValueError):
            return

        # Payload "ON"/"OFF" diterjemahkan menjadi bool agar mudah dipakai di UI.
        state = msg.payload.decode().strip().upper() == "ON"
        self.states[lamp_index] = state
        self.lamp_changed.emit(lamp_index, state)

    def _on_mcu_status(self, client, userdata, msg):
        online = msg.payload.decode().strip().lower() == "online"
        self.online = online
        self.mcu_status.emit(online)
