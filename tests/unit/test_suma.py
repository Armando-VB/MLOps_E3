from calculadora import Calculadora


def test_sumar_enteros():
    assert Calculadora.sumar(2, 3) == "El resultado de sumar 2 y 3 es: 5.0"


def test_sumar_decimales():
    assert Calculadora.sumar(1.5, 2.5) == "El resultado de sumar 1.5 y 2.5 es: 4.0"


def test_sumar_entrada_invalida():
    assert Calculadora.sumar("a", 3) == "Error: Ingrese números válidos"
    