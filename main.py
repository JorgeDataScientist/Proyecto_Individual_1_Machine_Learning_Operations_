from fastapi import FastAPI
import pandas as pd
import zipfile

# uvicorn main:app --reload
# ----------------------------------------------------
app = FastAPI()
# ----------------------------------------------------

# Cargar los datasets
# ----------------------------------------------------
def extract_data_from_zip():
    """
    Extrae y carga los conjuntos de datos desde un archivo comprimido.
    
    Returns:
        datasets_df (DataFrame): Dataframe que contiene los datos finales.
        crew_df (DataFrame): Dataframe que contiene los datos de equipo de producción.
        cast_df (DataFrame): Dataframe que contiene los datos de reparto de películas.
        movie_genres_df (DataFrame): Dataframe que contiene los géneros de películas.
    """
    zip_file = 'data.zip'
    
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('data.zip')  # Descomprime los archivos en el directorio '../data/'
    
    datasets_df = pd.read_csv('datasets_final.csv')
    crew_df = pd.read_csv('crew_data.csv')
    cast_df = pd.read_csv('cast_data.csv')
    movie_genres_df = pd.read_csv('movie_genres.csv')
    
    return datasets_df, crew_df, cast_df, movie_genres_df
# ----------------------------------------------------

# Rutas para los endpoints
# ----------------------------------------------------
@app.get("/cantidad-filmaciones-mes/{mes}")
async def cantidad_filmaciones_mes_endpoint(mes: str):
    """
    Endpoint para obtener la cantidad de filmaciones de películas realizadas en un mes específico.
    
    Args:
        mes (str): Nombre del mes en formato de texto.
    
    Returns:
        dict: Diccionario con el mensaje que indica la cantidad de filmaciones en el mes consultado.
    """
    # Convertir el nombre del mes a minúsculas para realizar la comparación
    mes = mes.lower()

    # Extraer los DataFrames del archivo ZIP
    datasets_df, _, _, _ = extract_data_from_zip()

    # Filtrar el DataFrame para obtener las filas correspondientes al mes consultado
    filmaciones_mes = datasets_df[datasets_df['month_time'].str.lower() == mes]

    # Obtener la cantidad de películas estrenadas en el mes consultado
    cantidad_filmaciones = len(filmaciones_mes)

    mensaje = f"La cantidad de películas estrenadas en {mes.capitalize()} es: {cantidad_filmaciones}"
    return {"mensaje": mensaje}

# ----------------------------------------------------
@app.get("/cantidad-filmaciones-dia/{dia}")
async def cantidad_filmaciones_dia_endpoint(dia: str):
    """
    Endpoint para obtener la cantidad de filmaciones de películas realizadas en un día específico.
    
    Args:
        dia (str): Nombre del día en formato de texto.
    
    Returns:
        dict: Diccionario con el mensaje que indica la cantidad de filmaciones en el día consultado.
    """
    # Convertir el nombre del día a minúsculas para realizar la comparación
    dia = dia.lower()

    # Extraer los DataFrames del archivo ZIP
    datasets_df, _, _, _ = extract_data_from_zip()

    # Filtrar el DataFrame para obtener las filas correspondientes al día consultado
    filmaciones_dia = datasets_df[datasets_df['day_time'].str.lower() == dia]

    # Obtener la cantidad de películas estrenadas en el día consultado
    cantidad_filmaciones = len(filmaciones_dia)

    mensaje = f"La cantidad de películas estrenadas en {dia.capitalize()} es: {cantidad_filmaciones}"
    return {"mensaje": mensaje}

# ----------------------------------------------------
@app.get("/titulo-de-la-filmacion/{titulo}")
async def titulo_de_la_filmacion_endpoint(titulo: str):
    """
    Endpoint para obtener información de una filmación a partir de su título.
    
    Args:
        titulo (str): Título de la filmación en formato de texto.
    
    Returns:
        dict: Diccionario con el mensaje que contiene el título, año de estreno y score/popularidad de la filmación.
              En caso de no encontrar la filmación, se devuelve un mensaje de error.
    """
    # Convertir el título de la filmación a minúsculas para realizar la comparación
    titulo = titulo.lower()

    # Extraer los DataFrames del archivo ZIP
    datasets_df, _, _, _ = extract_data_from_zip()

    # Filtrar el DataFrame para obtener la fila correspondiente al título de la filmación
    filmacion = datasets_df[datasets_df['title'].str.lower() == titulo]

    if filmacion.empty:
        return {"mensaje": f"No se encontró la filmación con el título: {titulo}"}

    # Obtener el título, año de estreno y score de la filmación
    titulo_filmacion = filmacion['title'].iloc[0]
    año_estreno = filmacion['release_year'].iloc[0]
    score = round(filmacion['popularity'].iloc[0], 2)

    mensaje = f"La película '{titulo_filmacion}' fue estrenada en el año {año_estreno} con un score/popularidad de {score}"
    return {"mensaje": mensaje}

# ----------------------------------------------------
@app.get("/votos-valor-de-la-filmacion/{titulo}")
async def votos_valor_de_la_filmacion_endpoint(titulo: str):
    """
    Endpoint para obtener información sobre los votos y valoraciones de una filmación a partir de su título.
    
    Args:
        titulo (str): Título de la filmación en formato de texto.
    
    Returns:
        dict: Diccionario con el mensaje que contiene el título, año de estreno, cantidad de votos y promedio de votaciones de la filmación.
              En caso de no encontrar la filmación o no cumplir con la cantidad mínima de votos, se devuelve un mensaje de error.
    """
    # Convertir el título de la filmación a minúsculas para realizar la comparación
    titulo = titulo.lower()

    # Extraer los DataFrames del archivo ZIP
    datasets_df, _, _, _ = extract_data_from_zip()

    # Filtrar el DataFrame para obtener la fila correspondiente al título de la filmación
    filmacion = datasets_df[datasets_df['title'].str.lower() == titulo]

    if filmacion.empty:
        return {"mensaje": f"No se encontró la filmación con el título: {titulo}"}

    # Obtener el título, año de estreno, cantidad de votos y promedio de votaciones de la filmación
    titulo_filmacion = filmacion['title'].iloc[0]
    año_estreno = filmacion['release_year'].iloc[0]
    cantidad_votos = round(filmacion['vote_count'].iloc[0])
    promedio_votaciones = filmacion['vote_average'].iloc[0]

    if cantidad_votos < 2000:
        return {"mensaje": f"La filmación '{titulo_filmacion}' no cumple con la condición de tener al menos 2000 votos"}

    mensaje = f"La película '{titulo_filmacion}' fue estrenada en el año {año_estreno}. La misma cuenta con un total de {cantidad_votos} valoraciones, con un promedio de {promedio_votaciones}"

    return {"mensaje": mensaje}

# ----------------------------------------------------
@app.get("/nombre-actor/{nombre}")
def nombre_actor(nombre: str):
    """
    Endpoint para obtener información sobre un actor a partir de su nombre.
    
    Args:
        nombre (str): Nombre del actor en formato de texto.
    
    Returns:
        dict: Diccionario con el nombre del actor, la cantidad de películas en las que ha participado, el promedio de retorno monetario de las películas
              y una lista de diccionarios con los títulos y retornos monetarios de las películas en las que ha participado.
    """
    datasets_df, _, cast_df, _ = extract_data_from_zip()

    # Filtrar las filas en las que el actor aparece en la columna "cast"
    actor_movies = cast_df[cast_df['cast'].str.contains(nombre, case=False)]
    
    # Obtener los ID de las películas en las que el actor ha participado
    movie_ids = actor_movies['id'].tolist()
    
    # Filtrar el dataset "datasets_df" para obtener los nombres y retornos monetarios de las películas correspondientes
    movies = datasets_df[datasets_df['id'].isin(movie_ids)]
    
    # Obtener la cantidad de películas en las que el actor ha participado
    movie_count = len(movies)
    
    # Obtener el promedio de retorno monetario de las películas
    average_revenue = round(movies['revenue'].mean(), 2)

    
    # Crear una lista de diccionarios con los nombres y retornos monetarios de las películas
    movie_info = []
    for _, row in movies.iterrows():
        movie_info.append({
            "titulo": row['title'],
            "retorno_monetario": row['revenue']
        })
    
    return {
        "nombre_actor": nombre,
        "cantidad_peliculas": movie_count,
        "promedio_retorno_monetario": average_revenue,
        "peliculas": movie_info
    }

# ----------------------------------------------------
@app.get("/nombre-director/{nombre}")
def nombre_director(nombre: str):
    """
    Endpoint para obtener información sobre un director a partir de su nombre.
    
    Args:
        nombre (str): Nombre del director en formato de texto.
    
    Returns:
        dict: Diccionario con el nombre del director, las ganancias totales de las películas que ha dirigido y una lista de diccionarios
              con los ID, títulos, años, presupuestos, ingresos y relaciones de las películas dirigidas por el director.
    """
    datasets_df, crew_df, _, _ = extract_data_from_zip()

    # Filtrar las filas en las que el director aparece en la columna "crew_name" y "crew_job" contiene "Director"
    director_movies = crew_df[(crew_df['crew_name'].str.contains(nombre, case=False)) & (crew_df['crew_job'].str.contains("Director"))]
    
    # Obtener los ID de las películas en las que el director ha trabajado
    movie_ids = director_movies['id'].tolist()
    
    # Filtrar el dataset "datasets_df" para obtener los nombres, años, presupuestos, ingresos y relación de las películas correspondientes
    movies = datasets_df[datasets_df['id'].isin(movie_ids)]
    
    # Calcular las ganancias sumando todas las relaciones de las películas
    ganancias = round(movies['return'].sum(), 2)
    
    # Crear una lista de diccionarios con los ID, nombres, años, presupuestos, ingresos y relación de las películas
    movie_info = []
    for _, row in movies.iterrows():
        movie_info.append({
            "id": row['id'],
            "titulo": row['title'],
            "anio": row['release_year'],
            "presupuesto": row['budget'],
            "ingresos": row['revenue'],
            "relacion": row['return']
        })
    
    return {
        "nombre_director": nombre,
        "ganancias": ganancias,
        "peliculas": movie_info
    }







# ----------------------------------------------------
# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
