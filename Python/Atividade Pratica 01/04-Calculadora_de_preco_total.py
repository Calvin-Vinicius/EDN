# Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:
# Nome do produto: "Cadeira Infantil", Preço unitário: R$ 12.40 Quantidade: 3 
# O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

id_produto = "Cadeira Infantil"
preco = 12.40
quantidade = 3

def _checkout(id_produto, preco, quantidade):
    total = preco * quantidade
    print(id_produto) 
    print(f"{quantidade}x R$ {preco:.2f}         R${total:.2f}")    
    print (f"O valor total da compra é de: R$ {total:.2f}")


_checkout(id_produto, preco, quantidade)