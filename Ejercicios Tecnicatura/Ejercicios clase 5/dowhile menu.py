sumar = 1
restar = 2
salir = 3
while True:
    opcion = int(input ("seleccione el menu: "))
    if opcion == 1:   
        print('usted eligio sumar')
    elif opcion == 2:
        print('usted eligio restar')
    elif opcion == 3:
        break
print("salio del menu")