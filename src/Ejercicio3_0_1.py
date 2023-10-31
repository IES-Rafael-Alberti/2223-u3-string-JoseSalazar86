'''
Ejercicio 3.0.1
Escribe un bucle while que comience con el último carácter en la cadena y 
haga un recorrido hacia atrás hasta el primer carácter en la cadena,
imprimiendo cada letra en una línea independiente.
'''
def leerEntrada()-> str:
    frase = input("Introduce una cadena de texto: ")
    return frase

def cadena(frase:str,fraseNueva:str)-> str:
    indice = len(frase)-1
    while indice >= 0:
        fraseNueva=fraseNueva+frase[indice]+"\n"
        indice = indice -1
        
    return fraseNueva

def mostrarMensaje(frase:str):
    return f"La cadena desde el final hasta el principio:\n{frase}\n"

if __name__ == "__main__":
    fraseNueva =""
    frase = leerEntrada()
    cadena = cadena(frase,fraseNueva)
    mensaje = mostrarMensaje(cadena)
    print(mensaje)