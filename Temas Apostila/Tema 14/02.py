# função que ira multiplicar o valor a receber por hora trabalhada
def pag(h_trabalhadas, v_por_hora):
    v_total = h_trabalhadas * v_por_hora
    return v_total

# entrada de dados pelo usuario
h = float(input("Digite o número de horas trabalhadas: "))
v_hora = float(input("Digite o valor por hora: "))
total_a_pagar = pag(h, v_hora)
# ira mostrar os resultados
print("O valor a ser pago é: R$", total_a_pagar)