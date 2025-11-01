"""Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:
Nome do produto: "Camiseta"
Preço original: R$ 50.00
Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes."""

nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_disconto = 20.00

def _calc_desconto(nome_produto:str ,valor:float , desconto :float):
    valor_desconto = (valor*desconto/100)
    print(f"{nome_produto}, valor R${valor:.2f} , desconto {desconto:.2f}%")
    print(f"O valor total do desconto do produto {nome_produto} é : R$ {valor_desconto:.2f}")
    
    return valor_desconto

def _calc_valor_final(nome_produto:str, valor_original:float, valor_descontado:float):
    
    preco_final = valor_original - valor_descontado
    print(f"O preço final do produto {nome_produto} é : R$ {preco_final}")



valor_desconto = _calc_desconto(nome_produto, preco_original, porcentagem_disconto)

_calc_valor_final(nome_produto, preco_original, valor_desconto)