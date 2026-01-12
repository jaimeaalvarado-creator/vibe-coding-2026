#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Visualización de Datos Médicos
=========================================

Uso:
    python visualizar_datos.py <archivo_datos> <columna_a_visualizar> [columna_grupos] [archivo_salida]

Ejemplos:
    # Visualización básica de FEV1
    python visualizar_datos.py datos.xlsx FEV1

    # Visualización de FEV1 por grupos de fumadores
    python visualizar_datos.py datos.xlsx FEV1 Fumador

    # Especificar archivo de salida
    python visualizar_datos.py datos.xlsx FEV1 Fumador mis_graficos.png

Genera:
    - Histograma con curva de distribución
    - Boxplot (diagrama de caja)
    - Gráfico de barras con medias (si hay grupos)
    - Gráfico de pastel con distribución de grupos (si hay grupos)
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


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

        return datos

    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{archivo}'")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        sys.exit(1)


def crear_histograma(ax, valores, columna_nombre, color='#3498db'):
    """
    Crea un histograma con curva de densidad.

    Parámetros:
        ax: Eje de matplotlib donde dibujar
        valores: Serie de pandas con los valores
        columna_nombre: Nombre de la variable
        color: Color para el histograma
    """
    # Histograma
    ax.hist(valores, bins=15, density=True, alpha=0.7,
            color=color, edgecolor='black', linewidth=1.2)

    # Curva de densidad (KDE)
    try:
        kde = stats.gaussian_kde(valores)
        x_range = np.linspace(valores.min(), valores.max(), 100)
        ax.plot(x_range, kde(x_range), 'r-', linewidth=2, label='Densidad')
    except:
        pass  # Si falla el KDE, simplemente no lo dibujamos

    # Línea de media
    media = valores.mean()
    ax.axvline(media, color='green', linestyle='--', linewidth=2, label=f'Media: {media:.2f}')

    # Línea de mediana
    mediana = valores.median()
    ax.axvline(mediana, color='orange', linestyle='--', linewidth=2, label=f'Mediana: {mediana:.2f}')

    ax.set_xlabel(columna_nombre, fontsize=12, fontweight='bold')
    ax.set_ylabel('Densidad', fontsize=12, fontweight='bold')
    ax.set_title(f'Distribución de {columna_nombre}', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)


def crear_boxplot(ax, datos, columna_valores, columna_grupos=None):
    """
    Crea un boxplot (diagrama de caja).

    Parámetros:
        ax: Eje de matplotlib donde dibujar
        datos: DataFrame con los datos
        columna_valores: Nombre de la columna con valores
        columna_grupos: Nombre de la columna con grupos (opcional)
    """
    if columna_grupos:
        # Boxplot por grupos
        datos_limpios = datos[[columna_valores, columna_grupos]].dropna()
        grupos = datos_limpios[columna_grupos].unique()

        datos_por_grupo = [datos_limpios[datos_limpios[columna_grupos] == grupo][columna_valores].values
                          for grupo in grupos]

        bp = ax.boxplot(datos_por_grupo, labels=grupos, patch_artist=True,
                       notch=True, showmeans=True)

        # Colorear cajas
        colores = plt.cm.Set3(np.linspace(0, 1, len(grupos)))
        for patch, color in zip(bp['boxes'], colores):
            patch.set_facecolor(color)

        ax.set_xlabel(columna_grupos, fontsize=12, fontweight='bold')
        ax.set_title(f'Boxplot de {columna_valores} por {columna_grupos}',
                    fontsize=14, fontweight='bold')
    else:
        # Boxplot simple
        valores = datos[columna_valores].dropna()
        bp = ax.boxplot([valores], labels=[columna_valores], patch_artist=True,
                       notch=True, showmeans=True)

        bp['boxes'][0].set_facecolor('#3498db')

        ax.set_title(f'Boxplot de {columna_valores}', fontsize=14, fontweight='bold')

    ax.set_ylabel(columna_valores, fontsize=12, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)


def crear_barras_medias(ax, datos, columna_valores, columna_grupos):
    """
    Crea un gráfico de barras con medias y barras de error.

    Parámetros:
        ax: Eje de matplotlib donde dibujar
        datos: DataFrame con los datos
        columna_valores: Nombre de la columna con valores
        columna_grupos: Nombre de la columna con grupos
    """
    # Calcular medias y errores estándar por grupo
    datos_limpios = datos[[columna_valores, columna_grupos]].dropna()
    grupos = datos_limpios.groupby(columna_grupos)[columna_valores]

    medias = grupos.mean()
    errores = grupos.sem()  # Error estándar de la media
    n_por_grupo = grupos.count()

    # Crear barras
    colores = plt.cm.Set2(np.linspace(0, 1, len(medias)))
    barras = ax.bar(range(len(medias)), medias, yerr=errores,
                   capsize=10, alpha=0.8, color=colores,
                   edgecolor='black', linewidth=1.5)

    # Añadir etiquetas con n
    for i, (barra, n) in enumerate(zip(barras, n_por_grupo)):
        altura = barra.get_height()
        ax.text(barra.get_x() + barra.get_width()/2., altura + errores.iloc[i],
               f'n={n}', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax.set_xlabel(columna_grupos, fontsize=12, fontweight='bold')
    ax.set_ylabel(f'{columna_valores} (Media ± ES)', fontsize=12, fontweight='bold')
    ax.set_title(f'Comparación de Medias: {columna_valores} por {columna_grupos}',
                fontsize=14, fontweight='bold')
    ax.set_xticks(range(len(medias)))
    ax.set_xticklabels(medias.index, rotation=45, ha='right')
    ax.grid(axis='y', alpha=0.3)


def crear_grafico_pastel(ax, datos, columna_grupos):
    """
    Crea un gráfico de pastel mostrando la distribución de grupos.

    Parámetros:
        ax: Eje de matplotlib donde dibujar
        datos: DataFrame con los datos
        columna_grupos: Nombre de la columna con grupos
    """
    # Contar frecuencias
    conteos = datos[columna_grupos].value_counts()

    # Crear gráfico de pastel
    colores = plt.cm.Set3(np.linspace(0, 1, len(conteos)))
    wedges, texts, autotexts = ax.pie(conteos, labels=conteos.index,
                                       autopct='%1.1f%%', startangle=90,
                                       colors=colores, explode=[0.05]*len(conteos))

    # Mejorar formato
    for text in texts:
        text.set_fontsize(11)
        text.set_fontweight('bold')

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(10)
        autotext.set_fontweight('bold')

    ax.set_title(f'Distribución de {columna_grupos}\n(N total = {len(datos)})',
                fontsize=14, fontweight='bold')


def crear_visualizaciones(datos, columna_valores, columna_grupos=None,
                          archivo_salida='graficos.png'):
    """
    Crea y guarda todas las visualizaciones.

    Parámetros:
        datos: DataFrame con los datos
        columna_valores: Nombre de la columna a visualizar
        columna_grupos: Nombre de la columna con grupos (opcional)
        archivo_salida: Nombre del archivo donde guardar los gráficos
    """
    # Limpiar datos
    valores = datos[columna_valores].dropna()

    # Configurar estilo
    sns.set_style("whitegrid")
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['font.family'] = 'sans-serif'

    # Determinar layout según si hay grupos o no
    if columna_grupos:
        # Con grupos: 4 gráficos (2x2)
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle(f'Análisis de {columna_valores}', fontsize=16, fontweight='bold', y=0.995)

        # 1. Histograma
        crear_histograma(axes[0, 0], valores, columna_valores)

        # 2. Boxplot por grupos
        crear_boxplot(axes[0, 1], datos, columna_valores, columna_grupos)

        # 3. Barras con medias
        crear_barras_medias(axes[1, 0], datos, columna_valores, columna_grupos)

        # 4. Gráfico de pastel
        crear_grafico_pastel(axes[1, 1], datos, columna_grupos)

    else:
        # Sin grupos: 2 gráficos (1x2)
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        fig.suptitle(f'Análisis de {columna_valores}', fontsize=16, fontweight='bold', y=0.98)

        # 1. Histograma
        crear_histograma(axes[0], valores, columna_valores)

        # 2. Boxplot
        crear_boxplot(axes[1], datos, columna_valores)

    # Ajustar espaciado
    plt.tight_layout()

    # Guardar figura
    plt.savefig(archivo_salida, dpi=300, bbox_inches='tight')
    print(f"\n💾 Gráficos guardados en: {archivo_salida}")

    # Mostrar figura (comentar esta línea si se ejecuta en servidor sin display)
    try:
        plt.show()
    except:
        pass  # Si no hay display, simplemente no mostramos


def imprimir_resumen(datos, columna_valores, columna_grupos=None):
    """
    Imprime un resumen de los datos a visualizar.

    Parámetros:
        datos: DataFrame con los datos
        columna_valores: Nombre de la columna con valores
        columna_grupos: Nombre de la columna con grupos (opcional)
    """
    valores = datos[columna_valores].dropna()

    print("\n" + "=" * 70)
    print("RESUMEN DE DATOS")
    print("=" * 70)
    print(f"Variable: {columna_valores}")
    print(f"N total: {len(valores)}")
    print(f"Media: {valores.mean():.2f}")
    print(f"Desviación estándar: {valores.std():.2f}")
    print(f"Mínimo: {valores.min():.2f}")
    print(f"Máximo: {valores.max():.2f}")

    if columna_grupos:
        print(f"\nGrupos en '{columna_grupos}':")
        for grupo, conteo in datos[columna_grupos].value_counts().items():
            print(f"  - {grupo}: {conteo} observaciones")

    print("=" * 70)


def main():
    """Función principal del script."""

    # Verificar argumentos
    if len(sys.argv) < 3:
        print("\n❌ Error: Argumentos insuficientes\n")
        print("Uso:")
        print("  python visualizar_datos.py <archivo_datos> <columna> [columna_grupos] [archivo_salida]\n")
        print("Ejemplos:")
        print("  python visualizar_datos.py datos.xlsx FEV1")
        print("  python visualizar_datos.py datos.xlsx FEV1 Fumador")
        print("  python visualizar_datos.py datos.xlsx FEV1 Fumador mis_graficos.png\n")
        sys.exit(1)

    # Obtener argumentos
    archivo = sys.argv[1]
    columna_valores = sys.argv[2]
    columna_grupos = sys.argv[3] if len(sys.argv) > 3 and not sys.argv[3].endswith('.png') else None
    archivo_salida = sys.argv[4] if len(sys.argv) > 4 else (sys.argv[3] if len(sys.argv) > 3 and sys.argv[3].endswith('.png') else 'graficos.png')

    print("\n" + "=" * 70)
    print("VISUALIZACIÓN DE DATOS MÉDICOS")
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

    # Imprimir resumen
    imprimir_resumen(datos, columna_valores, columna_grupos)

    # Crear visualizaciones
    print(f"\n📊 Generando visualizaciones...")
    crear_visualizaciones(datos, columna_valores, columna_grupos, archivo_salida)

    print("\n" + "=" * 70)
    print("✅ VISUALIZACIÓN COMPLETADA")
    print("=" * 70)
    print()


if __name__ == '__main__':
    main()
