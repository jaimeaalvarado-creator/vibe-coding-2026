# Guía de Python Básico para Profesionales de la Salud 🐍

Esta guía introduce los conceptos fundamentales de Python de manera accesible, sin asumir experiencia previa en programación.

## Tabla de Contenidos

1. [¿Qué es Python?](#qué-es-python)
2. [Variables y Tipos de Datos](#variables-y-tipos-de-datos)
3. [Operaciones Básicas](#operaciones-básicas)
4. [Listas y Colecciones](#listas-y-colecciones)
5. [Condicionales (if/else)](#condicionales-ifelse)
6. [Bucles (for/while)](#bucles-forwhile)
7. [Funciones](#funciones)
8. [Importar Librerías](#importar-librerías)
9. [Ejemplos Médicos](#ejemplos-médicos)

---

## ¿Qué es Python?

Python es un lenguaje de programación **fácil de leer y escribir**, ideal para análisis de datos. Se usa ampliamente en investigación médica, análisis estadístico y ciencia de datos.

**¿Por qué Python para estadística médica?**
- ✅ Sintaxis clara y legible (parece "pseudocódigo")
- ✅ Librerías especializadas para análisis de datos (pandas, scipy)
- ✅ Gratuito y de código abierto
- ✅ Gran comunidad y recursos de aprendizaje
- ✅ Potente para visualización de datos

---

## Variables y Tipos de Datos

Las **variables** son contenedores para guardar información.

### Variables Básicas

```python
# Números enteros (int)
edad_paciente = 45
numero_pacientes = 120

# Números decimales (float)
fev1 = 2.85
temperatura = 36.7

# Texto (string)
nombre = "Juan Pérez"
diagnostico = "Asma controlada"

# Booleanos (True/False)
es_fumador = True
tiene_sintomas = False

# Ver el valor de una variable
print(edad_paciente)  # Imprime: 45
print(f"FEV1: {fev1} L")  # Imprime: FEV1: 2.85 L
```

### Tipos de Datos Explicados

| Tipo | Descripción | Ejemplo Médico |
|------|-------------|----------------|
| `int` | Número entero | Edad: 45 |
| `float` | Número decimal | FEV1: 2.85 |
| `string` | Texto | Nombre: "Juan" |
| `bool` | Verdadero/Falso | es_fumador: True |

**Piensa en las variables como etiquetas en tubos de laboratorio** - cada una guarda un tipo específico de información.

---

## Operaciones Básicas

### Operaciones Matemáticas

```python
# Operaciones aritméticas
suma = 10 + 5          # 15
resta = 10 - 5         # 5
multiplicacion = 10 * 5  # 50
division = 10 / 5      # 2.0
potencia = 2 ** 3      # 8 (2 elevado a 3)

# Ejemplo médico: Calcular IMC
peso = 70  # kg
altura = 1.75  # metros
imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}")  # IMC: 22.86
```

### Operaciones con Texto

```python
# Concatenar (unir) texto
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido  # "Juan Pérez"

# Formatear texto
edad = 45
mensaje = f"Paciente: {nombre_completo}, Edad: {edad} años"
print(mensaje)  # Paciente: Juan Pérez, Edad: 45 años
```

### Operaciones de Comparación

```python
# Comparadores (devuelven True o False)
fev1 = 2.5

es_bajo = fev1 < 2.0          # False
es_normal = fev1 >= 2.0       # True
es_igual = fev1 == 2.5        # True
es_diferente = fev1 != 3.0    # True

# Operadores lógicos
edad = 45
fumador = True

riesgo_alto = (edad > 40) and fumador  # True
necesita_revision = (edad > 60) or fumador  # True
```

---

## Listas y Colecciones

Las **listas** guardan múltiples valores en una sola variable.

### Crear y Usar Listas

```python
# Lista de valores de FEV1 de varios pacientes
fev1_pacientes = [2.5, 3.1, 2.8, 2.2, 3.4]

# Acceder a elementos (¡empieza en 0!)
primer_valor = fev1_pacientes[0]   # 2.5
segundo_valor = fev1_pacientes[1]  # 3.1
ultimo_valor = fev1_pacientes[-1]  # 3.4

# Modificar elementos
fev1_pacientes[0] = 2.6  # Cambiar el primer valor

# Añadir elementos
fev1_pacientes.append(2.9)  # Añade al final

# Número de elementos
cantidad = len(fev1_pacientes)  # 6
```

### Operaciones con Listas

```python
edades = [45, 38, 52, 41, 67]

# Estadísticas básicas (requiere importar)
promedio = sum(edades) / len(edades)  # 48.6
maximo = max(edades)  # 67
minimo = min(edades)  # 38

# Ordenar
edades_ordenadas = sorted(edades)  # [38, 41, 45, 52, 67]

# Filtrar (ver en bucles más abajo)
```

### Diccionarios (Pares Clave-Valor)

Los **diccionarios** guardan información relacionada, como una ficha médica.

```python
# Información de un paciente
paciente = {
    "nombre": "Juan Pérez",
    "edad": 45,
    "fev1": 2.85,
    "fumador": True,
    "diagnostico": "Asma"
}

# Acceder a valores
nombre = paciente["nombre"]  # "Juan Pérez"
edad = paciente["edad"]      # 45

# Añadir nueva información
paciente["tratamiento"] = "Salbutamol"

# Modificar valores
paciente["fev1"] = 2.90
```

---

## Condicionales (if/else)

Los **condicionales** permiten tomar decisiones en el código.

### Estructura Básica

```python
# Sintaxis básica
if condicion:
    # Código si es verdadero
else:
    # Código si es falso
```

### Ejemplos Médicos

```python
# Ejemplo 1: Clasificar FEV1
fev1 = 2.3

if fev1 < 2.0:
    clasificacion = "Bajo"
elif fev1 < 3.0:
    clasificacion = "Normal"
else:
    clasificacion = "Alto"

print(f"FEV1: {fev1} - Clasificación: {clasificacion}")


# Ejemplo 2: Criterios de riesgo
edad = 65
fumador = True
fev1 = 1.8

if edad > 60 and fumador and fev1 < 2.0:
    print("⚠️ Paciente de alto riesgo")
    print("Requiere seguimiento estrecho")
elif edad > 60 or fev1 < 2.0:
    print("⚡ Paciente de riesgo moderado")
else:
    print("✅ Paciente de bajo riesgo")


# Ejemplo 3: Clasificación de IMC
imc = 28.5

if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"IMC: {imc:.1f} - Categoría: {categoria}")
```

---

## Bucles (for/while)

Los **bucles** repiten código múltiples veces, útil para procesar múltiples pacientes.

### Bucle FOR (número definido de repeticiones)

```python
# Iterar sobre una lista
fev1_pacientes = [2.5, 3.1, 2.8, 2.2, 3.4]

for fev1 in fev1_pacientes:
    print(f"FEV1: {fev1} L")


# Con índice (enumerar)
for i, fev1 in enumerate(fev1_pacientes):
    print(f"Paciente {i+1}: FEV1 = {fev1} L")


# Ejemplo: Clasificar múltiples valores
for fev1 in fev1_pacientes:
    if fev1 < 2.0:
        print(f"FEV1 {fev1}: Bajo ⚠️")
    elif fev1 < 3.0:
        print(f"FEV1 {fev1}: Normal ✅")
    else:
        print(f"FEV1 {fev1}: Alto 📈")


# Rango de números
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Iteración {i}")

for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(f"Paciente {i}")
```

### Bucle WHILE (repetir mientras se cumpla condición)

```python
# Ejemplo: Proceso iterativo
fev1_actual = 1.8
mejoria_por_sesion = 0.15
sesiones = 0

while fev1_actual < 2.5:
    sesiones += 1
    fev1_actual += mejoria_por_sesion
    print(f"Sesión {sesiones}: FEV1 = {fev1_actual:.2f}")

print(f"Total de sesiones necesarias: {sesiones}")
```

### List Comprehension (creación compacta de listas)

```python
# Forma tradicional
cuadrados = []
for i in range(5):
    cuadrados.append(i ** 2)

# List comprehension (más compacto)
cuadrados = [i ** 2 for i in range(5)]  # [0, 1, 4, 9, 16]


# Ejemplo médico: Filtrar valores
fev1_todos = [2.5, 1.8, 3.1, 1.5, 2.8, 2.2]

# Obtener solo valores bajos (< 2.0)
fev1_bajos = [fev1 for fev1 in fev1_todos if fev1 < 2.0]
# Resultado: [1.8, 1.5]

# Clasificar todos los valores
clasificaciones = ["Bajo" if fev1 < 2.0 else "Normal" for fev1 in fev1_todos]
```

---

## Funciones

Las **funciones** son bloques de código reutilizables, como "recetas" que puedes usar varias veces.

### Definir y Usar Funciones

```python
# Definir una función
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal.

    Parámetros:
        peso: Peso en kg
        altura: Altura en metros

    Retorna:
        IMC calculado
    """
    imc = peso / (altura ** 2)
    return imc


# Usar la función
imc_paciente1 = calcular_imc(70, 1.75)
imc_paciente2 = calcular_imc(85, 1.80)

print(f"IMC Paciente 1: {imc_paciente1:.2f}")
print(f"IMC Paciente 2: {imc_paciente2:.2f}")
```

### Funciones con Múltiples Retornos

```python
def analizar_fev1(fev1):
    """
    Analiza un valor de FEV1 y retorna clasificación y recomendación.
    """
    if fev1 < 2.0:
        clasificacion = "Bajo"
        recomendacion = "Considerar tratamiento intensivo"
    elif fev1 < 3.0:
        clasificacion = "Normal"
        recomendacion = "Mantener seguimiento regular"
    else:
        clasificacion = "Alto"
        recomendacion = "Función pulmonar excelente"

    return clasificacion, recomendacion


# Usar la función
clasif, recom = analizar_fev1(2.3)
print(f"Clasificación: {clasif}")
print(f"Recomendación: {recom}")
```

### Funciones con Argumentos Por Defecto

```python
def calcular_dosis(peso, dosis_por_kg=5):
    """
    Calcula dosis de medicamento basada en peso.

    Parámetros:
        peso: Peso del paciente en kg
        dosis_por_kg: Dosis en mg/kg (por defecto 5)
    """
    dosis_total = peso * dosis_por_kg
    return dosis_total


# Usar dosis por defecto
dosis1 = calcular_dosis(70)  # Usa 5 mg/kg por defecto

# Especificar dosis diferente
dosis2 = calcular_dosis(70, dosis_por_kg=10)

print(f"Dosis 1: {dosis1} mg")
print(f"Dosis 2: {dosis2} mg")
```

---

## Importar Librerías

Las **librerías** son colecciones de funciones predefinidas que extienden las capacidades de Python.

### Importar Librerías Completas

```python
# Importar librería completa
import math

raiz_cuadrada = math.sqrt(16)  # 4.0
print(f"Raíz cuadrada de 16: {raiz_cuadrada}")
```

### Importar Funciones Específicas

```python
# Importar solo funciones específicas
from math import sqrt, pi

raiz = sqrt(25)  # 5.0 (sin necesidad de "math.")
area_circulo = pi * (5 ** 2)
```

### Importar con Alias (nombres cortos)

```python
# Importar con alias (muy común en ciencia de datos)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ahora puedes usar "pd" en lugar de "pandas"
datos = pd.read_excel("datos.xlsx")
```

### Librerías Esenciales para Análisis Médico

```python
# Para análisis de datos
import pandas as pd           # Manipulación de datos tabulares
import numpy as np            # Operaciones numéricas

# Para estadística
from scipy import stats       # Pruebas estadísticas
import statsmodels.api as sm  # Modelos estadísticos avanzados

# Para visualización
import matplotlib.pyplot as plt  # Gráficos básicos
import seaborn as sns            # Gráficos estadísticos elegantes
```

---

## Ejemplos Médicos

### Ejemplo Completo 1: Análisis de Grupo de Pacientes

```python
# Datos de pacientes
pacientes = [
    {"nombre": "Juan", "edad": 45, "fev1": 2.5, "fumador": True},
    {"nombre": "María", "edad": 38, "fev1": 3.1, "fumador": False},
    {"nombre": "Pedro", "edad": 52, "fev1": 1.8, "fumador": True},
    {"nombre": "Ana", "edad": 41, "fev1": 2.9, "fumador": False},
]

# Función para clasificar paciente
def clasificar_riesgo(paciente):
    if paciente["fev1"] < 2.0 and paciente["fumador"]:
        return "Alto riesgo"
    elif paciente["fev1"] < 2.0 or paciente["fumador"]:
        return "Riesgo moderado"
    else:
        return "Bajo riesgo"

# Analizar cada paciente
print("ANÁLISIS DE PACIENTES")
print("=" * 50)

for paciente in pacientes:
    riesgo = clasificar_riesgo(paciente)
    print(f"Paciente: {paciente['nombre']}")
    print(f"  Edad: {paciente['edad']} años")
    print(f"  FEV1: {paciente['fev1']} L")
    print(f"  Fumador: {'Sí' if paciente['fumador'] else 'No'}")
    print(f"  Clasificación: {riesgo}")
    print()

# Calcular estadísticas del grupo
fev1_valores = [p["fev1"] for p in pacientes]
fev1_promedio = sum(fev1_valores) / len(fev1_valores)

print(f"FEV1 promedio del grupo: {fev1_promedio:.2f} L")
```

### Ejemplo Completo 2: Calculadora de Medicación

```python
def calcular_dosis_pediatrica(peso, edad, dosis_adulto=500):
    """
    Calcula dosis pediátrica usando la regla de Clark.

    Parámetros:
        peso: Peso del niño en kg
        edad: Edad del niño en años
        dosis_adulto: Dosis para adulto en mg
    """
    if edad >= 18:
        return dosis_adulto

    # Regla de Clark: Dosis = (Peso en kg / 70) x Dosis adulto
    dosis = (peso / 70) * dosis_adulto

    return round(dosis, 2)


# Usar la función
pacientes_pediatricos = [
    {"nombre": "Luis", "peso": 20, "edad": 7},
    {"nombre": "Sofía", "peso": 35, "edad": 12},
    {"nombre": "Carlos", "peso": 15, "edad": 5},
]

print("CÁLCULO DE DOSIS PEDIÁTRICAS")
print("=" * 50)

for paciente in pacientes_pediatricos:
    dosis = calcular_dosis_pediatrica(paciente["peso"], paciente["edad"])
    print(f"Paciente: {paciente['nombre']}")
    print(f"  Peso: {paciente['peso']} kg")
    print(f"  Edad: {paciente['edad']} años")
    print(f"  Dosis calculada: {dosis} mg")
    print()
```

---

## Resumen de Conceptos Clave

| Concepto | Descripción | Uso Médico |
|----------|-------------|------------|
| **Variables** | Guardar valores | Almacenar FEV1, edad, etc. |
| **Listas** | Colección de valores | Lista de valores de múltiples pacientes |
| **Diccionarios** | Pares clave-valor | Información completa de un paciente |
| **Condicionales** | Tomar decisiones | Clasificar según criterios clínicos |
| **Bucles** | Repetir operaciones | Procesar múltiples pacientes |
| **Funciones** | Código reutilizable | Cálculos que se repiten (IMC, dosis) |
| **Librerías** | Herramientas especializadas | pandas, scipy para análisis |

---

## Próximos Pasos

Ahora que conoces los fundamentos de Python, puedes avanzar a:

1. **[Pandas para Datos](pandas_guide.md)** - Manipular datos tabulares (Excel, CSV)
2. **[Estadística](statistics_guide.md)** - Realizar pruebas estadísticas
3. **[Visualización](visualization_guide.md)** - Crear gráficos profesionales

---

## Ejercicios Recomendados

1. Crea una función que calcule el IMC y lo clasifique
2. Haz una lista de 5 valores de FEV1 y calcula su promedio
3. Escribe un bucle que clasifique múltiples valores de FEV1
4. Crea un diccionario con información de un paciente y accede a sus valores

---

**¿Dudas?** Prueba el código en tu computadora. La mejor manera de aprender programación es **experimentando**.
