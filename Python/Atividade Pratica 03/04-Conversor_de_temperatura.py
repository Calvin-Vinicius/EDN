# Programa 4 - Conversor de Temperatura

temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

# Converte primeiro para Celsius
if origem == "C":
    celsius = temp
elif origem == "F":
    celsius = (temp - 32) * 5/9
elif origem == "K":
    celsius = temp - 273.15
else:
    print("Unidade de origem inválida.")
    exit()

# Converte de Celsius para destino
if destino == "C":
    convertido = celsius
elif destino == "F":
    convertido = (celsius * 9/5) + 32
elif destino == "K":
    convertido = celsius + 273.15
else:
    print("Unidade de destino inválida.")
    exit()

print(f"Temperatura convertida: {convertido:.2f} {destino}")
