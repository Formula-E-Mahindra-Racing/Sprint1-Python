# Sprint 2 - Computational Thinking With Python

## Equipe NexusCode

## Integrantes 👋
<ul>
    <li>Gabriel Barros (RM556309)</li>  
    <li>João Marcelo Furtado Romero (RM555199)</li>
    <li>Kayky Silva Stiliano (RM555148)</li>
    <li>Pedro Henrique Bizzo de Santana (RM557263)</li>
    <li>Pedro Henrique Mendes (RM555332)</li>
</ul>

## Instruções
O arquivo ```app.py``` é o arquivo principal que deve ser rodado e é recomendado usar o terminal no tamanho 75% ou tela cheia.

## Explicação do Projeto 📖
Um app em Python, feito para a Mahindra Racing/Tech Mahindra, que dá ao usuário escolhas de seção onde há uma seção de games, uma seção de dados capturados pelos sensores que é escolhida o circuito desejado no qual haverá duas opções de display das informações sendo uma "opções detalhadas" com todas os resultados encontrados para aquele circuito e outra "opções específicas" onde o usuário escolhe qual dado ele deseja ver tendo a possibilidade de fazer novas pesquisas também além de também ter a opção de procurar por dados dos pilotos. Por fim há uma seção de loja onde o usuário pode comprar merchandise entre outros produtos da equipe com as MahindraCoins, moedas virtuais que são de uso exclusivo do site.

 
## Dependências 📦
<ul>
    <li>helpers.py</li>
    <li>cadastro_login.py</li>
    <li>games.py</li>
    <li>sys_functions.py</li>
    <li>shop.py</li>
</ul>
<br>

## Explicando o <a href="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Python/blob/main/helpers.py">Código</a> 🧑‍💻
 
```c
def limpar_tela(linhas=10):
    print("\n" * linhas)
```
Essa função imprime várias linhas em branco para "limpar" a tela do console, o padrão é 10.
<br>
<hr>

```c
def forca_opcao(msg, opcoes, msg_erro):
    opcao = input(msg)
    while opcao not in opcoes:
        limpar_tela()
        print(msg_erro)
        opcao = input(msg)
    return opcao
```
Exibe uma mensagem (`msg`) e espera a entrada do usuário.
<br>
Continua solicitando uma opção válida (que esteja dentro do parâmetro `opcoes`) até o usuário digitar corretamente.
<br>
Se a entrada for inválida, imprime uma mensagem de erro (`msg_erro`) e limpa a tela antes de pedir novamente.
<hr>

```c
def meu_index(lista, buscar):
    for i in range(len(lista)):
        elem = lista[i]
        if elem == buscar:
            return i
    return False
```
Essa função `meu_index` procura por um elemento em uma lista e retorna a posição (índice) dele, caso o encontre. Se o elemento não estiver na lista, a função retorna `False`.
<hr>

```c
def verifica_numero(msg, msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    return int(num)
```
Essa função força o usuário a inserir um número válido.
Parâmetros: `msg`: Mensagem a ser exibida ao solicitar a entrada do usuário.
<br>
`msg_erro`: Mensagem de erro a ser exibida se a entrada não for um número.
<br>
Descrição: Solicita a entrada do usuário. Se a entrada não for numérica, exibe uma mensagem de erro e repete a solicitação até que um número seja inserido.
<br>
Retorno: O número inserido pelo usuário, convertido para inteiro.
<hr>

```c
def print_de_opcoes(lista, line_break=True):
    output = '\n'.join([f'- {item}' for item in lista]) if line_break else ', '.join(lista)
    print(output)
    return output1
```
Imprime uma lista de itens, um por linha se `line_break` for `True` (padrão), ou em uma única linha separada por vírgulas se for `False`.
<br>
Retorna a string formatada para possível reutilização.
<hr>

## Explicando o <a href="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Python/blob/main/cadastro_login.py">Código</a> 🧑‍💻

```c
def cadastrar_usuario():
    def solicitar_input(mensagem):
        while True:
            entrada = input(mensagem).strip()
            if entrada:
                return entrada
            else:
                print("Este campo não pode ficar vazio.")
    username = solicitar_input("Digite o nome de usuário para cadastro:\n--> ")
    if username in usuarios:
        print("Usuário já existe!")
        return None  
    senha = solicitar_input("Digite sua senha:\n--> ")
    email = solicitar_input("Digite seu email:\n--> ")
    is_admin = solicitar_input("O usuário é admin? (s/n):\n--> ").lower() == 's'
    if is_admin:
        mcs_inicial = 200000  
    else:
        mcs_inicial = 2500

    usuarios[username] = {
        "senha": senha, 
        "email": email, 
        "admin": is_admin, 
        "primeira_vez": True,
        "saldo_compras": [], 
        "MCs": mcs_inicial, 
        "carrinho": {},
        "endereco": {
            "estado": '',
            "rua": '',
            "numero": '',
            "complemento": '',
            "cep": ''
        }
    }
    print("Cadastro realizado com sucesso!")
    return login()
```
Solicita dados como nome de usuário, senha e email para cadastrar um novo usuário (Caso for vazio, a função auxiliar retorna a opção novamente.) e verifica se o nome de usuário já existe no dicionário `usuarios`. 
<br>
Define um saldo inicial de Mahindra Coins (MCs) de 200.000 para administradores e 2.500 para usuários normais.
<br>
Adiciona o novo usuário ao dicionário `usuarios` com suas respectivas informações. Após o cadastro, tenta realizar o login chamando a função `login()`.
<hr>

```c
def login():
    username = input("Digite o nome de usuário:\n--> ")
    if username not in usuarios:
        print("Usuário não encontrado!")
        return None  
    senha = input("Digite sua senha:\n--> ")
    if usuarios[username]["senha"] == senha:
        print(f"\nBem-vindo, {username}!")
        return {"username" : username, **usuarios[username]}  
    else:
        print("Senha incorreta!")
        return None
```
Solicita o nome de usuário e a senha para login. Verifica se o nome de usuário existe no dicionário `usuarios` e se a senha está correta. Se a autenticação for bem-sucedida, retorna as informações do usuário. Se falhar, exibe mensagens de erro apropriadas.
<hr>

```c
usuarios = {
    "admin": {
        "senha": "admin123", 
        "email": "admin@email.com", 
        "admin": True, 
        "primeira_vez": True,
        "saldo_compras": [], 
        "MCs": 200000, 
        "carrinho": {},
        "endereco": {
            "estado": 'estado',
            "rua": 'rua',
            "numero": 'numero',
            "complemento": 'complemento',
            "cep": 'cep'
        }
    },
    "user": {
        "senha": "userpass", 
        "email": "user@email.com", 
        "admin": False, 
        "primeira_vez": True,
        "saldo_compras": [], 
        "MCs": 2500, 
        "carrinho": {},
        "endereco": {
            "estado": 'estado',
            "rua": 'rua',
            "numero": 'numero',
            "complemento": 'complemento',
            "cep": 'cep'
        }
    }
}
```

Um dicionário que armazena informações dos usuários, onde as chaves são os nomes de usuário, e os valores são outros dicionários contendo senha, email, permissões de administrador, primeira vez jogando os minigames, saldo de compras, Mahindra Coins, carrinho de compras e o endereço.
<hr>

## Explicando o <a href="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Python/blob/main/app.py">Código</a> 🧑‍💻

```c
from helpers import forca_opcao, limpar_tela
from sys_functions import sys_dados
from cadastro_login import cadastrar_usuario, login
from shop import loja, produtos_disponiveis, produtos
from games import games_menu
```
Descrição: Importa as funções `forca_opcao` e `limpar_tela` do módulo `helpers`, a função `sys_dados` do módulo `sys_functions`, a função `cadastrar_usuario` e `login` do módulo `cadastro_login`, a função `loja`, a função `produtos_disponiveis` e o dicionário `produtos` do módulo `shop` e a função `games_menu` do módulo `games`.
<hr>

```c
opcoes = ['0', '1', '2', '3', '4']
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
                          "0 - Sair\n--> ", opcoes, "Opção inválida!")
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
            produtos_disponiveis()
            print("\nVocê precisa estar logado para acessar as funcionalidades da loja.")
    elif caminho == '4':
        opcao_login = forca_opcao("1 - Cadastro\n2 - Login\n--> ", opcoes, "Opção inválida!")
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
```
O arquivo `app.py` serve como o controlador principal, conectando as funcionalidades dos outros módulos do sistema. Ele cuida da interação com o usuário, fornecendo as opções de cadastro, login e acesso às diferentes funcionalidades, como o banco de dados de circuitos e pilotos, e a loja da Mahindra Racing.
<br>
Fluxo de Interação:
Login/Cadastro: O usuário começa no menu de login/cadastro. Caso já tenha uma conta, faz login, senão pode se cadastrar.
Menu Principal: Após o login, o usuário é direcionado ao menu principal (que é gerido em outro arquivo), onde pode acessar as funções de Banco de Dados (para consultar informações sobre circuitos e pilotos) ou a Loja (para gastar seus Mahindra Coins).
<hr>

## Explicando o <a href="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Python/blob/main/games.py">Código</a> 🧑‍💻

Essa seção implementa três mini-games temáticos.

```c
import random
```
Esta linha importa o módulo random, que é utilizado para gerar números aleatórios.
<hr>

```c
def game_forca():
    word = "MAHINDRA"
    guessed = ["_"] * len(word)
    tries = 6
    print("Welcome to Formula Forca!")
    while tries > 0:
        print(" ".join(guessed))
        guess = input("Guess a letter:\n--> ").upper()
        if guess in word:
            print("Good job!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            print("Oops, try again!")
            tries -= 1
        if "_" not in guessed:
            print("You won! The word was", word)
            return True
    print("Game over! The word was", word)
    return False
```

Função `game_forca()`:
<ul>
    <li>Esta função implementa o jogo da Forca.</li>
    <li>A palavra a ser adivinhada é "MAHINDRA".</li>
    <li>A variável guessed é uma lista de "", onde cada "" representa uma letra da palavra a ser adivinhada.</li>
    <li>O jogador tem 6 tentativas para adivinhar a palavra.</li>
    <li>O jogador insere uma letra e, se estiver correta, ela é revelada na posição correta na palavra.</li>
    <li>Se o jogador adivinhar todas as letras corretamente antes de esgotar as tentativas, ele vence o jogo.</li>
</ul>
<hr>

```c
def game_adivinhe_numero():
    number = random.randint(1, 100)  # a random number
    print("Welcome to Formula Guess!")
    while True:
        guess = int(input("Guess a number between 1 and 100:\n--> "))
        if guess == number:
            print("You won! The number was", number)
            return True
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
```

Função `game_adivinhe_numero()`:
<ul>
    <li>Esta função implementa o jogo de Adivinhar o Número.</li>
    <li>Um número aleatório é gerado entre 1 e 100.</li>
    <li>O jogador tem que adivinhar qual é esse número.</li>
    <li>O jogo dá feedback ao jogador se o palpite é muito alto ou muito baixo.</li>
</ul>
<hr>

```c
def game_complete_frase():
    frase = "CHECKED"
    print("Welcome to Formula Phrase!")
    while True:
        guess = input("Complete the phrase: 'In the final lap, the ... flag waves'\n--> ").upper()
        if guess == frase:
            print("You won! The phrase was 'In the final lap, the checked flag waves'")
            return True
        else:
            print("Oops, try again!")
```

Função `game_complete_frase()`:
<ul>
    <li>Esta função implementa o jogo de Completar a Frase.</li>
    <li>A frase a ser completada é "In the final lap, the ... flag waves".</li>
    <li>O jogador precisa inserir a palavra que completa a frase corretamente.</li>
</ul>
<hr>

```c
games = {
    "1": {"name": "Formula Forca", "game": game_forca},
    "2": {"name": "Formula Guess", "game": game_adivinhe_numero},
    "3": {"name": "Formula Phrase", "game": game_complete_frase},
}
```

Dicionário de Jogos:
<ul>
    <li>Um dicionário chamado games é criado para associar cada jogo a um número.</li>
    <li>Cada jogo tem um nome e uma função associada.</li>
</ul>

```c
def games_menu(usuario):
    while True:
        print("Escolha um jogo:")
        for key, game in games.items():
            print(f"{key}. {game['name']}")
        choice = input("Digite o número da escolha: ")
        if choice in games:
            if games[choice]["game"]():
                play_again = input("Deseja jogar novamente? (s/n): ")
                if play_again.lower() == "s":
                    limpar_tela()
                    continue
                else:
                    if usuario['primeira_vez']:
                        usuario['primeira_vez'] = False
                        usuario['MCs'] += 1000
                        print(f"{usuario['username']}, por ter jogado pela primeira vez algum de nossos jogos, você receberá 1000 MCs de bônus")
                    break
            else:
                play_again = input("Deseja jogar novamente? (s/n): ")
                if play_again.lower() == "s":
                    limpar_tela()
                    continue
                else:
                    if usuario['primeira_vez']:
                        usuario['primeira_vez'] = False
                        usuario['MCs'] += 1000
                        print(f"{usuario['username']}, por ter jogado pela primeira vez algum de nossos jogos, você receberá 1000 MCs de bônus")
                    break
        else:
            print("Opção inválida. Tente novamente!")
    return
```

Loop Principal:
<ul>
    <li>Quando a função é chamada o código entra em um loop infinito, onde o jogador pode escolher qual jogo jogar.</li>
    <li>O jogador seleciona um jogo digitando o número correspondente.</li>
    <li>Após jogar um jogo, o jogador tem a opção de jogar novamente ou sair.</li>
    <li>Se for a primeira vez do usuário ganhando algum jogo ele recebe 1000MCs de bônus.</li>
</ul>
<hr>

## Explicando o <a href="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Python/blob/main/game_dictionaries.py">Código</a> 🧑‍💻
Essa seção implementa os dicionários de informações importantes usados para os minigames.
```c
dict_game_forca = {
    "words": ["EPRIX", "CAMPEONATO", "CORRIDA", "ELETRICO", "CARROS", "PILOTOS", "EQUIPES", "TEMPORADA", "CLASSIFICACAO", "PONTOS", "POLEPOSITION", "VOLTAMAISRAPIDA", "PODIUM", "CAMPEAO", "FIA", "MAHINDRA", "GEN2", "GEN3", "ATTACKMODE", "FANBOOST", "SAFETYCAR", "VIRTUALSAFETYCAR", "DRS", "REGENERACAO", "ENERGIA", "BATERIA", "RECARGA", "CIDADE", "CIRCUITO", "URBANO", "SUSTENTABILIDADE", "MOBILIDADEELETRICA"],
    
    "tips": ["Cada corrida da Fórmula E", "Campeonato mundial de carros elétricos", "Prova de velocidade em um circuito", "Movido a eletricidade", "Veículos de competição", "Condutores dos carros", "Grupos que competem", "Período de corridas", "Ordem dos pilotos", "Sistema de pontuação", "Primeiro lugar na classificação", "Melhor tempo em uma volta", "Os três primeiros colocados", "Vencedor do campeonato", "Federação Internacional do Automóvel", "Nome da principal empresa de Formula E", "Segunda geração de carros", "Terceira geração de carros", "Modo de potência extra", "Votos dos fãs para potência extra", "Carro de segurança para neutralizar a corrida", "Sistema de segurança virtual", "Sistema de redução de arrasto", "Recuperação de energia na frenagem", "Fonte de potência dos carros", "Armazenamento de energia", "Abastecimento de energia", "Localização das corridas", "Local onde a corrida acontece", "Corrida em ambiente urbano", "Compromisso com o meio ambiente", "Transporte elétrico"]
}

dict_game_complete_frase = {
    "phrases": ["A Fórmula E é o ... do automobilismo!", "Corridas emocionantes e tecnologia de ...!", "Uma plataforma para a ... elétrica!", "O campeonato que ... os limites da inovação!", "E-Prix em cidades ao ... do mundo!", "A adrenalina da Fórmula E é ...!", "Uma ... para um futuro mais sustentável!"],
    
    "words": ["futuro", "ponta", "mobilidade", "desafia", "redor", "contagiante", "corrida"],
    
    "tips": ["Tempo que está por vir, o que está para acontecer.", "Parte mais alta ou avançada de algo.", "Facilidade de movimento, capacidade de se locomover.", "Tentar superar uma dificuldade, colocar à prova.", "Em volta de algo, em todos os lados.", "Que se espalha facilmente, que transmite emoções fortes.", "Competição de velocidade"]
}
```
<hr>

## Explicando o <a href="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Python/blob/main/sys_functions.py">Código</a> 🧑‍💻

Essa seção implementa um sistema de exibição de dados sobre os circuitos e pilotos.

```c
from helpers import forca_opcao, print_de_opcoes
```

Importa as funções `forca_opcao`, `print_de_opcoes` do módulo `helpers`.
<hr>

```c
def exibir_diagrama():
    print("\nDiagrama de informações:\n"
          "Umidade:\n - abaixo de 30% = ambiente seco\n - acima de 70% = possibilidade de chuva\n "
          "- entre 30 e 50% = estado ideal\n - entre 51 e 69% = em alerta de chuva\n"
          "\nTemperatura:\n - entre 25 e 50ºC = normal\n - acima de 80ºC = temperatura elevada\n - "
          "abaixo de 25ºC = temperatura baixa\n - entre 51 e 79 = temperatura em alerta\n"
          "\nProximidade:\n - acima ou igual a 200m = destroços não detectados\n - abaixo de 200m = "
          "objeto detectado\n - abaixo ou igual a 50m = destroços detectados\n")
```

Exibe uma explicação detalhada sobre os padrões de níveis de umidade, temperatura e proximidade com base em diferentes faixas, fornecendo informações sobre as condições climáticas e de proximidade.
<hr>

```c
def print_de_opcoes_circuitos(circuitos):
    print("\nCircuitos disponíveis:")
    for id_circuito, dados in circuitos.items():
        print(f"{id_circuito} - {dados['nome']}")
```

Exibe a lista de circuitos disponíveis, imprimindo o nome de cada circuito e seu respectivo ID.
<hr>

```c
def exibir_resultado(circuito_id):
    dados = circuitos[circuito_id]
    print(f"\nResultado: O circuito de {dados['nome']} está com umidade de {dados['umidade']}%, "
          f"temperatura de {dados['temperatura']}ºC, e proximidade de {dados['proximidade']} metros.")
```

Exibe o resultado detalhado das condições climáticas e de proximidade para um circuito específico, identificado pelo `circuito_id`.
<hr>

```c
def print_de_opcoes_pilotos(pilotos):
    print("\nPilotos disponíveis:")
    for piloto_id, dados in pilotos.items():
        print(f"{piloto_id} - {dados['nome']}")
```

Exibe a lista de pilotos disponíveis, mostrando seus IDs e nomes.
<hr>

```c
def exibir_dados_piloto(piloto_id):
    dados = pilotos[piloto_id]
    print(f"\nDados do piloto {dados['nome']}:\n"
          f"Equipe: {dados['equipe']}\n"
          f"Nacionalidade: {dados['nacionalidade']}\nColocação: {dados['colocacao']}\nPontos: {dados['pontos']}")
```

Exibe os detalhes de um piloto específico, incluindo equipe, nacionalidade, colocação e pontos.
<hr>

```c
def sys_dados():
    opcoes = ['0', '1', '2', '3']
    print(f"Bem-vindo ao banco de dados Mahindra Racing!")
    while True:
        tipo_dado = forca_opcao("Deseja acessar dados do circuito ou dos pilotos? (1 - Circuito, 2 - Pilotos)\n--> ",
                                opcoes, "Opção inválida!")
        if tipo_dado == '1':
            print_de_opcoes_circuitos(circuitos)
            circuito_id = forca_opcao("Digite o ID do circuito:\n--> ", circuitos.keys(), "Circuito inválido!")
            tipo_exibicao = forca_opcao("Você deseja ver opções detalhadas (1) ou específicas (2)?\n--> ", opcoes,
                                        "Opção inválida!")
            if tipo_exibicao == '1':
                exibir_diagrama()
                exibir_resultado(circuito_id)
            else:
                dado = forca_opcao("Qual dado específico deseja ver?\n1 - Umidade\n2 - Temperatura\n3 - Proximidade\n--> ",
                                   opcoes, "Opção inválida!")
                if dado == '1':
                    print(f"Umidade: {circuitos[circuito_id]['umidade']}%")
                elif dado == '2':
                    print(f"Temperatura: {circuitos[circuito_id]['temperatura']}ºC")
                elif dado == '3':
                    print(f"Proximidade: {circuitos[circuito_id]['proximidade']} metros")
        elif tipo_dado == '2':
            print_de_opcoes_pilotos(pilotos)
            piloto_id = forca_opcao("Digite o ID do piloto:\n--> ", pilotos.keys(), "ID do piloto inválido!")
            exibir_dados_piloto(piloto_id)
        continuar = forca_opcao("Deseja fazer uma nova pesquisa? (1 - Sim, 0 - Não)\n--> ", opcoes, "Opção inválida!")
        if continuar == '0':
            break
```
Uma função de controle principal que permite ao usuário escolher entre visualizar dados de circuitos ou pilotos. Dependendo da escolha do usuário, permite visualizar informações detalhadas ou específicas de um circuito ou piloto.
<hr>

## Explicando o <a href="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Python/blob/main/shop.py">Código</a> 🧑‍💻

Essa seção implementa uma loja virtual para a equipe Mahindra Racing, onde os usuários podem comprar itens como canecas, camisetas e ingressos usando a moeda virtual Mahindra Coins (MC). 
<br>

```c
def produtos_disponiveis():
    print("\nProdutos disponíveis:")
    for id_produto, info in produtos.items():
        print(f"{id_produto} - {info['nome']} : {info['preco']} MCs (Estoque: {info['estoque']})")
```

Printa o catálogo de produtos da loja.
<hr>

```c
def adicionar_ao_carrinho(usuario, id_produto, quantidade):
    if id_produto not in usuario["carrinho"]:
        usuario["carrinho"][id_produto] = 0
    usuario["carrinho"][id_produto] += quantidade
```

Adiciona um produto ao carrinho de compras do usuário. Se o produto já estiver no carrinho, aumenta a quantidade.
<hr>

```c
def finalizar_compra(usuario):
    if not usuario["endereco"].get("estado"):
        print("Precisamos do seu endereço para concluir a compra.")
        estado = input("Digite seu Estado:\n--> ")
        rua = input("Digite sua rua:\n--> ")
        numero = input("Digite o número da residência:\n--> ")
        complemento = input("Digite o complemento (deixe em branco se não houver):\n--> ")
        cep = input("Digite seu CEP:\n--> ")
        usuario["endereco"] = {
            "estado": estado,
            "rua": rua,
            "numero": numero,
            "complemento": complemento,
            "cep": cep
        }
    total_compra = 0
    itens_comprados = []
    for id_produto, quantidade in usuario["carrinho"].items():
        preco = produtos[id_produto]["preco"]
        estoque = produtos[id_produto]["estoque"]
        if quantidade <= estoque:
            total_compra += quantidade * preco
            produtos[id_produto]["estoque"] -= quantidade
            itens_comprados.append((produtos[id_produto]["nome"], quantidade, preco))
        else:
            print(f"Quantidade de {produtos[id_produto]['nome']} insuficiente no estoque. Sua compra será ajustada.")
            usuario["carrinho"][id_produto] = estoque
            total_compra += estoque * preco
            produtos[id_produto]["estoque"] = 0
            itens_comprados.append((produtos[id_produto]["nome"], estoque, preco))
    if usuario["MCs"] >= total_compra:
        usuario["MCs"] -= total_compra
        usuario["saldo_compras"].append({"itens": itens_comprados, "total": total_compra})
        usuario["carrinho"] = {}  
        endereco = usuario["endereco"]
        print(f"Compra realizada com sucesso! Total: {total_compra} MCs")
        print(f"Seu pedido será enviado para:\n"
              f"{endereco['rua']}, {endereco['numero']} {endereco['complemento']}\n"
              f"{endereco['estado']} - CEP: {endereco['cep']}")
    else:
        print("Você não tem Mahindra Coins suficientes para esta compra.")
```

Caso o usuário não tenha um endereço cadastrado ele é obrigado a preencher todos os campos e após isso finaliza-se a compra dos produtos no carrinho do usuário. Verifica se a quantidade de itens no carrinho está disponível no estoque, ajusta o carrinho se necessário e atualiza o estoque.
Deduz o total da compra do saldo de Mahindra Coins (MCs) do usuário, esvaziando o carrinho após a compra.
<hr>

```c
def exibir_compras_passadas(usuario):
    if not usuario["saldo_compras"]:
        print("Nenhuma compra realizada.")
    else:
        for id, compra in enumerate(usuario["saldo_compras"], start=1):
            print(f"\nCompra {id}:")
            for item in compra["itens"]:
                print(f"- Produto: {item[0]}, Quantidade: {item[1]}, Preço: {item[2]} MCs /cada")
            print(f"Total da compra: {compra['total']} MCs")
        print(f"Saldo restante: {usuario['MCs']} MCs")
```

Exibe as compras passadas do usuário. Para cada compra, exibe os itens comprados, suas quantidades, preços e o total gasto, além de mostrar o saldo restante de MCs.
<hr>

```c
def adicionar_produto():
    id_produto = str(len(produtos) + 1)
    nome_produto = input("Digite o nome do novo produto:\n--> ")
    preco = float(input("Digite o preço do produto:\n--> "))
    estoque = int(input("Digite a quantidade em estoque:\n--> "))
    produtos[id_produto] = {"nome": nome_produto, "preco": preco, "estoque": estoque}
    print(f"Produto {nome_produto} adicionado com sucesso!")
```

Permite a um administrador adicionar um novo produto à loja, solicitando ID, nome, preço e estoque.
<hr>

```c
def modificar_produto():
    id_produto = input("Digite o ID do produto que deseja modificar o estoque:\n--> ")
    if id_produto in produtos:
        novo_estoque = int(input("Digite a nova quantidade em estoque:\n--> "))
        produtos[id_produto]["estoque"] = novo_estoque
        print(f"Estoque do produto {produtos[id_produto]['nome']} atualizado para {novo_estoque}.")
        novo_preco = float(input("Digite o novo preço:\n--> "))
        produtos[id_produto]["preco"] = novo_preco
        print(f"Preço do produto {produtos[id_produto]['nome']} atualizado para {novo_preco}.")
    else:
        print("Produto não encontrado.")
```

Permite a um administrador modificar o estoque e o preço de um produto existente.
<hr>

```c
def remover_produto():
    id_produto = input("Digite o ID do produto que deseja remover:\n--> ")
    if id_produto in produtos:
        nome_produto = produtos[id_produto]["nome"]
        del produtos[id_produto]
        print(f"Produto '{nome_produto}' removido com sucesso!")
        novos_produtos = {}
        for novo_id, dados in enumerate(produtos.values(), start=1):
            novos_produtos[str(novo_id)] = dados
        produtos.clear()
        produtos.update(novos_produtos)
    else:
        print("Produto não encontrado.")
```

Permite a um administrador remover um produto existente.
<hr>

```c
def admin_zone():
    opcao_crud_admin = ["adicionar", "modificar", "remover"]
    admin_opcao = forca_opcao("Você deseja adicionar, modificar ou remover produtos? (s/n):\n--> ", ['s', 'n'], "Opção inválida!").lower()
    if admin_opcao == 's':
        admin_action = forca_opcao("Digite 'adicionar' para adicionar produtos, 'modificar' para alterar produto existente e 'remover' para remover produto:\n--> ", 
                                    opcao_crud_admin, "Opção inválida").lower()
        if admin_action == "adicionar":
            adicionar_produto()
        elif admin_action == "modificar":
            modificar_produto()
        elif admin_action == "remover":
            remover_produto()
        produtos_disponiveis()
```

Área de funcionalidades de um administrador onde funções anteriormente mencionadas são chamadas dependendo com a escolha do administrador.
<hr>

```c
def loja(usuario):
    print(f"Bem-vindo à loja da Mahindra Racing, {usuario['username']}!")
    print(f"Seu saldo atual é: {usuario['MCs']} MCs")
    while True:
        produtos_disponiveis()
        if usuario["admin"]:
            admin_zone()
        escolha = input("Digite o ID do produto que deseja comprar, 'compras' para ver suas compras, ou 'sair' para sair:\n--> ").lower()
        if escolha == "sair":
            print("Saindo da loja...")
            return
        if escolha == "compras":
            exibir_compras_passadas(usuario)
            continue
        if escolha in produtos:
            try:
                quantidade = int(input(f"Quantas unidades de {produtos[escolha]['nome']} você deseja adicionar ao carrinho?\n--> "))
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
            continue
        continuar = forca_opcao("Deseja continuar comprando? (s/n):\n--> ", ['s', 'n'], "Opção inválida!").lower()
        if continuar == 'n':
            finalizar_compra(usuario)
            break
```

Exibe a loja, mostrando os produtos disponíveis com seus respectivos preços e quantidades em estoque além de conter as funcionalidades dela. Se o usuário for um administrador, opções adicionais serão mostrados, como adicionar, modificar ou remover produtos.
<hr>

```c
produtos = {
    "1" : {"nome": "Caneca com a logo da Mahindra", "preco": 2000.0, "estoque": 50},
    "2" : {"nome": "Ingresso Formula E", "preco": 100000.0, "estoque": 3},
    "3" : {"nome": "Camiseta com a logo da Mahindra", "preco": 5000.0, "estoque": 15},
    "4" : {"nome": "Boné da escuderia Mahindra", "preco": 2500.0, "estoque": 25},
    "5" : {"nome": "Chaveiro com o símbolo da Mahindra", "preco": 500.0, "estoque": 100},
    "6" : {"nome": "Adesivo Mahindra Racing", "preco": 250.0, "estoque": 100}
}
```

Um dicionário que armazena o catálogo de produtos da loja virtual, onde as chaves são os IDs do respectivo produto, e os valores são outros dicionários contendo nome, preço e estoque do produto.
<hr>

<center>Este projeto encontra sob a <a href="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Python/blob/main/LICENSE">MIT License.</a></center>
