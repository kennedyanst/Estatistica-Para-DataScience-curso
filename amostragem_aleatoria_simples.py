import pandas as pd
import numpy as np

dataset = pd.read_csv("census.csv")
dataset.head()

dataset.shape

# Amostragem aleatória simples.
df_amostra_ale_simples = dataset.sample(n = 32561) # Pode misturar os dados e criar um novo dataset com a mesma quantidade de dados porém com a organização misturada. 

# Usar o random_state = "n", para retornar uma resultado padrão

df_amostra_ale_simples

def amostragem_aleatoria_simples(dataset, amostras):
    return dataset.sample(n = amostras, random_state=1)

df = amostragem_aleatoria_simples(dataset, 1000)

df