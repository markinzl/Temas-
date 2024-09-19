def calcular_area(base, altura):
    # Calcula a área de um triângulo.
    return (base * altura) / 2

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

area = calcular_area(base, altura)
print("A área do triângulo é:", area)