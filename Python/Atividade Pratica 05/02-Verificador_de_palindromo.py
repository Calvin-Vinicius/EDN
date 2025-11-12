def verificar_palindromo(texto: str) -> str:
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Exemplo de uso:
frase = input("Digite uma palavra ou frase: ")
print(verificar_palindromo(frase))
