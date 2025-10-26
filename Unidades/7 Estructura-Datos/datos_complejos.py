# 1. Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450
#Añadir las siguientes frutas con sus respectivos precios:
#Naranja = 1200, Manzana = 1500, Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


# 2. Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el 
# código desarrollado en el punto anterior, actualizar los precios de las siguientes 
# frutas:Banana = 1330, Manzana = 1700, Melón = 2800

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)


#3. Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el 
# código desarrollado en el punto anterior, crear una lista que contenga únicamente 
# las frutas sin los precios.

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)


# 4. Escribí un programa que permita almacenar y consultar números telefónicos.
#Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

for i in range(5):
    nombre = input("Ingresa el nombre del contacto: ")
    numero = input("Ingresa el número de teléfono: ")
    contactos[nombre.lower()] = numero

print("\nContactos guardados:")
print(contactos)

consulta = input("\n¿Qué contacto deseas consultar? ")

if consulta.lower() in contactos:
    print(f"{consulta} → {contactos[consulta.lower()]}")
else:
    print("El contacto no existe")


# 5. Solicita al usuario una frase e imprime:
#Las palabras únicas (usando un set).
#Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresa una frase: ")

palabras = frase.lower().split()

palabras_unicas = set(palabras)

print("\nPalabras únicas:", palabras_unicas)

conteo_palabras = {}
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print("Recuento:", conteo_palabras)


# 6. Permití ingresar los nombres de 3 alumnos, y para cada uno una 
# tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input("Ingresa el nombre del alumno: ")
    nota1 = int(input("Ingresa la nota 1: "))
    nota2 = int(input("Ingresa la nota 2: "))
    nota3 = int(input("Ingresa la nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

print("\nAlumnos y sus notas:")
print(alumnos)

print("\nPromedios:")
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {promedio}")


# 7. Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {101, 102, 103, 104, 105}
parcial2 = {103, 104, 106, 107, 108}

aprobaron_ambos = parcial1 & parcial2

aprobaron_solo_uno = parcial1 ^ parcial2

aprobaron_al_menos_uno = parcial1 | parcial2

print("Estudiantes que aprobaron ambos parciales:")
print(aprobaron_ambos)

print("\nEstudiantes que aprobaron solo uno de los dos:")
print(aprobaron_solo_uno)

print("\nEstudiantes que aprobaron al menos un parcial:")
print(aprobaron_al_menos_uno)


# 8. Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe.
# Agregar un nuevo producto si no existe.

stock = {"manzana": 50, "banana": 30, "naranja": 20, "pera": 15}

print("Stock inicial:")
print(stock)

producto = input("\nIngresa el nombre del producto: ").lower()

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]} unidades")
    agregar = int(input("¿Cuántas unidades quieres agregar? "))
    stock[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock[producto]} unidades")
else:
    print(f"El producto {producto} no existe.")
    cantidad = int(input("¿Cuántas unidades tiene el nuevo producto? "))
    stock[producto] = cantidad
    print(f"Producto {producto} agregado con {cantidad} unidades")

print("\nStock actualizado:")
print(stock)


# 9. Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {}

for i in range(3):
    dia = input("Ingresa el día: ")
    hora = input("Ingresa la hora: ")
    evento = input("Ingresa el evento: ")
    agenda[(dia, hora)] = evento

print("\nAgenda completa:")
print(agenda)

consulta_dia = input("\n¿Qué día quieres consultar? ")
consulta_hora = input("¿Qué hora quieres consultar? ")

if (consulta_dia, consulta_hora) in agenda:
    print(f"Evento: {agenda[(consulta_dia, consulta_hora)]}")
else:
    print("No hay evento en ese día y hora")


# 10. Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores.

original = {"Argentina": "Buenos Aires", "Venezuela": "Caracas"}

invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print("original =", original)
print("invertido =", invertido)



