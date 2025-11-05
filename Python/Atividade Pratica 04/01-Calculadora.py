def calculadora():
    while True:
        try:
            # Solicita os dois números
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            # Solicita a operação
            operacao = input("Digite a operação (+, -, *, /): ")

            # Verifica qual operação será realizada
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida.")

        except ValueError as ve:
            print(f"Erro: {ve}. Tente novamente.\n")
            continue
        except ZeroDivisionError as zde:
            print(f"Erro: {zde}. Tente novamente.\n")
            continue
        except Exception:
            print("Erro desconhecido. Tente novamente.\n")
            continue
        else:
            # Exibe o resultado e encerra o programa
            print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
            break


# Executa a calculadora
if __name__ == "__main__":
    calculadora()
