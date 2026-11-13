# Escribe la función más pequeña posible que evite repetir el cálculo del IVA en un programa que factura tres artículos.
def calcular_iva (precio: float, IVA: int = 21):
    calculo = precio * (1 + IVA / 100)
    return calculo


print(calcular_iva(20))
print(calcular_iva(50))
print(calcular_iva(100))
