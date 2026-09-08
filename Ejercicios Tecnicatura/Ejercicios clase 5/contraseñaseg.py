contraseña = 'python123'
ingcontr = input('ingrese su contraseña: ')
while ingcontr != contraseña:
    print ('contraseña incorrecta, intente nuevamente')
    ingcontr = input('ingrese la contraseña: ')
print ('bienvenido')

'''esta mal porque contraseña no deberia ser una variable'''