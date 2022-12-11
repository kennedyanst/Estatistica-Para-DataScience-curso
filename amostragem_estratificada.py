import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

dataset = pd.read_csv("census.csv")

dataset["income"].value_counts()

split = StratifiedShuffleSplit(test_size=0.1) # Criando uma maostra de 10% 
for x,y in split.split(dataset, dataset["income"]):
    df_x = dataset.iloc[x]
    df_y = dataset.iloc[y]

df_x.shape, df_y.shape

df_y.head(5)

df_y["income"].value_counts()

784 / len(df_y)

def amostragem_estratificada(dataset, percentual):
    split = StratifiedShuffleSplit(test_size=percentual, random_state=1) # Criando uma maostra de 10% 
    for _,y in split.split(dataset, dataset["income"]):
        df_y = dataset.iloc[y]
    return df_y

df_amostra_estratificada = amostragem_estratificada(dataset, 100)
df_amostra_estratificada.shape