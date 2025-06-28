"""
Calculadora Básica Python | Rama feature/raiz-potencia
Esta calculadora incluye todas las operaciones matemáticas básicas.
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
    def sumar(a, b):
        """Suma dos números."""
        resultado = float(a) + float(b)
        return f"El resultado de sumar {a} y {b} es: {resultado}"

    @staticmethod
    @validar_entrada
    def restar(a, b):
        """Resta dos números."""
        return float(a) - float(b)

    @staticmethod
    @validar_entrada
    def multiplicar(a, b):
        """Multiplica dos números."""
        return float(a) * float(b)

    @staticmethod
    @validar_entrada
    def dividir(a, b):
        """Divide dos números."""
        return float(a) / float(b)

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

    while opcion != "7":
        print("\nCalculadora - Rama feature/raiz-potencia")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("6. Raíz Cuadrada")
        print("7. Salir")

        opcion = input("\nSeleccione una operación (1-7): ")

        if opcion == "7":
            print("¡Hasta luego!")
            break

        if opcion not in ("1", "2", "3", "4", "5", "6"):
            print("Opción no válida")
            continue

        if opcion == "6":
            num1 = input("Ingrese un número: ")
            resultado = calc.raiz_cuadrada(num1)
            print(f"Resultado: {resultado}")
            continue

        if opcion == "5":
            num1 = input("Ingrese la base: ")
            num2 = input("Ingrese el exponente: ")
            resultado = calc.potencia(num1, num2)
            print(f"Resultado: {resultado}")
            continue

        num1 = input("Primer número: ")
        num2 = input("Segundo número: ")

        operaciones = {
            "1": calc.sumar,
            "2": calc.restar,
            "3": calc.multiplicar,
            "4": calc.dividir
        }

        resultado = operaciones[opcion](num1, num2)
        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
