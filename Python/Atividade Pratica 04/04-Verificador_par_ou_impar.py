def verificar_par_ou_impar():
    pares = 0
    impares = 0

    print("=== Verificador de Números Pares e Ímpares ===")
    print("Digite números inteiros. Digite 'fim' para encerrar.\n")

    while True:
        entrada = input("Digite um número: ").strip().lower()

        # Verifica se o usuário quer encerrar
        if entrada == "fim":
            break

        try:
            numero = int(entrada)  # Tenta converter para inteiro

            if numero % 2 == 0:
                print(f"{numero} é par.\n")
                pares += 1
            else:
                print(f"{numero} é ímpar.\n")
                impares += 1

        except ValueError:
            print("Entrada inválida! Digite um número inteiro ou 'fim' para encerrar.\n")

    # Exibe o resumo final
    print("\n=== Resultado Final ===")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")


# Executa o programa
if __name__ == "__main__":
    verificar_par_ou_impar()
