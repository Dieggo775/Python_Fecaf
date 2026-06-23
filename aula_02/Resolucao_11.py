# Exercício 11 - Maior número
numero1 = int(input("Primeiro número: ")) # Recebe o primeiro número.
numero2 = int(input("Segundo número: ")) # Recebe o segundo número.
if numero1 > numero2: # Verifica se o primeiro é maior.
    print("Maior:", numero1) # Mostra o primeiro.
elif numero2 > numero1: # Verifica se o segundo é maior.
    print("Maior:", numero2) # Mostra o segundo.
else: # Caso nenhum seja maior.
    print("Os números são iguais") # Mostra empate.