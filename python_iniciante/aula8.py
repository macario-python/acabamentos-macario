def exibir_cabecalho(titulo):
    print("=" * 35)
    print(f"  {titulo}")
    print("=" * 35)

exibir_cabecalho("CARDÁPIO - ESTAÇÃO GRANADA")
exibir_cabecalho("RELATÓRIO DO DIA")
exibir_cabecalho("FECHAMENTO MENSAL")

#=========================================

def calcular_subtotal(preco, quantidade):
    return preco * quantidade

def calcular_preco_venda(custo, margem):
    return custo / (1 - margem)

# Usando
sub = calcular_subtotal(54.50, 3)
print(f"Subtotal: R$ {sub:.2f}")

venda = calcular_preco_venda(8.50, 0.35)
print(f"Preço de venda: R$ {venda:.2f}")