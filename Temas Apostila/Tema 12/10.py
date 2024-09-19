# Solicita ao usuário um número de 1 a 10
numero = int(input("Digite um número de 1 a 10 para ver a tabuada: "))

# Verifica se o número digitado foi 1 a 10
if numero < 1 or numero > 10:
    print("Digite um valor entre 1 e 10.")
else:
    # Gera a tabuada do número digitado
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)