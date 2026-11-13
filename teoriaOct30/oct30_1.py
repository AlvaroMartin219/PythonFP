def presentar(nombre: str, edad: int) -> str:
    return f"{nombre} tiene {edad} años"

print(presentar("Ana", 36))           
print(presentar(edad=36, nombre="Ana"))


#FUNCION IVA
# EN LA PRIMERA LLAMADA LE PASO SOLAMENTE EL PRECIO Y EL IVA YA ESTA INICIALIZADO
# EN LA SEGUNDA LLAMADA LE PASO EL PRECIO Y EL IVA, LO QUE HACE ES DESTRUIR LO QUE VALE EL IVA Y PONER EL NUEVO VALOR
def precio_con_iva(precio: float, iva: int = 21) -> float:
    return precio * (1 + iva / 100)

print(precio_con_iva(100))
print(precio_con_iva(100, 10)) 


def calcular() -> int:
    total = 10
    return total

calcular()
print(total)