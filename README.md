# Calculadora MLOps E3 - Rama feature/raiz-potencia

## Descripción
Calculadora básica implementada en Python con operaciones matemáticas de potencia y raíz cuadrada. Este proyecto incluye pruebas unitarias, pruebas de integración y CI/CD con GitHub Actions.

**Rama actual: `feature/raiz-potencia`**

## Funcionalidades Disponibles en esta Rama
- ✅ Potencia
- ✅ Raíz cuadrada

## Estructura del Proyecto
```
MLOps_E3/
├── calculadora.py              # Implementación principal (solo potencia y raíz)
├── tests/
│   ├── unit/                   # Pruebas unitarias
│   │   └── test_calculadora.py
│   └── integration/            # Pruebas de integración
│       └── test_calculadora_integration.py
├── .github/workflows/          # GitHub Actions
│   └── python-ci.yml
└── README.md
```

## Instalación y Uso

### Requisitos
- Python 3.10+

### Instalación
```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd MLOps_E3

# Cambiar a la rama feature/raiz-potencia
git checkout feature/raiz-potencia

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecución
```bash
# Ejecutar la calculadora (solo potencia y raíz cuadrada)
python calculadora.py

# Ejecutar pruebas unitarias
pytest tests/unit/

# Ejecutar pruebas de integración
pytest tests/integration/

# Verificar estilo de código
flake8 .
```

## Pruebas
El proyecto incluye:
- **Pruebas unitarias**: Verifican cada función individualmente
- **Pruebas de integración**: Verifican la interacción entre potencia y raíz cuadrada
- **Validación de entrada**: Manejo de errores para entradas inválidas

## CI/CD
GitHub Actions ejecuta automáticamente:
- ✅ Verificación de estilo con flake8
- ✅ Pruebas unitarias con pytest
- ✅ Pruebas de integración con pytest

## Ramas del Proyecto
- `main`: Rama principal con todas las funcionalidades
- `feature/raiz-potencia`: Rama específica para potencia y raíz cuadrada (actual)

## Contribución
1. Crear una nueva rama para tu funcionalidad
2. Implementar las pruebas unitarias
3. Implementar las pruebas de integración
4. Crear un Pull Request
5. Esperar la revisión y aprobación

## Autor
Equipo MLOps E3
