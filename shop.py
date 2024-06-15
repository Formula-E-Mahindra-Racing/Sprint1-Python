from helpers import print_de_opcoes, forca_opcao, limpar_tela, verifica_numero


def desconto_final(number, discount):
    number = number - (number * (discount / 100))
    return number


def loja(primeira_vez=True):
    if primeira_vez:
        print('Seja bem vindo!! Esta é a loja da Mahindra Racing\nPor aqui, você pode\n - Comprar Canecas, Camisetas e até ingressos para a próxima corrida de Fórmula-E\n - Aqui usamos a Mahindra Coins(MC) como moeda para compra desses produtos.\n\n')

    preco_caneca = 390
    preco_ticket = 2000
    preco_camiseta = 500
    preco_bone = 130

    precos = [preco_caneca, preco_ticket, preco_camiseta, preco_bone]
    total = 0

    coisas_para_comprar = [
        f'(1). Caneca com a logo da Mahindra -> {preco_caneca}MC',
        f'(2). Ticket para a próxima corrida -> {preco_ticket}MC',
        f'(3). Camiseta com a logo da Mahindra -> {preco_camiseta}MC',
        f'(4). Boné da escuderia Mahindra -> {preco_bone}MC',
        '(5). Sair...'
    ]

    while True:
        sub_total = 0
        output_opcoes = print_de_opcoes(coisas_para_comprar)
        opcao_de_compra = forca_opcao(
            '', ['1', '2', '3', '4', '5'], 'Por favor, escolha somente os números: 1, 2, 3, 4, 5\n' + output_opcoes)
        if opcao_de_compra == '5':
            break

        quantidade = verifica_numero(
            'Quantos gostaria de adicionar ao carrinho?\n-->', 'Por favor, digite somente números inteiros')
        sub_total = precos[int(opcao_de_compra) - 1] * quantidade

        total += sub_total
        print(f'O subtotal é: {total}')

        continuar_comprando = forca_opcao(
            'Gostaria de continuar comprando (s/n)?\n-->', ['s', 'n'], 'Por favor, escolha somente uma das letras: s, n\n')
        if continuar_comprando == 's':
            limpar_tela()
            continue
        else:
            desconto = 0
            if total < 200:
                desconto = 2
            elif total < 1000:
                desconto = 8
            elif total < 2000:
                desconto = 12
            else:
                desconto = 15

            total = desconto_final(total, desconto)
            print(f'Um desconto de {desconto}% foi aplicado.')
            print(f'O total é: {total:.2f}MCs\nMuito obrigado e volte sempre')
            break
    return
