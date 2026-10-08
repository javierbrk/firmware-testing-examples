"""test_crc.py · sin hardware"""
import pytest

from firmware_utils import crc8


@pytest.mark.parametrize("data, expected", [
    (b"", 0x00),
    (b"\x00", 0x00),
    (b"\x01\x02\x03", 0x48),  # valor de referencia
])
def test_crc8(data, expected):
    assert crc8(data) == expected


def test_crc8_rejects_none():
    with pytest.raises(TypeError):
        crc8(None)
