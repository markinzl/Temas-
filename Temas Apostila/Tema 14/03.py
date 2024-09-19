# função que ira multiplicar a idade do usuario por um ano
# E mostrara quantos dias aproximadamente ja viveu
def d_de_vida(nome, idade):
    dias = idade * 365
    return nome + ", você já viveu aproximadamente " + str(dias) + " dias."

# Entrada de dados do usuario e print na tela da função
n_usuario = input("Digite seu nome: ")
idad_usuario = int(input("Digite sua idade: "))
print(d_de_vida(n_usuario, idad_usuario))