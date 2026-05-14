# 1. Primeiro, pedimos a entrada uma vez
vendas_dia = float(input("Digite um valor entre 1.000 e 3.000: R$ "))

# 2. O 'while' verifica: "O valor é inválido (menor ou igual a zero)?"
# Enquanto for inválido, ele repete o pedido.
while vendas_dia <= 0:
    print("\nValor inválido. Digite um número positivo.")
    vendas_dia = float(input("Digite um valor entre 1.000 e 3.000: R$ "))

if vendas_dia >= 2000:
    print(f"\n{vendas_dia:.2f} Meta batida! Dia excelente.")
elif vendas_dia >= 1500:
    print(f"\n{vendas_dia:.2f} Abaixo da meta, mas aceitável.")
elif vendas_dia >= 1000:
    print(f"\n{vendas_dia:.2f} Dia fraco. Verificar causas.")
else:
    print("\nDia crítico. Abaixo de R$1.000.")