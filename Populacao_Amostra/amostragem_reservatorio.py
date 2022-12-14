import pandas as pd
import random

dataset = pd.read_csv("census.csv")

stream = []
for i in range(len(dataset)):
    stream.append(i)

print(stream)


def amostragem_reservatorio(dataset, amostras):
    stream = []
    for i in range(len(dataset)):
        stream.append(i)

    i = 0
    tamanho = len(dataset)

    reservatorio = [0] * amostras
    for i in range(amostras):
        reservatorio[i] = stream[i]

    while i < tamanho:
        j=random.randrange(i + 1)
        if j < amostras:
            reservatorio[j] = stream[i]
        i += 1

    return dataset.iloc[reservatorio]

df_amostragem_reservatorio = amostragem_reservatorio(dataset, 100)

df_amostragem_reservatorio.shape