import ssl
import threading

import paho.mqtt.client as mqtt


class MqttClient:
    def __init__(
        self,
        broker="10.33.11.148",
        port=1883,
        username=None,
        password=None,
        ca_cert_path=None,
        use_tls=False,
        logger=None,
    ):
        self.broker = broker
        self.port = port
        self.logger = logger
        # Subscription disimpan dulu agar bisa didaftarkan ulang setelah connect sukses.
        self._subscriptions = []

        self.client = mqtt.Client()

        if use_tls:
            if ca_cert_path is None:
                raise ValueError("ca_cert_path is required when use_tls=True")

            self.client.tls_set(
                ca_certs=ca_cert_path,
                tls_version=ssl.PROTOCOL_TLSv1_2,
            )

        if username and password:
            self.client.username_pw_set(username, password)

        self.client.on_connect = self._on_connect

    def _log(self, message):
        if self.logger:
            self.logger(message)
        else:
            print(message)

    def start(self):
        # Loop MQTT dijalankan di thread terpisah supaya UI Qt tidak freeze.
        threading.Thread(target=self._run, daemon=True).start()

    def _run(self):
        try:
            self._log(f"[MQTT] Connecting to {self.broker}:{self.port}")
            self.client.connect(self.broker, self.port, 60)
            self.client.loop_forever()
        except Exception as exc:
            self._log(f"[MQTT] Connection failed: {exc}")

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self._log(f"[MQTT] Connected to {self.broker}:{self.port}")
            # Semua subscribe yang dikumpulkan sebelum connect didaftarkan di sini.
            for topic, callback in self._subscriptions:
                client.subscribe(topic)
                client.message_callback_add(topic, callback)
                self._log(f"[MQTT] Subscribed: {topic}")
        else:
            self._log(f"[MQTT] Connection failed with rc={rc}")

    def subscribe(self, topic, callback):
        self._subscriptions.append((topic, callback))

        # Jika client sudah online, subscription baru bisa langsung diaktifkan.
        if self.client.is_connected():
            self.client.subscribe(topic)
            self.client.message_callback_add(topic, callback)
            self._log(f"[MQTT] Subscribed: {topic}")

    def publish(self, topic, payload, retain=False):
        try:
            self.client.publish(topic, payload, retain=retain)
            self._log(f"[MQTT] Published: {topic} -> {payload}")
        except Exception as exc:
            self._log(f"[MQTT] Publish failed: {exc}")
