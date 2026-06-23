# Exercício 14 - Desconto por compra
valor = float(input("Valor da compra: ")) # Recebe o valor da compra.
if valor > 100: # Verifica se tem direito a desconto.
    desconto = valor * 0.10 # Calcula 10% do valor.
    valor_final = valor - desconto # Subtrai o desconto.
    print("Valor com desconto:", valor_final) # Mostra o valor final.
else: # Caso não tenha desconto.
    print("Valor sem desconto:", valor) # Mostra o valor original