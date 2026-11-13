def area_y_perimetro(base: float, altura: float) -> float:
    return base * altura, 2*(base*altura)

area, perimetro = area_y_perimetro(4,3)

print (f"El area de tu rectangulo es {area} y el perimetro es {perimetro}")