# Programa 6 - Calculadora de Comissão

nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o total de vendas do mês: "))

total = salario_fixo + (vendas * 0.15)

print(f"TOTAL = R$ {total:.2f}")
