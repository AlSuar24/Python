total = 0
precio = float(input('ingrese el precio del producto: $ (CERO PARA TERMINAR)'))
while precio != 0:
    total = total + precio
    precio = float(input('ingrese el precio del producto: $ (CERO PARA TERMINAR)'))
print (f'El total a pagar es: ${total}')

    
