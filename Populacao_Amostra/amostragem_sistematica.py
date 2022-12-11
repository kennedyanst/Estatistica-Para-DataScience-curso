import pandas as pd
import numpy as np
import random

dataset = pd.read_csv("census.csv")
dataset.head(5)

dataset.shape

# Implementando a amostragem sistematica com NumPy

random.seed(1)
random.randint(0, 325) # Pegando uma amostra de 1% da base

np.arange(68, len(dataset), step = 325)

# Criando a função para retornar as linhas da amostragem sistematica 
def amostragem_sistematica(dataset, amostras):
    intervalo = len(dataset) // amostras
    inicio = random.randint(0, intervalo)
    indices = np.arange(inicio, len(dataset), step = intervalo)
    amostra_sistematica = dataset.iloc[indices]
    return amostra_sistematica

amostragem_sistematica_base = amostragem_sistematica(dataset, 100)
amostragem_sistematica_base.head()