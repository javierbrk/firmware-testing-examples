"""Placeholder SIL (software-in-the-loop) para que el job `sil` del CI tenga
al menos un test. Reemplazar por tests contra el firmware compilado para host
o un emulador (QEMU, renode, etc.)."""
import pytest

from firmware_utils import crc8


@pytest.mark.sil
def test_sil_smoke():
    assert crc8(b"\x01\x02\x03") == 0x48
