#Q1
# Ler o comprimento do terreno
comprimento = int(input("Digite o comprimento do terreno (m): "))

# Ler a largura do terreno
largura = int(input("Digite a largura do terreno (m): "))

# Ler o preço do metro quadrado
preco_m2 = float(input("Digite o preço do metro quadrado (R$): "))

# Calcular a área do terreno em metros quadrados
area_m2 = comprimento * largura

# Calcular o preço total do terreno
preco_total = preco_m2 * area_m2

# Imprimir o resultado
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")

