'''
Dado que fruta es una variable de tipo cuenta, ¿qué significa fruta[:]?
Ejercicio 3.0.3¶

Tienes este código:

palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)

Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo 
que pueda aceptar una cuenta y una letra como argumentos.
'''
def leerEntrada() -> str:
    palabra = input("Introduce una palabra: ")

    contador = input("Introduce la letra que quieres contar: ")

    return palabra, contador



def cuenta(palabra,letraContar)->str:
    contador = 0
    for letra in palabra:
        if letra == letraContar:
            contador += 1
    return contador

def mostrarMensaje(palabra,letraContar,contador)-> str:
    return f"La palabra que has escrito es: {palabra} y la letra seleccionada es {letraContar} a contar aparece un total de {contador}"

if __name__ == "__main__":
    palabra, letra = leerEntrada()
    contador = cuenta(palabra, letra)
    mensaje= mostrarMensaje(palabra, letra, contador)
    print(mensaje)
