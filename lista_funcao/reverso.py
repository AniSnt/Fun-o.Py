def inverter_palavra(palavra):
    invertida = ''
    for i in range(len(palavra) - 1, -1, -1):
        invertida += palavra[i]
    return invertida

entrada = input("Digite uma palavra: ")
saida = inverter_palavra(entrada)
print(f"Palavra invertida: {saida}")
