#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Análisis Estadístico Básico para Datos Médicos
==========================================================

Uso:
    python analisis_basico.py <archivo_datos> <columna_a_analizar> [columna_grupos]

Ejemplos:
    # Análisis básico de FEV1
    python analisis_basico.py datos.xlsx FEV1

    # Análisis de FEV1 comparando fumadores vs no fumadores
    python analisis_basico.py datos.xlsx FEV1 Fumador

Genera:
    - Estadísticas descriptivas completas
    - Test de normalidad (Shapiro-Wilk)
    - Comparación entre grupos (t-test o ANOVA)
    - Resultados guardados en archivo de texto
"""

import sys
import pandas as pd
import numpy as np
from scipy import stats
from datetime import datetime


def leer_datos(archivo):
    """
    Lee un archivo de datos (Excel o CSV).

    Parámetros:
        archivo: Ruta al archivo (puede ser .xlsx, .xls, o .csv)

    Retorna:
        DataFrame de pandas con los datos
    """
    print(f"\n📂 Leyendo archivo: {archivo}")

    try:
        # Intentar leer como Excel
        if archivo.endswith(('.xlsx', '.xls')):
            datos = pd.read_excel(archivo)
        # Intentar leer como CSV
        elif archivo.endswith('.csv'):
            datos = pd.read_csv(archivo)
        else:
            print("❌ Error: El archivo debe ser .xlsx, .xls, o .csv")
            sys.exit(1)

        print(f"✅ Archivo leído exitosamente")
        print(f"   - Filas: {len(datos)}")
        print(f"   - Columnas: {len(datos.columns)}")
        print(f"   - Columnas disponibles: {', '.join(datos.columns)}")

        return datos

    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{archivo}'")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        sys.exit(1)


def estadisticas_descriptivas(datos, columna):
    """
    Calcula estadísticas descriptivas para una columna.

    Parámetros:
        datos: DataFrame con los datos
        columna: Nombre de la columna a analizar

    Retorna:
        Diccionario con las estadísticas
    """
    # Eliminar valores faltantes
    valores = datos[columna].dropna()

    estadisticas = {
        'n': len(valores),
        'n_faltantes': datos[columna].isna().sum(),
        'media': valores.mean(),
        'mediana': valores.median(),
        'desviacion_std': valores.std(),
        'minimo': valores.min(),
        'maximo': valores.max(),
        'q25': valores.quantile(0.25),
        'q75': valores.quantile(0.75),
        'rango_intercuartil': valores.quantile(0.75) - valores.quantile(0.25)
    }

    return estadisticas, valores


def test_normalidad(valores, nombre_columna):
    """
    Realiza el test de Shapiro-Wilk para normalidad.

    Parámetros:
        valores: Serie de pandas con los valores
        nombre_columna: Nombre de la variable (para el reporte)

    Retorna:
        Diccionario con resultados del test
    """
    if len(valores) < 3:
        return {
            'test': 'Shapiro-Wilk',
            'estadistico': None,
            'p_valor': None,
            'normal': None,
            'mensaje': 'Insuficientes datos para test de normalidad (n < 3)'
        }

    # Test de Shapiro-Wilk
    estadistico, p_valor = stats.shapiro(valores)

    # Interpretación (alpha = 0.05)
    es_normal = p_valor > 0.05

    return {
        'test': 'Shapiro-Wilk',
        'estadistico': estadistico,
        'p_valor': p_valor,
        'normal': es_normal,
        'mensaje': 'Distribución normal' if es_normal else 'Distribución NO normal'
    }


def comparar_grupos(datos, columna_valores, columna_grupos):
    """
    Compara una variable numérica entre grupos.

    Parámetros:
        datos: DataFrame con los datos
        columna_valores: Nombre de la columna con valores numéricos
        columna_grupos: Nombre de la columna con los grupos

    Retorna:
        Diccionario con resultados de la comparación
    """
    # Obtener grupos únicos
    grupos = datos[columna_grupos].dropna().unique()
    n_grupos = len(grupos)

    if n_grupos < 2:
        return {
            'test': None,
            'mensaje': f'Insuficientes grupos para comparación (n={n_grupos})'
        }

    # Separar datos por grupo
    datos_por_grupo = []
    estadisticas_por_grupo = {}

    for grupo in grupos:
        valores_grupo = datos[datos[columna_grupos] == grupo][columna_valores].dropna()
        datos_por_grupo.append(valores_grupo)
        estadisticas_por_grupo[grupo] = {
            'n': len(valores_grupo),
            'media': valores_grupo.mean(),
            'desv_std': valores_grupo.std()
        }

    # Realizar test apropiado
    if n_grupos == 2:
        # t-test para 2 grupos
        estadistico, p_valor = stats.ttest_ind(datos_por_grupo[0], datos_por_grupo[1])
        test_nombre = 't-test (dos grupos independientes)'

    else:
        # ANOVA para 3+ grupos
        estadistico, p_valor = stats.f_oneway(*datos_por_grupo)
        test_nombre = 'ANOVA (análisis de varianza)'

    # Interpretación
    significativo = p_valor < 0.05

    return {
        'test': test_nombre,
        'n_grupos': n_grupos,
        'grupos': list(grupos),
        'estadistico': estadistico,
        'p_valor': p_valor,
        'significativo': significativo,
        'estadisticas_grupos': estadisticas_por_grupo,
        'mensaje': 'Diferencia significativa entre grupos' if significativo else 'NO hay diferencia significativa'
    }


def generar_reporte(resultados, archivo_salida='resultados_analisis.txt'):
    """
    Genera un reporte en texto con los resultados del análisis.

    Parámetros:
        resultados: Diccionario con todos los resultados
        archivo_salida: Nombre del archivo de salida
    """
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        # Encabezado
        f.write("=" * 70 + "\n")
        f.write("REPORTE DE ANÁLISIS ESTADÍSTICO\n")
        f.write("=" * 70 + "\n")
        f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Archivo analizado: {resultados['archivo']}\n")
        f.write(f"Variable analizada: {resultados['columna']}\n")
        if resultados.get('columna_grupos'):
            f.write(f"Grupos comparados: {resultados['columna_grupos']}\n")
        f.write("=" * 70 + "\n\n")

        # Estadísticas descriptivas
        f.write("ESTADÍSTICAS DESCRIPTIVAS\n")
        f.write("-" * 70 + "\n")
        est = resultados['estadisticas']
        f.write(f"N (tamaño muestral):          {est['n']}\n")
        f.write(f"Valores faltantes:            {est['n_faltantes']}\n")
        f.write(f"Media:                        {est['media']:.4f}\n")
        f.write(f"Mediana:                      {est['mediana']:.4f}\n")
        f.write(f"Desviación estándar:          {est['desviacion_std']:.4f}\n")
        f.write(f"Mínimo:                       {est['minimo']:.4f}\n")
        f.write(f"Máximo:                       {est['maximo']:.4f}\n")
        f.write(f"Percentil 25:                 {est['q25']:.4f}\n")
        f.write(f"Percentil 75:                 {est['q75']:.4f}\n")
        f.write(f"Rango intercuartil (IQR):     {est['rango_intercuartil']:.4f}\n")
        f.write("\n")

        # Test de normalidad
        f.write("TEST DE NORMALIDAD\n")
        f.write("-" * 70 + "\n")
        norm = resultados['normalidad']
        f.write(f"Test: {norm['test']}\n")
        if norm['estadistico'] is not None:
            f.write(f"Estadístico W: {norm['estadistico']:.4f}\n")
            f.write(f"Valor p: {norm['p_valor']:.4f}\n")
            f.write(f"Resultado: {norm['mensaje']}\n")
            f.write(f"\nInterpretación: ")
            if norm['normal']:
                f.write("Los datos siguen una distribución normal (p > 0.05).\n")
                f.write("Se pueden usar pruebas paramétricas (t-test, ANOVA).\n")
            else:
                f.write("Los datos NO siguen una distribución normal (p ≤ 0.05).\n")
                f.write("Considerar pruebas no paramétricas (Mann-Whitney, Kruskal-Wallis).\n")
        else:
            f.write(f"Resultado: {norm['mensaje']}\n")
        f.write("\n")

        # Comparación de grupos (si aplica)
        if resultados.get('comparacion'):
            comp = resultados['comparacion']
            if comp.get('test'):
                f.write("COMPARACIÓN ENTRE GRUPOS\n")
                f.write("-" * 70 + "\n")
                f.write(f"Test aplicado: {comp['test']}\n")
                f.write(f"Número de grupos: {comp['n_grupos']}\n")
                f.write(f"Grupos: {', '.join(map(str, comp['grupos']))}\n\n")

                # Estadísticas por grupo
                f.write("Estadísticas por grupo:\n")
                for grupo, stats_grupo in comp['estadisticas_grupos'].items():
                    f.write(f"\n  {grupo}:\n")
                    f.write(f"    N:                  {stats_grupo['n']}\n")
                    f.write(f"    Media:              {stats_grupo['media']:.4f}\n")
                    f.write(f"    Desviación estándar: {stats_grupo['desv_std']:.4f}\n")

                f.write(f"\nEstadístico: {comp['estadistico']:.4f}\n")
                f.write(f"Valor p: {comp['p_valor']:.4f}\n")
                f.write(f"Resultado: {comp['mensaje']}\n")
                f.write(f"\nInterpretación: ")
                if comp['significativo']:
                    f.write("Hay diferencias estadísticamente significativas entre grupos (p < 0.05).\n")
                else:
                    f.write("NO hay diferencias estadísticamente significativas entre grupos (p ≥ 0.05).\n")
            else:
                f.write("COMPARACIÓN ENTRE GRUPOS\n")
                f.write("-" * 70 + "\n")
                f.write(f"{comp['mensaje']}\n")
            f.write("\n")

        # Pie
        f.write("=" * 70 + "\n")
        f.write("Fin del reporte\n")
        f.write("=" * 70 + "\n")

    print(f"\n💾 Reporte guardado en: {archivo_salida}")


def main():
    """Función principal del script."""

    # Verificar argumentos
    if len(sys.argv) < 3:
        print("\n❌ Error: Argumentos insuficientes\n")
        print("Uso:")
        print("  python analisis_basico.py <archivo_datos> <columna_a_analizar> [columna_grupos]\n")
        print("Ejemplos:")
        print("  python analisis_basico.py datos.xlsx FEV1")
        print("  python analisis_basico.py datos.xlsx FEV1 Fumador\n")
        sys.exit(1)

    # Obtener argumentos
    archivo = sys.argv[1]
    columna_valores = sys.argv[2]
    columna_grupos = sys.argv[3] if len(sys.argv) > 3 else None

    print("\n" + "=" * 70)
    print("ANÁLISIS ESTADÍSTICO DE DATOS MÉDICOS")
    print("=" * 70)

    # Leer datos
    datos = leer_datos(archivo)

    # Verificar que la columna existe
    if columna_valores not in datos.columns:
        print(f"\n❌ Error: La columna '{columna_valores}' no existe en el archivo")
        print(f"Columnas disponibles: {', '.join(datos.columns)}")
        sys.exit(1)

    # Verificar que la columna de grupos existe (si se especificó)
    if columna_grupos and columna_grupos not in datos.columns:
        print(f"\n❌ Error: La columna '{columna_grupos}' no existe en el archivo")
        print(f"Columnas disponibles: {', '.join(datos.columns)}")
        sys.exit(1)

    # Análisis descriptivo
    print(f"\n📊 Calculando estadísticas descriptivas...")
    estadisticas, valores = estadisticas_descriptivas(datos, columna_valores)
    print("✅ Completado")

    # Test de normalidad
    print(f"\n🔬 Realizando test de normalidad...")
    normalidad = test_normalidad(valores, columna_valores)
    print(f"✅ Completado - {normalidad['mensaje']}")

    # Preparar resultados
    resultados = {
        'archivo': archivo,
        'columna': columna_valores,
        'estadisticas': estadisticas,
        'normalidad': normalidad
    }

    # Comparación de grupos (si se especificó)
    if columna_grupos:
        print(f"\n🔍 Comparando grupos...")
        comparacion = comparar_grupos(datos, columna_valores, columna_grupos)
        resultados['columna_grupos'] = columna_grupos
        resultados['comparacion'] = comparacion
        if comparacion.get('test'):
            print(f"✅ Completado - {comparacion['mensaje']}")
        else:
            print(f"⚠️  {comparacion['mensaje']}")

    # Generar reporte
    print(f"\n📝 Generando reporte...")
    generar_reporte(resultados)

    print("\n" + "=" * 70)
    print("✅ ANÁLISIS COMPLETADO")
    print("=" * 70)
    print("\nResumen de resultados:")
    print(f"  - N: {estadisticas['n']}")
    print(f"  - Media: {estadisticas['media']:.2f} ± {estadisticas['desviacion_std']:.2f}")
    print(f"  - Distribución: {normalidad['mensaje']}")
    if columna_grupos and resultados.get('comparacion', {}).get('test'):
        print(f"  - Comparación: {resultados['comparacion']['mensaje']}")
    print()


if __name__ == '__main__':
    main()
