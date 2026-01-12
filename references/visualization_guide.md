# Guía de Visualización de Datos Médicos con Python 📈

Esta guía te enseñará a crear gráficos profesionales para presentar tus datos médicos usando matplotlib y seaborn.

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Configuración Inicial](#configuración-inicial)
3. [Histogramas](#histogramas)
4. [Boxplots (Diagramas de Caja)](#boxplots-diagramas-de-caja)
5. [Gráficos de Barras](#gráficos-de-barras)
6. [Gráficos de Dispersión](#gráficos-de-dispersión)
7. [Gráficos de Línea](#gráficos-de-línea)
8. [Gráficos Múltiples](#gráficos-múltiples)
9. [Personalización](#personalización)
10. [Ejemplos Médicos Completos](#ejemplos-médicos-completos)

---

## Introducción

**Matplotlib** es la librería base para visualización en Python.
**Seaborn** es una extensión que facilita crear gráficos estadísticos elegantes.

```python
# Importar librerías
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
```

---

## Configuración Inicial

### Configuración Básica

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Estilo visual
sns.set_style("whitegrid")  # Opciones: white, dark, whitegrid, darkgrid, ticks

# Paleta de colores
sns.set_palette("Set2")  # Opciones: Set1, Set2, Set3, husl, etc.

# Tamaño de figuras por defecto
plt.rcParams['figure.figsize'] = (10, 6)

# Fuente
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'sans-serif'
```

### Guardar Gráficos

```python
# Crear gráfico
plt.plot([1, 2, 3], [1, 4, 9])

# Guardar en alta resolución
plt.savefig('mi_grafico.png', dpi=300, bbox_inches='tight')

# Formatos disponibles: .png, .pdf, .svg, .jpg
```

---

## Histogramas

Los **histogramas** muestran la distribución de una variable continua.

### Histograma Básico

```python
import matplotlib.pyplot as plt
import numpy as np

# Datos: FEV1 de 100 pacientes
np.random.seed(42)
fev1 = np.random.normal(2.5, 0.5, 100)

# Crear histograma
plt.hist(fev1, bins=15, color='skyblue', edgecolor='black')
plt.xlabel('FEV1 (L)')
plt.ylabel('Frecuencia')
plt.title('Distribución de FEV1')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

### Histograma con Curva de Densidad

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Histograma + curva de densidad
plt.figure(figsize=(10, 6))

# Histograma
plt.hist(fev1, bins=15, density=True, alpha=0.7,
         color='skyblue', edgecolor='black', label='Frecuencia')

# Curva de densidad (KDE)
from scipy import stats
kde = stats.gaussian_kde(fev1)
x_range = np.linspace(fev1.min(), fev1.max(), 100)
plt.plot(x_range, kde(x_range), 'r-', linewidth=2, label='Densidad')

# Líneas de media y mediana
plt.axvline(fev1.mean(), color='green', linestyle='--',
            linewidth=2, label=f'Media: {fev1.mean():.2f}')
plt.axvline(np.median(fev1), color='orange', linestyle='--',
            linewidth=2, label=f'Mediana: {np.median(fev1):.2f}')

plt.xlabel('FEV1 (L)', fontsize=12, fontweight='bold')
plt.ylabel('Densidad', fontsize=12, fontweight='bold')
plt.title('Distribución de FEV1 con Estadísticas', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()
```

### Histogramas Múltiples (Comparar Grupos)

```python
# Datos de dos grupos
fumadores = np.random.normal(2.0, 0.4, 50)
no_fumadores = np.random.normal(2.8, 0.4, 50)

# Histogramas superpuestos
plt.figure(figsize=(10, 6))
plt.hist(fumadores, bins=15, alpha=0.6, label='Fumadores', color='red', edgecolor='black')
plt.hist(no_fumadores, bins=15, alpha=0.6, label='No fumadores', color='green', edgecolor='black')

plt.xlabel('FEV1 (L)', fontsize=12, fontweight='bold')
plt.ylabel('Frecuencia', fontsize=12, fontweight='bold')
plt.title('Distribución de FEV1: Fumadores vs No Fumadores', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()
```

---

## Boxplots (Diagramas de Caja)

Los **boxplots** muestran la distribución y detectan valores atípicos.

### Boxplot Básico

```python
import matplotlib.pyplot as plt

# Datos
fev1 = np.random.normal(2.5, 0.5, 100)

# Boxplot
plt.figure(figsize=(8, 6))
bp = plt.boxplot([fev1], labels=['FEV1'], patch_artist=True,
                 notch=True, showmeans=True)

# Colorear
bp['boxes'][0].set_facecolor('lightblue')

plt.ylabel('FEV1 (L)', fontsize=12, fontweight='bold')
plt.title('Boxplot de FEV1', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

**Componentes del Boxplot:**
- **Caja**: Rango intercuartil (Q1 a Q3)
- **Línea central**: Mediana
- **Diamante**: Media (si showmeans=True)
- **Bigotes**: 1.5 × IQR
- **Puntos**: Valores atípicos

### Boxplot por Grupos

```python
import pandas as pd
import seaborn as sns

# Crear datos
datos = pd.DataFrame({
    'FEV1': np.concatenate([
        np.random.normal(2.0, 0.4, 30),
        np.random.normal(2.8, 0.4, 30)
    ]),
    'Fumador': ['Sí']*30 + ['No']*30
})

# Boxplot con seaborn (más fácil para grupos)
plt.figure(figsize=(8, 6))
sns.boxplot(data=datos, x='Fumador', y='FEV1', palette='Set2')
plt.ylabel('FEV1 (L)', fontsize=12, fontweight='bold')
plt.xlabel('Fumador', fontsize=12, fontweight='bold')
plt.title('FEV1 por Grupo de Fumadores', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

### Boxplot con Puntos Individuales

```python
# Boxplot + puntos individuales
plt.figure(figsize=(10, 6))

# Boxplot
sns.boxplot(data=datos, x='Fumador', y='FEV1', palette='Set2', width=0.5)

# Puntos individuales (stripplot)
sns.stripplot(data=datos, x='Fumador', y='FEV1',
              color='black', alpha=0.3, size=3)

plt.ylabel('FEV1 (L)', fontsize=12, fontweight='bold')
plt.xlabel('Fumador', fontsize=12, fontweight='bold')
plt.title('FEV1 por Grupo (con datos individuales)', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

---

## Gráficos de Barras

### Gráfico de Barras con Medias

```python
import pandas as pd
import matplotlib.pyplot as plt

# Datos
datos = pd.DataFrame({
    'Grupo': ['A', 'B', 'C'],
    'FEV1_Media': [2.3, 2.7, 2.5],
    'FEV1_Error': [0.2, 0.15, 0.18]
})

# Gráfico de barras
plt.figure(figsize=(8, 6))
barras = plt.bar(datos['Grupo'], datos['FEV1_Media'],
                yerr=datos['FEV1_Error'], capsize=10,
                color=['#3498db', '#e74c3c', '#2ecc71'],
                edgecolor='black', linewidth=1.5)

plt.ylabel('FEV1 (L)', fontsize=12, fontweight='bold')
plt.xlabel('Grupo de Tratamiento', fontsize=12, fontweight='bold')
plt.title('FEV1 Medio por Grupo (Media ± ES)', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

# Añadir valores sobre las barras
for i, barra in enumerate(barras):
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura,
            f'{datos["FEV1_Media"].iloc[i]:.2f}',
            ha='center', va='bottom', fontweight='bold')

plt.show()
```

### Gráfico de Barras Agrupadas

```python
import numpy as np
import matplotlib.pyplot as plt

# Datos
grupos = ['Grupo A', 'Grupo B', 'Grupo C']
pre = [2.1, 2.3, 2.2]
post = [2.5, 2.8, 2.6]

x = np.arange(len(grupos))
ancho = 0.35

# Crear barras
fig, ax = plt.subplots(figsize=(10, 6))
barras1 = ax.bar(x - ancho/2, pre, ancho, label='Pre', color='lightcoral', edgecolor='black')
barras2 = ax.bar(x + ancho/2, post, ancho, label='Post', color='lightgreen', edgecolor='black')

ax.set_ylabel('FEV1 (L)', fontsize=12, fontweight='bold')
ax.set_xlabel('Grupo', fontsize=12, fontweight='bold')
ax.set_title('Comparación Pre-Post por Grupo', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(grupos)
ax.legend()
ax.grid(axis='y', alpha=0.3)

plt.show()
```

---

## Gráficos de Dispersión

Los **scatter plots** muestran la relación entre dos variables continuas.

### Scatter Plot Básico

```python
import matplotlib.pyplot as plt
import numpy as np

# Datos: Edad vs FEV1
edad = np.random.randint(20, 80, 100)
fev1 = 4.0 - 0.03 * edad + np.random.normal(0, 0.3, 100)

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(edad, fev1, alpha=0.6, s=50, color='steelblue', edgecolor='black')

plt.xlabel('Edad (años)', fontsize=12, fontweight='bold')
plt.ylabel('FEV1 (L)', fontsize=12, fontweight='bold')
plt.title('Relación entre Edad y FEV1', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.show()
```

### Scatter Plot con Línea de Regresión

```python
from scipy import stats

# Calcular regresión lineal
slope, intercept, r_value, p_value, std_err = stats.linregress(edad, fev1)
linea = slope * edad + intercept

# Gráfico
plt.figure(figsize=(10, 6))
plt.scatter(edad, fev1, alpha=0.6, s=50, color='steelblue',
            edgecolor='black', label='Datos')
plt.plot(edad, linea, 'r-', linewidth=2,
         label=f'y = {intercept:.2f} + {slope:.4f}x\nR² = {r_value**2:.3f}')

plt.xlabel('Edad (años)', fontsize=12, fontweight='bold')
plt.ylabel('FEV1 (L)', fontsize=12, fontweight='bold')
plt.title('Relación entre Edad y FEV1 con Regresión', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### Scatter Plot por Grupos

```python
import pandas as pd
import seaborn as sns

# Datos con grupos
datos = pd.DataFrame({
    'Edad': edad,
    'FEV1': fev1,
    'Fumador': np.random.choice(['Sí', 'No'], 100)
})

# Scatter plot con seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(data=datos, x='Edad', y='FEV1', hue='Fumador',
                style='Fumador', s=100, alpha=0.7)

plt.xlabel('Edad (años)', fontsize=12, fontweight='bold')
plt.ylabel('FEV1 (L)', fontsize=12, fontweight='bold')
plt.title('Edad vs FEV1 por Grupo de Fumadores', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(title='Fumador', fontsize=10)
plt.show()
```

---

## Gráficos de Línea

Los **line plots** son ideales para datos longitudinales o series de tiempo.

### Gráfico de Línea Básico

```python
import matplotlib.pyplot as plt

# Datos: Evolución de FEV1 en el tiempo
visitas = [0, 1, 2, 3, 4, 5, 6]  # meses
fev1_promedio = [2.0, 2.1, 2.3, 2.4, 2.5, 2.6, 2.6]

# Gráfico de línea
plt.figure(figsize=(10, 6))
plt.plot(visitas, fev1_promedio, marker='o', linewidth=2,
         markersize=8, color='steelblue')

plt.xlabel('Meses de Tratamiento', fontsize=12, fontweight='bold')
plt.ylabel('FEV1 Promedio (L)', fontsize=12, fontweight='bold')
plt.title('Evolución de FEV1 Durante Tratamiento', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.show()
```

### Múltiples Líneas (Comparar Grupos)

```python
# Datos de diferentes grupos
visitas = [0, 1, 2, 3, 4, 5, 6]
grupo_a = [2.0, 2.2, 2.4, 2.5, 2.7, 2.8, 2.9]
grupo_b = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.5]
grupo_c = [2.0, 2.0, 2.1, 2.1, 2.2, 2.2, 2.3]

# Gráfico
plt.figure(figsize=(12, 6))
plt.plot(visitas, grupo_a, marker='o', linewidth=2, label='Grupo A', color='#2ecc71')
plt.plot(visitas, grupo_b, marker='s', linewidth=2, label='Grupo B', color='#3498db')
plt.plot(visitas, grupo_c, marker='^', linewidth=2, label='Grupo C', color='#e74c3c')

plt.xlabel('Meses de Tratamiento', fontsize=12, fontweight='bold')
plt.ylabel('FEV1 Promedio (L)', fontsize=12, fontweight='bold')
plt.title('Evolución de FEV1 por Grupo de Tratamiento', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.show()
```

### Gráfico con Área de Error

```python
# Datos con errores estándar
error = [0.1, 0.09, 0.08, 0.08, 0.07, 0.07, 0.06]

plt.figure(figsize=(10, 6))
plt.plot(visitas, fev1_promedio, marker='o', linewidth=2,
         color='steelblue', label='Media')
plt.fill_between(visitas,
                 np.array(fev1_promedio) - np.array(error),
                 np.array(fev1_promedio) + np.array(error),
                 alpha=0.3, color='steelblue', label='± ES')

plt.xlabel('Meses de Tratamiento', fontsize=12, fontweight='bold')
plt.ylabel('FEV1 (L)', fontsize=12, fontweight='bold')
plt.title('Evolución de FEV1 (Media ± Error Estándar)', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

## Gráficos Múltiples

### Subplots (Varios Gráficos en Uno)

```python
import matplotlib.pyplot as plt
import numpy as np

# Datos
datos = np.random.normal(2.5, 0.5, 100)

# Crear figura con 4 subplots (2x2)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Análisis Completo de FEV1', fontsize=16, fontweight='bold')

# Subplot 1: Histograma
axes[0, 0].hist(datos, bins=15, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Histograma')
axes[0, 0].set_xlabel('FEV1 (L)')
axes[0, 0].set_ylabel('Frecuencia')
axes[0, 0].grid(axis='y', alpha=0.3)

# Subplot 2: Boxplot
axes[0, 1].boxplot([datos], labels=['FEV1'])
axes[0, 1].set_title('Boxplot')
axes[0, 1].set_ylabel('FEV1 (L)')
axes[0, 1].grid(axis='y', alpha=0.3)

# Subplot 3: Q-Q Plot (normalidad)
from scipy import stats
stats.probplot(datos, dist="norm", plot=axes[1, 0])
axes[1, 0].set_title('Q-Q Plot')
axes[1, 0].grid(True, alpha=0.3)

# Subplot 4: Serie de tiempo simulada
axes[1, 1].plot(datos[:30], marker='o')
axes[1, 1].set_title('Primeras 30 Mediciones')
axes[1, 1].set_xlabel('Paciente')
axes[1, 1].set_ylabel('FEV1 (L)')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## Personalización

### Colores y Estilos

```python
# Colores por nombre
plt.plot(x, y, color='red')
plt.plot(x, y, color='steelblue')

# Colores hexadecimales
plt.plot(x, y, color='#3498db')

# Estilos de línea
plt.plot(x, y, linestyle='-')   # Sólida
plt.plot(x, y, linestyle='--')  # Discontinua
plt.plot(x, y, linestyle='-.')  # Punto-raya
plt.plot(x, y, linestyle=':')   # Punteada

# Marcadores
plt.plot(x, y, marker='o')  # Círculo
plt.plot(x, y, marker='s')  # Cuadrado
plt.plot(x, y, marker='^')  # Triángulo
plt.plot(x, y, marker='*')  # Estrella
```

### Anotaciones

```python
plt.figure(figsize=(10, 6))
plt.scatter(edad, fev1)

# Añadir anotación
plt.annotate('Valor atípico',
            xy=(45, 3.5), xytext=(50, 3.8),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=12, color='red', fontweight='bold')

plt.xlabel('Edad')
plt.ylabel('FEV1')
plt.show()
```

### Texto en el Gráfico

```python
plt.figure(figsize=(10, 6))
plt.scatter(edad, fev1)

# Añadir texto
plt.text(30, 3.5, 'Media: 2.5 L', fontsize=12,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.show()
```

---

## Ejemplos Médicos Completos

### Ejemplo 1: Panel de Análisis Completo

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# Generar datos de ejemplo
np.random.seed(42)
datos = pd.DataFrame({
    'FEV1': np.concatenate([
        np.random.normal(2.0, 0.4, 50),
        np.random.normal(2.8, 0.4, 50)
    ]),
    'Fumador': ['Sí']*50 + ['No']*50,
    'Edad': np.random.randint(20, 80, 100)
})

# Crear figura con múltiples subplots
fig = plt.figure(figsize=(14, 10))
fig.suptitle('Análisis Completo: FEV1 y Factores de Riesgo',
             fontsize=16, fontweight='bold')

# 1. Histograma con KDE
ax1 = plt.subplot(2, 3, 1)
datos['FEV1'].hist(bins=20, alpha=0.7, color='skyblue', edgecolor='black', ax=ax1)
ax1.set_xlabel('FEV1 (L)', fontweight='bold')
ax1.set_ylabel('Frecuencia', fontweight='bold')
ax1.set_title('Distribución de FEV1')
ax1.grid(axis='y', alpha=0.3)
ax1.axvline(datos['FEV1'].mean(), color='red', linestyle='--',
            linewidth=2, label=f'Media: {datos["FEV1"].mean():.2f}')
ax1.legend()

# 2. Boxplot por grupo
ax2 = plt.subplot(2, 3, 2)
sns.boxplot(data=datos, x='Fumador', y='FEV1', palette='Set2', ax=ax2)
sns.stripplot(data=datos, x='Fumador', y='FEV1',
              color='black', alpha=0.3, size=3, ax=ax2)
ax2.set_ylabel('FEV1 (L)', fontweight='bold')
ax2.set_xlabel('Fumador', fontweight='bold')
ax2.set_title('FEV1 por Grupo')
ax2.grid(axis='y', alpha=0.3)

# 3. Scatter plot Edad vs FEV1
ax3 = plt.subplot(2, 3, 3)
sns.scatterplot(data=datos, x='Edad', y='FEV1', hue='Fumador',
                style='Fumador', s=50, alpha=0.7, ax=ax3)
# Regresión
slope, intercept, r, p, se = stats.linregress(datos['Edad'], datos['FEV1'])
ax3.plot(datos['Edad'], intercept + slope*datos['Edad'], 'r--',
         linewidth=2, label=f'R²={r**2:.3f}')
ax3.set_xlabel('Edad (años)', fontweight='bold')
ax3.set_ylabel('FEV1 (L)', fontweight='bold')
ax3.set_title('Edad vs FEV1')
ax3.grid(True, alpha=0.3)
ax3.legend(fontsize=8)

# 4. Barras con medias por grupo
ax4 = plt.subplot(2, 3, 4)
medias = datos.groupby('Fumador')['FEV1'].agg(['mean', 'sem'])
barras = ax4.bar(range(len(medias)), medias['mean'],
                yerr=medias['sem'], capsize=10,
                color=['#e74c3c', '#2ecc71'], edgecolor='black', linewidth=1.5)
ax4.set_xticks(range(len(medias)))
ax4.set_xticklabels(medias.index)
ax4.set_ylabel('FEV1 (L)', fontweight='bold')
ax4.set_xlabel('Fumador', fontweight='bold')
ax4.set_title('FEV1 Medio ± ES')
ax4.grid(axis='y', alpha=0.3)

# Añadir n y valores
for i, (idx, row) in enumerate(medias.iterrows()):
    n = len(datos[datos['Fumador'] == idx])
    ax4.text(i, row['mean'], f'{row["mean"]:.2f}\n(n={n})',
            ha='center', va='bottom', fontweight='bold', fontsize=9)

# 5. Gráfico de pastel
ax5 = plt.subplot(2, 3, 5)
conteos = datos['Fumador'].value_counts()
wedges, texts, autotexts = ax5.pie(conteos, labels=conteos.index, autopct='%1.1f%%',
                                    startangle=90, colors=['#e74c3c', '#2ecc71'])
for text in texts:
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
ax5.set_title('Distribución de Fumadores')

# 6. Estadísticas textuales
ax6 = plt.subplot(2, 3, 6)
ax6.axis('off')

# Calcular estadísticas
t_stat, p_valor = stats.ttest_ind(
    datos[datos['Fumador']=='Sí']['FEV1'],
    datos[datos['Fumador']=='No']['FEV1']
)

texto_estadisticas = f"""
ESTADÍSTICAS DESCRIPTIVAS

Total de pacientes: {len(datos)}

Fumadores (n={len(datos[datos['Fumador']=='Sí'])}):
  • Media: {datos[datos['Fumador']=='Sí']['FEV1'].mean():.2f} L
  • Desv. Std: {datos[datos['Fumador']=='Sí']['FEV1'].std():.2f} L

No fumadores (n={len(datos[datos['Fumador']=='No'])}):
  • Media: {datos[datos['Fumador']=='No']['FEV1'].mean():.2f} L
  • Desv. Std: {datos[datos['Fumador']=='No']['FEV1'].std():.2f} L

TEST ESTADÍSTICO
t-test: p = {p_valor:.4f}
{'✅ Diferencia significativa' if p_valor < 0.05 else '❌ No significativa'}

CORRELACIÓN
Edad vs FEV1: r = {r:.3f}, p = {p:.4f}
"""

ax6.text(0.1, 0.9, texto_estadisticas, fontsize=10,
         verticalalignment='top', family='monospace',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.savefig('analisis_completo_fev1.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Gráfico guardado como 'analisis_completo_fev1.png'")
```

### Ejemplo 2: Visualización de Evolución Pre-Post

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Datos de pacientes pre-post
np.random.seed(42)
n_pacientes = 15
datos = pd.DataFrame({
    'Paciente': [f'P{i+1}' for i in range(n_pacientes)],
    'FEV1_Pre': np.random.normal(2.0, 0.3, n_pacientes),
})
datos['FEV1_Post'] = datos['FEV1_Pre'] + np.random.normal(0.4, 0.15, n_pacientes)

# Crear figura
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Análisis Pre-Post Tratamiento', fontsize=16, fontweight='bold')

# Gráfico 1: Líneas individuales
for i, row in datos.iterrows():
    color = 'green' if row['FEV1_Post'] > row['FEV1_Pre'] else 'red'
    ax1.plot(['Pre', 'Post'],
            [row['FEV1_Pre'], row['FEV1_Post']],
            marker='o', color=color, alpha=0.5, linewidth=1.5)

# Medias con barras de error
medias = [datos['FEV1_Pre'].mean(), datos['FEV1_Post'].mean()]
errores = [datos['FEV1_Pre'].sem(), datos['FEV1_Post'].sem()]
ax1.errorbar(['Pre', 'Post'], medias, yerr=errores,
            color='black', linewidth=3, marker='D', markersize=10,
            capsize=10, label='Media ± ES')

ax1.set_ylabel('FEV1 (L)', fontsize=12, fontweight='bold')
ax1.set_title('Evolución Individual y Promedio', fontweight='bold')
ax1.legend()
ax1.grid(axis='y', alpha=0.3)

# Gráfico 2: Boxplots comparativos
datos_long = pd.DataFrame({
    'Momento': ['Pre']*n_pacientes + ['Post']*n_pacientes,
    'FEV1': list(datos['FEV1_Pre']) + list(datos['FEV1_Post'])
})

from scipy import stats as sp_stats
bp = ax2.boxplot([datos['FEV1_Pre'], datos['FEV1_Post']],
                 labels=['Pre', 'Post'], patch_artist=True,
                 notch=True, showmeans=True)
bp['boxes'][0].set_facecolor('lightcoral')
bp['boxes'][1].set_facecolor('lightgreen')

# Añadir resultado del t-test
t_stat, p_valor = sp_stats.ttest_rel(datos['FEV1_Pre'], datos['FEV1_Post'])
ax2.text(0.5, 0.95, f't-test pareado: p = {p_valor:.4f}\n' +
        ('✅ Cambio significativo' if p_valor < 0.05 else '❌ No significativo'),
        transform=ax2.transAxes, fontsize=11, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

ax2.set_ylabel('FEV1 (L)', fontsize=12, fontweight='bold')
ax2.set_title('Comparación Pre vs Post', fontweight='bold')
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('analisis_pre_post.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"Mejoría promedio: {(datos['FEV1_Post'] - datos['FEV1_Pre']).mean():.2f} L")
print(f"Pacientes que mejoraron: {(datos['FEV1_Post'] > datos['FEV1_Pre']).sum()}/{n_pacientes}")
```

---

## Consejos para Gráficos Profesionales

### ✅ Hacer

1. **Títulos descriptivos**: Que expliquen claramente qué muestra el gráfico
2. **Etiquetas de ejes**: Siempre incluir unidades (ej: "FEV1 (L)")
3. **Leyendas claras**: Cuando hay múltiples series
4. **Tamaño de texto legible**: Mínimo 10-12pt
5. **Alta resolución**: dpi=300 para publicaciones
6. **Colores accesibles**: Evitar solo rojo/verde (daltonismo)
7. **Grid sutil**: alpha=0.3 para no distraer

### ❌ Evitar

1. Gráficos 3D innecesarios
2. Demasiados colores
3. Texto muy pequeño
4. Ejes sin etiquetas
5. Escalas engañosas (eje Y que no empieza en 0)

---

## Paletas de Colores Recomendadas

```python
# Para grupos categóricos
sns.color_palette("Set2")       # Suave
sns.color_palette("Set1")       # Brillante
sns.color_palette("Pastel1")    # Pastel

# Para gradientes
sns.color_palette("Blues")      # Azules
sns.color_palette("RdYlGn")     # Rojo-Amarillo-Verde
sns.color_palette("viridis")    # Perceptualmente uniforme
```

---

## Resumen de Tipos de Gráficos

| Tipo de Datos | Gráfico Recomendado |
|---------------|---------------------|
| Una variable continua | Histograma, Boxplot |
| Dos grupos (comparar medias) | Boxplot, Barras con error |
| 3+ grupos (comparar medias) | Boxplot, Barras |
| Dos variables continuas | Scatter plot |
| Serie de tiempo | Línea |
| Proporciones/categorías | Barras, Pastel |
| Pre-Post | Líneas conectadas, Boxplot |

---

## Próximos Pasos

Ya tienes todas las herramientas para:
1. Analizar tus datos con **[Pandas](pandas_guide.md)**
2. Hacer pruebas estadísticas con **[SciPy](statistics_guide.md)**
3. Visualizar resultados profesionalmente con **matplotlib**

**¡Ahora puedes crear análisis completos de datos médicos!**

---

**Consejo final:** La mejor manera de aprender visualización es experimentar. Prueba diferentes tipos de gráficos con tus propios datos y ve cuál comunica mejor la información.
