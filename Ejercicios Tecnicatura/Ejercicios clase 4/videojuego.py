puntos_vida = int(input('ingrese los puntos de vida del personaje: '))
if puntos_vida >= 2:
    print ('El personaje puede luchar')
elif puntos_vida >= 1:
    print ('Soldado que huye sirve para otra batalla')
else:
    print ('GAME OVER')