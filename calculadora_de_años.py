año_actual = int(input("Introduce el año actual: "))
año_nuevo = int(input("Introduce otro año para calcular: "))

if año_actual == año_nuevo:
    print("Has ingresado el mismo año.")
else:
    diferencia = abs(año_actual - año_nuevo)

    if año_nuevo < año_actual:
        if diferencia == 1:
            print("Ha pasado 1 año desde", año_nuevo, "hasta", año_actual)
        else:
            print("Han pasado", diferencia, "años desde", año_nuevo, "hasta", año_actual)
    else:
        if diferencia == 1:
            print("Falta 1 año para llegar a", año_nuevo)
        else:
            print("Faltan", diferencia, "para llegar a", año_nuevo)