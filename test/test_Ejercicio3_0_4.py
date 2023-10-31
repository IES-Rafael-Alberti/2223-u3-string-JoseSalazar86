import pytest
from src.Ejercicio3_0_3 import cuenta, mostrarMensaje

def test_cuenta():
    
    assert cuenta("banana","a") == 3
    assert cuenta("banana","x") == 0
    assert cuenta("","b") == 0
    assert cuenta("banana","") == 0
