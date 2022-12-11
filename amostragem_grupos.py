import pandas as pd
import numpy as np
import random

dataset = pd.read_csv("census.csv")

len(dataset) / 10

grupos = []
id_grupo = 0
contagem = 0

for _ in dataset.iterrows():
    grupos.append(id_grupo)
    contagem += 1
    if contagem > 3256:
        contagem = 0
        id_grupo += 1


np.unique(grupos, return_counts=True)
np.shape(grupos)
np.shape(grupos), dataset.shape

dataset["grupo"] = grupos
dataset.tail()

df_agrupamento = dataset[dataset["grupo"] ==7]

df_agrupamento.shape

df_agrupamento["grupo"].value_counts()

# Criando a função para a amostragem por grupos
def amostragem_agrupamento(dataset, numero_grupos):
    intervalo = len(dataset) / numero_grupos

    grupos = []
    id_grupo = 0
    contagem = 0
    for _ in dataset.iterrows():
        grupos.append(id_grupo)
        contagem > intervalo
        if contagem > 3256:
            contagem = 0
            id_grupo += 1

    dataset["grupo"] = grupos
    random.seed(1)
    grupo_selecionado = random.randint(0, numero_grupos)
    return dataset[dataset["grupo"] == grupo_selecionado]

df_amostra_agrupamento = amostragem_agrupamento(dataset, 100)

df_amostra_agrupamento.head()
df_amostra_agrupamento.shape, df_amostra_agrupamento["grupo"].value_counts()