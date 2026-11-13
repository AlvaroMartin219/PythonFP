# Este código repite lo mismo tres veces. Reescríbelo con una sola función

print(f"Hola, Ada")
print(f"Hola, Alan")
print(f"Hola, Grace")

def saludo (nombre: str):
    return f"Hola, {nombre}"

print ("-------------")
print (saludo("Ada"))
print (saludo("Alan"))
print (saludo("Grace"))