"""Escenario de aceptación

# REQ-NET-12
# Dado un DUT en fábrica
# Cuando asocia a la red de test
# Entonces responde ping < 100 ms
"""
import pytest


@pytest.mark.labgrid
@pytest.mark.req("REQ-NET-12")
def test_assoc_and_ping(strategy, shell):
    strategy.transition("shell")
    shell.run_check("wifi join test-net")
    out = shell.run_check("ping -c 3 192.0.2.1")
    assert "3 received" in "".join(out)
