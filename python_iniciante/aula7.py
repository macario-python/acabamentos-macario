cardapio = [
    {"nome": "Frango Grelhado", "preco": 32.90},
    {"nome": "Picanha", "preco": 68.00},
    {"nome": "Salmão", "preco": 54.50},
    {"nome": "Risoto", "preco": 41.00},
    {"nome": "Sobremesa", "preco": 18.00},
]

print("=" * 35)
print("       CARDÁPIO - ESTAÇÃO GRANADA")
print("=" * 35)

for i, item in enumerate(cardapio, start=1):
    print(f"  {i}. {item['nome']:<22} R$ {item['preco']:>5.2f}")

print("=" * 35)

print()


# 1. Primeira tentativa
numero = int(input("Digite o número do item: "))

# 2. Validação (Só entra aqui se estiver errado)
while numero < 1 or numero > len(cardapio): # len() conta quantos itens tem na lista em tempo real. 
# Se você adicionar um 6º item, a validação se atualiza sozinha sem você mudar nada.
    print("Número inválido, digite novamente de 1 a 5")
    numero = int(input("Digite o número do item: "))

# 3. Agora sim, pede a quantidade (só uma vez!)
quantidade = int(input("Quantidade: "))

# 4. Cálculos
item_escolhido = cardapio[numero - 1]
subtotal = item_escolhido["preco"] * quantidade

print(f"\n{quantidade}x {item_escolhido['nome']} = R$ {subtotal:.2f}")