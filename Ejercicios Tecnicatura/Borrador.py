alumno = {
    "nombre": "Juan",
    "edad": 22,
    "carrera": "IA"
}

# Acceso directo de alta velocidad referenciando la clave nominal como índice
print(alumno["nombre"])  # Retorna el objeto asociado: "Juan"

# Inserción o actualización dinámica de un par clave-valor
alumno["edad"] = 23      # Modifica el valor de la clave existente
alumno["sucursal"] = 1   # Inserta una clave nueva en el mapa de datos

# Recorrido especializado abstrayendo los pares mediante el método .items()
for clave, valor in alumno.items():
    print(f"Clave de campo: {clave} : {valor}")