# Exercicio 7 -Produto com desconto
preco_original = float(input("Preço original: ")) # Recebe o preço antigo
preco_atual = float(input("Preço atual: ")) # Recebe o preço atual
if preco_atual < preco_original: # Verifica se o atual é menor
    print("Desconto aplicado") # Mostra que houve desconto
else: # Caso não esteja menor
    print("Sem desconto") # Mostra que não houve desconto    