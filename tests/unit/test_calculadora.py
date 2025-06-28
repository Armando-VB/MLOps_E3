import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest
from calculadora import Calculadora

def test_sumar():
    calc = Calculadora()
    assert "El resultado de sumar 2 y 3 es: 5.0" == calc.sumar(2, 3)
    assert "El resultado de sumar -1 y 1 es: 0.0" == calc.sumar(-1, 1)

def test_restar():
    calc = Calculadora()
    assert 5 == calc.restar(10, 5)
    assert -1 == calc.restar(2, 3)

def test_multiplicar():
    calc = Calculadora()
    assert 6 == calc.multiplicar(2, 3)
    assert -6 == calc.multiplicar(2, -3)

def test_dividir():
    calc = Calculadora()
    assert 2 == calc.dividir(10, 5)
    assert "Error: No se puede dividir por cero" == calc.dividir(5, 0)

def test_validacion_entrada():
    calc = Calculadora()
    assert "Error: Ingrese números válidos" == calc.sumar("a", 3)

def test_potencia():
    calc = Calculadora()
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(5, 0) == 1

def test_raiz_cuadrada():
    calc = Calculadora()
    assert calc.raiz_cuadrada(4) == 2
    assert calc.raiz_cuadrada(9) == 3
    assert calc.raiz_cuadrada(0) == 0
    assert "Error: No se puede calcular la raíz cuadrada de un número negativo" == calc.raiz_cuadrada(-1)
