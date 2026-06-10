import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

datos = pd.read_csv("titanic.csv")

fig, ax= plt.subplots()

g = sns.countplot(x = "Sex", hue = "Survived", data = datos, ax=ax)

g.figure.savefig("plot.png")

fig, ax= plt.subplots()

g2 = sns.countplot(x = "Pclass", hue = "Survived", data = datos, ax=ax)

g2.figure.savefig("plot2.png")
