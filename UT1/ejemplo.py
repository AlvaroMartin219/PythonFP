edad=int(input("Cuantos años tienes? "))
print(f"Tienes {edad}")

if edad <=0:
    print("No puedes tener menos de 0 años")
elif edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")