import pandas as pd

df = pd.read_csv(r"C:\wamp64\www\python\softex8\softex_media\notas_alunos.csv")
df = df.set_index('Alunos')
media = (df["nota_1"] + df["nota_2"])/2
df["media"] = media

df.loc[df["media"]>=7, "situação"] = "aprovado"
df.loc[df["faltas"]<5, "situação"] = "aprovado"
df.loc[df["media"] < 7, "situação"] = "Reprovado"
df.loc[df["faltas"] > 5, "situação"] = "Reprovado"
df.to_csv("alunos_situacao.csv")

maior_faltas = df["faltas"].max()
print("maior quantidade de falta é: " +str(maior_faltas))
maior_media = df["media"].max()
print("maior media é: " +str(maior_media))
media_geral = df["media"].median()
print("media geral é: " +str(media_geral))