#Nueva columna 
import pandas as pd
import numpy as np

df=pd.read_csv("StudentsPerformance.csv")

a=np.random.uniform(1,100,size=1000) #crear numeros decimales 

df["columna de arreglo"] =a

print(df)