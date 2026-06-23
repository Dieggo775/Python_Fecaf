# Exercício 17 - Caixa eletrônico simples
saldo = float(input("Digite seu saldo: ")) # Recebe o saldo.
saque = float(input("Valor do saque: ")) # Recebe o valor do saque.
if saque <= saldo: # Verifica se existe saldo suficiente.
    saldo = saldo - saque # Atualiza o saldo.
    print("Saque realizado") # Mostra sucesso.
    print("Saldo atual:", saldo) # Mostra o novo saldo.
else: # Caso o saque seja maior que o saldo.
    print("Saldo insuficiente") # Mostra erro.