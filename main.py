
from fastapi import FastAPI
import pandas as pd

df = pd.read_pickle('../MLOpsReviews/fichero/df_plataforma_score.pickle')


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World"}


@app.post("/max_duration/{year}/{platform}/{duration_type}")
async def get_max_duration(year:int, platform:str, duration_type:str):
    df_sorted=df[(df['release_year']==2013) & (df['show_id'].str.slice(0,1) == 'n') & (df['duration_type']=='min')].sort_values('duration_int', ascending=False)
    pelicula_duracion_maxima=df_sorted.reset_index().loc[0]['title']
    return pelicula_duracion_maxima


@app.post("/score_count/{platform}/{scored}/{year}")
async def get_score_count(platform:str, scored:float, year:int):
    cant_peliculas = df[(df['show_id'].str.slice(0,1) == platform) & (df['release_year']==year) & (df['promedio']>scored)].shape[0]
    return cant_peliculas


@app.post("/count_platform/{platform}")
async def get_count_platform(platform:str):
    cant_pelis_por_plataforma = df[(df['show_id'].str.slice(0,1) == platform)].shape[0]
    return cant_pelis_por_plataforma


@app.post("/get_actor/{platform}/{year}")
async def get_actor(platform:str, year:int):
    var = df[(df['show_id'].str.slice(0,1) == platform) & (df['release_year']==year)]
    # Contar el número de ocurrencias de cada valor
    counts = var['cast'].str.split(',', expand=True).stack().str.strip().value_counts()
    # Obtener el valor con el recuento más alto
    most_common_value = counts.index[0] 
    return most_common_value
    


    

