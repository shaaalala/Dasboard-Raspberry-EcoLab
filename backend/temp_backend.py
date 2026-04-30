from PySide6.QtCore import QObject, Signal


class TempBackend(QObject):
    # Signal Qt dipakai untuk meneruskan data backend ke UI secara reaktif.
    ac_status_changed = Signal(bool)
    temp_changed = Signal(int)
    mode_changed = Signal(str)
    mcu_status_changed = Signal(bool)

    TOPIC_AC_CONTROL = "ecolab/mcuB/ac/control"
    TOPIC_AC_STATUS = "ecolab/mcuB/ac/status"
    TOPIC_MCU_STATUS = "ecolab/mcuB/status"
    TOPIC_TEMP_A = "ecolab/mcuA/dht/temperature"
    TOPIC_TEMP_B = "ecolab/mcuB/dht/temperature"

    def __init__(self, mqtt_client, logger=None):
        super().__init__()
        self.mqtt = mqtt_client
        self.logger = logger

        # State lokal dipakai untuk sinkronisasi tampilan tombol dan setpoint.
        self.ac_on = False
        self.current_temp = 24
        self.current_mode = "COOL"
        self.online = False

        self._subscribe_topics()
        self.temp_changed.emit(self.current_temp)
        self.mode_changed.emit(self.current_mode)

    def _log(self, message):
        if self.logger:
            self.logger(message)
        else:
            print(message)

    def _subscribe_topics(self):
        # Satu backend menerima status AC, status MCU, dan dua sumber sensor suhu.
        self.mqtt.subscribe(self.TOPIC_AC_STATUS, self._on_ac_status)
        self.mqtt.subscribe(self.TOPIC_MCU_STATUS, self._on_mcu_status)
        self.mqtt.subscribe(self.TOPIC_TEMP_A, self._on_sensor_temp)
        self.mqtt.subscribe(self.TOPIC_TEMP_B, self._on_sensor_temp)

    def set_ac(self, state):
        # UI mengirim bool, tetapi perangkat di sisi MQTT memakai string ON/OFF.
        payload = "ON" if state else "OFF"
        self.mqtt.publish(self.TOPIC_AC_CONTROL, payload)
        self._log(f"[AC] {self.TOPIC_AC_CONTROL} -> {payload}")

    def set_temp(self, value):
        try:
            value = int(value)
        except (TypeError, ValueError):
            return

        # Perangkat AC menerima perintah step-by-step, bukan setpoint absolut.
        value = max(16, min(30, value))
        diff = value - self.current_temp

        if diff > 0:
            # Kirim beberapa perintah karena AC diasumsikan punya tombol naik/turun, bukan set nilai langsung.
            for _ in range(diff):
                self.mqtt.publish(self.TOPIC_AC_CONTROL, "TEMP_UP")
        elif diff < 0:
            for _ in range(abs(diff)):
                self.mqtt.publish(self.TOPIC_AC_CONTROL, "TEMP_DOWN")

        self.current_temp = value
        self.temp_changed.emit(self.current_temp)
        self._log(f"[AC] Setpoint -> {self.current_temp}C")

    def set_mode(self, mode):
        mode = str(mode).strip().upper()
        if mode == "COOL":
            payload = "MODE_COOL"
        elif mode == "FAN":
            payload = "MODE_FAN"
        else:
            return

        self.mqtt.publish(self.TOPIC_AC_CONTROL, payload)
        self.current_mode = mode
        self.mode_changed.emit(self.current_mode)
        self._log(f"[AC] Mode -> {self.current_mode}")

    def _on_ac_status(self, client, userdata, msg):
        # Callback ini dipanggil otomatis oleh paho-mqtt saat topic status AC menerima pesan.
        state = msg.payload.decode().strip().upper() == "ON"
        self.ac_on = state
        self.ac_status_changed.emit(state)

    def _on_mcu_status(self, client, userdata, msg):
        online = msg.payload.decode().strip().lower() == "online"
        self.online = online
        self.mcu_status_changed.emit(online)

    def _on_sensor_temp(self, client, userdata, msg):
        try:
            value = round(float(msg.payload.decode().strip()))
        except ValueError:
            return

        # Filter sederhana untuk menahan data sensor yang jelas tidak masuk akal.
        if -10 <= value <= 60:
            # Backend meneruskan suhu sensor ke UI tanpa mengubah setpoint AC lokal.
            self.temp_changed.emit(int(value))
