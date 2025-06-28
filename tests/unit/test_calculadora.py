import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from calculadora import Calculadora  # noqa: E402


def test_potencia():
    """Prueba la funcionalidad de potencia."""
    calc = Calculadora()
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(5, 0) == 1
    assert calc.potencia(3, 2) == 9
    assert calc.potencia(2, -1) == 0.5


def test_raiz_cuadrada():
    """Prueba la funcionalidad de raíz cuadrada."""
    calc = Calculadora()
    assert calc.raiz_cuadrada(4) == 2
    assert calc.raiz_cuadrada(9) == 3
    assert calc.raiz_cuadrada(0) == 0
    assert calc.raiz_cuadrada(16) == 4
    error_msg = "Error: No se puede calcular la raíz cuadrada de un número negativo"
    assert error_msg == calc.raiz_cuadrada(-1)


def test_division():
    """Prueba la funcionalidad de división."""
    calc = Calculadora()
    assert calc.dividir(10, 2) == 5.0
    assert calc.dividir(15, 3) == 5.0
    assert calc.dividir(7, 2) == 3.5
    assert calc.dividir(0, 5) == 0.0
    assert calc.dividir(-10, 2) == -5.0


def test_division_por_cero():
    """Prueba la división por cero."""
    calc = Calculadora()
    assert calc.dividir(10, 0) == "Error: No se puede dividir por cero"
    assert calc.dividir(0, 0) == "Error: No se puede dividir por cero"
    assert calc.dividir(-5, 0) == "Error: No se puede dividir por cero"


def test_validacion_entrada_potencia():
    """Prueba la validación de entrada para potencia."""
    calc = Calculadora()
    assert "Error: Ingrese números válidos" == calc.potencia("a", 3)
    assert "Error: Ingrese números válidos" == calc.potencia(2, "b")


def test_validacion_entrada_raiz():
    """Prueba la validación de entrada para raíz cuadrada."""
    calc = Calculadora()
    assert "Error: Ingrese números válidos" == calc.raiz_cuadrada("abc")


def test_validacion_entrada_division():
    """Prueba la validación de entrada para división."""
    calc = Calculadora()
    assert "Error: Ingrese números válidos" == calc.dividir("a", 3)
    assert "Error: Ingrese números válidos" == calc.dividir(2, "b")
    assert "Error: Ingrese números válidos" == calc.dividir("abc", "def")


def JPBS_resta():
    """Prueba la validación de entrada para división."""
    calc = Calculadora()
    assert "Error: Ingrese números válidos" == calc.restar("a", 3)
    assert "Error: Ingrese números válidos" == calc.restar(2, "b")
    assert "Error: Ingrese números válidos" == calc.restar("abc", "def")
