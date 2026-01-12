# Python para Estadística Médica 🩺📊

Guía completa de Python para análisis estadístico de datos médicos, diseñada específicamente para profesionales de la salud sin experiencia previa en programación.

## 📋 Contenido

- **Scripts automatizados** para análisis estadístico y visualización
- **Guías completas** en español de Python, Pandas, Estadística y Visualización
- **Ejemplos médicos** con datos respiratorios (FEV1, espirometrías, etc.)
- **Explicaciones paso a paso** sin asumir conocimientos previos

## 🚀 Inicio Rápido

### Instalación

```bash
# Clonar este repositorio
git clone https://github.com/jaimeaalvarado-creator/vibe-coding-2026.git
cd vibe-coding-2026

# Instalar dependencias
pip install -r requirements.txt
```

### Uso de Scripts

#### 1. Análisis Estadístico Básico

```bash
# Análisis de una columna
python scripts/analisis_basico.py datos.xlsx FEV1

# Análisis con comparación de grupos
python scripts/analisis_basico.py datos.xlsx FEV1 Fumador
```

**Genera:**

- Estadísticas descriptivas completas
- Test de normalidad (Shapiro-Wilk)
- Comparación entre grupos (t-test o ANOVA)

#### 2. Visualización de Datos

```bash
# Gráficos básicos
python scripts/visualizar_datos.py datos.xlsx FEV1

# Gráficos con comparación de grupos
python scripts/visualizar_datos.py datos.xlsx FEV1 Fumador graficos.png
```

**Genera:**

- Histogramas
- Boxplots
- Gráficos de barras con medias
- Gráficos de pastel (distribución de grupos)

## 📚 Guías de Aprendizaje

### Para Principiantes

1. **[Python Básico](references/python_basics.md)** - Variables, loops, funciones, conceptos fundamentales
2. **[Pandas para Datos](references/pandas_guide.md)** - Leer Excel/CSV, filtrar, agrupar, guardar resultados
3. **[Estadística](references/statistics_guide.md)** - t-test, ANOVA, Chi-cuadrado, correlación, regresión
4. **[Visualización](references/visualization_guide.md)** - Crear gráficos profesionales con matplotlib

### Características de las Guías

- ✅ Ejemplos con terminología médica familiar
- ✅ Código completamente comentado en español
- ✅ Explicaciones paso a paso
- ✅ Sin jerga técnica innecesaria
- ✅ Enfoque 100% práctico

## 🔧 Requisitos

- Python 3.7 o superior
- pandas
- numpy
- scipy
- matplotlib
- openpyxl (para leer archivos Excel)

Ver [`requirements.txt`](requirements.txt) para versiones específicas.

## 📊 Ejemplos de Uso

### Ejemplo 1: Análisis Descriptivo

```python
import pandas as pd

# Leer datos
datos = pd.read_excel('espirometrias.xlsx')

# Calcular estadísticas
print(f"Media FEV1: {datos['FEV1'].mean():.2f}")
print(f"Desviación estándar: {datos['FEV1'].std():.2f}")
```

### Ejemplo 2: Comparación de Grupos

```python
from scipy.stats import ttest_ind

# Separar grupos
fumadores = datos[datos['Fumador'] == 'Sí']['FEV1']
no_fumadores = datos[datos['Fumador'] == 'No']['FEV1']

# t-test
t_stat, p_value = ttest_ind(fumadores, no_fumadores)
print(f"Valor p: {p_value:.4f}")
```

### Ejemplo 3: Visualización

```python
import matplotlib.pyplot as plt

# Crear histograma
plt.hist(datos['FEV1'], bins=15, edgecolor='black')
plt.xlabel('FEV1 (L)')
plt.ylabel('Frecuencia')
plt.title('Distribución de FEV1')
plt.show()
```

## 🎯 Casos de Uso

Este repositorio es ideal para:

- Análisis de datos de espirometrías
- Estudios clínicos y epidemiológicos
- Análisis de pruebas de función pulmonar (IOS, MBW, etc.)
- Investigación en neumología
- Tesis y trabajos de investigación médica
- Aprender Python para análisis de datos médicos

## 📖 Estructura del Proyecto

```
vibe-coding-2026/
├── scripts/              # Scripts listos para usar
│   ├── analisis_basico.py
│   └── visualizar_datos.py
├── references/           # Guías de aprendizaje
│   ├── python_basics.md
│   ├── pandas_guide.md
│   ├── statistics_guide.md
│   └── visualization_guide.md
├── requirements.txt      # Dependencias
├── CLAUDE.md            # Guía para AI assistants
└── README.md            # Este archivo
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias, ejemplos adicionales, o encuentras errores, por favor:

1. Abre un Issue describiendo el problema o sugerencia
2. Haz un Fork del repositorio
3. Crea una rama para tu cambio
4. Envía un Pull Request

## 📝 Licencia

Este proyecto está bajo licencia MIT. Ver archivo LICENSE para más detalles.

## 👨‍⚕️ Autor

Creado por profesionales de la salud para profesionales de la salud.

## 📧 Contacto

Si tienes preguntas o necesitas ayuda, abre un Issue en este repositorio.

## 🌟 Agradecimientos

Diseñado específicamente para facilitar el análisis estadístico de datos médicos sin requerir experiencia previa en programación.

---

**¿Nuevo en Python?** Comienza leyendo las guías en el siguiente orden:

1. [Python Básico](references/python_basics.md)
2. [Pandas para Datos](references/pandas_guide.md)
3. [Estadística](references/statistics_guide.md)
4. [Visualización](references/visualization_guide.md)

**¿Necesitas resultados rápidos?** Usa los scripts en la carpeta `scripts/` directamente.
