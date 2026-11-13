# Escribe potencia(base, exponente) con exponente a 2 por defecto, y comprueba que los parámetros con valor por defecto van al final.

def potencia(base, exponente = 2):
    return base ** exponente

resultado = potencia(5, 5)

print (resultado):