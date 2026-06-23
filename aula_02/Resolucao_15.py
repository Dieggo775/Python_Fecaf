# Exercício 15 - Classificação por idade
idade = int(input("Digite sua idade: ")) # Recebe a idade.
if idade < 12: # Verifica se é menor que 12.
    print("Criança") # Mostra criança.
elif idade < 18: # Verifica se é menor que 18.
    print("Adolescente") # Mostra adolescente.
elif idade < 60: # Verifica se é menor que 60.
    print("Adulto") # Mostra adulto.
else: # Caso tenha 60 ou mais.
    print("Idoso") # Mostra idoso.