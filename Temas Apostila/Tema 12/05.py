par = 2 & 0 == 0

while True:
    num1 = int(input("Digite o seu primeiro número, ou digite zero para sair: "))
    if num1 == 0:
        print("Encerrando o programa.")
        break

    num2 = int(input("Digite o seu segundo número: "))
    num3 = int(input("Digite o seu terceiro número: "))
    num4 = int(input("Digite o seu quarto número: "))
    num5 = int(input("Digite o seu quinto número: "))

    # Inicializa variáveis para soma e contagem de números pares
    soma_pares = 0
    contagem_pares = 0

    # Verifica cada número e soma se for par
    for num in [num1, num2, num3, num4, num5]:
        if num % 2 == 0:
            soma_pares += num
            contagem_pares += 1

    if contagem_pares > 0:
        media_pares = soma_pares / contagem_pares
        print("A média dos números pares digitados é:", media_pares)
    else:
        print("Nenhum número par foi digitado.")