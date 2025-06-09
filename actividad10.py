import pandas as pd

df=pd.read_csv("users (1).csv")

usuariosdecanada=df[df["pais"] == 'Canada']

usuariosdealemania=df[df["pais"] == 'Germany']
            
usuariosdefrancia=df[df["pais"] == 'France']
         
print(df[df["edad"]>30], usuariosdecanada, usuariosdealemania, usuariosdefrancia)
