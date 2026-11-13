"""
total = 72.4185
print (f"{total}")
"""


producto: str = input("Producto: ")
unidades: int = int(input("Unidades: "))
precio: float = float(input("Precio:   "))

base: float = unidades * precio
iva: float = base * 21 / 100
total: float = base + iva

print()
print(f"{'Base':<12}{base:>8.2f}")
print(f"{'IVA (21%)':<12}{iva:>8.2f}")
print("-" * 20)
print(f"{'TOTAL':<12}{total:>8.2f}")