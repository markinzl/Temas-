#As linhas abaixos estão declarando os valores das variáveis
M = "M"
m = "m"
F = "F"
f = "f"
#A linha abaixo pede para o usuário digitar uma das variáves que foi criada
sexo = input("Digite M para sexo masculino ou F para sexo feminino: ")
#As linhas abaixo definira qual o genero da pessoa conforme a sua respota
if sexo == M:
    print ("Sexo Maculino")
elif sexo  == m:
    print ("Sexo Masculino")
elif sexo == F:
    print ("Sexo Feminino")
elif sexo == f:
    print ("Sexo Feminino")
else:
    print ("Erro, Digite M ou F")