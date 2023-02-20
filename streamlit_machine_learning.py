import streamlit as st
import pandas as pd
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import train_test_split
import numpy as np



header = st.container()
ingreso_datos = st.container()
model_training = st.container()
recomendacion = st.container()

with header:
    st.title('Bienvenido a mi Proyecto de Data Science')
    st.text('''Modelo de machine learning para armar un sistema de recomendación de películas.''')
    


df1 = pd.read_pickle('../MLOpsReviews/fichero/df1.pickle')
df_title = pd.read_pickle('../MLOpsReviews/fichero/df_title.pickle')


with ingreso_datos:


    st.header('Ingreso de datos (INPUT)')
    usuarios = list(df1['User'].unique())
    user = int(st.text_input('Ingrese Usuario ID',usuarios[0]))

    
    if user in usuarios:
        st.success('El usuario es correcto')
    else:
        st.error('El usuario no es correcto')

    
    movies = list(df_title['Name'].unique())
    movie = st.selectbox('Ingrese pelicula',movies,index=0)


    
with model_training:

    reader = Reader()
    N_filas = 100000 # Limitamos el dataset a N_filas
    data = Dataset.load_from_df(df1[['User', 'movie_id', 'Rating']][:N_filas], reader)

    # Separamos nuestros datos
    trainset, testset = train_test_split(data, test_size=.25)

    # Usaremos un modelo de Singular Value Decomposition
    from surprise import SVD
    model = SVD()

    # Entrenamos el modelo
    model.fit(trainset)

    # Predecimos
    predictions = model.test(testset)

    # Tomaremos al usuario para hacerle una recomendación
    usuario = user
    rating = 4   # Tomamos películas a las que haya calificado con 4 o 5 estrellas
    df_user = df1[(df1['User'] == usuario) & (df1['Rating'] >= rating)]
    df_user = df_user.reset_index(drop=True)
    df_user['Name'] = df_title['Name'].loc[df_user.movie_id].values

    # Hago una copia de los títulos
    recomendaciones_usuario = df_title.iloc[:].copy()

    # Debemos extraer las películas que ya ha visto
    usuario_vistas = df1[df1['User'] == usuario]
    recomendaciones_usuario.drop(usuario_vistas.movie_id, inplace = True)
    recomendaciones_usuario = recomendaciones_usuario.reset_index()

    # Recomendamos
    recomendaciones_usuario['Estimate_Score'] = recomendaciones_usuario['Movie_Id'].apply(lambda x: model.predict(usuario, x).est)




with recomendacion:
    st.header('Recomendación (OUTPUT)')
    # Une todas las peliculas (vistas y no vistas)
    usuario_vistas.drop(columns='User', inplace=True)
    usuario_vistas['Name'] = df_title.loc[usuario_vistas['movie_id']].values
    usuario_vistas = usuario_vistas.iloc[:,[0,2,1]]
    usuario_vistas.rename(columns={'movie_id':'Movie_Id', 'Rating':'Estimate_Score'},inplace=True)
    todas_las_peliculas = pd.concat([usuario_vistas,recomendaciones_usuario],ignore_index=True)

    
    # Muestra la recomendación
    if user in usuarios:

        # GENERA UNA SCORE DE REFERENCIA DINAMICO POR USUARIO (data_greater_than_bin5)
        data = np.array(recomendaciones_usuario.Estimate_Score)
        bins = pd.cut(data, bins=7)
        data_greater_than_bin5 = data[bins.codes >= 4]
        if todas_las_peliculas[todas_las_peliculas['Name'] == movie].reset_index().loc[0,'Estimate_Score']>=data_greater_than_bin5.min():
            st.write('Título Recomendado')
        else:
            st.write('Título NO Recomendado')
        

    
        







