import csv

# Dados de exemplo
dados = [
    {"Nome": "Ana", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Bruno", "Idade": 30, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carla", "Idade": 22, "Cidade": "Belo Horizonte"}
]

# Escrever em CSV
with open("pessoas.csv", "w", newline='', encoding="utf-8") as arquivo:
    colunas = ["Nome", "Idade", "Cidade"]
    writer = csv.DictWriter(arquivo, fieldnames=colunas)
    writer.writeheader()
    writer.writerows(dados)

print("Arquivo pessoas.csv criado com sucesso!")
