def notas (nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
nota3 = float(input("Introduce la tercera nota: "))

print(f"La media de tus notas es: {notas(nota1, nota2, nota3)}")