# Diccionario.py
import pandas as pd

provincia =["Cordoba", "Mendoza", "Formosa","Jujuy"]
poblacion =[1000, 5000, 4000, 500]

diccionario={"Provincia":provincia,"Poblacion":poblacion}

df= pd.DataFrame(diccionario)

print(df)

# lista de StudentsPerformarce
 import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")

print(df)

print(df.head())   (mostrar las primeras 5 )

print(df.tail())   (muestra lass ultima 5 )

print(df.to_string()) #(muestra todo)

print(df.shape) #(cantidad de filas y columnas) 

print(df.dtypes) #(muestra los tipos de datos de cada columna)

#print(df.info()) #(muestra datos sin completar, para limpiar los datos non-null)

#print(df.describe()) #(da datos estadisticos de cada tabla)

#print(df["gender"].head()) #(muestra los generos)

#print(df[["gender","lunch"]].head()) #(muestra de columnas de la lista)

# actividad 1 

import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")

print(df[["gender","math score"]].shape)

print(df.head(40))

print(df.tail(15))

print(df.mean())

print(df.dtypes)

# actividad 2
import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")

print(df.iloc[:, -3:])

print (df.head(100))

print (df.mean)

print (df.min)

# Actividad 3
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[45,5,67,86,65]

plt.plot(x,y)

plt.xlabel("eje X")

plt.xlabel("eje Y")

plt.title("grafico de ejemplo ")

plt.show()

print (df.max)

print (f'Cantidad: "{df.shape}')

print (df.to_string())

# actiidad 4
import matplotlib.pyplot as plt

label=["a","b","c","d"]

datos=[25,35,40,45]

colores=["gold","lightcoral","lightskyblue","lightgreen"]

plt.pie(datos,labels=label,colors=colores,autopct="%1.1f%%",startangle=140)

plt.axis("equal")

plt.show()
# actividad 5 "nueva columna"

import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")

df["nueva columna"]= 70

print(df)
# actividad 5 #como areglar

import pandas as pd

import numpy as np

df=pd.read_csv("StudentsPerformance.csv")

a=np.arange(0,1000)

df["columna de arreglo"] =a

print(df)
# actividad 6

import pandas as pd

import numpy as np

df=pd.read_csv("StudentsPerformance.csv")

a=np.random.randint(1,100,size=1000) #crear una columna con numeros aletorios

df["columna de arreglo"] =a

print(df)

# ACTIVIDAD7 
import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")

print(df["math score"].sum) #suma

print(df["math score"].count) #resta

print(df["math score"].median) #la media

print(df["math score"].std) #estandar

print(df["math score"].max) #maximo

print(df["math score"].min) #minimo

print(df.head)

 # actividad8
import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")

print(df["math score"]+df["reading score"]+df["writing score"]) 

#print(df.head)

# actividad 9

import pandas as pd
import numpy as np

df=pd.read_csv("StudentsPerformance")

df.sort_values("math score")

df.sort_values(["math score"], ascending=False)

# Actividad10
obtener a los 5 usuarios mas viejos de Alemania 

import pandas as pd

df=pd.read_csv("users (1).csv")

usuariosAlemanes=df[df["pais"] == 'Germany']

edadmedia=usuariosAlemanes["edad"].mean

print("la edad media es",edadmedia)

# Actividad11
Obtenertodods los usuarios entre las edades 40 y 50 años  

import pandas as pd

df=pd.read_csv("users (1).csv")

print(df[df["edad"].between(40,50)])

# Actividad12
obtener los nombres de todos los usuarios mayores a 30 años del pais de Canada

import pandas as pd

df=pd.read_csv("users (1).csv")

usuariosdecanada=df[df["pais"] == 'Canada']
         
print(df[df["edad"]>30], usuariosdecanada)

# actividad13

import pandas as pd

df=pd.read_csv("users (1).csv")

usuariosdecanada=df[df["pais"] == 'Canada']

usuariosdealemania=df[df["pais"] == 'Germany']
            
usuariosdefrancia=df[df["pais"] == 'France']
         
print(df[df["edad"]>30], usuariosdecanada, usuariosdealemania, usuariosdefrancia)

# actividad14

import pandas as pd

df = pd.read_csv('users.csv')

France_jovenes = df[df['pais'] == 'France'].sort_values(by='edad').head(5)

# 5 más jóvenes de Australia
Australia_jovenes = df[df['pais'] == 'Australia'].sort_values(by='edad').head(5)

print("5 usuarios más jóvenes de Francia:")
print(France_jovenes)

print("\n5 usuarios más jóvenes de Australia:")
print(Australia_jovenes)

# actividad15

#actividad15
#obtener el nombre de todos los usuarios mayores a 50años 
#dividir entre masculino y femenino
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('users.csv')

mayores_50 = df[df['edad'] > 50]

masculinos = mayores_50[mayores_50['genero'] == 'male']['nombre']
femeninos = mayores_50[mayores_50['genero'] == 'female']['nombre']
 
print("Masculinos mayores de 50:")
print(masculinos)

print("\nFemeninos mayores de 50:")
print(femeninos)

mayores_50.plot(kind="bar", color=colores)
plt.title('Promedio de usuarios mayores de 30')
plt.xlabel('edad')
plt.ylabel("Masculino","femenino")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# actividad16
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('users.csv')

# Filtrar usuarios mayores de 50 años
mayores_50 = df[df['edad'] > 50]

# Contar cuántos hay por género
conteo_genero = mayores_50['genero'].value_counts()

# Mostrar gráfico de barras
conteo_genero.plot(kind='bar', color=['skyblue', 'lightcoral'])

plt.title('Usuarios mayores de 50 años por género')
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# actividad17

#actividad15
#obtener el nombre de todos los usuarios mayores a 50años 
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv('users.csv')

# Normalizar nombres de columnas
df.columns = df.columns.str.lower()

# Limpiar valores de texto
df['pais'] = df['pais'].str.lower()
df['genero'] = df['genero'].str.lower()

# Filtrar usuarios del Reino Unido
uk_users = df[df['pais'].isin(['uk', 'united kingdom'])]

# Obtener los 20 más viejos
top_20_uk = uk_users.sort_values(by='edad', ascending=False).head(20)

# Dividir por género
conteo_genero = top_20_uk['genero'].value_counts()

# Mostrar usuarios divididos
print("Usuarios masculinos:")
print(top_20_uk[top_20_uk['genero'] == 'masculino'][['nombre', 'edad']])

print("\nUsuarios femeninos:")
print(top_20_uk[top_20_uk['genero'] == 'femenino'][['nombre', 'edad']])

# Crear gráfico de pastel
colors = ['skyblue', 'lightcoral']  # Puedes agregar más colores si hay más géneros
conteo_genero.plot(kind='pie', autopct='%1.1f%%', colors=colors, startangle=90)

plt.title('Distribución por género - Top 20 usuarios más viejos del Reino Unido')
plt.ylabel('')  # Ocultar etiqueta del eje Y
plt.tight_layout()
plt.show()






