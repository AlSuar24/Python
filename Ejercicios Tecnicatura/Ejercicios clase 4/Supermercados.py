importe = int(input('ingrese el monto de compra: $'))
if importe > 10000 :
    print (f'El importe tiene un 10% de descuento y el total a pagar es: ${importe - (importe*0.10)}')
else:
    print (f'El total es: ${importe}')