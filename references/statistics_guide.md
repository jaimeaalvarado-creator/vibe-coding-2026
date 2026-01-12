# Guía de Estadística para Datos Médicos con Python 📊

Esta guía cubre las pruebas estadísticas más comunes en investigación médica usando Python, con ejemplos prácticos y explicaciones claras.

## Tabla de Contenidos

1. [Introducción a scipy.stats](#introducción-a-scipystats)
2. [Estadística Descriptiva](#estadística-descriptiva)
3. [Tests de Normalidad](#tests-de-normalidad)
4. [Comparación de Dos Grupos](#comparación-de-dos-grupos)
5. [Comparación de Múltiples Grupos](#comparación-de-múltiples-grupos)
6. [Tests No Paramétricos](#tests-no-paramétricos)
7. [Correlación](#correlación)
8. [Regresión Lineal](#regresión-lineal)
9. [Chi-Cuadrado](#chi-cuadrado)
10. [Ejemplos Médicos Completos](#ejemplos-médicos-completos)

---

## Introducción a scipy.stats

**SciPy** es la librería principal para análisis estadístico en Python. El módulo `stats` contiene todas las pruebas estadísticas.

```python
# Importar
from scipy import stats
import numpy as np
import pandas as pd
```

---

## Estadística Descriptiva

### Medidas de Tendencia Central

```python
import numpy as np

# Datos de ejemplo: FEV1 de 10 pacientes
fev1 = [2.5, 3.1, 2.8, 2.2, 3.4, 2.6, 2.9, 2.3, 3.0, 2.7]

# Media (promedio)
media = np.mean(fev1)
print(f"Media: {media:.2f} L")  # 2.75 L

# Mediana (valor central)
mediana = np.median(fev1)
print(f"Mediana: {mediana:.2f} L")  # 2.75 L

# Moda (valor más frecuente) - usar scipy.stats
from scipy import stats
moda = stats.mode(fev1, keepdims=True)
print(f"Moda: {moda.mode[0]:.2f} L")
```

### Medidas de Dispersión

```python
# Desviación estándar
std = np.std(fev1, ddof=1)  # ddof=1 para muestra (no población)
print(f"Desviación estándar: {std:.2f} L")

# Varianza
varianza = np.var(fev1, ddof=1)
print(f"Varianza: {varianza:.2f}")

# Rango
rango = np.max(fev1) - np.min(fev1)
print(f"Rango: {rango:.2f} L")

# Rango intercuartil (IQR)
q25 = np.percentile(fev1, 25)
q75 = np.percentile(fev1, 75)
iqr = q75 - q25
print(f"IQR: {iqr:.2f} L")

# Error estándar de la media
sem = stats.sem(fev1)
print(f"Error estándar: {sem:.2f}")
```

### Intervalos de Confianza

```python
# Intervalo de confianza del 95% para la media
confianza = 0.95
intervalo = stats.t.interval(
    confianza,
    len(fev1) - 1,  # grados de libertad
    loc=np.mean(fev1),  # media
    scale=stats.sem(fev1)  # error estándar
)

print(f"IC 95%: [{intervalo[0]:.2f}, {intervalo[1]:.2f}]")
print(f"Media: {np.mean(fev1):.2f} (IC 95%: {intervalo[0]:.2f}-{intervalo[1]:.2f})")
```

---

## Tests de Normalidad

### ¿Por qué es importante?
- **Distribución normal**: Usar tests paramétricos (t-test, ANOVA)
- **Distribución NO normal**: Usar tests no paramétricos (Mann-Whitney, Kruskal-Wallis)

### Test de Shapiro-Wilk

```python
from scipy import stats

fev1 = [2.5, 3.1, 2.8, 2.2, 3.4, 2.6, 2.9, 2.3, 3.0, 2.7]

# Test de Shapiro-Wilk (mejor para n < 50)
estadistico, p_valor = stats.shapiro(fev1)

print(f"Estadístico W: {estadistico:.4f}")
print(f"Valor p: {p_valor:.4f}")

# Interpretación
if p_valor > 0.05:
    print("✅ Los datos siguen una distribución normal (p > 0.05)")
    print("   → Usar tests paramétricos")
else:
    print("❌ Los datos NO siguen una distribución normal (p ≤ 0.05)")
    print("   → Usar tests no paramétricos")
```

### Test de Kolmogorov-Smirnov

```python
# Test de Kolmogorov-Smirnov (mejor para n ≥ 50)
estadistico, p_valor = stats.kstest(fev1, 'norm')

print(f"Valor p: {p_valor:.4f}")
```

---

## Comparación de Dos Grupos

### t-test Independiente (Dos Grupos Diferentes)

**Uso:** Comparar medias de dos grupos independientes (ej: fumadores vs no fumadores)

**Requisitos:**
- Distribución normal en ambos grupos
- Muestras independientes

```python
from scipy import stats

# Datos: FEV1 de fumadores y no fumadores
fumadores = [1.8, 2.1, 1.9, 2.0, 1.7, 2.2]
no_fumadores = [2.8, 3.1, 2.9, 3.0, 2.7, 3.2]

# t-test independiente
estadistico, p_valor = stats.ttest_ind(fumadores, no_fumadores)

print("t-TEST INDEPENDIENTE")
print("=" * 50)
print(f"Media fumadores: {np.mean(fumadores):.2f} L")
print(f"Media no fumadores: {np.mean(no_fumadores):.2f} L")
print(f"Estadístico t: {estadistico:.4f}")
print(f"Valor p: {p_valor:.4f}")

# Interpretación
if p_valor < 0.05:
    print("✅ Diferencia SIGNIFICATIVA (p < 0.05)")
    print("   Los grupos son estadísticamente diferentes")
else:
    print("❌ Diferencia NO significativa (p ≥ 0.05)")
    print("   No hay evidencia de diferencia entre grupos")
```

### t-test Pareado (Mismo Grupo, Dos Momentos)

**Uso:** Comparar medidas pre-post en los mismos pacientes

```python
# Datos: FEV1 antes y después de tratamiento
fev1_pre = [1.8, 2.1, 1.9, 2.0, 1.7, 2.2]
fev1_post = [2.2, 2.4, 2.3, 2.3, 2.0, 2.5]

# t-test pareado
estadistico, p_valor = stats.ttest_rel(fev1_pre, fev1_post)

print("t-TEST PAREADO (PRE-POST)")
print("=" * 50)
print(f"Media PRE: {np.mean(fev1_pre):.2f} L")
print(f"Media POST: {np.mean(fev1_post):.2f} L")
print(f"Cambio medio: {np.mean(fev1_post) - np.mean(fev1_pre):.2f} L")
print(f"Valor p: {p_valor:.4f}")

if p_valor < 0.05:
    print("✅ El tratamiento tuvo efecto SIGNIFICATIVO")
else:
    print("❌ El tratamiento NO tuvo efecto significativo")
```

### Welch's t-test (Varianzas Desiguales)

```python
# Si las varianzas son muy diferentes, usar Welch's t-test
estadistico, p_valor = stats.ttest_ind(fumadores, no_fumadores, equal_var=False)
print(f"Welch's t-test - Valor p: {p_valor:.4f}")
```

---

## Comparación de Múltiples Grupos

### ANOVA (Análisis de Varianza)

**Uso:** Comparar medias de 3 o más grupos

**Requisitos:**
- Distribución normal en cada grupo
- Varianzas homogéneas

```python
from scipy import stats

# Datos: FEV1 de tres grupos de tratamiento
grupo_a = [2.5, 2.7, 2.6, 2.8, 2.4]
grupo_b = [2.1, 2.3, 2.2, 2.4, 2.0]
grupo_c = [3.0, 3.2, 3.1, 2.9, 3.3]

# ANOVA
estadistico_f, p_valor = stats.f_oneway(grupo_a, grupo_b, grupo_c)

print("ANOVA (ANÁLISIS DE VARIANZA)")
print("=" * 50)
print(f"Media Grupo A: {np.mean(grupo_a):.2f} L")
print(f"Media Grupo B: {np.mean(grupo_b):.2f} L")
print(f"Media Grupo C: {np.mean(grupo_c):.2f} L")
print(f"Estadístico F: {estadistico_f:.4f}")
print(f"Valor p: {p_valor:.4f}")

if p_valor < 0.05:
    print("✅ Hay diferencias SIGNIFICATIVAS entre los grupos")
    print("   (al menos un grupo es diferente)")
else:
    print("❌ NO hay diferencias significativas entre grupos")
```

### Post-hoc Tests (Después de ANOVA)

Si ANOVA es significativo, usar post-hoc para saber QUÉ grupos difieren:

```python
from scipy.stats import ttest_ind

# Comparaciones por pares (Bonferroni correction)
alpha = 0.05 / 3  # Corrección de Bonferroni para 3 comparaciones

print("\nCOMPARACIONES POST-HOC (Bonferroni)")
print("=" * 50)

# A vs B
_, p_ab = ttest_ind(grupo_a, grupo_b)
print(f"A vs B: p = {p_ab:.4f} {'✅ Significativo' if p_ab < alpha else '❌ No significativo'}")

# A vs C
_, p_ac = ttest_ind(grupo_a, grupo_c)
print(f"A vs C: p = {p_ac:.4f} {'✅ Significativo' if p_ac < alpha else '❌ No significativo'}")

# B vs C
_, p_bc = ttest_ind(grupo_b, grupo_c)
print(f"B vs C: p = {p_bc:.4f} {'✅ Significativo' if p_bc < alpha else '❌ No significativo'}")
```

---

## Tests No Paramétricos

### Mann-Whitney U Test (Alternativa a t-test)

**Uso:** Comparar dos grupos cuando los datos NO son normales

```python
from scipy import stats

fumadores = [1.8, 2.1, 1.9, 2.0, 1.7, 2.2, 1.5]
no_fumadores = [2.8, 3.1, 2.9, 3.0, 2.7, 3.2, 2.6]

# Mann-Whitney U test
estadistico, p_valor = stats.mannwhitneyu(fumadores, no_fumadores, alternative='two-sided')

print("MANN-WHITNEY U TEST (No paramétrico)")
print("=" * 50)
print(f"Mediana fumadores: {np.median(fumadores):.2f} L")
print(f"Mediana no fumadores: {np.median(no_fumadores):.2f} L")
print(f"Valor p: {p_valor:.4f}")

if p_valor < 0.05:
    print("✅ Diferencia SIGNIFICATIVA entre grupos")
else:
    print("❌ NO hay diferencia significativa")
```

### Wilcoxon Test (Alternativa a t-test pareado)

**Uso:** Comparar medidas pre-post cuando datos NO son normales

```python
# Datos pre-post
fev1_pre = [1.8, 2.1, 1.9, 2.0, 1.7, 2.2]
fev1_post = [2.2, 2.4, 2.3, 2.3, 2.0, 2.5]

# Wilcoxon signed-rank test
estadistico, p_valor = stats.wilcoxon(fev1_pre, fev1_post)

print("WILCOXON TEST (Pre-Post no paramétrico)")
print("=" * 50)
print(f"Mediana PRE: {np.median(fev1_pre):.2f} L")
print(f"Mediana POST: {np.median(fev1_post):.2f} L")
print(f"Valor p: {p_valor:.4f}")
```

### Kruskal-Wallis Test (Alternativa a ANOVA)

**Uso:** Comparar 3+ grupos cuando datos NO son normales

```python
grupo_a = [2.5, 2.7, 2.6, 2.8, 2.4]
grupo_b = [2.1, 2.3, 2.2, 2.4, 2.0]
grupo_c = [3.0, 3.2, 3.1, 2.9, 3.3]

# Kruskal-Wallis test
estadistico, p_valor = stats.kruskal(grupo_a, grupo_b, grupo_c)

print("KRUSKAL-WALLIS TEST (ANOVA no paramétrico)")
print("=" * 50)
print(f"Valor p: {p_valor:.4f}")

if p_valor < 0.05:
    print("✅ Hay diferencias SIGNIFICATIVAS entre grupos")
else:
    print("❌ NO hay diferencias significativas")
```

---

## Correlación

### Correlación de Pearson (Datos Normales)

**Uso:** Medir relación lineal entre dos variables continuas

**Valor r:**
- r = 1: Correlación positiva perfecta
- r = 0: Sin correlación
- r = -1: Correlación negativa perfecta

```python
from scipy import stats
import numpy as np

# Datos: Edad y FEV1
edad = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
fev1 = [3.5, 3.4, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8]

# Correlación de Pearson
r, p_valor = stats.pearsonr(edad, fev1)

print("CORRELACIÓN DE PEARSON")
print("=" * 50)
print(f"Coeficiente r: {r:.4f}")
print(f"Valor p: {p_valor:.4f}")

# Interpretación de r
if abs(r) < 0.3:
    fuerza = "débil"
elif abs(r) < 0.7:
    fuerza = "moderada"
else:
    fuerza = "fuerte"

direccion = "positiva" if r > 0 else "negativa"

print(f"Interpretación: Correlación {fuerza} {direccion}")

if p_valor < 0.05:
    print("✅ Correlación SIGNIFICATIVA (p < 0.05)")
else:
    print("❌ Correlación NO significativa")
```

### Correlación de Spearman (Datos No Normales)

```python
# Correlación de Spearman (no paramétrica)
rho, p_valor = stats.spearmanr(edad, fev1)

print("CORRELACIÓN DE SPEARMAN")
print("=" * 50)
print(f"Coeficiente rho: {rho:.4f}")
print(f"Valor p: {p_valor:.4f}")
```

---

## Regresión Lineal

### Regresión Lineal Simple

**Uso:** Predecir una variable (Y) basándose en otra (X)

```python
from scipy import stats
import numpy as np

# Datos: Predecir FEV1 basándose en edad
edad = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
fev1 = np.array([3.5, 3.4, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8])

# Regresión lineal
slope, intercept, r_value, p_value, std_err = stats.linregress(edad, fev1)

print("REGRESIÓN LINEAL")
print("=" * 50)
print(f"Ecuación: FEV1 = {intercept:.4f} + {slope:.4f} × Edad")
print(f"R²: {r_value**2:.4f}")
print(f"Valor p: {p_value:.4f}")

# Predecir para nueva edad
edad_nueva = 42
fev1_predicho = intercept + slope * edad_nueva
print(f"\nPredicción para edad {edad_nueva}: FEV1 = {fev1_predicho:.2f} L")

# Interpretación
print(f"\nInterpretación:")
print(f"Por cada año adicional de edad, el FEV1 disminuye {abs(slope):.4f} L")
```

---

## Chi-Cuadrado

### Test de Independencia (Tablas de Contingencia)

**Uso:** Determinar si dos variables categóricas están relacionadas

```python
from scipy import stats
import numpy as np

# Tabla de contingencia: Fumador vs Enfermedad
#                  Enfermo  Sano
# Fumador             30      20
# No fumador          10      40

tabla = np.array([
    [30, 20],  # Fumadores
    [10, 40]   # No fumadores
])

# Chi-cuadrado
chi2, p_valor, dof, expected = stats.chi2_contingency(tabla)

print("TEST DE CHI-CUADRADO")
print("=" * 50)
print("Tabla observada:")
print(tabla)
print(f"\nEstadístico χ²: {chi2:.4f}")
print(f"Grados de libertad: {dof}")
print(f"Valor p: {p_valor:.4f}")

if p_valor < 0.05:
    print("✅ Hay asociación SIGNIFICATIVA entre variables")
    print("   (Fumar y enfermedad están relacionados)")
else:
    print("❌ NO hay asociación significativa")

# Frecuencias esperadas
print("\nFrecuencias esperadas:")
print(expected)
```

### Test de Chi-Cuadrado de Bondad de Ajuste

```python
# Verificar si los datos siguen una distribución esperada
# Ejemplo: Distribución de grupos sanguíneos

observado = [45, 42, 10, 3]  # O, A, B, AB
esperado = [45, 40, 11, 4]   # Distribución esperada

chi2, p_valor = stats.chisquare(observado, esperado)

print(f"χ²: {chi2:.4f}")
print(f"Valor p: {p_valor:.4f}")
```

---

## Ejemplos Médicos Completos

### Ejemplo 1: Estudio Completo Fumadores vs No Fumadores

```python
import pandas as pd
import numpy as np
from scipy import stats

# Crear datos de ejemplo
np.random.seed(42)
datos = pd.DataFrame({
    'FEV1': np.concatenate([
        np.random.normal(2.0, 0.4, 30),  # Fumadores
        np.random.normal(2.8, 0.4, 30)   # No fumadores
    ]),
    'Fumador': ['Sí']*30 + ['No']*30
})

print("=" * 70)
print("ANÁLISIS: COMPARACIÓN FUMADORES VS NO FUMADORES")
print("=" * 70)

# 1. Estadística descriptiva por grupo
print("\n1. ESTADÍSTICA DESCRIPTIVA")
print("-" * 70)
for grupo in ['Sí', 'No']:
    datos_grupo = datos[datos['Fumador'] == grupo]['FEV1']
    print(f"\n{grupo} fumadores:")
    print(f"  N: {len(datos_grupo)}")
    print(f"  Media: {datos_grupo.mean():.2f} L")
    print(f"  Desv. Std: {datos_grupo.std():.2f} L")
    print(f"  Mediana: {datos_grupo.median():.2f} L")
    print(f"  Rango: {datos_grupo.min():.2f} - {datos_grupo.max():.2f} L")

# 2. Test de normalidad en cada grupo
print("\n2. TEST DE NORMALIDAD (Shapiro-Wilk)")
print("-" * 70)
for grupo in ['Sí', 'No']:
    datos_grupo = datos[datos['Fumador'] == grupo]['FEV1']
    stat, p = stats.shapiro(datos_grupo)
    es_normal = "✅ Normal" if p > 0.05 else "❌ No normal"
    print(f"{grupo} fumadores: p = {p:.4f} - {es_normal}")

# 3. Comparación entre grupos
print("\n3. COMPARACIÓN ENTRE GRUPOS")
print("-" * 70)

fumadores = datos[datos['Fumador'] == 'Sí']['FEV1']
no_fumadores = datos[datos['Fumador'] == 'No']['FEV1']

# t-test
t_stat, p_ttest = stats.ttest_ind(fumadores, no_fumadores)
print(f"t-test independiente:")
print(f"  Estadístico t: {t_stat:.4f}")
print(f"  Valor p: {p_ttest:.4f}")

if p_ttest < 0.05:
    print(f"  ✅ Diferencia SIGNIFICATIVA (p < 0.05)")
    dif = no_fumadores.mean() - fumadores.mean()
    print(f"  Diferencia de medias: {dif:.2f} L")
else:
    print(f"  ❌ NO hay diferencia significativa")

# Mann-Whitney (alternativa no paramétrica)
u_stat, p_mann = stats.mannwhitneyu(fumadores, no_fumadores)
print(f"\nMann-Whitney U test:")
print(f"  Valor p: {p_mann:.4f}")

# 4. Tamaño del efecto (Cohen's d)
print("\n4. TAMAÑO DEL EFECTO")
print("-" * 70)
cohens_d = (no_fumadores.mean() - fumadores.mean()) / np.sqrt(
    ((len(fumadores)-1)*fumadores.std()**2 + (len(no_fumadores)-1)*no_fumadores.std()**2) /
    (len(fumadores) + len(no_fumadores) - 2)
)
print(f"Cohen's d: {cohens_d:.4f}")
if abs(cohens_d) < 0.2:
    print("  Efecto: Pequeño")
elif abs(cohens_d) < 0.5:
    print("  Efecto: Mediano")
else:
    print("  Efecto: Grande")

print("\n" + "=" * 70)
```

### Ejemplo 2: Análisis Pre-Post Tratamiento

```python
import pandas as pd
import numpy as np
from scipy import stats

# Datos pre-post
np.random.seed(42)
n_pacientes = 20
datos = pd.DataFrame({
    'Paciente': [f'P{i+1}' for i in range(n_pacientes)],
    'FEV1_Pre': np.random.normal(2.0, 0.3, n_pacientes),
})
datos['FEV1_Post'] = datos['FEV1_Pre'] + np.random.normal(0.3, 0.15, n_pacientes)

print("=" * 70)
print("ANÁLISIS PRE-POST TRATAMIENTO")
print("=" * 70)

# 1. Estadística descriptiva
print("\n1. ESTADÍSTICA DESCRIPTIVA")
print("-" * 70)
print(f"Media PRE: {datos['FEV1_Pre'].mean():.2f} ± {datos['FEV1_Pre'].std():.2f} L")
print(f"Media POST: {datos['FEV1_Post'].mean():.2f} ± {datos['FEV1_Post'].std():.2f} L")

# 2. Calcular cambio
datos['Cambio'] = datos['FEV1_Post'] - datos['FEV1_Pre']
datos['Cambio_Pct'] = (datos['Cambio'] / datos['FEV1_Pre']) * 100

print(f"Cambio medio: {datos['Cambio'].mean():.2f} L")
print(f"Cambio %: {datos['Cambio_Pct'].mean():.1f}%")

# 3. Test de normalidad del cambio
stat, p_norm = stats.shapiro(datos['Cambio'])
print(f"\nNormalidad del cambio: p = {p_norm:.4f}")

# 4. t-test pareado
t_stat, p_valor = stats.ttest_rel(datos['FEV1_Pre'], datos['FEV1_Post'])

print("\n2. t-TEST PAREADO")
print("-" * 70)
print(f"Estadístico t: {t_stat:.4f}")
print(f"Valor p: {p_valor:.4f}")

if p_valor < 0.05:
    print("✅ El tratamiento tuvo efecto SIGNIFICATIVO")
else:
    print("❌ El tratamiento NO tuvo efecto significativo")

# 5. Intervalo de confianza del cambio
ic = stats.t.interval(0.95, len(datos['Cambio'])-1,
                      loc=datos['Cambio'].mean(),
                      scale=stats.sem(datos['Cambio']))
print(f"\nIC 95% del cambio: [{ic[0]:.2f}, {ic[1]:.2f}] L")

# 6. Cuántos pacientes mejoraron
mejoraron = (datos['Cambio'] > 0).sum()
print(f"\nPacientes que mejoraron: {mejoraron}/{n_pacientes} ({mejoraron/n_pacientes*100:.1f}%)")

print("\n" + "=" * 70)
```

---

## Guía Rápida: ¿Qué Test Usar?

| Situación | Test Paramétrico | Test No Paramétrico |
|-----------|------------------|---------------------|
| **2 grupos independientes** | t-test independiente | Mann-Whitney U |
| **2 grupos pareados (pre-post)** | t-test pareado | Wilcoxon |
| **3+ grupos independientes** | ANOVA | Kruskal-Wallis |
| **Correlación** | Pearson | Spearman |
| **Variables categóricas** | - | Chi-cuadrado |

**¿Paramétrico o No Paramétrico?**
1. Test de normalidad (Shapiro-Wilk)
2. Si p > 0.05 → Normal → Usar test paramétrico
3. Si p ≤ 0.05 → No normal → Usar test no paramétrico

---

## Interpretación de Valores p

| Valor p | Interpretación | Significancia |
|---------|----------------|---------------|
| p < 0.001 | Altamente significativo | *** |
| p < 0.01 | Muy significativo | ** |
| p < 0.05 | Significativo | * |
| p ≥ 0.05 | No significativo | ns |

---

## Próximos Pasos

1. **[Visualización](visualization_guide.md)** - Crear gráficos de tus análisis estadísticos

---

**Importante:** El valor p solo indica si hay diferencia estadística, NO si la diferencia es clínicamente importante. Siempre considera el contexto clínico y el tamaño del efecto.
