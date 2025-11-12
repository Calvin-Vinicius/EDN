import urllib.request

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        with urllib.request.urlopen(url) as resposta:
            conteudo = resposta.read().decode("utf-8")

            # Exemplo de resposta:
            # {"USDBRL":{"code":"USD","codein":"BRL","name":"Dólar Comercial/Real Brasileiro","high":"5.45",...}}

            # Extrair valores com busca textual
            def extrair(campo):
                inicio = conteudo.find(f'"{campo}":"')
                if inicio == -1:
                    return None
                inicio += len(campo) + 4
                fim = conteudo.find('"', inicio)
                return conteudo[inicio:fim]

            codigo = extrair("code")
            nome = extrair("name")
            bid = extrair("bid")
            high = extrair("high")
            low = extrair("low")
            pct = extrair("pctChange")
            data = extrair("create_date")

            if codigo and bid:
                print("\n=== COTAÇÃO DE MOEDA (AwesomeAPI) ===")
                print(f"Moeda: {codigo} / BRL")
                print(f"Nome: {nome}")
                print(f"Valor atual: R${float(bid):.2f}")
                print(f"Máximo do dia: R${float(high):.2f}")
                print(f"Mínimo do dia: R${float(low):.2f}")
                print(f"Variação: {pct}%")
                print(f"Última atualização: {data}\n")
            else:
                print("❌ Não foi possível encontrar os dados da moeda.")

    except urllib.error.URLError as e:
        print("Erro ao conectar à API:", e)
    except Exception as e:
        print("Erro inesperado:", e)


if __name__ == "__main__":
    print("=== CONSULTA DE COTAÇÃO (SEM JSON) ===")
    moeda = input("Informe o código da moeda (ex: USD, EUR, GBP): ").upper().strip()
    consultar_cotacao(moeda)
