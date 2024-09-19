n = int(input("Digite um número: "))
soma = sum(i for i in range(2, n+1, 2))
print("A soma dos números pares entre 1 e", n, "é:", soma)