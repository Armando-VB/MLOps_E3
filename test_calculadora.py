from calculadora import Calculadora

def probar(nombre, funcion, a, b):
    resultado = funcion(a, b)
    print(f"{nombre}({a}, {b}) = {resultado}")

if __name__ == "__main__":
    calc = Calculadora()

    print("\n== PRUEBAS DE LA CALCULADORA ==")

    # Pruebas válidas
    probar("Sumar", calc.sumar, 5, 3)         # Esperado: El resultado de sumar 5 y 3 es: 8.0
    probar("Restar", calc.restar, 10, 4)      # Esperado: 6.0
    probar("Multiplicar", calc.multiplicar, 6, 7)  # Esperado: 42.0
    probar("Dividir", calc.dividir, 12, 4)    # Esperado: 3.0

    # Prueba división por cero
    probar("Dividir", calc.dividir, 10, 0)    # Esperado: Error: No se puede dividir por cero

    # Prueba con datos no numéricos
    probar("Sumar", calc.sumar, "a", 2)       # Esperado: Error: Ingrese números válidos

