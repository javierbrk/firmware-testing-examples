"""test_boot_shell.py · Labgrid + pytest"""
import pytest


@pytest.mark.labgrid
def test_device_reaches_shell(strategy, shell):
    """Strategy: power → boot → shell. Teardown restaura estado."""
    strategy.transition("shell")
    output = shell.run_check("uname -a")
    assert "Linux" in output[0]


@pytest.mark.labgrid
@pytest.mark.req("REQ-BOOT-01")
def test_version_matches_build(strategy, shell, build_version):
    strategy.transition("shell")
    got = shell.run_check("cat /etc/version")[0].strip()
    assert got == build_version
