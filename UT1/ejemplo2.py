"""
nombre: str = input ("Cual es tu nombre: ")
saludo: str = "Hola " + nombre
print (f"Hola como estas, {nombre} este es mi saludo: {saludo}")
"""
# nombre: str = input ("Cual es tu nombre: ")
# saludo: str = "Hola " + nombre
# print (f"Hola como estas, {nombre} este es mi saludo: {saludo}")

"""

nombre: str = input ("Cual es tu nombre: ")
saludo: str = "Hola " + nombre
print (f"Hola como estas, {nombre} este es mi saludo: {saludo}")
"""
"""
n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
suma = n1 + n2
print (f"La suma de tus numeros es: {suma}")

"""
"""
suma = 0
contador = 0
for i in range (1,10):
    contador=+1
    numero = int(input(f"Introduce el numero {contador} que quieres sumar: "))
    
    suma = suma + numero
    print (f"La suma de tus numeros es: {suma}")
"""

caracter: str = "Alvaro"
numero: int = 2
decimal: float = 2.4
condicion: bool = True
print(f"Caracter {caracter}, tipo {type(caracter)}")
print(f"el segundo tipo es un numero entero: {numero}, tipo {type(numero)}")
print(f"el tercer tipo es decimal: {decimal}, tipo {type(decimal)}")
print(f"el cuarto tipo es booleano: {condicion}, tipo {type(condicion)}")
