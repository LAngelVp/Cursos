#//EJERCICIOS PYTHON
# Número par o impar:
# Escribe un programa que pida un número al usuario y determine si es par o impar.

# numero = input("INGRESAR NUMERO: ")

# try:
#     if int(numero) % 2 == 0:
#         print("EL NUMERO ES PAR")
#     else:
#         print("EL NUMERO ES IMPAR")
# except:
#     ("INGRESE UN NUMERO VALIDO")

# Mayor de tres números:
# Escribe un programa que pida tres números y determine cuál es el mayor de ellos.

# numero1 = input("numero 1: ")
# numero2 = input("numero 2: ")
# numero3 = input("numero 3: ")

# mayor = max(numero1, numero2, numero3)

# print(f'El numero mayor es: {mayor}')

# numeros = []
# for i in range(1, 4):
#     while True:
#         try:
#             numero = int(input(f"INGRESE NUMERO {i}: "))
#             numeros.append(numero)
#             break
#         except ValueError:
#             print("Esi no es un numero valido")
# print(f'estos son los numeros: {numeros}')
# mayor = numeros[0]

# for i in numeros:
#     if i > mayor:
#         mayor = i
        
# print(mayor)
# #[1,2,3] i
# #[1,2,3] mayor

# Contar números positivos y negativos:
# Escribe un programa que reciba una lista de números y cuente cuántos son positivos, negativos y cuántos son cero.

# palabra = "PALA, BRA"
# lista = palabra.split(",")
# lista_sin_espacios = []
# for i in lista:
#     print(i.strip())
#     lista_sin_espacios.append(i.strip())

# print(lista)
# print(lista_sin_espacios)

# numeros = list(map(int, input("ESCRIBE NUMEROS SEPARADOS POR ESPACIO: ").split()))

# positivos = 0
# negativos = 0
# cero = 0

# for numero in numeros:
#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1
#     else:
#         cero += + 1
        
# print(f'''
#     numeros positivos : {positivos}
#     numeros negativos : {negativos}
#     cero : {cero}
#     ''')

# Contar vocales en una cadena:
# Escribe un programa que reciba una cadena de texto y cuente cuántas vocales contiene.

# cadena = input("ingrese una cadena: ")

# vacales = "aeiouAEIOU"

# contador = 0
# for letra in cadena:
#     if letra in vacales:
#         contador += 1
        
# print(f'Cantidad de vocales : {contador}')

# Revertir una cadena:
# Escribe un programa que reciba una cadena y la imprima en orden inverso.

# CADENA = input("CADENA: ")

# cadena_invertida = CADENA[::-1]

# cadena_invertida = ""
# for caracter in CADENA:
#     cadena_invertida = caracter + cadena_invertida
    
# print(f"CADENA INVERTIDA: {cadena_invertida}") 

# Palíndromo:
# Escribe un programa que determine si una cadena es un palíndromo (que se lee igual de izquierda a derecha que de derecha a izquierda).

# CADENA = input("INGRESA UN PALINDROMO: ")

# cadena_sin_espacios = CADENA.replace(" ", "").lower()

# if cadena_sin_espacios == cadena_sin_espacios[::-1]:
#     print("Es un palindromo")
# else:
#     print("No es un palindromo")

# Suma de elementos en una lista:
# Escribe un programa que reciba una lista de números y calcule su suma.

# numeros = [1, 2, 3, 4, 5]
# suma = sum(numeros)
# print(f"La suma de los elementos de la lista es: {suma}")

# Buscar un número en una lista:
# Escribe un programa que reciba una lista de números y determine si un número específico se encuentra en la lista.

# lista = [1, 2, 4, 5]
# numero = 3

# if numero in lista:
#     print(f"El número {numero} se encuentra en la lista")
# else:
#     print(f"El número {numero} no se encuentra en la lista")

# Ordenar una lista de números de menor a mayor:
# Escribe un programa que ordene una lista de números de menor a mayor.

# lista = [1,2,6,4,76,9,3]
# lista_ordenada = sorted(lista)
# print(f"La lista ordenada es: {lista_ordenada}")

# Eliminar elementos duplicados de una lista:
# Escribe un programa que reciba una lista y elimine los elementos duplicados.

# lista = [1,1,1,2,2,34,65,87,43,87,231,65]

# numero_unicos = list(set(lista))
# print(f"La lista sin elementos duplicados es: {numero_unicos}")

# Función para calcular la suma de los primeros n números:
# Escribe una función que reciba un número n y calcule la suma de los primeros n números enteros.

# def suma_numeros(n):
#     return sum(range(1, n + 1))

# numero = int(input("Ingresa un número para calcular la suma de los primeros n números: "))
# print(f"La suma de los primeros {numero} números es {suma_numeros(numero)}")

# Función para calcular el área de un círculo:
# Escribe una función que reciba el radio de un círculo y calcule su área.

# import math

# def calcular_area(radio):
#     resultado = math.pi * (radio ** 2)
#     return resultado

# radio = 3.5
# resultado = calcular_area(radio)
# print(f"El área del círculo con radio {radio} es {resultado}")

# Uso de diccionario para contar palabras:
# Escribe un programa que reciba una cadena de texto y cuente cuántas veces aparece cada palabra, usando un diccionario.

# def contar_palabras(cadena_texto):
#     palabras = cadena_texto.split()
#     contador_palbras = {}
    
#     for palabra in palabras:
#         palabras = palabra.lower()
#         if palabra in contador_palbras:
#             contador_palbras[palabra] += 1
#         else:
#             contador_palbras[palabra] = 1
#     return contador_palbras

# texto = "que esta pasando el dia de hoy que que"
# resultado = contar_palabras(texto)
# print(resultado)

# Eliminar una clave de un diccionario
# def eliminar_clave(diccionario, clave):
#     if clave in diccionario:
#         del diccionario[clave]
#     else:
#         pass
#     return diccionario

# diccionario = {"a":1,"b":2, "c": 3}
# clave = "b"
# diccionario_actualizado = eliminar_clave(diccionario, clave)
# print(diccionario_actualizado)

# buscar una clave

# def buscar_clave(diccionario, clave):
#     if clave in diccionario:
#         return diccionario[clave]
#     else:
#         return
    
# diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Bogota"}
# edad = "edad"
# resultado = buscar_clave(diccionario, edad)
# print(resultado)

# Trabajar con archivos

# def leer_archivo(nombre_archivo):
#     try:
#         with open(nombre_archivo, 'r') as archivo:
#             contenido = archivo.read()
#             print("lectura exitosa")
#             print(contenido)
#             return contenido
#     except FileNotFoundError:
#         print(f"El archivo {nombre_archivo} no existe")
#         return None

# leer_archivo("archivo.txt")

# def escribir_archivo(nombre_archivo, contenido):
#     with open(nombre_archivo, 'w') as archivo:
#         archivo.write(contenido)

# escribir_archivo("archivo.txt", "Fugiat occaecat quis occaecat excepteur anim Lorem cupidatat mollit id. Veniam quis ea enim reprehenderit. Nisi qui nulla eu in commodo. Elit proident sit aute ex deserunt pariatur sunt. Fugiat occaecat quis occaecat excepteur anim Lorem cupidatat mollit id. Veniam quis ea enim reprehenderit. Nisi qui nulla eu in commodo. Elit proident sit aute ex deserunt pariatur sunt. Fugiat occaecat quis occaecat excepteur anim Lorem cupidatat mollit id. Veniam quis ea enim reprehenderit. Nisi qui nulla eu in commodo. Elit proident sit aute ex deserunt pariatur sunt.")

# def buscar_palabra(nombre_archivo, palabra):
#     try:
#         with open(nombre_archivo, 'r') as archivo:
#             contenido = archivo.read()
#             ocurrencias = contenido.lower().count(palabra.lower())
#             print(f"La palabra {palabra} aparece {ocurrencias} veces en el archivo")
#     except FileNotFoundError:
#         print(f"El archivo {nombre_archivo} no existe")
        
# buscar_palabra("archivo.txt", "elit")

# from datetime import datetime

# POO
# class Persona:
#     def __init__(self, nombre, edad, ciudad, fecha_salida):
#         self.nombre = nombre
#         self.edad = edad
#         self.ciudad = ciudad
#         self.fecha_ingreso = datetime.strptime("2024-01-01", "%Y-%m-%d")
#         self.fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d")
        
#     def calcular_antiguedad(self):
#         diferencia = self.fecha_salida - self.fecha_ingreso
#         return diferencia.days
                
#     def __str__(self):
#         return f"Persona: {self.nombre}, Edad: {self.edad}, Ciudad: {self.ciudad}, fecha de ingreso : {self.fecha_ingreso}, fecha de salida : {self.calcular_antiguedad()}"
        
# persona = Persona("Juan", 25, "Bogota", "2024-12-11")
# persona2 = Persona("Moises", 26, "Mexico", "2024-09-11")
# print(persona)
# print(persona2)

# class Persona:
#     def __init__(self, nombre, edad, genero):
#         self.nombre = nombre
#         self.edad = edad
#         self.genero = genero
        
# class Empleado(Persona):
#     def __init__(self, nombre, edad, genero, salario):
#         super().__init__(nombre, edad, genero)
#         self.salario = salario
        
#     def __str__(self):
#         return f"Empleado: {self.nombre}, Edad: {self.edad}, Genero: {self.genero}, Salario: {self.salario}"
        
# empleado = Empleado("Laura", 32, "Femenino", 1000000)
# print(empleado)

# CARROS
# class Coche:
#     def __init__(self, marca, modelo, año):
#         self._marca = marca
#         self._modelo = modelo
#         self._año = año
        
#     @property    
#     def marca(self):
#         return self._marca
    
#     @marca.setter
#     def marca(self, marca):
#         self._marca = marca
    
#     @property
#     def modelo(self):
#         return self._modelo

#     @modelo.setter
#     def modelo(self, modelo):
#         self._modelo = modelo
    
#     @property    
#     def año(self):
#         return self._año
    
#     @año.setter
#     def año(self, año):
#         self._año = año
    
# carro =  Coche("KENWORTH", "T680", 2024)
# print(f"""
#       {carro.marca}
#       {carro.modelo}
#       {carro.año}
#       """)
# carro.marca = "DAF"
# carro.modelo = "XF"

# print(f"""
#       {carro.marca}
#       {carro.modelo}
#       {carro.año}
#       """)

