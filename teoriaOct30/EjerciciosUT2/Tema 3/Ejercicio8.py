# Añade a saludar(nombre, saludo) un valor por defecto para que saludo sea "Hola" si no se indica.

def saludar (nombre, saludo = "Hola") -> str:
    return f"{saludo} {nombre}"

print(saludar("Alvaro"))

print(saludar("Lucas", "Buenos dias"))