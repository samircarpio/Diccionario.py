import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")

print(df[["gender","math score"]].shape)

print(df.head(40))

print(df.tail(15))

print(df.mean())

print(df.dtypes)


