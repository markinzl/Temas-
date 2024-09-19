primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))   
terceiro = int(input("Digite o terceiro número: "))

if primeiro > segundo and primeiro > terceiro:
    maiornumero = primeiro
elif segundo > primeiro and segundo > terceiro:
    maiornumero = segundo
else:
    maiornumero = terceiro

if primeiro < segundo and primeiro < terceiro:
    menornumero = primeiro
elif segundo < primeiro and segundo < terceiro:
    menornumero = segundo
else:
    menornumero = terceiro

diferenca = maiornumero - menornumero


print("O maior número é: ", maiornumero)
print("O menor número é: ", menornumero)
print("A diferença entre eles é: ", diferenca)