import pandas as pd #importa la libreria pandas y la llama pd
import csv
import seaborn as sb # estadistica para graficar matlab
import matplotlib.pyplot as plt #graficar
import warnings
with warnings.catch_warnings():
    warnings.simplefilter(action='ignore', category=FutureWarning)
dataset = pd.read_csv('train.csv') #usa la libreria pandas con la funcion de lectura cvs para leer el archivo y ponerlo en la variable
#print(dataset.head())# imprime la variable dataset con la funcion de mostrar cabecera del archivo primeras lineas

#print(dataset.shape)# imprime la variable dataset pcon la funcion de mostrar cantidad de filas y columnas
#print(dataset.columns)# imprime columnas 
#print(dataset.info) # información general, se puede verificar si tiene nulls nulos - imprime toda la información de la variable
#print(dataset.describe) #imprime media, estandar, rango, mediana y cuartiles
#dataset['dteday'].value_counts() #toma por categoria e imprime cuantos tiene esa categoria
#print(hourData['cnt'].describe()) # imprime solo la columna 'cnt' y sus valores asociados


#sb.countplot(dataset, x='Survived')# grafica la columna seleccionada
#plt.show()

#sb.countplot(dataset, x='Pclass')
#plt.show()

#sb.countplot(dataset, x='Age')
#plt.show()
#pd.option_context('mode.use_inf_as_na', True)
#sb.histplot(dataset, x='Age', bins=20)

#print(dataset['Age'].value_counts()) # imprime valores de edades por grupos

#print(dataset.describe()) # medidas de dispersion - estadisticas de cada variable - cuartiles 
#print(sb.boxplot(x=dataset["Age"])) # graficos de caja para ver valores atipicos
#print(sb.boxplot(x=dataset["Age"]))

#**DUPLICIDAD Y VALORES FALTANTES****

#nos permite ver valores nulos - falsos y verdaderos a nivel general
#df.isnull()
#df.isnull().sum() # suma dos veces por columnas y luego por todas las columnas
#df.isnull().sum() # suma 1 sola vez para ver solo por columna


