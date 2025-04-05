# lista de palavras 
palavras = ["casa", "flamengo", "paralelepipedo", "computador", "livro", "caneta"]

def maiorPalavra(lista_palavras: list):

    if len(lista_palavras) == 0:
        return print("a lista esta vazia ")

    palavra_mais_longa = ""
    for palavra in lista_palavras:
        if palavra > palavra_mais_longa:
            palavra_mais_longa = palavra

    return palavra_mais_longa
    
def menorPalavra(lista_palavras: list):
    
    if len(lista_palavras) == 0:
        return print("a lista esta vazia, não podemos fazer nada por você")
    
    palavra_mais_curta = lista_palavras[0]
    for palavra in lista_palavras:
        if len(palavra) < len(palavra_mais_curta):
            palavra_mais_curta = palavra
            
    return palavra_mais_curta
            
print(f"Palavra mais longa da lista: {maiorPalavra(palavras)}")
print(f"Palavra mais curta da lista: {menorPalavra(palavras)}")
 
 
