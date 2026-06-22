#Define a função principal do programa
def main():
    #Pede o nome do usuario e guarda na variavel nome
    nome = input("Digite seu nome:")

    # Pede a idade do usuario, converte para inteiro e guarda na variavel idade
    idade = int(input("Digite sua idade:"))

    # Calcula a idade que o usuario terá daqui a 10 anos
    idade_futura = idade + 10

    # Mostra uma linha de separação na tela
    print("------------------------------")

    # Mostra uma saudação usando o nome digitado
    print("Olá,", nome)

    # Mostra a idade atual
    print("Hoje, você tem", idade, "anos")

    # Mostra a idade futura calculada pelo programa
    print("Daqui a 10 anos você terá", idade_futura, "anos!")

# Verifica se este arquivo está sendo executado diretamente
if __name__ == "__main__":
    #Chama a função principal para iniciar o programa
    main()