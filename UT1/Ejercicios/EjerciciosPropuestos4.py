DESCUENTO = 15
precio = float(input("Introduce el precio: "))

precio_final = precio - precio * DESCUENTO / 100

print(f"El precio final de tu producto es: {precio_final:.2f}€")
