n = input("Digite um número: ")
if n == n[::-1]:
    print(n, "é um número palíndromo")
else:
    print(n, "não é um número palíndromo")