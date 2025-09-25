import random

#1  Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for numero in range(0, 101):
   print(numero)

#2 Desarrolla un programa que solicite al usuario un número entero y determine la cantidad 
# de dígitos que contiene. 

entrada_usuario = input("Por favor, introduce un número entero: ")

try:
    numero_entero = int(entrada_usuario)

    longitud_texto = len(entrada_usuario)

    cantidad_digitos = longitud_texto

    if entrada_usuario.startswith('-'):
        cantidad_digitos = longitud_texto - 1

    print(f"El número {entrada_usuario} tiene {cantidad_digitos} dígito(s).")

except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")

#3 Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados 
# por el usuario, excluyendo esos dos valores. 

try:
    numero_inicial = int(input("Introduce el primer número: "))
    numero_final = int(input("Introduce el segundo número: "))
except ValueError:
    print("Entrada no válida. Por favor, introduce solo números enteros.")
    exit()

suma_total = 0

if numero_inicial > numero_final:
    temp = numero_inicial
    numero_inicial = numero_final
    numero_final = temp

contador = numero_inicial + 1

while contador < numero_final:
    suma_total += contador
    contador += 1

print(f"La suma de los números entre {numero_inicial} y {numero_final} es: {suma_total}")

#4 Elabora un programa que permita al usuario ingresar números enteros y los sume 
# en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el 
# usuario ingrese un 0.

try:
    numero_ingresado = int(input("Introduce un número entero (ingresa 0 para terminar): "))
    suma_total = numero_ingresado

    while numero_ingresado != 0:
        numero_ingresado = int(input("Introduce un número entero (ingresa 0 para terminar): "))
        suma_total += numero_ingresado
    
    print(f"El total acumulado es: {suma_total}")

except ValueError:
    print("Entrada no válida. Por favor, introduce solo números enteros.")


#5 Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, 
# el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

print("Adivina el número entre 0 y 9")

while not adivinado:
    intento = int(input("Ingresa tu número: "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! El número era {numero_secreto}.")
        print(f"Lo lograste en {intentos} intentos.")
        adivinado = True
    else:
        print("No es ese, intenta de nuevo.")

#6 Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

numero = 100

while numero >= 0:
    print(numero)
    numero -= 2

#7 Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.

n = int(input("Ingresa un número entero positivo: "))

suma = 0
i = 0

while i <= n:
    suma += i
    i += 1

print(f"La suma de los números de 0 a {n} es: {suma}")


#8 Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

cantidad = 100  # <-- puedes cambiarlo para probar con menos

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    
    # Par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")


#9 Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule 
# la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero 
# debe poder procesar 100 números cambiando solo un valor).

cantidad = 100  # <-- cambia este valor para probar con menos

suma = 0
i = 0

while i < cantidad:
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero
    i += 1

media = suma / cantidad
print(f"\nLa media de los {cantidad} números es: {media}")


#10 Escribe un programa que invierta el orden de los dígitos de un número ingresado por 
# el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

numero = int(input("Ingresa un número: "))

invertido = 0

while numero > 0:
    digito = numero % 10          # último dígito
    invertido = invertido * 10 + digito
    numero //= 10                 # quitamos el último dígito

print(f"El número invertido es: {invertido}")

