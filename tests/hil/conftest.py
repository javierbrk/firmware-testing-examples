"""Fixtures para tests HIL con Labgrid.

`target` y `strategy` los provee el plugin de Labgrid (--lg-env).
"""
import os

import pytest


@pytest.fixture
def shell(target):
    # Se obtiene sin activar: la strategy lo activa en transition("shell").
    return target.get_driver("ShellDriver", activate=False)


@pytest.fixture(scope="session")
def build_version():
    """Versión esperada del build bajo prueba (la inyecta el CI)."""
    return os.environ.get("BUILD_VERSION", "dev")
