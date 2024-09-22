from helpers import forca_opcao, limpar_tela
from sys_functions import sys_dados
from cadastro_login import cadastrar_usuario, login
from shop import loja, produtos
from games import games_menu

nome_da_empresa = "Mahindra Racing"
usuario = None  
while True:
    print()
    if usuario:
        print(f"Seja bem-vindo(a), {usuario['username']} à {nome_da_empresa}!")
    else:
        print(f"Seja bem-vindo à {nome_da_empresa}!!!")
    caminho = forca_opcao("Por qual caminho você deseja seguir:\n"
                          "1 - Jogos\n"
                          "2 - Dados\n"
                          "3 - Loja\n"
                          "4 - Cadastro/Login\n"
                          "0 - Sair\n--> ", ['1', '2', '3', '4', '0'], "Opção inválida!")
    limpar_tela()
    if caminho == '1':
        if usuario:
            games_menu(usuario)
        else:
            print('\nVocê precisa estar logado para jogar.')
    elif caminho == '2':
        sys_dados()
    elif caminho == '3':
        if usuario:
            loja(usuario)
        else:
            for id_produto, info in produtos.items():
                print(f"- ID: {id_produto} | {info['nome']} : {info['preco']} MCs (Estoque: {info['estoque']})")
            print("\nVocê precisa estar logado para acessar as funcionalidades da loja.")
    elif caminho == '4':
        opcao_login = forca_opcao("1 - Cadastro\n2 - Login\n--> ", ['1', '2'], "Opção inválida!")
        if opcao_login == '1':
            usuario_atual = cadastrar_usuario()
            if usuario_atual:
                usuario = usuario_atual
        elif opcao_login == '2':
            usuario_atual = login()
            if usuario_atual: 
                usuario = usuario_atual
    elif caminho == '0':
        break
