import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from calculadora import Calculadora  # noqa: E402


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


def test_division_y_potencia():
    """Prueba la integración entre división y potencia."""
    calc = Calculadora()
    # Calcular división y luego elevar el resultado a una potencia
    resultado_division = calc.dividir(20, 4)
    assert 5.0 == resultado_division

    resultado_potencia = calc.potencia(resultado_division, 2)
    assert 25 == resultado_potencia


def test_potencia_y_division():
    """Prueba la integración entre potencia y división."""
    calc = Calculadora()
    # Calcular potencia y luego dividir el resultado
    resultado_potencia = calc.potencia(4, 3)
    assert 64 == resultado_potencia

    resultado_division = calc.dividir(resultado_potencia, 8)
    assert 8.0 == resultado_division


def test_raiz_y_division():
    """Prueba la integración entre raíz cuadrada y división."""
    calc = Calculadora()
    # Calcular raíz cuadrada y luego dividir el resultado
    resultado_raiz = calc.raiz_cuadrada(25)
    assert 5 == resultado_raiz

    resultado_division = calc.dividir(resultado_raiz, 2)
    assert 2.5 == resultado_division


def test_division_y_raiz():
    """Prueba la integración entre división y raíz cuadrada."""
    calc = Calculadora()
    # Calcular división y luego la raíz cuadrada del resultado
    resultado_division = calc.dividir(50, 2)
    assert 25.0 == resultado_division

    resultado_raiz = calc.raiz_cuadrada(resultado_division)
    assert 5 == resultado_raiz


def test_manejo_errores_integrado():
    """Prueba el manejo de errores en secuencia."""
    calc = Calculadora()

    # Probar el manejo de errores en secuencia
    assert "Error: Ingrese números válidos" == calc.potencia("abc", 5)
    error_msg = "Error: No se puede calcular la raíz cuadrada de un número negativo"
    assert error_msg == calc.raiz_cuadrada(-1)
    assert "Error: No se puede dividir por cero" == calc.dividir(10, 0)
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


def test_operaciones_secuenciales_con_division():
    """Prueba operaciones secuenciales incluyendo división."""
    calc = Calculadora()

    # Secuencia: potencia -> división -> raíz
    resultado1 = calc.potencia(3, 3)  # 27
    assert 27 == resultado1

    resultado2 = calc.dividir(resultado1, 3)  # 9
    assert 9.0 == resultado2

    resultado3 = calc.raiz_cuadrada(resultado2)  # 3
    assert 3 == resultado3


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


def test_division_integration():
    """Prueba integración específica de división."""
    calc = Calculadora()
    assert calc.dividir(20, 4) == 5.0
    assert calc.dividir(15, 3) == 5.0
    assert calc.dividir(10, 0) == "Error: No se puede dividir por cero"


def test_multiplicacion_y_suma():
    """Prueba integración: multiplicación y suma."""
    calc = Calculadora()
    mult = calc.multiplicar(2, 3)
    suma = calc.sumar(mult, 4)
    assert "10.0" in suma  # sumar devuelve string


def test_multiplicacion_y_resta():
    """Prueba integración: multiplicación y resta."""
    calc = Calculadora()
    mult = calc.multiplicar(5, 2)
    resta = calc.restar(mult, 3)
    assert resta == 7.0


def test_multiplicacion_y_division():
    """Prueba integración: multiplicación y división."""
    calc = Calculadora()
    mult = calc.multiplicar(8, 2)
    div = calc.dividir(mult, 4)
    assert div == 4.0


def JPBS_resta():
    """Prueba de integracion para restar()"""
    calc = Calculadora()
    resultado1 = calc.restar(10, 3)
    resultado2 = calc.restar(resultado1, 2)
    assert resultado2 == 5
    