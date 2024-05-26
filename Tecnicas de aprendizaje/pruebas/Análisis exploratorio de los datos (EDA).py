import numpy as np
import pandas as pd
hourData = pd.read_csv('hour.csv')
hourData.head()

import seaborn as sns # analisis estadistico
import matplotlib as mpl # matrices
import matplotlib.pyplot as plt # grafica o ploteo de la información

# Preparamos una figura de m x n
mpl.rc('font', size=14)
mpl.rc('axes', titlesize=15)
figure, axes = plt.subplots(nrows=3, ncols=2) # M 3rows 2columns
figure.set_size_inches(10, 9) # Tamaño total de la figura

# Distribución de alquileres según las features: season, month, day, hour, workingday

sns.barplot(x='yr', y='cnt', data=hourData, ax=axes[0, 0])
sns.barplot(x='mnth', y='cnt', data=hourData, ax=axes[0, 1])
sns.barplot(x='workingday', y='cnt', data=hourData, ax=axes[1, 0])
sns.barplot(x='hr', y='cnt', data=hourData, ax=axes[1, 1])
sns.barplot(x='season', y='cnt', data=hourData, ax=axes[2,0])

# Titulos
axes[0, 0].set(title='Alquileres year')
axes[0, 1].set(title='Alquileres month')
axes[1, 0].set(title='Alquileres workingday')
axes[1, 1].set(title='Alquileres hour')
axes[2, 0].set(title='Alquileres season')
# axes[2, 1].set(title='Alquileres by second')

# Rotamos 90 grados las etiquetas del eje x de la fila 1
axes[1, 0].tick_params(axis='x', labelrotation=90)
axes[1, 1].tick_params(axis='x', labelrotation=90)

#se reemplazan los faltantes con la media
media_CO = df['CO(GT)'].mean()
df_faltanCO=df
df_faltanCO['CO(GT)'] = df_faltanCO['CO(GT)'].fillna(media_CO)
media_PT08S1 = df['PT08.S1(CO)'].mean()
df_faltanPT08S1=df
df_faltanPT08S1['PT08.S1(CO)'] = df_faltanPT08S1['PT08.S1(CO)'].fillna(media_CO)
media_NMHC = df['NMHC(GT)'].mean()
df_faltanNMHC=df
df_faltanNMHC['NMHC(GT)'] = df_faltanNMHC['NMHC(GT)'].fillna(media_CO)
media_C6H6 = df['C6H6(GT)'].mean()
df_faltanC6H6=df
df_faltanC6H6['C6H6(GT)'] = df_faltanC6H6['C6H6(GT)'].fillna(media_CO)
media_PT08S2 = df['PT08.S2(NMHC)'].mean()
df_faltanPT08S2=df
df_faltanPT08S2['PT08.S2(NMHC)'] = df_faltanPT08S2['PT08.S2(NMHC)'].fillna(media_CO)
media_NOx = df['NOx(GT)'].mean()
df_faltanNOx=df
df_faltanNOx['NOx(GT)'] = df_faltanNOx['NOx(GT)'].fillna(media_CO)
media_PT08S3 = df['PT08.S3(NOx)'].mean()
df_faltanPT08S3=df
df_faltanPT08S3['PT08.S3(NOx)'] = df_faltanPT08S3['PT08.S3(NOx)'].fillna(media_CO)
media_NO2 = df['NO2(GT)'].mean()
df_faltanNO2=df
df_faltanNO2['NO2(GT)'] = df_faltanNO2['NO2(GT)'].fillna(media_CO)
media_PT08S4 = df['PT08.S4(NO2)'].mean()
df_faltanPT08S4=df
df_faltanPT08S4['PT08.S4(NO2)'] = df_faltanPT08S4['PT08.S4(NO2)'].fillna(media_CO)
media_PT08S5 = df['PT08.S5(O3)'].mean()
df_faltanPT08S5=df
df_faltanPT08S5['PT08.S5(O3)'] = df_faltanPT08S5['PT08.S5(O3)'].fillna(media_CO)
media_T = df['T'].mean()
df_faltanT=df
df_faltanT['T'] = df_faltanT['T'].fillna(media_CO)
media_RH = df['RH'].mean()
df_faltanRH=df
df_faltanRH['RH'] = df_faltanRH['RH'].fillna(media_CO)
media_AH = df['AH'].mean()
df_faltanAH=df
df_faltanAH['AH'] = df_faltanAH['AH'].fillna(media_CO)
print(df_faltan)