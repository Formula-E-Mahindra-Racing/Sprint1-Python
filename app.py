from helpers import forca_opcao, limpar_tela
from sys_functions import sys_dados
from shop import loja
from games import games_menu

nome_da_empresa = "Mahindra Racing"

menu_opcoes = {
    '1': games_menu,
    '2': sys_dados,
    '3': loja,
    '0': 'sair'
}

while True:
    print(f"Seja bem-vindo à {nome_da_empresa}!!!")
    caminho = forca_opcao(
        "Por qual caminho você deseja seguir:\n1 - Jogos\n2 - Dados\n3 - Loja\n0 - Sair\n--> ", 
        menu_opcoes.keys(), 
        "Opção inválida! Digite apenas os números correspondentes ao caminho indicado"
    )
    
    limpar_tela()
    
    if caminho == '0':
        break
    else:
        menu_opcoes[caminho]()
