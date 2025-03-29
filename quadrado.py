def quadrado(A, B, C, D):
   
    if A == B == C == D :
        return True 
    else:
        return False


A = 5
B = 5
C = 5
D = 5

print (A,B,C,D) 

if quadrado(A, B, C, D):
    print("É um quadrado!")
else:
    print("Não é um quadrado.")
