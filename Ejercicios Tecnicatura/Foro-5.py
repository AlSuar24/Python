#ejercicio foro 5
Archivero_uno = range(1,121)
buscar = int (input("ingrese numero de legajo solicitado "))
if buscar in Archivero_uno:
    print ("el legajo", buscar, "se encuentra en el archivero uno")
else:
    print ("el legajo", buscar, "NO está en el archivero uno")
