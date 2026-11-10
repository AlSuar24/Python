num = int(input('ingrese numero: '))
if num % 2==0 and num > 0:
    print (f'el numero {num} es par y positivo')
elif num % 2 == 0 and num <= 0:
    print (f'el numero {num} es par y negativo')
elif num % 2 != 0 and num > 0:
    print (f'el numero {num} es impar y positivo')
else:
    print (f'el numero {num} es impar y negativo')