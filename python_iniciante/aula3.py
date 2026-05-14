nome_prato = input("nome do lanche: ")
custo_total = float(input("Custo total dos ingredientes (R$): "))
margem = float(input(" Margem desejada (ex: 0.35 para 35%): "))

preco_venda = custo_total / (1 - margem)

print(f"\nprato: {nome_prato}")
print(f"custo: R$ {custo_total:.2f}")
print(f"Preço de venda sugerido: R$ {preco_venda:.2f}")
