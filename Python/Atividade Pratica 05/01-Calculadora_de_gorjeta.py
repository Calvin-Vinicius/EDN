def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso:
valor = float(input("Digite o valor total da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))
print(f"Valor da gorjeta: R$ {calcular_gorjeta(valor, porcentagem):.2f}")
