#// Principio de Responsabilidad Única
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_pago(self):
        # Lógica para calcular el pago
        return self.salario

    def guardar_empleado(self):
        # Lógica para guardar al empleado en la base de datos
        pass
    
    
    
# Mejorado: Dividimos la responsabilidad en dos clases: una para los empleados y otra para manejar la persistencia de datos.
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_pago(self):
        return self.salario

class EmpleadoRepository:
    def guardar_empleado(self, empleado):
        # Lógica para guardar al empleado en la base de datos
        pass
    
#// Cohesión Alta
# Una clase CuentaBancaria debe manejar solo las operaciones relacionadas con una cuenta bancaria, como los depósitos y retiros.
class CuentaBancaria:
    def __init__(self, balance_inicial):
        self.balance = balance_inicial

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("Fondos insuficientes")

    def consultar_balance(self):
        return self.balance
# En este caso, todos los métodos están relacionados con la gestión de una cuenta bancaria, lo que mantiene una alta cohesión en la clase

#// Acoplamiento Bajo
# Imagina que tienes una clase Factura que necesita calcular el impuesto, pero en lugar de hacerlo directamente, delega esta tarea a una clase separada.
# Mal diseño (alto acoplamiento):
class Factura:
    def __init__(self, total):
        self.total = total

    def calcular_impuesto(self):
        return self.total * 0.21
    
# Buen diseño (bajo acoplamiento):
class CalculadoraImpuesto:
    def calcular(self, total):
        return total * 0.21

class Factura:
    def __init__(self, total, calculadora_impuesto):
        self.total = total
        self.calculadora_impuesto = calculadora_impuesto

    def calcular_impuesto(self):
        return self.calculadora_impuesto.calcular(self.total)
# En el diseño mejorado, Factura no está directamente acoplada a la lógica de cálculo de impuestos, sino que depende de una clase CalculadoraImpuesto, lo que reduce el acoplamiento.

#// Principio de Abierto/Cerrado (OCP - Open/Closed Principle)

# Supongamos que tienes una clase Notificador que envía mensajes a través de diferentes canales (correo, SMS). En lugar de modificar la clase cada vez que se agrega un nuevo canal, puedes extender la funcionalidad.
# Mal diseño (modificar la clase cada vez):
class Notificador:
    def notificar(self, mensaje, tipo):
        if tipo == "email":
            # Enviar correo
            print(f"Enviando correo: {mensaje}")
        elif tipo == "sms":
            # Enviar SMS
            print(f"Enviando SMS: {mensaje}")
# Buen diseño (extender la clase sin modificarla):
class Notificador:
    def notificar(self, mensaje):
        raise NotImplementedError()

class NotificadorEmail(Notificador):
    def notificar(self, mensaje):
        print(f"Enviando correo: {mensaje}")

class NotificadorSMS(Notificador):
    def notificar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")
# De este modo, puedes agregar nuevos canales de notificación (como push notifications o WhatsApp) sin tocar la clase base Notificador, solo creando nuevas subclases.

#// Principio de Sustitución de Liskov (LSP - Liskov Substitution Principle)
# Si tienes una clase Animal y una subclase Perro, la subclase Perro debe comportarse de la misma manera que la clase Animal.
class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

# Uso de la clase base y la subclase de manera intercambiable
def hacer_sonido_del_animal(animal: Animal):
    print(animal.hacer_sonido())

perro = Perro()
hacer_sonido_del_animal(perro)  # Imprime "Guau"
# La subclase Perro es completamente intercambiable con la clase base Animal en el contexto de llamar al método hacer_sonido.

#// Principio de Segregación de Interfaces (ISP - Interface Segregation Principle)
# Supón que tienes una interfaz para manejar vehículos, pero no todos los vehículos tienen la misma funcionalidad (por ejemplo, no todos vuelan). En lugar de tener una única interfaz con todos los métodos, dividimos las funcionalidades en interfaces más pequeñas.
# Mal diseño (una interfaz grande):
class Vehiculo:
    def conducir(self):
        pass
    
    def volar(self):
        pass

class Coche(Vehiculo):
    def conducir(self):
        print("Conduciendo el coche")

    def volar(self):
        raise NotImplementedError("Este vehículo no puede volar")
# Buen diseño (interfaces separadas):
class VehiculoTerrestre:
    def conducir(self):
        pass

class VehiculoAereo:
    def volar(self):
        pass

class Coche(VehiculoTerrestre):
    def conducir(self):
        print("Conduciendo el coche")

class Avion(VehiculoAereo):
    def volar(self):
        print("Volando el avión")
# Ahora, Coche y Avion no están obligados a implementar métodos que no usan, lo que mejora la flexibilidad del sistema.

#// Principio de Inversión de Dependencias (DIP - Dependency Inversion Principle)
# Si tienes una clase Coche que depende de una clase Motor, lo ideal es que ambas dependan de una interfaz Motor.
class Motor:
    def arrancar(self):
        pass

class MotorElectrico(Motor):
    def arrancar(self):
        print("Motor eléctrico arrancado")

class Coche:
    def __init__(self, motor: Motor):
        self.motor = motor

    def arrancar(self):
        self.motor.arrancar()

# Uso
motor = MotorElectrico()
coche = Coche(motor)
coche.arrancar()  # "Motor eléctrico arrancado"
# De esta forma, el Coche no depende de la implementación concreta de MotorElectrico, sino de la abstracción Motor.
#// Composición sobre Herencia
# Supón que tienes una clase Vehiculo que tiene un motor. En lugar de usar herencia, podemos usar composición.
# Mal diseño (herencia):
class Vehiculo:
    def __init__(self):
        self.motor = Motor()
    
    def arrancar(self):
        self.motor.arrancar()
# Buen diseño (composición):
class Motor:
    def arrancar(self):
        print("Motor arrancado")

class Vehiculo:
    def __init__(self, motor: Motor):
        self.motor = motor

    def arrancar(self):
        self.motor.arrancar()
# La composición es más flexible, ya que permite cambiar el motor sin tener que modificar la clase Vehiculo.

#// Uso de Métodos Especiales (Dunder Methods)
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)
    
    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

p1 = Punto(1, 2)
p2 = Punto(3, 4)
print(p1 + p2)  # Salida: Punto(4, 6)
# Este ejemplo usa el método especial __add__ para permitir la suma de objetos Punto y el método __repr__ para la representación en cadena de los objetos.


# RELACIONES
#// ASOCIACIÓN
# Imagina que tenemos una clase Estudiante que está asociada con la clase Curso. Un estudiante puede estar inscrito en muchos cursos, y un curso puede tener muchos estudiantes.
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def inscribirse(self, curso):
        print(f"{self.nombre} se ha inscrito en el curso {curso.nombre}")

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre

# Creando instancias
estudiante = Estudiante("Juan")
estudiante2 = Estudiante("Moises")

curso = Curso("Matemáticas")
curso2 = Curso("Física")

# Asociación: el estudiante se asocia con el curso
estudiante.inscribirse(curso)
estudiante2.inscribirse(curso2)
# En este caso, un Estudiante puede estar asociado con un Curso a través del método inscribirse(), pero ambos objetos (Estudiante y Curso) siguen existiendo de forma independiente.

#// AGREGACIÓN
# Supongamos que tenemos una clase Departamento y una clase Empleado. Un Departamento tiene varios Empleados, pero si el Departamento se elimina, los Empleados pueden seguir existiendo.
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nombre} agregado al departamento {self.nombre}")

# Creando instancias
empleado1 = Empleado("Ana")
empleado2 = Empleado("Luis")
departamento = Departamento("Recursos Humanos")

# Agregación: El departamento agrega empleados, pero los empleados pueden existir sin el departamento
departamento.agregar_empleado(empleado1)
departamento.agregar_empleado(empleado2)
# En este caso, los objetos Empleado existen de forma independiente de la clase Departamento. Si el Departamento se elimina, los Empleado todavía pueden existir, lo que indica una relación de agregación.


#// COMPOSICIÓN
# Imagina que tienes una clase Coche que tiene un Motor. Un Motor no tiene sentido sin un Coche, ya que no puede existir de forma independiente, y si el Coche se destruye, el Motor también lo hará.
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def arrancar(self):
        print(f"Motor {self.tipo} arrancado")

class Coche:
    def __init__(self, modelo, motor_tipo):
        self.modelo = modelo
        # El Motor es una parte del Coche y se crea dentro de la clase Coche (composición)
        self.motor = Motor(motor_tipo)

    def arrancar(self):
        print(f"{self.modelo} arrancando...")
        self.motor.arrancar()

# Creando instancias
coche = Coche("Toyota", "V6")
coche.arrancar()

# Aquí, el Motor es una parte del Coche. Si el Coche es destruido (por ejemplo, si eliminamos la instancia coche), el Motor también será destruido. Esto ilustra una relación de composición.

#// LISTAS
# Definir una lista en Python
mi_lista = [10, 25, 20, 30, 40, 50]

# Acceso por índice
print(mi_lista[0])  # Imprime 10

# Agregar un elemento al final
mi_lista.append(50)

# Eliminar un elemento
mi_lista.remove(20)

# Insertar en una posición específica
mi_lista.insert(1, 25)

# Recorrer la lista
for elemento in mi_lista:
    print(elemento)


#// LISTA ENLAZADA
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

# Uso de la lista enlazada
lista = ListaEnlazada()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.imprimir()


#// PILAS
class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Uso de la pila
pila = Pila()
pila.push(10)
pila.push(20)
pila.push(30)
# [10,20,30]
print(pila.pop())  # Imprime 30
print(pila.peek())  # Imprime 20
print(pila.is_empty())  # Imprime False


#// COLAS
class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Uso de la cola
cola = Cola()
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
# [20,30]
print(cola.dequeue())  # Imprime 10
print(cola.peek())  # Imprime 20
print(cola.is_empty())  # Imprime False


#// DEQUE
from collections import deque

# Crear un deque
mi_deque = deque()

# Agregar elementos al final
mi_deque.append(10)
mi_deque.append(20)
#[5,10,20]
# Agregar elementos al inicio
mi_deque.appendleft(5)
#[5,10]
# Eliminar elementos del final
print(mi_deque.pop())  # Imprime 20
#[10]
# Eliminar elementos del inicio
print(mi_deque.popleft())  # Imprime 5
#[10]
# Ver el deque actual
print(mi_deque)  # Imprime deque([10])
