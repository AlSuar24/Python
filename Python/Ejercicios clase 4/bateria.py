bateria = int(input('ingrese el nivel de bateria del dispositivo: % '))

if bateria <= 20:
    print ('El nivel de bateria es bajo, por favor cargue el dispositivo')
elif bateria > 20 and bateria <= 80:
    print ('El nivel de bateria es medio, puede seguir usando el dispositivo')
else:   
    print ('El nivel de bateria es alto, el dispositivo esta completamente cargado')   