

#for numero in range(1, 11):
#    if numero % 2 == 1:
#        continue
#    print(f'{numero} es un numero par')

    # Uso de la sentencia continue

#numero = 0
#while numero < 11:
#    numero += 1
#    if numero % 2 == 0:
#        continue
#    print(f'{numero} es un numero impar')

# Uso de la sentencia break

#numero = int(input('Ingrese un digito: '))
#limite_inferor = 0
#limite_superor = 10
#buscado = 5
#intentos = 0

# while True:
#     intentos += 1
#     if intentos == buscado:
#         print(f'El {numero} numero fue encontrado en {intentos} intentos')
#         break
#     elif numero < buscado:
#         limite_superor = buscado
#         buscado = (buscado + limite_inferor) // 2
#     else:
#         limite_inferor = buscado
#         buscado = (buscado + limite_superor) // 2

# print('Fin del programa')


# Uso de la funcion exit()

# numero = int(input('Ingrese un digito: '))
# limite_inferor = 0
# limite_superor = 10
# buscado = 5
# intentos = 0

# while True:
#     intentos += 1
#     if intentos == buscado:
#         print(f'El {numero} numero fue encontrado en {intentos} intentos')
#         exit()
#     elif numero < buscado:
#         limite_superor = buscado
#         buscado = (buscado + limite_inferor) // 2
#     else:
#         limite_inferor = buscado
#         buscado = (buscado + limite_superor) // 2

# print('Fin del programa')
# print('Impresion despues del uso de la senrencia break')
# print('Impresion despues del uso de la senrencia exit()')

intentos = 0
while True:
    intentos += 1
    print(f'Intento {intentos}')
    if intentos == 20:
        print('Fin del programa')
    exit()
