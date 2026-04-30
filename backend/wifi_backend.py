import subprocess

class WifiBackend:
    def connect(self, ssid, password):
        try:
            # Modul ini bergantung pada `nmcli`, jadi hanya relevan di Linux yang menyediakan NetworkManager.
            cmd = f"nmcli dev wifi connect '{ssid}' password '{password}'"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

            if result.returncode == 0:
                return True, "WiFi berhasil connect"
            else:
                return False, result.stderr

        except Exception as e:
            return False, str(e)
