from helpers import print_de_opcoes, forca_opcao, limpar_tela, verifica_numero

produtos = {
    '1': {'nome': 'Caneca com a logo da Mahindra', 'preco': 2000},
    '2': {'nome': 'Ticket para a próxima corrida', 'preco': 100000},
    '3': {'nome': 'Camiseta com a logo da Mahindra', 'preco': 5000},
    '4': {'nome': 'Boné da escuderia Mahindra', 'preco': 2500}
}

def desconto_final(total, desconto):
    return total - (total * (desconto / 100))

def loja(primeira_vez=True):
    if primeira_vez:
        print('Seja bem vindo à loja da Mahindra Racing!')
    total = 0
    while True:
        print_de_opcoes([f"({key}). {produto['nome']} -> {produto['preco']}MC" for key, produto in produtos.items()])
        opcao = forca_opcao("Escolha um produto ou digite 5 para sair:\n--> ", produtos.keys() | {'5'}, "Opção inválida!")
        if opcao == '5':
            break
        quantidade = verifica_numero('Quantos gostaria de adicionar ao carrinho?\n--> ', 'Digite um número válido.')
        total += produtos[opcao]['preco'] * quantidade
        print(f'O subtotal é: {total} MC')
        continuar = forca_opcao('Gostaria de continuar comprando (s/n)?\n--> ', ['s', 'n'], 'Digite "s" ou "n".')
        if continuar == 'n':
            if total < 200:
                desconto = 2
            elif total < 1000:
                desconto = 8
            elif total < 2000:
                desconto = 12
            else:
                desconto = 15
            print(f'Você ganhou {desconto}% de desconto por suas compras!')
            total_com_desconto = desconto_final(total, desconto)
            print(f'Total a pagar com desconto: {total_com_desconto} MC')
            break
    print('Obrigado pela compra! Volte sempre!')
    limpar_tela()
