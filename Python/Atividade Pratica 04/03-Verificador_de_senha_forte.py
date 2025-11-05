def verificar_senha():
    print("=== Verificador de Senhas Fortes ===")
    print("A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        senha = input("Digite uma senha: ").strip()

        # Permite sair do programa
        if senha.lower() == "sair":
            print("\nEncerrando o verificador de senhas.")
            break

        # Verifica se a senha tem pelo menos 8 caracteres
        if len(senha) < 8:
            print("Senha fraca! Ela deve ter pelo menos 8 caracteres.\n")
            continue

        # Verifica se contém pelo menos um número
        if not any(char.isdigit() for char in senha):
            print("Senha fraca! Ela deve conter pelo menos um número.\n")
            continue

        # Se passou em todas as verificações
        print("Senha forte! ✅")
        break


# Executa o programa
if __name__ == "__main__":
    verificar_senha()
