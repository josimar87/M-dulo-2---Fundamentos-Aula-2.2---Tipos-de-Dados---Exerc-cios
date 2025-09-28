#Q4
# Ler a quantia em reais
quantia = int(input())

# Notas possíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Calcular a quantidade de notas necessárias
for nota in notas:
    quantidade = quantia // nota
    quantia %= nota
    print(f"{quantidade} nota(s) de R${nota:,.2f}")