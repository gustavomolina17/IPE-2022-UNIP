print ("Programa Detetive")
print ("Responda as perguntas abaixo com s (sim) ou n (nao)")

perguntas = ("Voce telefonou para a vitima? ",
             "Voce esteve no local do crime? ",
             "Voce mora perto da vitima? ",
             "Voce devia para a vitima? ",
             "Voce trabalhou para a vitima? ")

respostas = []

for pergunta in perguntas:
    respostas.append(input(pergunta))

classificacao = 0
for resposta in respostas:
    if (resposta == 's'):
        classificacao += 1

if (classificacao < 2):
    print ("Inocente")
elif (classificacao == 2):
    print ("Suspeito")
elif (classificacao <= 4):
    print ("Cumplice")
else:
    print ("Assassino")