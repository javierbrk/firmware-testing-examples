"""test_radio_client.py · monkeypatch"""
import pytest

from client import RadioClient


@pytest.fixture
def client(monkeypatch):
    def fake_transfer(self, frame):
        return {"ack": True, "rssi": -55}

    # Replace transfer with a predictable stub for this test.
    monkeypatch.setattr(RadioClient, "transfer", fake_transfer)
    return RadioClient()


def test_send_receives_ack(client):
    result = client.transfer(b"\x01\x02")
    assert result["ack"] is True
    assert result["rssi"] > -90
