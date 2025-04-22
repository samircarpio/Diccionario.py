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



