pessoas = []
for i in range(0, 5):
    pessoa = []
    pessoa.append(int(input("Informe a idade da pessoa: ")))
    pessoa.append(float(input("Informe a altura da pessoa: ")))
    pessoas.append(pessoa)

pessoas.reverse()
for pessoa in pessoas:
    print ("Idade: - Altura: ",(pessoa[0], pessoa[1]))