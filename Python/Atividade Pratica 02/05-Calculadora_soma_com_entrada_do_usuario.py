"""5- Calculadora de Soma com Entrada do Usuário
Leia 2 valores inteiros e armazene-os nas variáveis A e B. 

Efetue a soma de A e B, atribuindo o seu resultado à variável X. 

Entrada: A entrada contém 2 valores inteiros informados pelo usuário. 

Saída: Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha."""

def _leitura_numeros_inteiros(numero_inteiro):
    while True:
        
        try:
            valor = int(input(f"Insira o valor de {numero_inteiro}: "))
            return valor
        except ValueError:
            print("O Valor informado não é um nÚmero inteiro tente novamente")



A = _leitura_numeros_inteiros("A")
B = _leitura_numeros_inteiros("B")


x = (A+B)

print(f"X = {x} ")