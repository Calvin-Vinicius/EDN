import json

# Dados de uma pessoa
pessoa = {
    "nome": "Lucas",
    "idade": 28,
    "cidade": "Curitiba"
}

# Escrever em arquivo JSON
with open("pessoa.json", "w", encoding="utf-8") as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

# Ler o arquivo JSON
with open("pessoa.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    print("Dados lidos do JSON:")
    print(dados)
