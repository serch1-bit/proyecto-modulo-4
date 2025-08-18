while True:
     contraseña = input("Ingrese una contraseña: ")
     if contraseña[0].isdigit():
         break 
     else:
         print("La contraseña debe empezar con un número. Intenta de nuevo.")

intentos = 0
while intentos < 3:
      confirmar = input("Vuelva a ingresar la contraseña: ")
if confirmar == contraseña:
        print("Contraseña correcta.")
        break
else:
         print("La contraseña no coincide.")
         intentos += 1

if intentos == 3:
        print("Demasiados intentos. Programa finalizado.")

        