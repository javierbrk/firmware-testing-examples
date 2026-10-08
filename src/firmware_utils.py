"""Utilidades de firmware testeables sin hardware."""


def crc8(data: bytes, poly: int = 0x07, init: int = 0x00) -> int:
    """CRC-8 (polinomio 0x07, init 0x00, sin reflexión ni xor final)."""
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError(f"data debe ser bytes, no {type(data).__name__}")
    crc = init
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = ((crc << 1) ^ poly) & 0xFF if crc & 0x80 else (crc << 1) & 0xFF
    return crc
