# Exercício 16 - Média escolar completa
nota1 = float(input("Primeira nota: ")) # Recebe a primeira nota.
nota2 = float(input("Segunda nota: ")) # Recebe a segunda nota.
media = (nota1 + nota2) / 2 # Calcula a média.
print("Média:", media) # Mostra a média.
if media >= 7: # Verifica aprovação.
    print("Aprovado") # Mostra aprovado.
elif media >= 5: # Verifica recuperação.
    print("Recuperação") # Mostra recuperação.
else: # Caso esteja abaixo de 5.
    print("Reprovado") # Mostra reprovado.