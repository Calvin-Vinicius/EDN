def calcular_preco_desconto(preco_original: float, percentual_desconto: float) -> float:
    desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - desconto
    return round(preco_final, 2)

# Exemplo de uso:
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))
preco_final = calcular_preco_desconto(preco, desconto)
print(f"Preço final com desconto: R$ {preco_final:.2f}")
