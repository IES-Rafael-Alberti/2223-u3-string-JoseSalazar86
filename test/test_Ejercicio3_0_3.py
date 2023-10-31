import pytest
from src.Ejercicio3_0_3 import leerEntrada, cuenta, mostrarMensaje

def test_cuenta():
    assert cuenta("banana","a") == 3
    assert cuenta("banana","b") == 1
    assert cuenta("banana","x") == 0