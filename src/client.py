"""Cliente de radio: la dependencia de hardware que se mockea en los tests."""


class RadioClient:
    def __init__(self, port: str | None = None):
        self.port = port

    def transfer(self, frame: bytes) -> dict:
        """Envía un frame y devuelve {'ack': bool, 'rssi': int}.

        La implementación real habla con el transceiver (SPI/UART);
        en los tests unitarios se reemplaza con monkeypatch.
        """
        raise RuntimeError("RadioClient.transfer requiere hardware")
