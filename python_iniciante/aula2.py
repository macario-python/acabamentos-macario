nome_prato = "X-Salada"
custo_total = 8.50
margem = 0.35

preco_venda = custo_total / (1 - margem)

print(f"prato: {nome_prato}")
print(f"custo: R$ {custo_total:.2f}")
print(f"Preço de venda sugerido: R$ {preco_venda:.2f}")