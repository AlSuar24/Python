saldo = int(input('ingrese el saldo de la cuenta: $'))
monto_ret = int(input('ingrese el monto a retirar: $')) 
if monto_ret > 0 and monto_ret <= saldo:
    print (f'Puede retirar: ${monto_ret}\n El saldo restante es: ${saldo - monto_ret}')
else:    print ('No se puede realizar el retiro, saldo insuficiente')