"""
Calculadora Básica Python | Decoradores 
Esta es una calculadora básica que permite realizar operaciones de suma, resta, multiplicación y división.
"""

def validar_entrada(func):
    def wrapper(*args):
        try:
            return func(*args)
        except (ValueError, TypeError):
            return "Error: Ingrese números válidos"
        except ZeroDivisionError:
            return "Error: No se puede dividir por cero"
    return wrapper

"""
Clase Calculadora
Esta clase contiene métodos estáticos para realizar operaciones matemáticas básicas.
"""

class Calculadora:
    @staticmethod
    @validar_entrada
    def sumar(a, b):
        resultado = float(a) + float(b)
        return f"El resultado de sumar {a} y {b} es: {resultado}"

    @staticmethod
    @validar_entrada
    def restar(a, b):
        return float(a) - float(b)

    @staticmethod
    @validar_entrada
    def multiplicar(a, b):
        return float(a) * float(b)

    @staticmethod
    @validar_entrada
    def dividir(a, b):
        return float(a) / float(b)


def main():
    calc = Calculadora()
    opcion = ""  

    while opcion != "5":
        print("\nCalculadora Básica")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("\nSeleccione una operación (1-5): ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opción no válida")
            continue

        try:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
        except ValueError:
            print("Por favor ingrese números válidos")
            continue

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
# fin del archivo calculadora.py - fin del archivo calculadora.py