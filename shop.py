def adicionar_produto():
    nome_produto = input("Digite o nome do novo produto: ")
    preco = int(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))
    produtos[nome_produto] = {"preco" : preco, "estoque" : estoque}
    print(f"Produto {nome_produto} adicionado com sucesso!")

def modificar_estoque():
    nome_produto = input("Digite o nome do produto que deseja modificar o estoque: ")
    if nome_produto in produtos:
        novo_estoque = int(input("Digite a nova quantidade em estoque: "))
        produtos[nome_produto]["estoque"] = novo_estoque
        print(f"Estoque do produto {nome_produto} atualizado para {novo_estoque}.")
    else:
        print("Produto não encontrado.")

def loja(usuario):
    print("Bem-vindo à loja da Mahindra Racing!")
    if usuario["admin"]:
        admin_opcao = input("Você deseja adicionar ou modificar produtos? (s/n): ").lower()
        if admin_opcao == 's':
            admin_action = input("Digite 'adicionar' para adicionar produtos ou 'modificar' para alterar estoque: ").lower()
            if admin_action == "adicionar":
                adicionar_produto()
            elif admin_action == "modificar":
                modificar_estoque()
    while True:
        print("\nProdutos disponíveis:")
        for produto_id, info in produtos.items():
            print(f"- ID: {produto_id} | {info['nome']} : {info['preco']} MCs (Estoque: {info['estoque']})")
        escolha = input("\nDigite o ID do produto que deseja comprar ou 'sair' para sair: ").lower()
        if escolha == "sair":
            break
        if escolha in produtos:
            produto = produtos[escolha]
            if produto["estoque"] > 0:
                quantidade = int(input(f"Quantas unidades de {produto['nome']} você deseja comprar? "))
                total = quantidade * produto["preco"]
                if usuario["MCs"] >= total:
                    if quantidade <= produto["estoque"]:
                        usuario["MCs"] -= total
                        produto["estoque"] -= quantidade
                        print(f"Compra realizada com sucesso! Total: {total} MCs")
                        print(f"Estoque atualizado: {produto['estoque']} unidades restantes.")
                        print(f"Saldo restante: {usuario['MCs']} MCs")
                    else:
                        print("Quantidade em estoque insuficiente.")
                else:
                    print("Saldo insuficiente de Mahindra Coins.")
            else:
                print(f"{produto['nome']} está fora de estoque.")
        else:
            print("Produto não encontrado.")

produtos = {
    "1" : {"nome" : "Caneca com a logo da Mahindra", "preco" : 2000, "estoque" : 50},
    "2" : {"nome" : "Ingresso Formula E", "preco" : 100000, "estoque" : 3},
    "3" : {"nome" : "Camiseta com a logo da Mahindra", "preco" : 5000, "estoque" : 15},
    "4" : {"nome" : "Boné da escuderia Mahindra", "preco" : 2500, "estoque" : 25}
}

