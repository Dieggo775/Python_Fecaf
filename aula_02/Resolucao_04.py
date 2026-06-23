# Exercicio 4 - Compra aprovada
saldo = float(input("Digite seu saldo: ")) # Recebe o saldo disponivel
preco = float(input("Digite o preço do produtos: ")) # Recebe o preço do produto
if saldo >= preco: # Verifica se o saldo paga o produto
    print("Compra aprovada") # Mostra que pode comprar
else: # Caso o saldo seja menor que o preço
    print("Saldo insulficiente") # Mostra que não pode comprar