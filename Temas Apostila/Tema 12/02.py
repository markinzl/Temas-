numeroinicial = int(input("Digite o seu número inicial: "))
numerofinal = int(input("Digite o seu número final: "))

if numeroinicial > numerofinal:
    print("O número final tem que ser menor ou igual ao final: ")
else:
    for i in range (numeroinicial, numerofinal + 1):
        print ("Os números iniciais e finais são: ", i)