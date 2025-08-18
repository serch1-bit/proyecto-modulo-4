import matplotlib.pyplot as plt 

# Pedir rango de años
año_inicial = int(input("Ingrese el año inicial: "))
año_final = int(input("Ingrese el año final: "))

# Listas para guardar datos
años = []
ventas = []

# Recolección de datos
for año in range(año_inicial, año_final + 1):
    venta = float(input(f"Ingrese las ventas del año {año}: "))
    años.append(año)
    ventas.append(venta)

# Mostrar los datos ingresados
print("Años ingresados:", años)
print("Ventas correspondientes:", ventas)

# Graficar datos
plt.plot(años, ventas, color="blue")
plt.title(f"Venta del {año_inicial} al {año_final}")
plt.xlabel("Años")
plt.ylabel("Ventas")
plt.grid(True)
plt.show()

