import random
from statistics import mode, median, mean


# 1) Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en 
# pantalla que diga “Es mayor de edad”.

edad = int(input("Por favor, ingresa tu edad: "))

if edad > 18:
    print("Es mayor de edad")


# 2) Escribir un programa que solicite su nota al usuario. Si la nota 
# es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga 
# “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. 

nota = float(input("Ingresa tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# 3) Escribir un programa que permita ingresar solo números pares. Si el 
# usuario ingresa un número par, imprimir por pantalla el mensaje 
# "Ha ingresado un número par"; en caso contrario, imprimir por pantalla 
# "Por favor, ingrese un número par". Nota: investigar el uso del operador 
# de módulo (%) en Python para evaluar si un número es par o impar. 

numero = 0
es_par = False
msj_par = "Ha ingresado un numero par"
msj_impar = "Por favor, Ingrese un numero par"

numero = int(input("Pro favor, ingrese un numero: "))

es_par = numero % 2 == 0

if es_par:
    print(msj_par)
else:
    print(msj_impar)


# 4) Escribir un programa que solicite al usuario su edad e imprima por 
# pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

edad = 0
categoria = ""
mensaje_solicitud = "Por favor, ingresa tu edad: "
categoria_nino = "Niño/a"
categoria_adolescente = "Adolescente"
categoria_adulto_joven = "Adulto/a joven"
categoria_adulto = "Adulto/a"

edad = int(input(mensaje_solicitud))

if edad < 12:
    categoria = categoria_nino
elif edad >= 12 and edad < 18:
    categoria = categoria_adolescente
elif edad >= 18 and edad < 30:
    categoria = categoria_adulto_joven
else:
    categoria = categoria_adulto

print(f"Perteneces a la categoría: {categoria}")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 
# caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de 
# longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una 
# contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, 
# ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el 
# uso de la función len() en Python para evaluar la cantidad de elementos 
# que tiene un iterable tal como una lista o un string. 

contraseña = ""
longitud = 0
longitud_minima = 8
longitud_maxima = 14
mensaje_solicitud = "Por favor, ingrese su contraseña: "
mensaje_correcta = "Ha ingresado una contraseña correcta"
mensaje_incorrecta = "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"

contraseña = input(mensaje_solicitud)

longitud = len(contraseña)

if longitud >= longitud_minima and longitud <= longitud_maxima:
    print(mensaje_correcta)
else:
    print(mensaje_incorrecta)


# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su 
# moda, su mediana y su media y las compare para determinar si hay sesgo 
# positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

numeros_aleatorios = []
moda = 0
mediana = 0
media = 0
tipo_sesgo = ""
mensaje_moda = ""
mensaje_mediana = ""
mensaje_media = ""
mensaje_sesgo = ""

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

try:
    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)
    
    mensaje_moda = f"Moda: {moda}"
    mensaje_mediana = f"Mediana: {mediana}"
    mensaje_media = f"Media: {media:.2f}"
    
    if media > mediana > moda:
        tipo_sesgo = "Sesgo positivo o a la derecha"
    elif media < mediana < moda:
        tipo_sesgo = "Sesgo negativo o a la izquierda"
    elif media == mediana == moda:
        tipo_sesgo = "Sin sesgo"
    else:
        tipo_sesgo = "Distribución irregular (no sigue los patrones clásicos)"
    
    mensaje_sesgo = f"Resultado: {tipo_sesgo}"
    
    print("=== ANÁLISIS ESTADÍSTICO ===")
    print(f"Lista generada: {numeros_aleatorios}")
    print()
    print("Parámetros estadísticos:")
    print(mensaje_media)
    print(mensaje_mediana)
    print(mensaje_moda)
    print()
    print(mensaje_sesgo)
    
except:
    print("Error: No se pudo calcular la moda (posiblemente no hay valores repetidos)")


# 7) Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación 
# al final e imprimir el string resultante por pantalla; en caso contrario, 
# dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla. 

frase_usuario = ""
vocales = "aeiouAEIOU"
ultimo_caracter = ""
termina_en_vocal = False
frase_resultante = ""
mensaje_solicitud = "Por favor, ingrese una frase o palabra: "

frase_usuario = input(mensaje_solicitud)

ultimo_caracter = frase_usuario[-1]

termina_en_vocal = ultimo_caracter in vocales

if termina_en_vocal:
    frase_resultante = frase_usuario + "!"
else:
    frase_resultante = frase_usuario

print(frase_resultante)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el 
# número 1, 2 o 3 dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. 
# Por ejemplo: Pedro. El programa debe transformar el nombre ingresado de 
# acuerdo a la opción seleccionada por el usuario e imprimir el resultado 
# por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() 
# de Python para convertir entre mayúsculas y minúsculas. 

nombre_usuario = ""
opcion_usuario = 0
nombre_transformado = ""
mensaje_nombre = "Por favor, ingrese su nombre: "
mensaje_opcion = """Seleccione una opción:
1. Nombre en mayúsculas
2. Nombre en minúsculas
3. Nombre con primera letra mayúscula
Ingrese su opción (1, 2 o 3): """
mensaje_error = "Error: Debe seleccionar una opción válida (1, 2 o 3)"

nombre_usuario = input(mensaje_nombre)

try:
    opcion_usuario = int(input(mensaje_opcion))
    
    if opcion_usuario == 1:
        nombre_transformado = nombre_usuario.upper()
    elif opcion_usuario == 2:
        nombre_transformado = nombre_usuario.lower()
    elif opcion_usuario == 3:
        nombre_transformado = nombre_usuario.title()
    else:
        print(mensaje_error)
        nombre_transformado = None
    
    if nombre_transformado is not None:
        print(f"Resultado: {nombre_transformado}")
        
except ValueError:
    print("Error: Debe ingresar un número válido")


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, 
# clasifique la magnitud en una de las siguientes categorías según la escala 
# de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). 
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). 
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

magnitud = 0.0
categoria = ""
descripcion = ""
mensaje_solicitud = "Ingrese la magnitud del terremoto en la escala de Richter: "

categoria_muy_leve = "Muy leve"
descripcion_muy_leve = "(imperceptible)"
categoria_leve = "Leve"
descripcion_leve = "(ligeramente perceptible)"
categoria_moderado = "Moderado"
descripcion_moderado = "(sentido por personas, pero generalmente no causa daños)"
categoria_fuerte = "Fuerte"
descripcion_fuerte = "(puede causar daños en estructuras débiles)"
categoria_muy_fuerte = "Muy Fuerte"
descripcion_muy_fuerte = "(puede causar daños significativos)"
categoria_extremo = "Extremo"
descripcion_extremo = "(puede causar graves daños a gran escala)"

try:
    magnitud = float(input(mensaje_solicitud))
    
    # Clasificar según la escala de Richter
    if magnitud < 3:
        categoria = categoria_muy_leve
        descripcion = descripcion_muy_leve
    elif magnitud >= 3 and magnitud < 4:
        categoria = categoria_leve
        descripcion = descripcion_leve
    elif magnitud >= 4 and magnitud < 5:
        categoria = categoria_moderado
        descripcion = descripcion_moderado
    elif magnitud >= 5 and magnitud < 6:
        categoria = categoria_fuerte
        descripcion = descripcion_fuerte
    elif magnitud >= 6 and magnitud < 7:
        categoria = categoria_muy_fuerte
        descripcion = descripcion_muy_fuerte
    else:  # magnitud >= 7
        categoria = categoria_extremo
        descripcion = descripcion_extremo
    
    print(f"Magnitud: {magnitud}")
    print(f"Clasificación: {categoria} {descripcion}")
    
except ValueError:
    print("Error: Debe ingresar un número válido")



# 10) Escribir un programa que pregunte al usuario en cuál emisferio se encuentra 
# (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información 
# para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera 
# o verano. 
# -- La informacion aportada esta en la tabla del pdf: periodo del año, Estacion del 
# emisferio norte y Estacion en el emisferio sur. ---

hemisferio = ""
mes = 0
dia = 0
estacion = ""
fecha_valida = False
hemisferio_valido = False

# Mensajes para el usuario
mensaje_hemisferio = "¿En qué hemisferio se encuentra? (N para Norte / S para Sur): "
mensaje_mes = "Ingrese el número del mes (1-12): "
mensaje_dia = "Ingrese el día del mes (1-31): "
mensaje_error_hemisferio = "Error: Debe ingresar N para Norte o S para Sur"
mensaje_error_mes = "Error: El mes debe ser un número entre 1 y 12"
mensaje_error_dia = "Error: El día debe ser un número entre 1 y 31"
mensaje_error_formato = "Error: Debe ingresar un número válido"

invierno = "Invierno"
primavera = "Primavera"
verano = "Verano"
otono = "Otoño"

try:
    hemisferio = input(mensaje_hemisferio).upper().strip()
    
    if hemisferio == "N" or hemisferio == "S":
        hemisferio_valido = True
    else:
        print(mensaje_error_hemisferio)
        hemisferio_valido = False
    
    if hemisferio_valido:
        # Solicitar mes y día
        mes = int(input(mensaje_mes))
        dia = int(input(mensaje_dia))
        
        # Validar mes
        if mes < 1 or mes > 12:
            print(mensaje_error_mes)
            fecha_valida = False
        # Validar día
        elif dia < 1 or dia > 31:
            print(mensaje_error_dia)
            fecha_valida = False
        else:
            fecha_valida = True
        
        # Determinar estación si los datos son válidos
        if fecha_valida:
            # Determinar estación según el período
            if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
                # Del 21 de diciembre al 20 de marzo
                if hemisferio == "N":
                    estacion = invierno
                else:  # hemisferio == "S"
                    estacion = verano
                    
            elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
                # Del 21 de marzo al 20 de junio
                if hemisferio == "N":
                    estacion = primavera
                else:  # hemisferio == "S"
                    estacion = otono
                    
            elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
                # Del 21 de junio al 20 de septiembre
                if hemisferio == "N":
                    estacion = verano
                else:  # hemisferio == "S"
                    estacion = invierno
                    
            else:  # (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20)
                # Del 21 de septiembre al 20 de diciembre
                if hemisferio == "N":
                    estacion = otono
                else:  # hemisferio == "S"
                    estacion = primavera
            
            hemisferio_nombre = "Norte" if hemisferio == "N" else "Sur"
            print(f"Fecha: {dia}/{mes}")
            print(f"Hemisferio: {hemisferio_nombre}")
            print(f"Estación: {estacion}")

except ValueError:
    print(mensaje_error_formato)


