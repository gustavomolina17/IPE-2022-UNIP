vet1 = []
vet2 = []
vet3 = []
vet4 = []

print ("Informe os valores do primeiro vetor")
for i in range(0, 5):
    vet1.append(int(input("Informe um numero: ")))

print ('Informe os valores do segundo vetor')
for i in range(0, 5):
    vet2.append(int(input("Informe um numero: ")))

print ("Informe os valores do terceiro vetor")
for i in range(0, 5):
    vet3.append(int(input("Informe um numero: ")))

for i in range(0, 5):
    vet4.append(vet1[i])
    vet4.append(vet2[i])
    vet4.append(vet3[i])


print (vet4)