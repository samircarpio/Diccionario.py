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

print (df.max)

print (f'Cantidad: "{df.shape}')

print (df.to_string())
