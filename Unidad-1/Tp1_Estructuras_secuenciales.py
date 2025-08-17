# 1. Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo")


# 2. Crear un programa que pida al usuario su nombre e imprima por pantalla 
# un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, 
# el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f...) para realizar la 
# impresión por pantalla.

nombre = input("Cual es tu nombre?: ")
print(f"Hola {nombre}!")


# 3. Crear un programa que pida al usuario su nombre, apellido, edad y lugar de 
# residencia e imprima por pantalla una oración con los datos ingresados. 
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, 
# el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
# Consejo: esto será más sencillo si utilizas print(f...) para realizar la impresión por pantalla.

nombre = input("Cual es tu nombre?: ")
apellido = input("Cual es tu apellido?: ")
age = input("Que edad tienes?: ")
direccion = input("Donde vives?: ")
print(f"Soy {nombre} {apellido}, tengo {age} años y vivo en {direccion}.")


# 4. Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Añade el radio del circulo: "))
pi = 3.14159
area = pi * radio * radio
perimetro = 2 * pi * radio

print("Radio:", radio)
print("Área:", area)
print("Perímetro:", perimetro)


# 5. Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla 
# a cuántas horas equivale.

segundos = int(input("Ingresa la cantidad de segundos: "))
horas = int(segundos / 3600)

print(f"Tu segundos quivalen a: {horas} Hora/s")


# 6. Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.

numero = int(input("Ingresa un número: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)


# 7. Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre 
# por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Ingresa el primer número (distinto de 0): "))
numero2 = int(input("Ingresa el segundo número (distinto de 0): "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("Resultados:")
print(numero1, "+", numero2, "=", suma)
print(numero1, "-", numero2, "=", resta)
print(numero1, "*", numero2, "=", multiplicacion)
print(numero1, "/", numero2, "=", division)


# 8. Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su 
# índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del 
# siguiente modo: IMC = peso en kg / (altura en m)2

altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kg: "))

imc = peso / (altura * altura)

print(f"Tu IMC es: {imc}")


# 9. Crear un programa que pida al usuario una temperatura en grados Celsius e imprima 
# por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
# Temperatura en fahrenheit = 9 / 5. Temperatura en celsius + 32

celsius = int(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = int((9/5) * celsius + 32)

print(f"Temperatura en Fahrenheit: {fahrenheit}°F")


# 10. Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio es: {promedio}")