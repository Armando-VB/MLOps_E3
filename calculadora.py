"""
Calculadora Básica Python | Rama feature/raiz-potencia
Esta calculadora incluye solo las funcionalidades de potencia y raíz cuadrada.
"""

import math


def validar_entrada(func):
    """Decorador para validar entradas y manejar errores."""

    def wrapper(*args):
        try:
            return func(*args)
        except (ValueError, TypeError):
            return "Error: Ingrese números válidos"
        except ZeroDivisionError:
            return "Error: No se puede dividir por cero"

    return wrapper


class Calculadora:
    """Clase Calculadora con métodos estáticos para operaciones matemáticas."""

    @staticmethod
    @validar_entrada
    def potencia(a, b):
        """Calcula la potencia de un número."""
        return float(a) ** float(b)

    @staticmethod
    @validar_entrada
    def raiz_cuadrada(a):
        """Calcula la raíz cuadrada de un número."""
        if float(a) < 0:
            return "Error: No se puede calcular la raíz cuadrada de un número negativo"
        return math.sqrt(float(a))


def main():
    """Función principal que ejecuta la interfaz de la calculadora."""
    calc = Calculadora()
    opcion = ""

    while opcion != "3":
        print("\nCalculadora - Rama feature/raiz-potencia")
        print("1. Potencia")
        print("2. Raíz Cuadrada")
        print("3. Salir")

        opcion = input("\nSeleccione una operación (1-3): ")

        if opcion == "3":
            print("¡Hasta luego!")
            break

        if opcion not in ("1", "2"):
            print("Opción no válida")
            continue

        if opcion == "2":
            num1 = input("Ingrese un número: ")
            resultado = calc.raiz_cuadrada(num1)
            print(f"Resultado: {resultado}")
            continue

        if opcion == "1":
            num1 = input("Ingrese la base: ")
            num2 = input("Ingrese el exponente: ")
            resultado = calc.potencia(num1, num2)
            print(f"Resultado: {resultado}")
            continue


if __name__ == "__main__":
    main()
