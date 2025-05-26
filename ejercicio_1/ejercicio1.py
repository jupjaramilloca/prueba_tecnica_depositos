"""
Ejercicio 1 - Pilares de la Programación Orientada a Objetos
Autor: Juan Pa
Fecha: 2025-05-24
Descripción:
Programa interactivo en Python que explica y ejemplifica
los cuatro pilares fundamentales de la POO: Encapsulamiento,
Herencia, Polimorfismo y Abstracción. Cada pilar se presenta
con ejemplos dinámicos y explicaciones claras.
"""

# Importamos ABC y abstractmethod para definir clases abstractas
from abc import ABC, abstractmethod

# ==============================
# Encapsulamiento
# ==============================
# Clase que simula una cuenta bancaria con atributos privados
class CuentaBancaria:
    # Método constructor que inicializa el titular y saldo como privados
    def __init__(self, titular, saldo):
        self.__titular = titular  # atributo privado titular
        self.__saldo = saldo      # atributo privado saldo

    # Método público para depositar dinero en la cuenta
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    # Método público para mostrar el saldo y titular de la cuenta
    def mostrar_saldo(self):
        return f"Titular: {self.__titular} - Saldo: ${self.__saldo}"

# Función que ejecuta el ejemplo de encapsulamiento con interacción
def ejemplo_encapsulamiento():
    print("\n--- Encapsulamiento ---")
    print("Encapsulamiento significa proteger los atributos internos de un objeto para que solo puedan ser modificados por métodos definidos.")
    print("Usamos variables como 'titular' y 'saldo' para simular una cuenta bancaria segura.\n")

    # Solicita al usuario datos para crear la cuenta
    titular = input("Ingresa el nombre del titular de la cuenta: ")
    saldo = float(input("Ingresa el saldo inicial: "))
    cantidad = float(input("Ingresa la cantidad a depositar: "))
    
    # Creación del objeto CuentaBancaria y operación depósito
    cuenta = CuentaBancaria(titular, saldo)
    cuenta.depositar(cantidad)

    # Muestra el resultado final
    print("Resultado:", cuenta.mostrar_saldo())
    input("\nPresiona Enter para volver al menú...")

# ==============================
# Herencia
# ==============================
# Clase base Animal con un atributo nombre
class Animal:
    # Constructor que recibe el nombre del animal
    def __init__(self, nombre):
        self.nombre = nombre

    # Método que define el sonido genérico del animal
    def hablar(self):
        return "Hace un sonido."

# Clase derivada Perro que hereda de Animal
class Perro(Animal):
    # Método que sobreescribe hablar para dar un sonido específico
    def hablar(self):
        return f"{self.nombre} dice: ¡Guau!"

# Función que ejecuta el ejemplo de herencia con interacción
def ejemplo_herencia():
    print("\n--- Herencia ---")
    print("La herencia permite que una clase hija herede atributos y métodos de una clase padre.")
    print("Usamos 'Animal' como clase padre y 'Perro' como clase hija que hereda y modifica el método 'hablar'.\n")

    # Solicita al usuario el nombre del perro
    nombre = input("Ingresa el nombre del perro: ")
    perro = Perro(nombre)

    # Muestra el resultado de la llamada al método hablar
    print("Resultado:", perro.hablar())
    input("\nPresiona Enter para volver al menú...")

# ==============================
# Polimorfismo
# ==============================
# Clase derivada Gato que hereda de Animal
class Gato(Animal):
    # Método que sobreescribe hablar para dar un sonido diferente
    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"

# Función que ejecuta el ejemplo de polimorfismo con interacción
def ejemplo_polimorfismo():
    print("\n--- Polimorfismo ---")
    print("El polimorfismo permite que diferentes clases compartan un método con el mismo nombre, pero diferente implementación.")
    print("Usamos 'Perro' y 'Gato' como clases con el método 'hablar', pero con sonidos diferentes.\n")

    # Solicita una lista de nombres y tipos de animales separados por coma
    nombres = input("Escribe nombres de animales separados por coma (ej. Toby,Luna): ").split(",")
    tipos = input("Escribe el tipo (perro/gato) por cada uno, separados por coma (ej. perro,gato): ").split(",")

    animales = []
    # Crea objetos Perro o Gato según el tipo ingresado
    for nombre, tipo in zip(nombres, tipos):
        nombre = nombre.strip()
        tipo = tipo.strip().lower()
        if tipo == "perro":
            animales.append(Perro(nombre))
        elif tipo == "gato":
            animales.append(Gato(nombre))

    # Muestra el resultado llamando al método hablar de cada objeto
    print("Resultados:")
    for animal in animales:
        print(animal.hablar())
    
    input("\nPresiona Enter para volver al menú...")

# ==============================
# Abstracción
# ==============================
# Clase abstracta Vehiculo que define método abstracto encender
class Vehiculo(ABC):
    @abstractmethod
    def encender(self):
        pass

# Clase Carro que implementa el método abstracto
class Carro(Vehiculo):
    def encender(self):
        return "El carro está encendido."

# Clase Moto que implementa el método abstracto
class Moto(Vehiculo):
    def encender(self):
        return "La moto está encendida."

# Función que ejecuta el ejemplo de abstracción con interacción
def ejemplo_abstraccion():
    print("\n--- Abstracción ---")
    print("La abstracción permite definir estructuras base sin necesidad de implementar completamente sus métodos.")
    print("Usamos la clase abstracta 'Vehiculo' y luego implementamos 'Carro' y 'Moto'.\n")

    # Solicita al usuario qué tipo de vehículo desea encender
    tipo = input("¿Qué deseas encender? (carro/moto): ").lower()
    if tipo == "carro":
        vehiculo = Carro()
    elif tipo == "moto":
        vehiculo = Moto()
    else:
        print("Tipo no reconocido.")
        input("\nPresiona Enter para volver al menú...")
        return
    print("Resultado:", vehiculo.encender())
    input("\nPresiona Enter para volver al menú...")

# ==============================
# Menú principal para seleccionar ejemplos
# ==============================
def menu():
    while True:
        print("\n=== Pilares de la Programación Orientada a Objetos ===")
        print("1. Encapsulamiento")
        print("2. Herencia")
        print("3. Polimorfismo")
        print("4. Abstracción")
        print("5. Todos")
        print("0. Salir")
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            ejemplo_encapsulamiento()
        elif opcion == "2":
            ejemplo_herencia()
        elif opcion == "3":
            ejemplo_polimorfismo()
        elif opcion == "4":
            ejemplo_abstraccion()
        elif opcion == "5":
            ejemplo_encapsulamiento()
            ejemplo_herencia()
            ejemplo_polimorfismo()
            ejemplo_abstraccion()
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Punto de entrada del script
if __name__ == "__main__":
    menu()
