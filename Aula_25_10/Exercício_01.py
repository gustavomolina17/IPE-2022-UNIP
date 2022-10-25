p = int(input("Digite o 1° termo: "))
r= int(input("Digite a razão da PA: "))
qtde = int(input("Digite a quantidade de termos: "))

L = [] #inicia a lista vazia
cont = 0
while (cont<qtde):
    L.append(p)  # acrescenta p em L
    p = p+r 
    cont +=1
print ("PA resultante: ",L)

