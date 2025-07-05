entrada_actual = input("Ingrese el año actual: ")

if entrada_actual.isnumeric():
    print("La entrada es numerica")
    año_actual = int(entrada_actual)
else:
    print("Error: dato incorrecto debe ser numerica ")

otra_entrada = input("Ingrese otro año: ")
if otra_entrada.isnumeric():
    print("La entrada es numerica")
    otro_año = int(otra_entrada)
else:
    print("Error: dato incorrecto debe ser numerica ")


if año_actual == otro_año:
        print("Has introducido el mismo año.")

elif otro_año < año_actual:
        años_pasados = año_actual - otro_año
        print(f"Han pasado {años_pasados} años")

else:
        años_pasados = otro_año - año_actual
        print(f"Faltan {años_pasados} años")    