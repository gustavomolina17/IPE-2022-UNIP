L = []  #inicia uma lista vazia
x = int(input("Digite um inteiro: ")) # Lê o 1º valor
while (x !=0):
    L.append(x) #insere na lista
    x = int(input("Digite um inteiro: ")) # lê o próximo
print("Lista resultante: ", L)
print ("O tamanho dessa lista é: ", (len(L)))  