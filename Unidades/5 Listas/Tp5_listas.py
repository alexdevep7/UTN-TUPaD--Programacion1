import random

#1 Crear una lista con las notas de 10 estudiantes. 
# 	Mostrar la lista completa. 
# 	Calcular y mostrar el promedio. 
#   Indicar la nota más alta y la más baja. 

# Lista con las notas de 10 estudiantes
notas = [15, 12, 18, 10, 14, 16, 19, 13, 17, 11]

print("Notas de los estudiantes:")
for nota in notas:
    print(nota)

# Calcular promedio
suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
print("\nPromedio de notas:", promedio)

# Buscar nota más alta y más baja 
nota_max = notas[0]
nota_min = notas[0]

for nota in notas:
    if nota > nota_max:
        nota_max = nota
    if nota < nota_min:
        nota_min = nota

print("Nota más alta:", nota_max)
print("Nota más baja:", nota_min)

#2 Pedir al usuario que cargue 5 productos en una lista. 
# 	Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
#   Preguntar al usuario qué producto desea eliminar y actualizar la lista. 

productos = []

# Pedir al usuario que cargue 5 productos
for i in range(5):
    prod = input(f"Ingrese el producto {i+1}: ")
    productos.append(prod)

# Mostrar la lista ordenada alfabéticamente usando sorted()
print("\nLista de productos ordenada alfabéticamente:")
lista_ordenada = sorted(productos)
for prod in lista_ordenada:
    print(prod)

eliminar = input("\nIngrese el producto que desea eliminar: ")

# Si el producto está en la lista, lo eliminamos
if eliminar in productos:
    productos.remove(eliminar)
    print(f"\nEl producto '{eliminar}' fue eliminado.")
else:
    print(f"\nEl producto '{eliminar}' no se encuentra en la lista.")

# Mostrar lista actualizada
print("\nLista actualizada de productos:")
for prod in productos:
    print(prod)


#3 Generar una lista con 15 números enteros al azar entre 1 y 100. 
# 	Crear una lista con los pares y otra con los impares. 
#   Mostrar cuántos números tiene cada lista. 

numeros = []
for i in range(15):
    numeros.append(random.randint(1, 100))

print("Lista de números generados:")
for num in numeros:
    print(num)

# Crear listas de pares e impares
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Mostrar listas y cantidad de elementos
print("\nNúmeros pares:")
for p in pares:
    print(p)
print("Cantidad de pares:", len(pares))

print("\nNúmeros impares:")
for imp in impares:
    print(imp)
print("Cantidad de impares:", len(impares))


#4 Dada una lista con valores repetidos: 
# 	Crear una nueva lista sin elementos repetidos. 
# 	Mostrar el resultado. 
# 	datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# 	Crear una nueva lista sin elementos repetidos. 
#   Mostrar el resultado. 

# Lista original con valores repetidos
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

print("Lista original:")
for d in datos:
    print(d)

# Crear nueva lista sin elementos repetidos
sin_repetidos = []

for d in datos:
    if d not in sin_repetidos:
        sin_repetidos.append(d)

# Mostrar resultado
print("\nLista sin elementos repetidos:")
for d in sin_repetidos:
    print(d)

#5 Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# 	Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
#   Mostrar la lista final actualizada. 

# Lista inicial con 8 estudiantes
estudiantes = ["Ana", "Luis", "Pedro", "María", "Sofía", "Carlos", "Lucía", "Diego"]

print("Lista de estudiantes actuales:")
for est in estudiantes:
    print(est)

# Preguntar al usuario qué desea hacer
opcion = input("\n¿Desea agregar o eliminar un estudiante? (escriba 'agregar' o 'eliminar'): ").lower()

if opcion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"\nEl estudiante '{nuevo}' fue agregado.")

elif opcion == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print(f"\nEl estudiante '{eliminar}' fue eliminado.")
    else:
        print(f"\nEl estudiante '{eliminar}' no se encuentra en la lista.")

else:
    print("\nOpción no válida.")

# Mostrar la lista final actualizada
print("\nLista final de estudiantes:")
for est in estudiantes:
    print(est)


#6 Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#   último pasa a ser el primero). 

numeros = [10, 20, 30, 40, 50, 60, 70]

print("Lista original:")
for n in numeros:
    print(n)

# Rotar una posición hacia la derecha
# Guardamos el último elemento
ultimo = numeros[-1]

# Movemos todos los demás elementos hacia la derecha
for i in range(len(numeros) - 1, 0, -1):
    numeros[i] = numeros[i - 1]

numeros[0] = ultimo

# Mostrar lista rotada
print("\nLista después de rotar una posición a la derecha:")
for n in numeros:
    print(n)


#7 Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana. 
# 	Calcular el promedio de las mínimas y el de las máximas. 
#   Mostrar en qué día se registró la mayor amplitud térmica. 

temperaturas = [
    [15, 25],  # Día 1
    [12, 28],  # Día 2
    [14, 26],  # Día 3
    [13, 29],  # Día 4
    [16, 27],  # Día 5
    [11, 30],  # Día 6
    [15, 24]   # Día 7
]

# Mostrar la matriz
print("Temperaturas de la semana (mín, máx):")
for i, dia in enumerate(temperaturas, start=1):
    print(f"Día {i}: {dia}")

# Calcular promedio de mínimas y máximas
suma_min = 0
suma_max = 0

for dia in temperaturas:
    suma_min += dia[0]
    suma_max += dia[1]

promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print(f"\nPromedio de temperaturas mínimas: {promedio_min:.2f}")
print(f"Promedio de temperaturas máximas: {promedio_max:.2f}")

# Encontrar el día con mayor amplitud térmica
mayor_amplitud = 0
dia_amplitud = 0

for i, dia in enumerate(temperaturas):
    amplitud = dia[1] - dia[0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_amplitud = i + 1  # +1 porque queremos que el día empiece en 1

print(f"Mayor amplitud térmica: {mayor_amplitud}°C, registrada el Día {dia_amplitud}")


#8 Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# 	Mostrar el promedio de cada estudiante. 
#   Mostrar el promedio de cada materia. 

notas = [
    [15, 18, 14],  # Estudiante 1
    [12, 17, 16],  # Estudiante 2
    [14, 13, 15],  # Estudiante 3
    [16, 19, 18],  # Estudiante 4
    [10, 12, 14]   # Estudiante 5
]

# Mostrar la matriz
print("Notas de los estudiantes:")
for i, estudiante in enumerate(notas, start=1):
    print(f"Estudiante {i}: {estudiante}")

# Promedio de cada estudiante
print("\nPromedio de cada estudiante:")
for i, estudiante in enumerate(notas, start=1):
    promedio = sum(estudiante) / len(estudiante)
    print(f"Estudiante {i}: {promedio:.2f}")

# Promedio de cada materia
print("\nPromedio de cada materia:")
num_materias = len(notas[0])
for j in range(num_materias):
    suma_materia = 0
    for i in range(len(notas)):
        suma_materia += notas[i][j]
    promedio_materia = suma_materia / len(notas)
    print(f"Materia {j+1}: {promedio_materia:.2f}")


#9 Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
# 	Inicializarlo con guiones "-" representando casillas vacías. 
# 	Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#   Mostrar el tablero después de cada jugada. 

# Inicializar tablero 3x3 con "-"
tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    print("\nTablero actual:")
    for fila in tablero:
        for casilla in fila:
            print(casilla, end=" ")
        print()

mostrar_tablero()

# Ciclo para 5 jugadas por jugador (para no exceder 9)
for turno in range(9):
    jugador = "X" if turno % 2 == 0 else "O"
    print(f"\nTurno del jugador {jugador}")
    
    # Pedir fila y columna
    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))
    
    # Verificar si la casilla está vacía
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        mostrar_tablero()
    else:
        print("Casilla ocupada, intente de nuevo.")
        # Repetir el turno
        turno -= 1


#10 Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
# 	Mostrar el total vendido por cada producto. 
# 	Mostrar el día con mayores ventas totales. 
#   Indicar cuál fue el producto más vendido en la semana. 

ventas = [
    [10,12,8,15,9,11,14],
    [5,7,6,8,10,9,7],
    [20,18,25,22,19,17,21],
    [8,10,9,7,6,12,11]
]

print("Ventas por producto/día:")
for i, prod in enumerate(ventas, start=1):
    print(f"Producto {i}: {prod}")

totales_productos = []
for prod in ventas:
    suma = 0
    for v in prod:
        suma += v
    totales_productos.append(suma)

print("Total por producto:")
for i, total in enumerate(totales_productos, start=1):
    print(f"Producto {i}: {total}")

totales_dias = []
for j in range(7):
    suma_dia = 0
    for i in range(4):
        suma_dia += ventas[i][j]
    totales_dias.append(suma_dia)

# Día con mayores ventas usando bucle
max_ventas = totales_dias[0]
dia_max = 1
for i in range(1,len(totales_dias)):
    if totales_dias[i] > max_ventas:
        max_ventas = totales_dias[i]
        dia_max = i+1
print(f"Día con mayores ventas: Día {dia_max} ({max_ventas} unidades)")

# Producto más vendido usando bucle
max_prod = totales_productos[0]
producto_max = 1
for i in range(1,len(totales_productos)):
    if totales_productos[i] > max_prod:
        max_prod = totales_productos[i]
        producto_max = i+1
print(f"Producto más vendido: Producto {producto_max} ({max_prod} unidades)")


