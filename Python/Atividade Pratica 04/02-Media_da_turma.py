def registrar_notas():
    notas = []

    print("=== Registro de Notas da Turma ===")
    print("Digite as notas dos alunos (0 a 10).")
    print("Digite 'fim' para encerrar e calcular a média.\n")

    while True:
        entrada = input("Digite a nota: ").strip().lower()

        # Verifica se o usuário quer encerrar
        if entrada == 'fim':
            break

        try:
            nota = float(entrada)

            # Verifica se a nota está no intervalo válido
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.\n")

        except ValueError:
            print("Entrada inválida! Digite um número válido ou 'fim' para encerrar.\n")

    # Exibe o resultado final
    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")


# Executa o programa
if __name__ == "__main__":
    registrar_notas()
