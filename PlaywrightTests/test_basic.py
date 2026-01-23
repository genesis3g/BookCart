"""
Test simple para verificar que pytest y playwright funcionan
"""
import pytest


def test_simple():
    """Test básico para verificar que pytest funciona"""
    assert 1 + 1 == 2


def test_browser(browser):
    """Test que verifica que el navegador se abre"""
    assert browser is not None
