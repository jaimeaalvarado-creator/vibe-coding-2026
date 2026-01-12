# Guía de Pandas para Análisis de Datos Médicos 🐼

Pandas es la librería principal para trabajar con datos tabulares (como Excel o CSV) en Python. Esta guía te enseñará a leer, manipular y analizar datos médicos.

## Tabla de Contenidos

1. [¿Qué es Pandas?](#qué-es-pandas)
2. [Leer Datos](#leer-datos)
3. [Explorar Datos](#explorar-datos)
4. [Seleccionar y Filtrar](#seleccionar-y-filtrar)
5. [Operaciones con Columnas](#operaciones-con-columnas)
6. [Agrupar y Resumir](#agrupar-y-resumir)
7. [Datos Faltantes](#datos-faltantes)
8. [Guardar Resultados](#guardar-resultados)
9. [Ejemplos Médicos Completos](#ejemplos-médicos-completos)

---

## ¿Qué es Pandas?

**Pandas** es una librería de Python especializada en manipular datos tabulares (filas y columnas), como:
- Archivos Excel (.xlsx, .xls)
- Archivos CSV (.csv)
- Bases de datos
- Cualquier dato organizado en tablas

**Conceptos clave:**
- **DataFrame**: Una tabla de datos (como una hoja de Excel)
- **Serie**: Una columna de un DataFrame
- **Index**: Los números de fila (como números de fila en Excel)

```python
# Importar pandas (siempre se usa el alias 'pd')
import pandas as pd
```

---

## Leer Datos

### Leer desde Excel

```python
import pandas as pd

# Leer un archivo Excel
datos = pd.read_excel('espirometrias.xlsx')

# Leer una hoja específica
datos = pd.read_excel('espirometrias.xlsx', sheet_name='Pacientes_2024')

# Leer especificando que la primera fila son encabezados
datos = pd.read_excel('espirometrias.xlsx', header=0)
```

### Leer desde CSV

```python
# Leer CSV (separado por comas)
datos = pd.read_csv('espirometrias.csv')

# CSV con separador punto y coma
datos = pd.read_csv('espirometrias.csv', sep=';')

# CSV con codificación específica (para caracteres especiales)
datos = pd.read_csv('espirometrias.csv', encoding='utf-8')
```

### Crear DataFrame Manualmente

```python
# Desde un diccionario
datos = pd.DataFrame({
    'Paciente': ['Juan', 'María', 'Pedro', 'Ana'],
    'Edad': [45, 38, 52, 41],
    'FEV1': [2.5, 3.1, 1.8, 2.9],
    'Fumador': ['Sí', 'No', 'Sí', 'No']
})

print(datos)
```

---

## Explorar Datos

### Ver los Datos

```python
# Ver las primeras filas (por defecto 5)
datos.head()

# Ver las primeras 10 filas
datos.head(10)

# Ver las últimas filas
datos.tail()

# Ver una muestra aleatoria
datos.sample(5)  # 5 filas aleatorias
```

### Información General

```python
# Dimensiones (filas, columnas)
print(datos.shape)  # Ejemplo: (120, 5)

# Nombres de columnas
print(datos.columns)

# Tipos de datos de cada columna
print(datos.dtypes)

# Información completa
datos.info()

# Resumen estadístico de columnas numéricas
datos.describe()
```

### Ejemplo Práctico

```python
import pandas as pd

# Leer datos
datos = pd.read_excel('espirometrias.xlsx')

# Exploración inicial
print("=" * 50)
print("EXPLORACIÓN DE DATOS")
print("=" * 50)
print(f"Total de pacientes: {len(datos)}")
print(f"Columnas: {', '.join(datos.columns)}")
print("\nPrimeros pacientes:")
print(datos.head())
print("\nResumen estadístico:")
print(datos.describe())
```

---

## Seleccionar y Filtrar

### Seleccionar Columnas

```python
# Una columna (devuelve Serie)
fev1 = datos['FEV1']

# Múltiples columnas (devuelve DataFrame)
seleccion = datos[['Paciente', 'FEV1', 'Edad']]

# Forma alternativa para una columna
fev1 = datos.FEV1  # Solo si el nombre no tiene espacios
```

### Filtrar Filas

```python
# Filtro simple: FEV1 menor a 2.0
fev1_bajo = datos[datos['FEV1'] < 2.0]

# Filtro con condición específica
fumadores = datos[datos['Fumador'] == 'Sí']

# Múltiples condiciones (AND)
alto_riesgo = datos[(datos['FEV1'] < 2.0) & (datos['Fumador'] == 'Sí')]

# Múltiples condiciones (OR)
revision = datos[(datos['Edad'] > 60) | (datos['FEV1'] < 2.0)]

# Excluir (NOT)
no_fumadores = datos[datos['Fumador'] != 'Sí']

# Filtrar por valores en una lista
nombres = ['Juan', 'María']
pacientes_especificos = datos[datos['Paciente'].isin(nombres)]

# Filtrar por rango
edad_media = datos[(datos['Edad'] >= 40) & (datos['Edad'] <= 60)]
```

### Seleccionar Filas y Columnas Simultáneamente

```python
# loc: por etiquetas
# iloc: por posiciones numéricas

# Seleccionar filas 0-4, columnas específicas
seleccion = datos.loc[0:4, ['Paciente', 'FEV1']]

# Seleccionar por posición numérica
# Filas 0-4, columnas 0 y 2
seleccion = datos.iloc[0:5, [0, 2]]

# Primera fila completa
primera_fila = datos.iloc[0]

# Último paciente
ultimo_paciente = datos.iloc[-1]
```

### Ejemplos Médicos

```python
# Pacientes con FEV1 anormal
fev1_anormal = datos[datos['FEV1'] < 2.0]
print(f"Pacientes con FEV1 < 2.0: {len(fev1_anormal)}")

# Fumadores mayores de 50 años
fumadores_mayores = datos[(datos['Fumador'] == 'Sí') & (datos['Edad'] > 50)]

# Pacientes que requieren seguimiento
seguimiento = datos[
    (datos['FEV1'] < 2.5) |
    (datos['Fumador'] == 'Sí') |
    (datos['Edad'] > 65)
]

# Guardar subset filtrado
fev1_anormal.to_excel('pacientes_alto_riesgo.xlsx', index=False)
```

---

## Operaciones con Columnas

### Crear Nuevas Columnas

```python
# Columna calculada
datos['IMC'] = datos['Peso'] / (datos['Altura'] ** 2)

# Columna condicional simple
datos['FEV1_Categoría'] = datos['FEV1'].apply(
    lambda x: 'Bajo' if x < 2.0 else 'Normal'
)

# Columna con múltiples condiciones
def clasificar_fev1(valor):
    if valor < 2.0:
        return 'Bajo'
    elif valor < 3.0:
        return 'Normal'
    else:
        return 'Alto'

datos['FEV1_Clasificación'] = datos['FEV1'].apply(clasificar_fev1)

# Usando numpy para condiciones múltiples
import numpy as np

datos['Riesgo'] = np.where(
    (datos['FEV1'] < 2.0) & (datos['Fumador'] == 'Sí'),
    'Alto',
    np.where(
        (datos['FEV1'] < 2.0) | (datos['Fumador'] == 'Sí'),
        'Moderado',
        'Bajo'
    )
)
```

### Modificar Columnas

```python
# Renombrar columna
datos = datos.rename(columns={'FEV1': 'FEV1_Litros'})

# Redondear valores
datos['FEV1'] = datos['FEV1'].round(2)

# Convertir tipo de dato
datos['Edad'] = datos['Edad'].astype(int)

# Reemplazar valores
datos['Fumador'] = datos['Fumador'].replace({'Sí': True, 'No': False})

# Eliminar columnas
datos = datos.drop(columns=['Columna_Innecesaria'])

# Reordenar columnas
columnas_orden = ['Paciente', 'Edad', 'FEV1', 'Fumador']
datos = datos[columnas_orden]
```

### Operaciones Matemáticas en Columnas

```python
# Operaciones básicas
datos['FEV1_Doble'] = datos['FEV1'] * 2
datos['FEV1_Porcentaje'] = datos['FEV1'] / datos['FEV1_Predicho'] * 100

# Estadísticas de columna
media_fev1 = datos['FEV1'].mean()
mediana_fev1 = datos['FEV1'].median()
std_fev1 = datos['FEV1'].std()
maximo_fev1 = datos['FEV1'].max()
minimo_fev1 = datos['FEV1'].min()

# Estandarizar (z-score)
datos['FEV1_Z'] = (datos['FEV1'] - datos['FEV1'].mean()) / datos['FEV1'].std()
```

---

## Agrupar y Resumir

### Agrupar por Categorías

```python
# Agrupar por una variable
por_fumador = datos.groupby('Fumador')

# Media por grupo
medias_por_grupo = datos.groupby('Fumador')['FEV1'].mean()
print(medias_por_grupo)
# Salida:
# Fumador
# No     2.95
# Sí     2.15

# Múltiples estadísticas
estadisticas = datos.groupby('Fumador')['FEV1'].agg(['mean', 'std', 'count'])
print(estadisticas)

# Agrupar por múltiples variables
por_fumador_edad = datos.groupby(['Fumador', 'Grupo_Edad'])['FEV1'].mean()

# Aplicar función personalizada
def rango(serie):
    return serie.max() - serie.min()

rangos = datos.groupby('Fumador')['FEV1'].apply(rango)
```

### Tablas de Contingencia

```python
# Contar frecuencias
tabla = pd.crosstab(datos['Fumador'], datos['Sexo'])
print(tabla)
# Salida:
#         Sexo    F   M
# Fumador
# No            30  25
# Sí            15  30

# Con porcentajes
tabla_pct = pd.crosstab(datos['Fumador'], datos['Sexo'], normalize='all')

# Tabla con valores de otra variable
tabla_media = pd.crosstab(
    datos['Fumador'],
    datos['Sexo'],
    values=datos['FEV1'],
    aggfunc='mean'
)
```

### Resumen Completo por Grupos

```python
# Resumen detallado
resumen = datos.groupby('Fumador').agg({
    'FEV1': ['mean', 'std', 'min', 'max', 'count'],
    'Edad': ['mean', 'median'],
    'IMC': 'mean'
})

print(resumen)
```

### Ejemplo Médico Completo

```python
# Análisis por grupo de fumadores
print("ANÁLISIS POR GRUPO DE FUMADORES")
print("=" * 60)

for nombre_grupo, datos_grupo in datos.groupby('Fumador'):
    print(f"\nGrupo: {nombre_grupo}")
    print(f"  N: {len(datos_grupo)}")
    print(f"  FEV1 medio: {datos_grupo['FEV1'].mean():.2f} L")
    print(f"  FEV1 std: {datos_grupo['FEV1'].std():.2f} L")
    print(f"  Edad media: {datos_grupo['Edad'].mean():.1f} años")

# Crear tabla resumen
resumen = datos.groupby('Fumador').agg({
    'FEV1': ['count', 'mean', 'std'],
    'Edad': 'mean'
}).round(2)

print("\nTabla Resumen:")
print(resumen)

# Guardar resumen
resumen.to_excel('resumen_por_grupo.xlsx')
```

---

## Datos Faltantes

### Detectar Datos Faltantes

```python
# Contar valores faltantes por columna
print(datos.isnull().sum())

# Verificar si hay algún valor faltante
print(datos.isnull().any())

# Ver filas con valores faltantes
filas_con_faltantes = datos[datos.isnull().any(axis=1)]

# Porcentaje de datos faltantes
porcentaje = (datos.isnull().sum() / len(datos)) * 100
print(porcentaje)
```

### Manejar Datos Faltantes

```python
# Eliminar filas con cualquier valor faltante
datos_limpios = datos.dropna()

# Eliminar filas con faltantes en columna específica
datos_limpios = datos.dropna(subset=['FEV1'])

# Rellenar con un valor específico
datos['FEV1'].fillna(0, inplace=True)

# Rellenar con la media
media_fev1 = datos['FEV1'].mean()
datos['FEV1'].fillna(media_fev1, inplace=True)

# Rellenar con la mediana (más robusto)
mediana_fev1 = datos['FEV1'].median()
datos['FEV1'].fillna(mediana_fev1, inplace=True)

# Forward fill (usar valor anterior)
datos['FEV1'].fillna(method='ffill', inplace=True)

# Rellenar por grupo
datos['FEV1'] = datos.groupby('Fumador')['FEV1'].transform(
    lambda x: x.fillna(x.mean())
)
```

---

## Guardar Resultados

### Guardar en Excel

```python
# Guardar DataFrame completo
datos.to_excel('resultados.xlsx', index=False)

# Guardar sin el índice (recomendado)
datos.to_excel('resultados.xlsx', index=False)

# Guardar en hoja específica
with pd.ExcelWriter('analisis_completo.xlsx') as writer:
    datos.to_excel(writer, sheet_name='Datos_Completos', index=False)
    resumen.to_excel(writer, sheet_name='Resumen', index=False)

# Guardar solo columnas específicas
datos[['Paciente', 'FEV1', 'Clasificación']].to_excel(
    'resultados_seleccion.xlsx',
    index=False
)
```

### Guardar en CSV

```python
# Guardar CSV
datos.to_csv('resultados.csv', index=False)

# CSV con separador punto y coma
datos.to_csv('resultados.csv', sep=';', index=False)

# CSV con codificación específica
datos.to_csv('resultados.csv', encoding='utf-8', index=False)
```

### Guardar Subsets Filtrados

```python
# Guardar diferentes grupos en archivos separados
fumadores = datos[datos['Fumador'] == 'Sí']
no_fumadores = datos[datos['Fumador'] == 'No']

fumadores.to_excel('fumadores.xlsx', index=False)
no_fumadores.to_excel('no_fumadores.xlsx', index=False)
```

---

## Ejemplos Médicos Completos

### Ejemplo 1: Análisis Completo de Espirometrías

```python
import pandas as pd
import numpy as np

# Leer datos
print("Leyendo datos...")
datos = pd.read_excel('espirometrias.xlsx')

# Exploración inicial
print("\n" + "=" * 60)
print("ANÁLISIS DE ESPIROMETRÍAS")
print("=" * 60)
print(f"Total de pacientes: {len(datos)}")
print(f"Rango de edades: {datos['Edad'].min()} - {datos['Edad'].max()} años")
print(f"FEV1 promedio: {datos['FEV1'].mean():.2f} L")

# Crear categorías
def clasificar_fev1(valor):
    if valor < 2.0:
        return 'Bajo'
    elif valor < 3.0:
        return 'Normal'
    else:
        return 'Alto'

datos['FEV1_Categoría'] = datos['FEV1'].apply(clasificar_fev1)

# Crear grupos de edad
datos['Grupo_Edad'] = pd.cut(
    datos['Edad'],
    bins=[0, 40, 60, 100],
    labels=['<40', '40-60', '>60']
)

# Análisis por fumador
print("\nAnálisis por grupo de fumadores:")
resumen_fumador = datos.groupby('Fumador').agg({
    'FEV1': ['count', 'mean', 'std'],
    'Edad': 'mean'
}).round(2)
print(resumen_fumador)

# Tabla de contingencia
print("\nDistribución FEV1 por fumador:")
tabla = pd.crosstab(datos['Fumador'], datos['FEV1_Categoría'])
print(tabla)

# Identificar pacientes de alto riesgo
alto_riesgo = datos[
    (datos['FEV1'] < 2.0) &
    (datos['Fumador'] == 'Sí') &
    (datos['Edad'] > 50)
]

print(f"\nPacientes de alto riesgo: {len(alto_riesgo)}")

# Guardar resultados
print("\nGuardando resultados...")
with pd.ExcelWriter('analisis_espirometrias.xlsx') as writer:
    datos.to_excel(writer, sheet_name='Datos_Completos', index=False)
    resumen_fumador.to_excel(writer, sheet_name='Resumen_Fumador')
    alto_riesgo.to_excel(writer, sheet_name='Alto_Riesgo', index=False)

print("✅ Análisis completado!")
```

### Ejemplo 2: Comparación Pre-Post Tratamiento

```python
import pandas as pd

# Datos de pacientes con mediciones pre y post
datos = pd.DataFrame({
    'Paciente': ['P1', 'P2', 'P3', 'P4', 'P5'],
    'FEV1_Pre': [1.8, 2.1, 1.5, 2.3, 1.9],
    'FEV1_Post': [2.2, 2.4, 1.9, 2.5, 2.3],
    'Tratamiento': ['A', 'A', 'B', 'B', 'A']
})

# Calcular cambio
datos['Cambio_Absoluto'] = datos['FEV1_Post'] - datos['FEV1_Pre']
datos['Cambio_Porcentual'] = (
    (datos['FEV1_Post'] - datos['FEV1_Pre']) / datos['FEV1_Pre'] * 100
).round(2)

# Clasificar respuesta
datos['Respuesta'] = datos['Cambio_Porcentual'].apply(
    lambda x: 'Buena' if x > 15 else 'Moderada' if x > 5 else 'Pobre'
)

print("ANÁLISIS PRE-POST TRATAMIENTO")
print("=" * 60)
print(datos)

# Análisis por tratamiento
print("\nEfectividad por tratamiento:")
resumen = datos.groupby('Tratamiento').agg({
    'Cambio_Absoluto': 'mean',
    'Cambio_Porcentual': 'mean'
}).round(2)
print(resumen)

# Contar respuestas
print("\nDistribución de respuestas:")
print(datos['Respuesta'].value_counts())

# Guardar
datos.to_excel('analisis_pre_post.xlsx', index=False)
```

### Ejemplo 3: Datos Longitudinales

```python
import pandas as pd

# Datos de seguimiento
datos = pd.DataFrame({
    'Paciente': ['P1', 'P1', 'P1', 'P2', 'P2', 'P2'],
    'Visita': [1, 2, 3, 1, 2, 3],
    'Fecha': ['2024-01-01', '2024-02-01', '2024-03-01',
              '2024-01-01', '2024-02-01', '2024-03-01'],
    'FEV1': [1.8, 2.0, 2.2, 2.3, 2.4, 2.5]
})

# Convertir fecha a datetime
datos['Fecha'] = pd.to_datetime(datos['Fecha'])

# Análisis por paciente
print("ANÁLISIS LONGITUDINAL")
print("=" * 60)

for paciente, datos_paciente in datos.groupby('Paciente'):
    print(f"\n{paciente}:")
    print(f"  FEV1 inicial: {datos_paciente['FEV1'].iloc[0]:.2f} L")
    print(f"  FEV1 final: {datos_paciente['FEV1'].iloc[-1]:.2f} L")
    mejoria = datos_paciente['FEV1'].iloc[-1] - datos_paciente['FEV1'].iloc[0]
    print(f"  Mejoría: {mejoria:.2f} L")

# Calcular tendencia general
print("\nTendencia general:")
print(datos.groupby('Visita')['FEV1'].mean())
```

---

## Operaciones Avanzadas Útiles

### Unir DataFrames

```python
# Unir por columna común (como JOIN en SQL)
datos_clinicos = pd.DataFrame({
    'Paciente': ['P1', 'P2', 'P3'],
    'FEV1': [2.5, 3.1, 1.8]
})

datos_demograficos = pd.DataFrame({
    'Paciente': ['P1', 'P2', 'P3'],
    'Edad': [45, 38, 52],
    'Sexo': ['M', 'F', 'M']
})

# Unir (merge)
datos_completos = pd.merge(datos_clinicos, datos_demograficos, on='Paciente')
```

### Ordenar Datos

```python
# Ordenar por una columna
datos_ordenados = datos.sort_values('FEV1')

# Orden descendente
datos_ordenados = datos.sort_values('FEV1', ascending=False)

# Ordenar por múltiples columnas
datos_ordenados = datos.sort_values(['Fumador', 'FEV1'])
```

### Eliminar Duplicados

```python
# Identificar duplicados
duplicados = datos.duplicated()

# Eliminar duplicados
datos_unicos = datos.drop_duplicates()

# Eliminar duplicados basados en columna específica
datos_unicos = datos.drop_duplicates(subset=['Paciente'])
```

---

## Resumen de Funciones Clave

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `read_excel()` | Leer Excel | `pd.read_excel('datos.xlsx')` |
| `head()` | Ver primeras filas | `datos.head()` |
| `describe()` | Resumen estadístico | `datos.describe()` |
| `[]` | Filtrar | `datos[datos['FEV1'] < 2.0]` |
| `groupby()` | Agrupar | `datos.groupby('Fumador')` |
| `apply()` | Aplicar función | `datos['FEV1'].apply(func)` |
| `fillna()` | Rellenar faltantes | `datos.fillna(0)` |
| `to_excel()` | Guardar Excel | `datos.to_excel('resultado.xlsx')` |

---

## Próximos Pasos

Ahora que dominas Pandas, puedes:

1. **[Estadística](statistics_guide.md)** - Realizar pruebas estadísticas con tus datos
2. **[Visualización](visualization_guide.md)** - Crear gráficos de tus análisis

---

**Consejo:** Pandas tiene muchísimas funciones. No necesitas memorizarlas todas. Aprende las básicas y consulta la documentación cuando necesites algo específico.
