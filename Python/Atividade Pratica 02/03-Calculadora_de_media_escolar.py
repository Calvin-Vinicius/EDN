"""Crie um programa que calcula a média escolar de uma aluno. Use as seguintes notas:
Nota 1: 7.5
Nota 2: 8.0
Nota 3 6.5
O programa deve calcular a média e exibir todas as notas e o resultao final, arredondando para duas casas decimais"""

nota_1 = 7.5
nota_2 = 8.0
nota_3 = 6.5
quant_notas = 3

def _calc_media(n1, n2, n3):
    media_notas = (n1 + n2+ n3)/quant_notas
    print(f"Notas {n1 , n2, n3} média final {media_notas:.2f}")

_calc_media(nota_1, nota_2, nota_3)