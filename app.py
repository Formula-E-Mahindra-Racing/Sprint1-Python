from helpers import forca_opcao, limpar_tela
from sys_functions import sys_dados
from shop import loja 

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
        # Mendes' Part (Jogos)
        print(f"Bem-vindo à área de jogos {nome_da_empresa},\n...")
        # Função do sistema de jogos
    elif caminho == '2':
        print(f"Bem-vindo ao banco de dados {nome_da_empresa},\naqui você encontrará todos os tipos de dados "
              f"capturados pelos nossos sensores e muito mais!\n")
        sys_dados()
    elif caminho == '3':
        loja()
    elif caminho == '0':
        break
