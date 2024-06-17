from helpers import forca_opcao, limpar_tela
from sys_functions import sys_dados
from shop import loja
from games import games_menu


nome_da_empresa = "Mahindra Racing"
lista_menu_opcao = ['1', '2', '3', '0']

while True:
    print(f"Seja bem-vindo à {nome_da_empresa}!!!")
    caminho = forca_opcao("Por qual caminho você deseja seguir:\n"
                          "1 - Jogos\n"
                          "2 - Dados\n"
                          "3 - Loja\n"
                          "0 - Sair\n--> ", lista_menu_opcao, "Opção inválida! Digite apenas os números correspondentes ao caminho indicado")
    limpar_tela()
    if caminho == '1':
        games_menu()
    elif caminho == '2':
        sys_dados()
    elif caminho == '3':
        loja()
    elif caminho == '0':
        break
