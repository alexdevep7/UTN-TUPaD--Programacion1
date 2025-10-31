# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. 
# Cada línea debe tener: nombre,precio,cantidad

# Crear y escribir en el archivo
with open("productos.txt", "w") as archivo:
    archivo.write("Laptop,850.99,5\n")
    archivo.write("Mouse,25.50,20\n")
    archivo.write("Teclado,45.00,15\n")

print("✓ Archivo productos.txt creado exitosamente!")

# Opcional: Leer el archivo para verificar que se creó correctamente
print("\nContenido del archivo:")
with open("productos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)


# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, 
# la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

print("=== LISTA DE PRODUCTOS ===\n")

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    
    for linea in lineas:
        # Limpiar espacios y saltos de línea
        linea_limpia = linea.strip()
        
        # Separar por comas
        datos = linea_limpia.split(",")
        
        # Extraer cada dato
        nombre = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        
        # Mostrar en el formato solicitado
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

print("\n Productos mostrados correctamente!")


# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, 
# le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.

print("=== LISTA DE PRODUCTOS ===\n")

# Leer y mostrar productos existentes
with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    
    for linea in lineas:
        linea_limpia = linea.strip()
        datos = linea_limpia.split(",")
        nombre = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

print("\n" + "="*40)

# Pedir datos del nuevo producto al usuario
print("\n--- AGREGAR NUEVO PRODUCTO ---")
nuevo_nombre = input("Ingrese el nombre del producto: ")
nuevo_precio = input("Ingrese el precio: ")
nueva_cantidad = input("Ingrese la cantidad: ")

# Agregar el nuevo producto al archivo (modo "a" para append)
with open("productos.txt", "a") as archivo:
    archivo.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")

print(f"\n✓ Producto '{nuevo_nombre}' agregado exitosamente!")

# Mostrar todos los productos actualizados
print("\n=== LISTA ACTUALIZADA DE PRODUCTOS ===\n")
with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    
    for linea in lineas:
        linea_limpia = linea.strip()
        datos = linea_limpia.split(",")
        nombre = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos, 
# donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.

print("=== CARGANDO PRODUCTOS EN LISTA DE DICCIONARIOS ===\n")

# Lista para almacenar los productos
productos = []

# Leer el archivo y cargar datos
with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    
    for linea in lineas:
        # Limpiar y separar
        linea_limpia = linea.strip()
        datos = linea_limpia.split(",")
        
        # Crear diccionario para cada producto
        producto = {
            'nombre': datos[0],
            'precio': datos[1],
            'cantidad': datos[2]
        }
        
        # Agregar el diccionario a la lista
        productos.append(producto)

print(f"✓ Se cargaron {len(productos)} productos en la lista\n")

# Mostrar la lista completa
print("Lista de productos (estructura completa):")
print(productos)

print("\n" + "="*50 + "\n")

# Mostrar cada producto de forma legible
print("Productos cargados:")
for i, producto in enumerate(productos, 1):
    print(f"{i}. {producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")

print("\n" + "="*50 + "\n")

# Ejemplo de cómo acceder a datos específicos
print("Ejemplos de acceso a datos:")
print(f"Primer producto: {productos[0]['nombre']}")
print(f"Precio del segundo producto: ${productos[1]['precio']}")
print(f"Cantidad del tercer producto: {productos[2]['cantidad']}")


# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. 
# Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. 
# Si no existe, mostrar un mensaje de error.


print("=== SISTEMA DE BÚSQUEDA DE PRODUCTOS ===\n")

# Cargar productos en lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    
    for linea in lineas:
        linea_limpia = linea.strip()
        datos = linea_limpia.split(",")
        
        producto = {
            'nombre': datos[0],
            'precio': datos[1],
            'cantidad': datos[2]
        }
        productos.append(producto)

print(f"✓ {len(productos)} productos cargados en el sistema\n")

# Mostrar lista de productos disponibles
print("Productos disponibles:")
for producto in productos:
    print(f"  - {producto['nombre']}")

print("\n" + "="*50 + "\n")

# Pedir al usuario el nombre del producto a buscar
nombre_buscar = input("Ingrese el nombre del producto a buscar: ")

# Buscar el producto
producto_encontrado = None

for producto in productos:
    if producto['nombre'].lower() == nombre_buscar.lower():
        producto_encontrado = producto
        break

# Mostrar resultado
print("\n" + "="*50 + "\n")

if producto_encontrado:
    print("✓ PRODUCTO ENCONTRADO:")
    print(f"  Nombre: {producto_encontrado['nombre']}")
    print(f"  Precio: ${producto_encontrado['precio']}")
    print(f"  Cantidad: {producto_encontrado['cantidad']}")
else:
    print(f"✗ ERROR: El producto '{nombre_buscar}' no existe en el sistema")

print("\n" + "="*50)


# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, 
# sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.

print("=== SISTEMA DE GESTIÓN DE PRODUCTOS ===\n")

# PASO 1: Cargar productos en lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    
    for linea in lineas:
        linea_limpia = linea.strip()
        datos = linea_limpia.split(",")
        
        producto = {
            'nombre': datos[0],
            'precio': datos[1],
            'cantidad': datos[2]
        }
        productos.append(producto)

print(f"✓ {len(productos)} productos cargados\n")

# PASO 2: Mostrar productos actuales
print("Productos actuales:")
for i, producto in enumerate(productos, 1):
    print(f"{i}. {producto['nombre']} - ${producto['precio']} - Stock: {producto['cantidad']}")

print("\n" + "="*50 + "\n")

# PASO 3: Agregar nuevo producto a la lista
print("--- AGREGAR NUEVO PRODUCTO ---")
nuevo_nombre = input("Ingrese el nombre del producto: ")
nuevo_precio = input("Ingrese el precio: ")
nueva_cantidad = input("Ingrese la cantidad: ")

# Crear el diccionario del nuevo producto
nuevo_producto = {
    'nombre': nuevo_nombre,
    'precio': nuevo_precio,
    'cantidad': nueva_cantidad
}

# Agregar a la lista
productos.append(nuevo_producto)

print(f"\n✓ Producto '{nuevo_nombre}' agregado a la lista")

print("\n" + "="*50 + "\n")

# PASO 4: Sobrescribir el archivo con todos los productos actualizados
with open("productos.txt", "w") as archivo:
    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea)

print("✓ Archivo productos.txt actualizado correctamente")

print("\n" + "="*50 + "\n")

# PASO 5: Verificar - Leer y mostrar el archivo actualizado
print("Lista actualizada de productos (desde el archivo):")
with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    
    for i, linea in enumerate(lineas, 1):
        linea_limpia = linea.strip()
        datos = linea_limpia.split(",")
        print(f"{i}. {datos[0]} - ${datos[1]} - Stock: {datos[2]}")

print(f"\n✓ Total de productos en archivo: {len(lineas)}")