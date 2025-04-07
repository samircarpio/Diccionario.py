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
