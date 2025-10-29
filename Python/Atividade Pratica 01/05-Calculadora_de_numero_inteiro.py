#Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
#Entrada: O arquivo de entrada contém 4 valores inteiros. 
#Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.

def _leitura_numeros_inteiros(numero_inteiro):
    while True:
        
        try:
            valor = int(input(f"Insira o valor de {numero_inteiro}: "))
            return valor
        except ValueError:
            print("O Valor informado não é um nÚmero inteiro tente novamente")



A = _leitura_numeros_inteiros("A")
B = _leitura_numeros_inteiros("B")
C = _leitura_numeros_inteiros("C")
D = _leitura_numeros_inteiros("D")

DIFERENCA = (A * B - C * D)

print(f"DIFERENCA = {DIFERENCA}")