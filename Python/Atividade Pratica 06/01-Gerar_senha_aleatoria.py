import random
import string

def gerar_senha(tamanho):
    # Conjunto de caracteres: letras maiúsculas, minúsculas, números e caracteres especiais
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Gera senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    print("=== GERADOR DE SENHA ALEATÓRIA ===")
    try:
        tamanho = int(input("Informe o tamanho da senha: "))
        if tamanho <= 0:
            print("O tamanho deve ser maior que zero.")
        else:
            senha = gerar_senha(tamanho)
            print(f"Senha gerada: {senha}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
