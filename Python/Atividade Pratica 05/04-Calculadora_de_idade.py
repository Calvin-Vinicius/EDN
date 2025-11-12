from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

# Exemplo de uso:
ano = int(input("Digite seu ano de nascimento: "))
print(f"Sua idade aproximada em dias é: {calcular_idade_em_dias(ano)} dias")
