tiempo = int(input("Introduce el tiempo en segundos: "))

horas = tiempo / 3600
minutos = (tiempo % 3600)/60
segundos = tiempo % 60

print(f"El tiempo {tiempo} en horas, minutos y segundos es: {horas}:{minutos}:{segundos}")