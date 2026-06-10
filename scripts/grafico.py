import pandas as pd
import seaborn as sns

datos = pd.read_csv("titanic.csv")

g = sns.countplot(x = "Sex", hue = "Survived", data = datos, ax=ax)

g.figure.savefig("plot.png")

g = sns.countplot(x = "Pclass", hue = "Survived", data = datos, ax=ax)

g.figure.savefig("plot2.png")
