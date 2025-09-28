#Q3
# Inicializar o preço total
preco_total = 0

# Loop para cada produto
for i in range(1, 4):
    # Ler o nome do produto
    nome = input(f"Digite o nome do produto {i}: ")

    # Ler o preço unitário do produto
    preco_unitario = float(input(f"Digite o preço unitário do produto {i}: "))

    # Ler a quantidade do produto
    quantidade = int(input(f"Digite a quantidade do produto {i}: "))

    # Calcular o preço do produto e adicionar ao preço total
    preco_total += preco_unitario * quantidade

# Imprimir o preço total
print(f"Total: R${preco_total:,.2f}")