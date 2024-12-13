# numero = 1
# print(numero)
# print(float(numero))

def factorial(n):
    # FACTORIAL(N) = N * FACTORIAL(N-1) PARA N > 0
    # Condición base: el factorial de 0 es 1
    if n == 0:
        return 1
    else:
        # Llamada recursiva: factorial(n) = n * factorial(n-1)
        return n * factorial(n - 1)

# Ejemplo de uso
numero = 5
print(f"El factorial de {numero} es: {factorial(numero)}")

#POLIMORFISMO
# class Persona:
#     def __init__(self, nombre, edad, sexo = None):
#         self.__nombre = nombre
#         self.edad = edad
#         self.sexo = sexo
        
#     def mostrar_nombre(self):
#         return self.__nombre
    
#     def mostrar_datos_completos(self):
#         return f"Nombre: {self.__nombre}, Edad: {self.edad}, Sexo:{self.sexo}"

#     def cambiar_nombre(self, nombre):
#         self.__nombre = nombre
    
    
# persona = Persona("Juan Solano", 24)
# print(persona.mostrar_nombre())
# persona.cambiar_nombre("Moises")
# print(persona.mostrar_datos_completos())

# persona2 = Persona("Rosa Me La manguera", 17, "Femenino")
# print(persona2.mostrar_nombre())
# print(persona2.mostrar_datos_completos())

#ABSTRACCIÓN
# from abc import ABC, abstractmethod
# class Animal:
#     @abstractmethod
#     def hacer_sonido(self):
#         pass

# class Perro(Animal):
#     def hacer_sonido(self):
#         return "Guau"
    
# class Gato(Animal):
#     def hacer_sonido(self):
#         return "Miau"
    
# perro = Perro()
# print(perro.hacer_sonido())

# gato = Gato()
# print(gato.hacer_sonido())

#HERENCIA
# class Animal:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def hablar(self):
#         pass

# class Perro(Animal):
#     def hablar(self):
#         nombre = self.nombre
#         return f"nombre: {nombre} - sonido: Guau"

# class Gato(Animal):
#     def hablar(self):
#         nombre = self.nombre
#         return f"nombre: {nombre} - sonido : Miau"

# # Uso de herencia
# perro = Perro("Max")
# print(perro.hablar())  # "Guau"
# gato = Gato("Felix")
# print(gato.hablar())  # "Miau"