# Exercício 20 - Sistema simples de aluno
nome = input("Nome do aluno: ") # Recebe o nome.
idade = int(input("Idade do aluno: ")) # Recebe a idade.
nota = float(input("Nota do aluno: ")) # Recebe a nota.
print("Aluno:", nome) # Mostra o nome.
if idade >= 18: # Verifica maioridade.
    print("Maior de idade") # Mostra maior.
else: # Caso seja menor.
    print("Menor de idade") # Mostra menor.
if nota >= 7: # Verifica aprovação.
    print("Situação: Aprovado") # Mostra aprovado.
elif nota >= 5: # Verifica recuperação.
    print("Situação: Recuperação") # Mostra recuperação.
else: # Caso esteja abaixo de 5.
    print("Situação: Reprovado") # Mostra reprovado