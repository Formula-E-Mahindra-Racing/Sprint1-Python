def adicionar_ao_carrinho(usuario, id_produto, quantidade):
    if id_produto not in usuario["carrinho"]:
        usuario["carrinho"][id_produto] = 0
    usuario["carrinho"][id_produto] += quantidade

def finalizar_compra(usuario):
    total_compra = 0
    for id_produto, quantidade in usuario["carrinho"].items():
        preco = produtos[id_produto]["preco"]
        estoque = produtos[id_produto]["estoque"]
        if quantidade <= estoque:
            total_compra += quantidade * preco
            produtos[id_produto]["estoque"] -= quantidade
        else:
            print(f"Quantidade de {produtos[id_produto]['nome']} insuficiente no estoque. Sua compra será ajustada.")
            usuario["carrinho"][id_produto] = estoque
            total_compra += estoque * preco
            produtos[id_produto]["estoque"] = 0
    if usuario["MCs"] >= total_compra:
        usuario["MCs"] -= total_compra
        usuario["carrinho"] = {}  
        print(f"Compra realizada com sucesso! Total: {total_compra} MCs")
    else:
        print("Você não tem Mahindra Coins suficientes para esta compra.")
    
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
        while True:
            escolha = input("\nDigite o ID do produto que deseja comprar ou 'sair' para sair: ").lower()
            if escolha == "sair":
                print("Saindo da loja...")
                break
            if escolha in produtos:
                try:
                    quantidade = int(input(f"Quantas unidades de {produtos[escolha]['nome']} você deseja adicionar ao carrinho? "))
                except ValueError:
                    print("Por favor, insira um número válido para a quantidade.")
                    continue
                if quantidade <= produtos[escolha]["estoque"]:
                    adicionar_ao_carrinho(usuario, escolha, quantidade)
                    print(f"{quantidade} unidade(s) de {produtos[escolha]['nome']} adicionada(s) ao carrinho.")
                else:
                    print("Quantidade em estoque insuficiente.")
            else:
                print("Produto não encontrado.")
            continuar = input("Deseja continuar comprando? (s/n): ").lower()
            if continuar == 'n':
                finalizar_compra(usuario)
                break  
        if escolha == "sair":
            break

produtos = {
    "1" : {"nome" : "Caneca com a logo da Mahindra", "preco" : 2000.0, "estoque" : 50},
    "2" : {"nome" : "Ingresso Formula E", "preco" : 100000.0, "estoque" : 3},
    "3" : {"nome" : "Camiseta com a logo da Mahindra", "preco" : 5000.0, "estoque" : 15},
    "4" : {"nome" : "Boné da escuderia Mahindra", "preco" : 2500.0, "estoque" : 25},
    "5" : {"nome" : "Chaveiro com o símbolo da Mahindra", "preco" : 500.0, "estoque" : 100},
    "6" : {"nome" : "Adesivo Mahindra Racing", "preco" : 250.0, "estoque" : 100}
}
