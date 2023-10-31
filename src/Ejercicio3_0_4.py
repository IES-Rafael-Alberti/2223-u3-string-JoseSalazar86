'''
Ejercicio 3.0.4¶

Hay un método de cadenas llamado count que es similar a find. 
Lee la documentación de este método en: * Métodos en ingles * Métodos en castellano

y escribe el código necesario para invocar a este método y contar el número de veces 
que una letra aparece en “banana”
'''

def leerEntrada():
    palabra = input("Introduce la palabra: ")
    letra = input("Introduce la letra: ")
    return palabra, letra


def cuenta(palabra: str, letra: str) -> int:
    return palabra.count(letra)

def mostrarMensaje(palabra,letra,contador):
    return f"La letra '{letra}' aparece {contador} veces en la frase {palabra}."


if __name__ == "__main__":
    palabra, letra = leerEntrada()
    contador = cuenta(palabra, letra)
    mensaje = mostrarMensaje(palabra, letra, contador)
    print(mensaje)
