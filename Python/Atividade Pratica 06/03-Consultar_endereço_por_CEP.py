import urllib.request
import json

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        with urllib.request.urlopen(url) as resposta:
            dados = resposta.read().decode("utf-8")
            dados_json = json.loads(dados)

            if "erro" in dados_json:
                print("❌ CEP não encontrado.")
            else:
                print("=== CONSULTA DE CEP ===")
                print(f"Logradouro: {dados_json.get('logradouro', 'Não informado')}")
                print(f"Bairro: {dados_json.get('bairro', 'Não informado')}")
                print(f"Cidade: {dados_json.get('localidade', 'Não informado')}")
                print(f"Estado: {dados_json.get('uf', 'Não informado')}")

    except Exception as e:
        print("Erro ao consultar o CEP:", e)

if __name__ == "__main__":
    cep = input("Digite o CEP (somente números): ").strip()
    consultar_cep(cep)
