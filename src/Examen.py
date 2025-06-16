# 1. Crea una función de nombre enviarMensaje, que se le pasa por parámetro
#    un nombre, y al ser llamada, imprime un mensaje con el nombre de la persona
def enviarMensaje ():
    nombre = input("Escriba su nombre: ")
    return f"Hola {nombre}"

print(enviarMensaje())
'''
OUTPUT:
Hola, Fulano
'''



# 2. Dada la siguiente lista de números, imprime línea a línea cada número
numeros = [4, 3, 2, 5, 6]

def imprimirNumeros(lista):
    for i in lista:
        print(f"{i}")
    
imprimirNumeros(numeros)

'''
OUTPUT:
4
3
2
5
6
'''



# 3. Genera un bucle while que se rompe cuando el valor es un número negativo. Inicialmente,
#    el valor empieza en 5 y va reduciendo
numero = 5

'''
OUTPUT:
El número ahora es 5
El número ahora es 4
El número ahora es 3
El número ahora es 2
El número ahora es 1
'''



# 4. Generar una función que se le pasa dos números, el usuario indica por consola cada número,
#    y una vez indicados se llama a la función pasando los números que el usuario ha escrito.
#    La función sumará los números y devolverá el resultado

# print(f"SUMA: {sumar(numero1, numero2)}")



# 5. Crea una función para que, cuando se le pase una lista cualquiera, imprima sus valores en orden inverso

nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]

def imprimirListaInversa (lista):
    al_reves = lista[::-1]
    print (f"{al_reves}")


imprimirListaInversa(nombres)
'''
OUTPUT:
- Perantano
- Zutano
- Fulano
- Mengano
'''


# 6. Crear una función que busque una palabra en una lista, se le pasa la lista y la palabra a buscar
#    Si la palabra existe, devuelve True, de lo contrario False

lista_palabras = ["Fulano", "Mengano", "Zutano"]

def buscarPalabra (lista):
    
    nombre = input("Escriba un nombre: ")
    for i in lista:
        if i == nombre:
            return True
        
    return False

print(buscarPalabra(lista_palabras)) # OUTPUT: True



# 7. Crea un diccionario que contenga como clave tu nombre y como valor la cantidad de letras de la clave,
#    lo mismo con el primer y segundo apellido, quedando un diccionario de tamaño 3. Luego, utiliza un bucle
#    para imprimir el contenido



'''
OUTPUT:
Nombre
Apellido1
Apellido2
'''