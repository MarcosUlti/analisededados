import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("respostas.csv")

generos = df["Gênero Favorito"].value_counts()

plataformas = df["Plataforma Favorita"].value_counts()

plt.figure(figsize=(8, 5))
generos.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Preferência de Gêneros de Jogos")
plt.xlabel("Gênero")
plt.ylabel("Quantidade de Pessoas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_generos_barra.png")
plt.show()

plt.figure(figsize=(6, 6))
plt.pie(plataformas, labels=plataformas.index, autopct="%1.1f%%", startangle=90)
plt.title("Plataformas Favoritas")
plt.tight_layout()
plt.savefig("grafico_plataformas_pizza.png")
plt.show()
