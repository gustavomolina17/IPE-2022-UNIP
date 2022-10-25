letras = []
vogais = ["a", "e", "i", "o", "u"]

for i in range(0, 10):
    letras.append(input("Informe um caracter: "))

totConsoantes = 0
consoantes = []
for i in range(0, 10):
    if letras[i] not in vogais:
        consoantes.append(letras[i])
        totConsoantes += 1

print ("Voce digitou", totConsoantes, "consoantes")
print (consoantes)