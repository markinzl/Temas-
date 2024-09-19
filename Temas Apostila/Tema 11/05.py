n = int(input("Digite um número: "))
if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "não é um número primo")
            break
    else:
        print(n, "é um número primo")
else:
    print(n, "não é um número primo")