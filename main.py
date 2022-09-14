#Importacion de librerias
import matplotlib.pyplot as plt
import pandas as pd

#Ajustar el formato de matplotlib
plt.style.use('seaborn-whitegrid')

#Convertimos el archivo csv en DataFrame y llenamos los espacios nulos con 0
dfClima = pd.read_csv('asset/AirPollution.csv', index_col=None)
dfClima = dfClima.fillna(0)
dfClimaBogota = dfClima.loc[dfClima['City']=='Bogota']
#dfClimaMedellin = dfClima.loc[dfClima['City']=='Medellin']

print(dfClimaBogota.iloc[0])
print(dfClimaBogota.iloc[1])
print(dfClimaBogota.iloc[2])
print(dfClimaBogota.iloc[3])

dfClimaBogota.plot(x='Year',y='PM2.5 (μg/m3)')
plt.title('Contaminación en Bogotá')
plt.xlabel('Años')
plt.ylabel('Materia particulada PM2.5')
plt.show()
