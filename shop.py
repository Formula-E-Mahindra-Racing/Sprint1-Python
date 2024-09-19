def adicionar_produto():
    id_produto = input("Digite o ID do novo produto: ")
    nome_produto = input("Digite o nome do novo produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))
    if id_produto in produtos:
        print("Produto já existe. Use 'modificar' para alterar o produto existente.")
    else:
        produtos[id_produto] = {"nome": nome_produto, "preco": preco, "estoque": estoque}
        print(f"Produto {nome_produto} adicionado com sucesso!")

def modificar_estoque():
    id_produto = input("Digite o ID do produto que deseja modificar o estoque: ")
    if id_produto in produtos:
        novo_estoque = int(input("Digite a nova quantidade em estoque: "))
        produtos[id_produto]["estoque"] = novo_estoque
        print(f"Estoque do produto {produtos[id_produto]['nome']} atualizado para {novo_estoque}.")
        novo_preco = float(input("Digite o novo preço: "))
        produtos[id_produto]["preco"] = novo_preco
        print(f"Preço do produto {produtos[id_produto]['preco']} atualizado para {novo_preco}.")
    else:
        print("Produto não encontrado.")

def loja(usuario):
    print("Bem-vindo à loja da Mahindra Racing!")
    while True:
        print("\nProdutos disponíveis:")
        for id_produto, info in produtos.items():
            print(f"- ID: {id_produto} | {info['nome']} : {info['preco']} MCs (Estoque: {info['estoque']})")
        if usuario["admin"]:
            admin_opcao = input("Você deseja adicionar ou modificar produtos? (s/n): ").lower()
            if admin_opcao == 's':
                admin_action = input("Digite 'adicionar' para adicionar produtos ou 'modificar' para alterar estoque: ").lower()
                if admin_action == "adicionar":
                    adicionar_produto()
                elif admin_action == "modificar":
                    modificar_estoque()
        for id_produto, info in produtos.items():
            print(f"- ID: {id_produto} | {info['nome']} : {info['preco']} MCs (Estoque: {info['estoque']})")
        escolha = input("\nDigite o ID do produto que deseja comprar ou 'sair' para sair: ").lower()
        if escolha == "sair":
            break
        if escolha in produtos:
            if produtos[escolha]["estoque"] > 0:
                quantidade = int(input(f"Quantas unidades de {produtos[escolha]['nome'].title()} você deseja comprar? "))
                if quantidade <= produtos[escolha]["estoque"]:
                    total = quantidade * produtos[escolha]["preco"]
                    if usuario["MCs"] >= total:
                        usuario["MCs"] -= total
                        produtos[escolha]["estoque"] -= quantidade
                        print(f"Compra realizada com sucesso! Total: {total} MCs")
                        print(f"Estoque atualizado: {produtos[escolha]['estoque']} unidades restantes.")
                    else:
                        print("Você não tem Mahindra Coins suficientes para esta compra.")
                else:
                    print("Quantidade em estoque insuficiente.")
            else:
                print(f"{produtos[escolha]['nome'].title()} está fora de estoque.")
        else:
            print("Produto não encontrado.")
        
produtos = {
    "1" : {"nome" : "Caneca com a logo da Mahindra", "preco" : 2000.0, "estoque" : 50},
    "2" : {"nome" : "Ingresso Formula E", "preco" : 100000.0, "estoque" : 3},
    "3" : {"nome" : "Camiseta com a logo da Mahindra", "preco" : 5000.0, "estoque" : 15},
    "4" : {"nome" : "Boné da escuderia Mahindra", "preco" : 2500.0, "estoque" : 25},
    "5" : {"nome" : "Chaveiro com o símbolo da Mahindra", "preco" : 500.0, "estoque" : 100},
    "6" : {"nome" : "Adesivo Mahindra Racing", "preco" : 250.0, "estoque" : 100}
}
