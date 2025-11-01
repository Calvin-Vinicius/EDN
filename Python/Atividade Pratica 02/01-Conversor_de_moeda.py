"""Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados: 
Valor em reais: R$ 100.00
Taxa do dólar: R$ 5.60
Taxa do euro: R$ 6.60 """

valor_real = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60
nome_taxa_D = "Dólar"
nome_taxa_E = "Euro"

def _conversor(valor: float, taxa: str , valor_taxa: float):
    valor_convertido = f"{(valor_real/valor_taxa):.2f}" 
    print(f"O valor convertido em {taxa} é : {valor_convertido}")

_conversor(valor_real, nome_taxa_E, taxa_dolar)
_conversor(valor_real, nome_taxa_D, taxa_euro)
