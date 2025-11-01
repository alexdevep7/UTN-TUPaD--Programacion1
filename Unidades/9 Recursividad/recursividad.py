# 1. Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular 
# y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Programa principal
numero = int(input("Ingresa un número: "))

print(f"\nFactoriales de 1 hasta {numero}:")
print("-" * 30)

# Calcular y mostrar el factorial de cada número
for i in range(1, numero + 1):
    resultado = factorial(i)
    print(f"Factorial de {i} = {resultado}")



# 2. Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(n):
    if n == 0:  # Caso base 1
        return 0
    elif n == 1:  # Caso base 2
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Llamada recursiva


# Programa principal
posicion = int(input("Ingresa la posición de Fibonacci a calcular: "))

print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
print("-" * 40)

# Mostrar la serie completa
for i in range(posicion + 1):
    resultado = fibonacci(i)
    print(f"Fibonacci({i}) = {resultado}")



# 3. Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:  # Caso base
        return 1
    else:
        return base * potencia(base, exponente - 1)  # Llamada recursiva


# Programa principal
print("Cálculo de Potencias")
print("=" * 40)

base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

resultado = potencia(base, exponente)

print(f"\n{base}^{exponente} = {resultado}")

# Pruebas adicionales
print("\n" + "=" * 40)
print("Ejemplos adicionales:")
print("-" * 40)
print(f"2^3 = {potencia(2, 3)}")
print(f"5^4 = {potencia(5, 4)}")
print(f"10^2 = {potencia(10, 2)}")
print(f"3^0 = {potencia(3, 0)}")



# 4. Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. 
# Para convertir un número decimal a binario, se puede seguir este procedimiento: 
# Dividir el número por 2.
# Guardar el resto (0 o 1).
# Repetir el proceso con el cociente hasta que llegue a 0.
# Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
# Convertir el número 10 a binario: 10 ÷ 2 = 5  resto: 0, 5 ÷ 2 = 2  resto: 1, 2 ÷ 2 = 1  resto: 0, 1 ÷ 2 = 0   resto: 1 

def decimal_a_binario(n):
    if n <= 1:  # Caso base
        return str(n)
    else:
        # Llamada recursiva: dividir por 2 y concatenar el resto
        return decimal_a_binario(n // 2) + str(n % 2)


# Programa principal
print("Conversión de Decimal a Binario")
print("=" * 40)

numero = int(input("Ingresa un número decimal positivo: "))

if numero < 0:
    print("Error: El número debe ser positivo")
else:
    binario = decimal_a_binario(numero)
    print(f"\nEl número {numero} en binario es: {binario}")
    
    # Mostrar el proceso paso a paso
    print(f"\nProceso de conversión:")
    print("-" * 40)
    temp = numero
    pasos = []
    while temp > 0:
        cociente = temp // 2
        resto = temp % 2
        pasos.append(f"{temp} ÷ 2 = {cociente}  resto: {resto}")
        temp = cociente
    
    for paso in pasos:
        print(paso)
    
    print(f"\nLeyendo los restos de abajo hacia arriba: {binario}")

# Ejemplos adicionales
print("\n" + "=" * 40)
print("Ejemplos adicionales:")
print("-" * 40)
print(f"5 en binario: {decimal_a_binario(5)}")
print(f"15 en binario: {decimal_a_binario(15)}")
print(f"25 en binario: {decimal_a_binario(25)}")
print(f"100 en binario: {decimal_a_binario(100)}")



# 5. Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
# y devuelva True si es un palíndromo o False si no lo es.
#Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    # Caso base 1: palabra vacía o de un solo carácter
    if len(palabra) <= 1:
        return True
    
    # Caso base 2: primer y último carácter diferentes
    if palabra[0] != palabra[-1]:
        return False
    
    # Caso recursivo: verificar la palabra sin primer y último carácter
    return es_palindromo(palabra[1:-1])


# Programa principal
print("Verificador de Palíndromos")
print("=" * 40)

palabra = input("Ingresa una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(palabra):
    print(f"\n✓ '{palabra}' ES un palíndromo")
else:
    print(f"\n✗ '{palabra}' NO es un palíndromo")

# Ejemplos y pruebas
print("\n" + "=" * 40)
print("Pruebas con varias palabras:")
print("-" * 40)

palabras_prueba = ["oso", "radar", "anilina", "python", "reconocer", 
                   "neuquen", "somos", "casa", "ojo", "civic"]

for p in palabras_prueba:
    resultado = "SÍ" if es_palindromo(p) else "NO"
    print(f"{p:15} → {resultado}")



# 6. Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos. 


def suma_digitos(n):
    # Caso base: cuando el número es 0
    if n == 0:
        return 0
    else:
        ultimo_digito = n % 10  # Obtener el último dígito
        resto = n // 10          # Eliminar el último dígito
        return ultimo_digito + suma_digitos(resto)


# Programa principal
print("Suma de Dígitos (Recursiva)")
print("=" * 40)

numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("Error: El número debe ser positivo")
else:
    resultado = suma_digitos(numero)
    print(f"\nLa suma de los dígitos de {numero} es: {resultado}")
    
    print(f"\nProceso:")
    print("-" * 40)
    temp = numero
    digitos = []
    while temp > 0:
        digito = temp % 10
        digitos.insert(0, digito)
        temp = temp // 10
    
    print(f"Dígitos: {' + '.join(map(str, digitos))} = {resultado}")

# Ejemplos de prueba
print("\n" + "=" * 40)
print("Ejemplos:")
print("-" * 40)
print(f"suma_digitos(1234) = {suma_digitos(1234)}")
print(f"suma_digitos(9) = {suma_digitos(9)}")
print(f"suma_digitos(305) = {suma_digitos(305)}")
print(f"suma_digitos(9876) = {suma_digitos(9876)}")
print(f"suma_digitos(100) = {suma_digitos(100)}")



# 7. Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
# y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques 
# que necesita para construir toda la pirámide.

def contar_bloques(n):
    # Caso base: solo un nivel con 1 bloque
    if n == 1:
        return 1
    else:
        # Caso recursivo: bloques del nivel actual + bloques de niveles superiores
        return n + contar_bloques(n - 1)


# Programa principal
print("Contador de Bloques de Pirámide")
print("=" * 40)

niveles = int(input("Ingresa el número de bloques en el nivel más bajo: "))

if niveles < 1:
    print("Error: Debe haber al menos 1 bloque")
else:
    total = contar_bloques(niveles)
    print(f"\nTotal de bloques necesarios: {total}")
    
    # Mostrar la construcción de la pirámide
    print(f"\nConstrucción de la pirámide:")
    print("-" * 40)
    bloques_por_nivel = []
    for i in range(niveles, 0, -1):
        bloques_por_nivel.append(str(i))
        espacios = " " * (niveles - i)
        print(f"Nivel {niveles - i + 1}: {espacios}{'█ ' * i}")
    
    print(f"\nSuma: {' + '.join(bloques_por_nivel)} = {total}")

# Ejemplos de prueba
print("\n" + "=" * 40)
print("Ejemplos:")
print("-" * 40)
print(f"contar_bloques(1) = {contar_bloques(1)}")
print(f"contar_bloques(2) = {contar_bloques(2)}")
print(f"contar_bloques(4) = {contar_bloques(4)}")
print(f"contar_bloques(5) = {contar_bloques(5)}")
print(f"contar_bloques(10) = {contar_bloques(10)}")



# 8. Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y 
# un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    # Caso base: cuando el número llega a 0
    if numero == 0:
        return 0
    else:
        # Obtener el último dígito del número
        ultimo_digito = numero % 10
        # Eliminar el último dígito
        resto = numero // 10
        
        # Si el último dígito coincide con el buscado, sumar 1
        if ultimo_digito == digito:
            return 1 + contar_digito(resto, digito)
        else:
            return contar_digito(resto, digito)


# Programa principal
print("Contador de Dígitos en un Número")
print("=" * 40)

numero = int(input("Ingresa un número entero positivo: "))
digito = int(input("Ingresa el dígito a buscar (0-9): "))

if numero < 0:
    print("Error: El número debe ser positivo")
elif digito < 0 or digito > 9:
    print("Error: El dígito debe estar entre 0 y 9")
else:
    resultado = contar_digito(numero, digito)
    
    if resultado == 0:
        print(f"\nEl dígito {digito} NO aparece en {numero}")
    elif resultado == 1:
        print(f"\nEl dígito {digito} aparece 1 vez en {numero}")
    else:
        print(f"\nEl dígito {digito} aparece {resultado} veces en {numero}")

# Ejemplos de prueba
print("\n" + "=" * 40)
print("Ejemplos:")
print("-" * 40)
print(f"contar_digito(12233421, 2) = {contar_digito(12233421, 2)}")
print(f"contar_digito(5555, 5) = {contar_digito(5555, 5)}")
print(f"contar_digito(123456, 7) = {contar_digito(123456, 7)}")
print(f"contar_digito(100200, 0) = {contar_digito(100200, 0)}")
print(f"contar_digito(9999999, 9) = {contar_digito(9999999, 9)}")
