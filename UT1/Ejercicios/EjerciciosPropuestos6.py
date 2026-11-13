dinero_cent = int(input("Introduce el dinero que tienes en centimos: "))

moneda_50 = dinero_cent / 50
moneda_20 = dinero_cent / 50
moneda_10 = (dinero_cent / 20)%10
moneda_5 = (dinero_cent / 10)% 5
moneda_2 = (dinero_cent  / 5)% 2
moneda_1 = (dinero_cent / 2) %1

print (f"El dinero {dinero_cent} en monedas es: \n{moneda_50}50cent \n{moneda_20}20cent \n{moneda_10}10cent \n{moneda_5}5cent \n{moneda_2}2cent \n{moneda_1}1cent")


c: int = int(input("Céntimos: "))
for valor in (50, 20, 10, 5, 2, 1):
    print(f"{valor}c: {c // valor}")
    c = c % valor