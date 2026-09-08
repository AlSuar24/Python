peso_equip = int(input('ingrese el peso del equipaje: '))
if peso_equip < 8:
    print ('El equipaje esta dentro del peso permitido\n Puede viajar')
else:
    print ('El equipaje excede el peso permitido\n Se cobrara un adicional')