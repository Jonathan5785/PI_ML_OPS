# PI_ML_OPS

¡Bienvenidos a mi primer proyecto individual de la etapa de labs! 

El siguiente trabajo consiste en realizar un Sistema de Recomendación de Películas situándome en el rol de un MLOps Engineer.


## Objectivos del proyecto
- Realizar la ingesta de datos desde diversos datasets.
- Hacer las transformaciones necesarias y unificar el dataset.
- Llevar a cabo el desarrollo de la API a través de FastApi.
- Ejecutar el deployment de la API en Deta.
- Efectuar el Análisis Exploratorio de Datos (EDA) a los datasets.
- Realizar el modelo de machine learning y realizar una interfaz gráfica con la librería Streamlit


## Fuente de datos
Para realizar este trabajo se utilizaron los archivos ubicados en la carpeta Datasets que corresponden a informacion sobre series y peliculas de las plataformas de Amazon, Disney, Hulu y Netflix.

   
Pasos a seguir:
1. Transformaciones:
Para ello utilicé Python , más especificamente las librería pandas. Generé el archivo [df_plataforma_score.pickle](https://drive.google.com/file/d/1lZs5Lq_lC2r7IlWQduG-XLJFZ1IbgvWJ/view?usp=share_link) que se usará para las 4 consultas solicitadas en la API.
Adicionalmente generé los archivos [df_plataforma.pickle](https://drive.google.com/file/d/1-4G3TWU10SqsvPhb1htB4VTk_9zkwNdr/view?usp=share_link) y [df_score.pickle](https://drive.google.com/file/d/1yQeB0sXkCT1utPB-tLiIlg-SrFD6wfXT/view?usp=share_link) que son los que usaré en el EDA.

2. Desarrollo API:
Para ello utilicé un entorno virtual donde instalé las librerías fastapi, uvicorn y pandas. Luego desarrollé la API con FastApi, dicho código se encuentra dentro del archivo [main.py](main.py).

- get_max_duration: Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
- get_score_count: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.
- get_count_platform: Cantidad de películas por plataforma con filtro de PLATAFORMA.
- get_actor: Actor que más se repite según plataforma y año.
Durante la etapa de desarrollo revisé el funcionamiento integral de la API y sus consultas de manera local desde la terminal con el comando uvicorn main:app --reload en mi localhost.



3. Deployment en Deta:
Una vez comprobado el funcionamiento de la API con todas las consultas, se realiza el deployment en Deta Space.
Como primer paso se debe crear una cuenta, luego crear el archivo requirements.txt el cual contiene las librerías usadas en main.py.

A continuación comparto los datos de mi deployment en Deta Space:

- Usuario Deta Space: jonathan5785
- Nombre del Proyecto: Proyecto1
- [Deployment de mi API en Deta Space](https://deta.space/discovery/r/cwm6zqxu6a6htyxj)



4. Análisis exploratorio de los datos (Exploratory Data Analysis-EDA): 
En esta etapa me encargué de analizar los campos que servirían para el modelo de machine learning. Obteniendo los siguientes archivo: [df1](https://drive.google.com/file/d/1QN_hAihOW4SPJQNk7zARyUKzEQXSqP4_/view?usp=share_link) y [df_title](https://drive.google.com/file/d/1y5LpP22NdQBtsVHRVhMyFIAchdG5eagE/view?usp=share_link)

5. Sistema de Recomendación: 
Finalmente el modelo de machine learning lo realizé con los archivos generado en el paso anterior (EDA) y usando una interfaz gráfica de usuario con la librería Streamlit.
[![gui-streamlit.jpg](https://i.postimg.cc/D0QC4NxG/gui-streamlit.jpg)](https://postimg.cc/D4ZQtxkf)

### [ENLACE VIDEO](https://drive.google.com/file/d/1D742jcTdNO0HnhVyVg_OPY5T6uYPGNKg/view)



