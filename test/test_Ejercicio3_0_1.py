import pytest
from src.Ejercicio3_0_1 import leerEntrada, cadena, mostrarMensaje

def test_cadena():

    assert cadena(cadena("hello", ""), "o\nl\nl\ne\nh\n")

def test_mostrarMensaje():
    frase = "hola"
    resultadoEsperado = f"La cadena desde el final hasta el principio:\n{frase}\n"
    assert mostrarMensaje(frase) == resultadoEsperado