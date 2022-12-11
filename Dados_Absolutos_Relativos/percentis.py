import pandas as pd

dataset = pd.read_csv("census.csv")

dataset2 = dataset[["income", "education"]]
dataset2

dataset3 = dataset2.groupby(["education", "income"])["education"].count()

dataset3

dataset3.index

dataset3[" Bachelors", " <=50K"], dataset3[" Bachelors", " >50K"]