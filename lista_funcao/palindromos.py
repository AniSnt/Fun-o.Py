def eh_palindromo(palavra):
    invertida = ''
    for i in range(len(palavra) - 1, -1, -1):
        invertida += palavra[i]
        
    return invertida == palavra

entrada = input("Digite uma palavra: ")
saida = eh_palindromo(entrada)
print(f"É palindromo: {saida}")
