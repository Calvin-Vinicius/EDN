#Crie um programa que calcule o volume de uma caixa retangular. Use as seguintes dimensões:
# Comprimento: 12 cm, Largura: 14 cm, Altura: 20 cm 

altura = 20
comprimento = 12
largura = 14

def _calc_ret_volume(l,w,h):
    volume_caixa = (l*w*h)
    print(f" O valor do volume da caixa é: {volume_caixa}cm³ ou {volume_caixa/1000}L")
   
    
_calc_ret_volume(largura,comprimento,altura)