import os

# Lista de lojas com estrutura mais completa, incluindo 'ativo'
lojas = [{'nome': 'Loja 01', 'ativo': False}, 
         {'nome': 'Loja 02', 'ativo': True}]

# Função para exibir o nome do programa
def exibir_nome_programa():
    print('Cadastro de Lojas\n')

# Exibe as opções disponíveis no menu
def exibir_opcoes():
    print('1. Cadastrar loja')
    print('2. Listar lojas')
    print('3. Alternar estado da loja')
    print('4. Sair\n')

# Função para finalizar o app
def finalizar_app():
    exibir_subtitulo('Finalizando o app')

# Função para exibir subtítulos e limpar a tela
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

# Função para voltar ao menu principal
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu: ')
    main()

# Exibe uma mensagem para opção inválida
def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()

# Função para cadastrar uma nova loja
def cadastrar_nova_loja():
    exibir_subtitulo('Cadastro de novas lojas')
    nome_da_loja = input('Digite o nome da loja que deseja cadastrar: ')
    dados_da_loja = {'nome': nome_da_loja, 'ativo': False}  # Por padrão, a loja é cadastrada como inativa
    lojas.append(dados_da_loja)
    print(f'A loja {nome_da_loja} foi cadastrada com sucesso!')
    voltar_ao_menu_principal()

# Função para listar as lojas cadastradas
def listar_lojas():
    exibir_subtitulo('Listagem de lojas')

    print(f'{"Nome da loja".ljust(20)} | Status')
    for loja in lojas:
        nome_loja = loja['nome']
        ativo = 'ativada' if loja['ativo'] else 'desativada'
        print(f'{nome_loja.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()

# Função para alternar o estado de uma loja (ativada/desativada)
def alternar_estado_loja():
    exibir_subtitulo('Alterar estado da loja')
    nome_loja = input('Digite o nome da loja que deseja alterar o estado: ')
    loja_encontrada = False

    for loja in lojas:
        if nome_loja == loja['nome']:
            loja_encontrada = True
            loja['ativo'] = not loja['ativo']
            estado = 'ativada' if loja['ativo'] else 'desativada'
            print(f'A loja {nome_loja} foi {estado} com sucesso!')
    
    if not loja_encontrada:
        print('Loja não encontrada.')
    
    voltar_ao_menu_principal()

# Função para escolher a opção do menu
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_nova_loja()
        elif opcao_escolhida == 2:
            listar_lojas()
        elif opcao_escolhida == 3:
            alternar_estado_loja()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

# Função principal
def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()