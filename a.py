import os

def exibir_nome_programa():
    print("Sabor Express\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app(): #função que finaliza o app
    os.system('cls') #limpando o terminal
    print("Saindo do programa...\n")
    exit()

def escolher_opcao():
    opcao_escolhida = int(input("Escolher uma opção: ")) # Obrigando que a minha variável seja um número inteiro

    if opcao_escolhida == 1:
        print("Cadastrar restaurante\n")
    elif opcao_escolhida == 2:
        print("Listar restaurante\n")
    elif opcao_escolhida == 3:
        print("Ativar restaurante\n")
    else:
        finalizar_app()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()