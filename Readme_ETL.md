# Proyecto Individual #1

Descripción breve del proyecto.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Proceso de Limpieza de Datos](#requisitos)
- [Diccionario de Películas](#diccionario)

## Descripción

El objetivo de este proyecto individual es realizar la limpieza y preparación de datos del conjunto de datos `dataset_movies.csv`, con el propósito de construir una API utilizando FastAPI para realizar consultas de películas. La API permitirá a los usuarios buscar películas por diferentes criterios y obtener información detallada sobre las mismas.

## Proceso de Limpieza de Datos

El proceso de limpieza de datos consistirá en varias etapas:

1. **Carga de Datos** : Se realizará la carga del conjunto de datos `dataset_movies.csv` en un DataFrame utilizando la biblioteca Pandas.
2. **Eliminación de Columnas Innecesarias** : Se identificarán las columnas que no son relevantes para el objetivo de la API y se eliminarán del DataFrame.
3. **Limpieza de Datos Faltantes** : Se realizará una exploración del DataFrame para identificar columnas con datos faltantes. Se aplicarán técnicas de imputación o eliminación de filas/columnas dependiendo del caso.
4. **Extracción de Datos de Columnas Anidadas** : Se analizarán las columnas que contienen datos anidados, como por ejemplo `production_companies` y `production_countries`. Se extraerán los datos relevantes de estas columnas y se crearán columnas separadas en el DataFrame.
5. **Transformación de Datos** : Se aplicarán transformaciones necesarias a las columnas, como por ejemplo convertir formatos de fechas, eliminar caracteres especiales, normalizar textos, etc.
6. **Validación y Control de Calidad** : Se realizará una validación exhaustiva de los datos limpios para asegurarse de que cumplan con los requisitos de la API y no contengan errores o inconsistencias.

## Diccionarios

A continuación se muestra un diccionario que describe cada columna en el conjunto de datos del archivo datasets_final.csv:

```python
column_description = {
    'id': 'ID de la película',
    'title': 'Título de la película',
    'overview': 'Descripción de la película',
    'popularity': 'Popularidad de la película',
    'vote_average': 'Promedio de votos de la película',
    'vote_count': 'Número de votos de la película',
    'status': 'Estado de la película',
    'original_language': 'Idioma original de la película',
    'runtime': 'Duración de la película en minutos',
    'budget': 'Presupuesto de la película',
    'revenue': 'Ingresos generados por la película',
    'tagline': 'Lema de la película',
    'id_btc': 'ID de la película en BTC',
    'name_btc': 'Nombre de la película en BTC',
    'poster_btc': 'URL del póster de la película en BTC',
    'backdrop_btc': 'URL del fondo de la película en BTC',
    'iso_639_1': 'Código ISO 639-1 del idioma',
    'language_name': 'Nombre del idioma',
    'release_year': 'Año de lanzamiento de la película',
    'return': 'Relación entre ingresos y presupuesto de la película',
    'companies_id': 'ID de las compañías de producción',
    'companies_name': 'Nombres de las compañías de producción',
    'countries_iso': 'Códigos ISO de los países de producción',
    'countries_name': 'Nombres de los países de producción',
    'release_date': 'Fecha de lanzamiento de la película',
    'month_time': 'Mes en el que se creó la película',
    'day_time': 'Día en el que se creó la película'
}

```

A continuación se muestra un diccionario que describe cada columna en el conjunto de datos del archivo ML_data.csv:

```python
column_description = {
    'id': 'ID de la película',
    'title': 'Título de la película',
    'genero': 'Género de la película',
    'popularity': 'Popularidad de la película'
}

```

A continuación se muestra un diccionario que describe cada columna en el conjunto de datos del archivo cast_data.csv:

```python
column_description = {
    'id': 'ID de la película',
    'cast': 'Elenco de la película en formato JSON'
}
```

A continuación se muestra un diccionario que describe cada columna en el conjunto de datos del archivo crew_data.csv:

```python
column_description = {
    'id': 'ID de la película',
    'crew_credit_id': 'ID de crédito del equipo de producción',
    'crew_department': 'Departamento del equipo de producción',
    'crew_gender': 'Género del equipo de producción',
    'crew_id': 'ID del miembro del equipo de producción',
    'crew_job': 'Trabajo del miembro del equipo de producción',
    'crew_name': 'Nombre del miembro del equipo de producción',
    'crew_profile_path': 'Ruta del perfil del miembro del equipo de producción'
}

```

A continuación se muestra un diccionario que describe cada columna en el conjunto de datos del archivo movie_genres.csv:

```python
column_description = {
    'id': 'ID de la película',
    'id_genres': 'ID de géneros asociados a la película',
    'genero': 'Géneros de la película'
}

```
