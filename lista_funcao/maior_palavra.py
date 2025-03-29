 # lista de palavras 
palavras = ["casa", "flamengo", "paralelepipedo", "computador", "livro", "caneta"]

def maiorPalavra(lista_palavras):
    palavra_mais_longa = lista_palavras

    for palavra in lista_palavras:
        if len(palavra) > len(palavra_mais_longa):
            palavra_mais_longa = palavra

    return palavra_mais_longa
    
def menorPalavra(lista_palavras):
    palavra_mais_curta = lista_palavras

    for palavra in lista_palavras:
        if len(palavra) < len(palavra_mais_curta):
            palavra_mais_curta = palavra
                
    return palavra_mais_curta
            
print(f"Palavra mais longa da lista: {maiorPalavra(palavras)}")
print(f"Palavra mais curta da lista: {menorPalavra(palavras)}")
 