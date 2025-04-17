#  Quando se usa from collections import Counter,
#  pode simplificar bastante a lógica de comparação de anagramas.
#  O Counter cria um dicionário com a frequência de cada caractere,
#  o que é ideal para esse tipo de verificação.

from collections import Counter

def eh_anagramas(p1, p2):
    # Remove espaços e coloca tudo em minúsculas
    p1 = p1.replace(" ", "").lower()
    p2 = p2.replace(" ", "").lower()
    
    # Compara os contadores de caracteres
    # Counter("amor")   => {'a': 1, 'm': 1, 'o': 1, 'r': 1}
    # Counter("roma")   => {'r': 1, 'o': 1, 'm': 1, 'a': 1}

    return Counter(p1) == Counter(p2)

# Entrada do usuário
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
