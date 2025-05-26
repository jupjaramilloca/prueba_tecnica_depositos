"""
Autor: Juan Pablo
Fecha: 2025-05-24
Descripción: Función para multiplicar múltiples argumentos numéricos,
             con validación que muestra mensaje en caso de argumentos inválidos
             y que se asegure que se ingresen 3 o más números,
             decorador que mide tiempo de ejecución,
             y ciclo que permite reintentar si hay errores.
"""

import time

# Decorador que mide el tiempo de ejecución y muestra el resultado
def medir_tiempo(func):
    def wrapper(*args):
        invalidos = [str(arg) for arg in args if not isinstance(arg, (int, float))]
        if invalidos:
            print(f"Error: Los siguientes argumentos no son numéricos o válidos: {', '.join(invalidos)}")
            return None
        inicio = time.time()
        resultado = func(*args)
        fin = time.time()
        print(f"Resultado: {resultado}")
        print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def multiplicar_numeros(*args):
    producto = 1
    for num in args:
        producto *= num
    return producto

if __name__ == "__main__":
    print("Multiplicador de números con validación y medición de tiempo.\n")
    print('Escribe "salir" para terminar el programa.\n')

    while True:
        entrada = input("Ingresa 3 o más números separados por coma: ")
        if entrada.lower() == "salir":
            print("Programa terminado.")
            break

        lista_argumentos = [x.strip() for x in entrada.split(",")]

        # Convertimos entrada a números si es posible
        argumentos = []
        invalidos_input = []
        for valor in lista_argumentos:
            try:
                num = float(valor)
                argumentos.append(num)
            except ValueError:
                invalidos_input.append(valor)

        # Mensajes de error acumulados
        errores = []

        if invalidos_input:
            errores.append(f"Error: Los siguientes argumentos no son numéricos o válidos: {', '.join(invalidos_input)}")

        if len(argumentos) < 3:
            errores.append("Error: Debes ingresar al menos 3 números válidos.")

        # Si hay errores, los mostramos y volvemos a pedir
        if errores:
            print("\n".join(errores))
            print("Por favor, ingresa solo números válidos y al menos 3 de ellos.\n")
            continue

        # Si pasa las validaciones, se ejecuta la función
        resultado = multiplicar_numeros(*argumentos)
        if resultado is not None:
            print("Operación exitosa.\n")