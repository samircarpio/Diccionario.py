#obtener la cantidad de personas que hay en españa y cuantos son femenino y masculinos (hacer un grafico)
import pandas as pd
import matplotlib.pyplot as plt

# Leer el CSV
df = pd.read_csv('users.csv')

# Filtrar usuarios de España
españoles = df[df['pais'] == 'Spain']

# Contar total y por género
total = len(españoles)
conteo_genero = españoles['genero'].value_counts()

# Crear gráfico
plt.figure(figsize=(6, 4))
conteo_genero.plot(kind='bar', color=['skyblue', 'lightcoral'])
plt.title('Cantidad de personas por género en España')
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


