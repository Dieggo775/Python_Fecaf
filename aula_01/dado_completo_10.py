# Define a função principal do programa
def main():
    # Pede o nome do usuario
    nome = input("Digite o seu nome: ")

    # Pede a profissão do usuário
    profissao = input("Digite a sua Profissão: ")

    # Pede a cidade do usuário
    cidade = input("Digite a sua cidade: ")

    # Pede a idade e converte para número inteiro
    idade = int(input("Digite a sua idade: "))

    # Calcula a idade daqui 5 anos
    idade_futura = idade + 5

    # Mostra o titulo do cadastro
    print("==== CADASTRO ====")

    # Mostra o nome digitado
    print("Ola,", nome)

    # Mostra a profissão digitada
    print("A sua profissão é ", profissao)

    # Mostra a cidade digitada
    print("Você reside em", cidade)

    # Mostra a idade calculada
    print("Idade atual:", idade)

    # Mostra a idade digitada
    print("Idade daqui a 5 anos:", idade_futura)

# Garante que o programa inicie quando o arquivo for executado
if __name__=="__main__":
    # Chama a função principal
    main()
