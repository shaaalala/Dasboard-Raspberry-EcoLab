from __future__ import annotations

import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CONFIG_DIR = BASE_DIR / "config"
MQTT_CONFIG_PATH = CONFIG_DIR / "mqtt_settings.json"


DEFAULT_MQTT_CONFIG = {
    "active_profile": "laptop",
    "profiles": {
        "ecolab": {
            "broker": "10.33.11.148",
            "port": 8883,
            "username": "portableraspi",
            "password": "raspi123",
            "use_tls": True,
            "ca_cert_path": "credentials/ca.crt",
        },
        "laptop": {
            "broker": "DESKTOP-CVPE153",
            "port": 8883,
            "username": "portableraspi",
            "password": "raspi123",
            "use_tls": True,
            "ca_cert_path": "credentials/ca2.crt",
        },
    },
}


def _normalize_ca_path(raw_path: str) -> str | None:
    # Path sertifikat di JSON boleh relatif, tetapi saat runtime diubah ke absolut.
    raw_path = (raw_path or "").strip()
    if not raw_path:
        return None

    path = Path(raw_path)
    if not path.is_absolute():
        path = BASE_DIR / path
    return str(path)


def _validate_tls_config(config: dict) -> dict:
    # Validasi ini dibuat agar salah path sertifikat langsung ketahuan saat startup.
    if not config.get("use_tls"):
        return config

    ca_cert_path = config.get("ca_cert_path")
    profile_name = config.get("profile_name", "unknown")
    if not ca_cert_path:
        raise ValueError(
            f"MQTT profile '{profile_name}' requires ca_cert_path when TLS is enabled."
        )

    cert_path = Path(ca_cert_path)
    if not cert_path.exists():
        raise FileNotFoundError(
            f"MQTT profile '{profile_name}' expects certificate at '{cert_path}'."
        )

    return config


def ensure_mqtt_config() -> None:
    # Buat file config default jika project dijalankan di folder baru tanpa JSON.
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if not MQTT_CONFIG_PATH.exists():
        MQTT_CONFIG_PATH.write_text(
            json.dumps(DEFAULT_MQTT_CONFIG, indent=2),
            encoding="utf-8",
        )


def load_mqtt_config() -> dict:
    ensure_mqtt_config()

    with MQTT_CONFIG_PATH.open("r", encoding="utf-8") as file:
        loaded = json.load(file)

    # Backward compatibility for older single-profile JSON.
    if "profiles" not in loaded:
        config = dict(DEFAULT_MQTT_CONFIG["profiles"]["ecolab"])
        config.update(loaded)
        config["ca_cert_path"] = _normalize_ca_path(config.get("ca_cert_path", ""))
        config["port"] = int(config["port"])
        config["profile_name"] = "legacy"
        return _validate_tls_config(config)

    # Merge hasil file user dengan default supaya field yang belum ditulis tetap aman.
    profiles = {
        name: dict(value)
        for name, value in DEFAULT_MQTT_CONFIG["profiles"].items()
    }
    for name, value in loaded.get("profiles", {}).items():
        merged = dict(profiles.get(name, {}))
        merged.update(value)
        profiles[name] = merged

    active_profile = loaded.get(
        "active_profile",
        DEFAULT_MQTT_CONFIG["active_profile"],
    )
    if active_profile not in profiles:
        active_profile = DEFAULT_MQTT_CONFIG["active_profile"]

    # Output final selalu berupa 1 profile aktif yang siap dipakai oleh main.py.
    config = dict(profiles[active_profile])
    config["ca_cert_path"] = _normalize_ca_path(config.get("ca_cert_path", ""))
    config["port"] = int(config["port"])
    config["profile_name"] = active_profile
    return _validate_tls_config(config)
