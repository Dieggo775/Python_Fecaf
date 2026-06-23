# Exercício 19 - Calculadora simples
numero1 = float(input("Primeiro número: ")) # Recebe o primeiro número.
numero2 = float(input("Segundo número: ")) # Recebe o segundo número.
operacao = input("Operação (+, -, *, /): ") # Recebe a operação.
if operacao == "+": # Verifica soma.
    print("Resultado:", numero1 + numero2) # Mostra soma.
elif operacao == "-": # Verifica subtração.
    print("Resultado:", numero1 - numero2) # Mostra subtração.
elif operacao == "*": # Verifica multiplicação.
    print("Resultado:", numero1 * numero2) # Mostra multiplicação.
elif operacao == "/": # Verifica divisão.
    if numero2 != 0: # Evita divisão por zero.
        print("Resultado:", numero1 / numero2) # Mostra divisão.
    else: # Caso o segundo número seja zero.
        print("Não é possível dividir por zero") # Mostra erro.
else: # Caso a operação não exista.
    print("Operação inválida") # Mostra operação inválida.