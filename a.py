import os

restaurantes = []  # lista de restaurantes

def exibir_nome_programa():  # exibe o nome do programa
    print("Back-end on Aplication\n")

def exibir_opcoes():  # exibe as opções do menu
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app():  # finaliza o app
    os.system('cls')  # limpando o terminal
    print("Saindo do programa...\n")
    exit()

def opcao_invalida():  # exibe uma mensagem de opção inválida
    print("Opção inválida!\n")
    input("Pressione Enter para voltar ao menu\n")

def cadastrar_novo_restaurante():  # cadastra um novo restaurante
    os.system('cls')
    print("Cadastro de novo restaurante\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante) # adiciona o restaurante à lista
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    input("Pressione Enter para voltar ao menu\n")

def escolher_opcao():  # coleta o input do usuário e chama a função correspondente
    try:
        opcao_escolhida = int(input("Escolher uma opção: "))  # obriga que a variável a ser um número inteiro

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print("Listar restaurante\n")
        elif opcao_escolhida == 3:
            print("Ativar restaurante\n")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():  # função principal
    while True:
        os.system('cls')
        exibir_nome_programa()
        exibir_opcoes()
        escolher_opcao()

if __name__ == '__main__':
    main()