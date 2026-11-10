import random
numero_secreto = random.randint(1, 100)

print("¡Bienvenido al juego de adivinanza!")
print("He pensado un número entre 1 y 100. ¿Puedes adivinarlo?")

while True:
    intento = int(input("Introduce tu número: "))
    
    if intento < numero_secreto:
        print("El número secreto es mayor. ¡Intenta otra vez!")
    elif intento > numero_secreto:
        print("El número secreto es menor. ¡Intenta otra vez!")
    else:
        print(f"¡Felicitaciones! Acertaste, el número era {numero_secreto}.")
        break