import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest
from calculadora import Calculadora

def test_secuencia_operaciones():
    calc = Calculadora()
    
    # Probar una secuencia de operaciones
    resultado1 = calc.sumar(5, 3)
    assert "El resultado de sumar 5 y 3 es: 8.0" == resultado1
    
    resultado2 = calc.multiplicar(float(resultado1.split()[-1]), 2)
    assert 16.0 == resultado2
    
    resultado3 = calc.dividir(resultado2, 4)
    assert 4.0 == resultado3

def test_manejo_errores_integrado():
    calc = Calculadora()
    
    # Probar el manejo de errores en secuencia
    assert "Error: Ingrese números válidos" == calc.multiplicar("abc", 5)
    assert "Error: No se puede dividir por cero" == calc.dividir(10, 0)
    assert "El resultado de sumar 1 y 2 es: 3.0" == calc.sumar(1, 2)  # Operación válida después de errores

def test_potencia_y_raiz():
    calc = Calculadora()
    resultado = calc.potencia(3, 2)
    assert 9 == resultado
    resultado2 = calc.raiz_cuadrada(resultado)
    assert 3 == resultado2

def test_operaciones_basicas():
    calc = Calculadora()
    assert calc.sumar(1, 2) == "El resultado de sumar 1 y 2 es: 3.0"
    assert calc.restar(5, 3) == 2
    assert calc.multiplicar(2, 3) == 6
    assert calc.dividir(10, 2) == 5

def test_potencia_integration():
    calc = Calculadora()
    assert calc.potencia(2, 4) == 16

# Solo en la rama "feature/raiz_cuadrada"
# def test_raiz_cuadrada_integration():
#     calc = Calculadora()
#     assert calc.raiz_cuadrada(16) == 4
