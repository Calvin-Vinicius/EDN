import urllib.request
import json

def gerar_usuario():
    url = "https://randomuser.me/api/"
    try:
        with urllib.request.urlopen(url) as resposta:
            dados = resposta.read().decode("utf-8")
            dados_json = json.loads(dados)

            usuario = dados_json["results"][0]
            nome = f"{usuario['name']['first']} {usuario['name']['last']}"
            email = usuario["email"]
            pais = usuario["location"]["country"]

            print("=== PERFIL DE USUÁRIO ALEATÓRIO ===")
            print(f"Nome:  {nome}")
            print(f"E-mail: {email}")
            print(f"País:  {pais}")

    except Exception as e:
        print("Erro ao consultar a API:", e)

if __name__ == "__main__":
    gerar_usuario()
