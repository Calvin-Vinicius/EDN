import pandas as pd

# Leitura do arquivo de log (ex: log.csv com coluna "tempo_execucao")
df = pd.read_csv("log.csv")

media = df["tempo_execucao"].mean()
desvio_padrao = df["tempo_execucao"].std()

print(f"Média do tempo de execução: {media:.2f}")
print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f}")
