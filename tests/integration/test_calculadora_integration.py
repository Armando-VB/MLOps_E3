import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest
from calculadora import Calculadora

def test_potencia_y_raiz():
    """Prueba la integración entre potencia y raíz cuadrada."""
    calc = Calculadora()
    # Calcular potencia y luego su raíz cuadrada
    resultado_potencia = calc.potencia(3, 2)
    assert 9 == resultado_potencia
    
    resultado_raiz = calc.raiz_cuadrada(resultado_potencia)
    assert 3 == resultado_raiz

def test_raiz_y_potencia():
    """Prueba la integración entre raíz cuadrada y potencia."""
    calc = Calculadora()
    # Calcular raíz cuadrada y luego elevarla al cuadrado
    resultado_raiz = calc.raiz_cuadrada(16)
    assert 4 == resultado_raiz
    
    resultado_potencia = calc.potencia(resultado_raiz, 2)
    assert 16 == resultado_potencia

def test_manejo_errores_integrado():
    """Prueba el manejo de errores en secuencia."""
    calc = Calculadora()
    
    # Probar el manejo de errores en secuencia
    assert "Error: Ingrese números válidos" == calc.potencia("abc", 5)
    assert "Error: No se puede calcular la raíz cuadrada de un número negativo" == calc.raiz_cuadrada(-1)
    assert 8 == calc.potencia(2, 3)  # Operación válida después de errores

def test_operaciones_secuenciales():
    """Prueba operaciones secuenciales con potencia y raíz."""
    calc = Calculadora()
    
    # Secuencia: potencia -> raíz -> potencia
    resultado1 = calc.potencia(2, 4)  # 16
    assert 16 == resultado1
    
    resultado2 = calc.raiz_cuadrada(resultado1)  # 4
    assert 4 == resultado2
    
    resultado3 = calc.potencia(resultado2, 3)  # 64
    assert 64 == resultado3

def test_potencia_integration():
    """Prueba integración específica de potencia."""
    calc = Calculadora()
    assert calc.potencia(2, 4) == 16
    assert calc.potencia(5, 2) == 25

def test_raiz_cuadrada_integration():
    """Prueba integración específica de raíz cuadrada."""
    calc = Calculadora()
    assert calc.raiz_cuadrada(16) == 4
    assert calc.raiz_cuadrada(25) == 5
