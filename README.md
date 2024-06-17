# Sprint 1 - Computational Thinking With Python

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
    <li>shop.py</li>
    <li>games.py</li>
    <li>sys_functions.py</li>
</ul>
 
<br>

## Explicando o <a href="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Python/blob/main/helpers.py">Código</a> 🧑‍💻
 
```c
def limpar_tela(linhas=20):
    for i in range(linhas):
        print("\n")
    return
```
Essa função imprime várias linhas em branco para "limpar" a tela do console.
Parâmetros: `linhas`: Número de linhas em branco a serem impressas. O padrão é 20.
<br>
Descrição: O loop `for` imprime uma nova linha (`\n`) a cada iteração, criando a impressão de uma tela limpa.
<hr>

```c
def meu_in(lista, buscar):
    for i in range(len(lista)):
        elem = lista[i]
        if elem == buscar:
            return True
    return False
```
Essa função verifica se um elemento está presente em uma lista.
Parâmetros: `lista`: A lista onde será feita a busca. 
<br>
`buscar`: O elemento a ser buscado na lista.
<br>
Descrição: Itera sobre cada elemento da lista. Se o elemento é igual ao buscado, retorna `True`.
Se o loop termina sem encontrar o elemento, retorna `False`.
<hr>

```c
def meu_index(lista, buscar):
    for i in range(len(lista)):
        elem = lista[i]
        if elem == buscar:
            return i
    return False
```
Essa função retorna o índice de um elemento em uma lista ou `False` se não for encontrado.
Parâmetros: `lista`: A lista onde será feita a busca. 
<br>
`buscar`: O elemento a ser buscado na lista.
<br>
Descrição: Itera sobre cada elemento da lista. Se o elemento é igual ao buscado, retorna seu índice.
Se o loop termina sem encontrar o elemento, retorna `False`.
<hr>

```c
def forca_opcao(msg, lista, msg_erro):
    opcao = input(msg)
    while not meu_in(lista, opcao):
        limpar_tela()
        print(msg_erro)
        opcao = input(msg)
    return opcao
```
Essa função força o usuário a escolher uma opção válida a partir de uma lista.
Parâmetros: `msg`: Mensagem a ser exibida ao solicitar a entrada do usuário. 
<br>
`lista`: Lista de opções válidas.
<br>
`msg_erro`: Mensagem de erro a ser exibida se a opção não for válida.
<br>
Descrição: Solicita a entrada do usuário. Se a entrada não estiver na lista, limpa a tela e mostra uma mensagem de erro, repetindo a solicitação até que uma opção válida seja inserida.
<br>
Retorno: A opção válida escolhida pelo usuário.
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
    output = ''
    for i in range(len(lista)):
        if line_break:
            output += f'- {lista[i]}\n'
        else:
            prefix = ''
            if i > 0:
                prefix = ', '
            output += f'{prefix}{lista[i]}'
    if line_break:
        print(output)
    return output
```
Essa função imprime uma lista de opções formatada, com ou sem quebras de linha.
Parâmetros: `lista`: A lista de opções a serem impressas.
<br>
`line_break`: Booleano que determina se as opções devem ser impressas com quebras de linha (`True`) ou em uma única linha (`False`).
<br>
Descrição: Itera sobre a lista, adicionando cada elemento a uma string de saída.
Se line_break é `True`, adiciona uma nova linha após cada elemento. Caso contrário, adiciona os elementos em uma linha, separados por vírgulas.
<br>
Retorno: A string formatada com as opções.
<hr>

## Explicando o <a href="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Python/blob/main/app.py">Código</a> 🧑‍💻

```c
from helpers import forca_opcao, limpar_tela
from sys_functions import sys_dados
from shop import loja
```
Descrição: Importa as funções `forca_opcao` e `limpar_tela` do módulo `helpers`, a função `sys_dados` do módulo `sys_functions` e a função `loja` do módulo `shop`.
<hr>

```c
nome_da_empresa = "Mahindra Racing"
lista_menu_opcao = ['1', '2', '3', '0']
```
Descrição: `lista_menu_opcao`: Contém as opções de menu principais ('1', '2', '3', '0').
<hr>


```c
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
```
Descrição: O loop `while True` exibe continuamente o menu principal até que o usuário escolha sair (opção '0').
<br>
Passos no Loop:
Exibição do Menu:
O sistema exibe uma mensagem de boas-vindas e solicita ao usuário que escolha uma das opções disponíveis no menu.
<br>
Processamento da Escolha:
A função `forca_opcao` é usada para garantir que o usuário insira uma opção válida. Caso contrário, uma mensagem de erro é exibida.
<br>
Limpeza da Tela:
`limpar_tela` é chamada para limpar a tela antes de continuar com a ação selecionada.
<br>
Execução da Função Correspondente:
Dependendo da escolha do usuário, uma das três funções é chamada: Jogos: `games`; Dados Capturados: `sys_dados`; Loja: `loja`; Saída do Loop:
Se a escolha for '0', o loop é interrompido e o programa termina.
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
    word = "FERRARI"
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
<hr>

Função `game_forca()`:
<ul>
    <li>Esta função implementa o jogo da Forca.</li>
    <li>A palavra a ser adivinhada é "MAHINDRA".</li>
    <li>A variável guessed é uma lista de "", onde cada "" representa uma letra da palavra a ser adivinhada.</li>
    <li>O jogador tem 6 tentativas para adivinhar a palavra.</li>
    <li>O jogador insere uma letra e, se estiver correta, ela é revelada na posição correta na palavra.</li>
    <li>Se o jogador adivinhar todas as letras corretamente antes de esgotar as tentativas, ele vence o jogo.</li>
</ul>

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
<hr>

Função `game_adivinhe_numero()`:
<ul>
    <li>Esta função implementa o jogo de Adivinhar o Número.</li>
    <li>Um número aleatório é gerado entre 1 e 100.</li>
    <li>O jogador tem que adivinhar qual é esse número.</li>
    <li>O jogo dá feedback ao jogador se o palpite é muito alto ou muito baixo.</li>
</ul>

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
<hr>

Função game_complete_frase():
<ul>
    <li>Esta função implementa o jogo de Completar a Frase.</li>
    <li>A frase a ser completada é "In the final lap, the ... flag waves".</li>
    <li>O jogador precisa inserir a palavra que completa a frase corretamente.</li>
</ul>

```c
games = {
    "1": {"name": "Formula Forca", "game": game_forca},
    "2": {"name": "Formula Guess", "game": game_adivinhe_numero},
    "3": {"name": "Formula Phrase", "game": game_complete_frase},
}
```
<hr>

Dicionário de Jogos:
<ul>
    <li>Um dicionário chamado games é criado para associar cada jogo a um número.</li>
    <li>Cada jogo tem um nome e uma função associada.</li>
</ul>

```c
while True:
    print("Choose a game:")
    for key, game in games.items():
        print(f"{key}. {game['name']}")
    choice = input("Enter the number of your choice: ")
    if choice in games:
        if games[choice]["game"]():
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() == "y":
                continue
            else:
                break
        else:
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() == "y":
                continue
            else:
                break
    else:
        print("Invalid choice. Try again!")
```
<hr>

Loop Principal:
<ul>
    <li>O código entra em um loop infinito, onde o jogador pode escolher qual jogo jogar.</li>
    <li>O jogador seleciona um jogo digitando o número correspondente.</li>
    <li>Após jogar um jogo, o jogador tem a opção de jogar novamente ou sair.</li>
</ul>
<hr>

## Explicando o <a href="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Python/blob/main/sys_functions.py">Código</a> 🧑‍💻

Essa seção implementa um sistema de exibição de dados sobre os circuitos e pilotos.

```c
from helpers import forca_opcao, meu_index, print_de_opcoes
```

Descrição: Importa as funções forca_opcao, verifica_numero, meu_index, print_de_opcoes do módulo helpers.
<hr>

```c
lista_tipo_dados = ['1', '2']
lista_dados_opcao = ['1', '0']
lista_dados_especificos = ['1', '2', '3', '4', '5']
```
<hr>

Definição de Listas:
<ul>
    <li>`lista_tipo_dados`: Uma lista que contém as opções disponíveis para o tipo de dados (circuito ou pilotos).</li>
    <li>`lista_dados_opcao`: Uma lista que contém as opções disponíveis para a escolha de continuar ou voltar ao menu principal.</li>
    <li>`lista_dados_especificos`: Uma lista que contém as opções disponíveis para dados específicos (umidade, temperatura, proximidade).</li>
</ul>

```c
lista_circuitos = ["Monaco", "Anhembi", "Paris"]
sensor_DHT_umidade = [35, 55, 15]
sensor_DHT_temp = [30, 15, 5]
sensor_proximidade_destrocos = [50, 150, 200]

lista_pilotos = ["King", "Mortara", "De Vries"]
equipe_pilotos = ["Mahindra", "Mahindra", "Mahindra"]
colocacao_pilotos = ["23", "20", "17"]
pontos_pilotos = ["4", "7", "21"]
```
<hr>

Listas relacionadas a circuitos e pilotos, contendo seus nomes e dados associados.

`sys_dados()`
<hr>
A função principal que controla o sistema de exibição de dados.

```c
def exibir_diagrama():
        print("\nDiagrama de informações:\n"
              "Umidade:\n - abaixo de 30% = ambiente seco\n - acima de 70% = possibilidade de chuva\n "
              "- entre 30 e 50 = estado ideal\n - entre 51 e 69 = em alerta de chuva\n"
              "Temperatura:\n - entre 25 e 50ºC = normal\n - acima de 80ºC = temperatura elevada\n - " 
              "abaixo de 25ºC = temperatura abaixo\n - entre 51 e 79 = temperatura em alerta\n"
              "Proximidade:\n - acima ou igual a 200m = destroços não detectados\n - abaixo de 200m = "
              "objeto detectado\n - abaixo ou igual a 50m = destroços detectados\n")
```
<hr>

Função para exibir informações sobre um diagrama.

```c
def exibir_resultado(local_circuito):
        print(f"\nResultado: O circuito de(o) {lista_circuitos[local_circuito]} está com "
              f"umidade de {sensor_DHT_umidade[local_circuito]}%, "
              f"temperatura está em {sensor_DHT_temp[local_circuito]}ºC, "
              f"e a distância do sensor de proximidade é de {sensor_proximidade_destrocos[local_circuito]} metros\n")
```
<hr>

Função para exibir os resultados dos circuitos.

```c
def exibir_dado_especifico(local_circuito, dado_especifico):
        if dado_especifico == '1':
            print("Umidade:\n - abaixo de 30% = ambiente seco\n - acima de 70% = possibilidade de chuva\n - entre 30 e 50% = estado ideal\n - entre 51 e 69% = em alerta de chuva\n"
                  f"Umidade está em {sensor_DHT_umidade[local_circuito]}%\n")
        elif dado_especifico == '2':
            print("Temperatura:\n - entre 25 e 50ºC = normal\n - acima de 80ºC = temperatura elevada\n - " 
                  "abaixo de 25ºC = temperatura abaixo\n - entre 51 e 79 = temperatura em alerta\n"
                  f"Temperatura está em {sensor_DHT_temp[local_circuito]}ºC\n")
        elif dado_especifico == '3':
            print("Proximidade:\n - acima ou igual a 200m = destroços não detectados\n - abaixo de 200m = "
                  "objeto detectado\n - abaixo ou igual a 50m = destroços detectados\n"
                  f"Distância do sensor de proximidade é de {sensor_proximidade_destrocos[local_circuito]} metros\n")
```
<hr>

Função para exibir um dado específico de um circuito (umidade, temperatura, proximidade) escolhido pelo usuário.

```c
def exibir_dados_piloto(local_piloto):
        print(f"\nDados do piloto {lista_pilotos[local_piloto]}:\n"
              f"Equipe: {equipe_pilotos[local_piloto]}\n"
              f"Colocação: {colocacao_pilotos[local_piloto]}\n"
              f"Pontos: {pontos_pilotos[local_piloto]}\n")
```
<hr>

Função para exibir os dados de um piloto escolhido pelo usuário.
<br>
O código entra em um loop enquanto o usuário quiser continuar exibindo dados.

```c
 while True:
        escolha_tipo_dado = forca_opcao("Deseja acessar dados do circuito ou dos pilotos? (1 - Circuito, 2 - Pilotos)\n--> ",
                                        lista_tipo_dados, "Opção inválida! Digite 1 para Circuito ou 2 para Pilotos.")
        if escolha_tipo_dado == '1':
            escolha_circuito = forca_opcao("Digite um circuito que deseja procurar dados\n --> ", lista_circuitos, "Opção Inválida!\nPor favor, escolha um dos circuitos disponíveis:\n" + print_de_opcoes(lista_circuitos))
            local_circuito = meu_index(lista_circuitos, escolha_circuito)
            escolha_tipo_dados = forca_opcao("Você deseja ver opções detalhadas ou específicas? (1 - opções detalhadas e 2 - opções específicas)\n--> ",
                                             lista_tipo_dados, "Digite apenas os números correspondentes ao caminho indicado")
            if escolha_tipo_dados == '1':
                exibir_diagrama()
                exibir_resultado(local_circuito)
            elif escolha_tipo_dados == '2':
                dados_especifico = forca_opcao("Qual dado você deseja procurar?\n 1 - Umidade\n 2 - Temperatura\n 3 - Proximidade\n--> ",
                                               lista_dados_especificos, "Digite apenas os números correspondentes ao caminho indicado")
                exibir_dado_especifico(local_circuito, dados_especifico)
        
        elif escolha_tipo_dado == '2':
            escolha_piloto = forca_opcao("Digite o piloto que deseja procurar dados\n --> ", lista_pilotos, "Opção inválida!\nPor favor, escolha um dos pilotos disponíveis:\n" + print_de_opcoes(lista_pilotos))
            local_piloto = meu_index(lista_pilotos, escolha_piloto)
            exibir_dados_piloto(local_piloto)

        escolha_dados = forca_opcao("O que você deseja fazer?\n 1 - Nova pesquisa\n 0 - Voltar para o menu\n--> ",
                                    lista_dados_opcao, "Opção inválida! Digite apenas os números correspondentes ao caminho indicado")
        if escolha_dados == '1':
            continue
        elif escolha_dados == '0':
            break
```
<hr>

Loop Principal:
<ul>
    <li>O usuário escolhe entre acessar dados de circuito ou pilotos.</li>
    <li>Se escolher circuito, ele seleciona um circuito específico e pode optar por ver opções detalhadas ou específicas sobre esse circuito.</li>
    <li>Se escolher opções detalhadas, mostra um diagrama e os resultados do circuito.</li>
    <li>Se escolher opções específicas, mostra um dado específico sobre o circuito (umidade, temperatura, proximidade).</li>
    <li>Se escolher pilotos, ele seleciona um piloto específico e mostra os dados desse piloto.</li>
    <li>Após a exibição dos dados, o usuário pode optar por fazer uma nova pesquisa ou voltar ao menu principal.</li>
</ul>
<hr>

## Explicando o <a href="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Python/blob/main/shop.py">Código</a> 🧑‍💻

Essa seção implementa uma loja virtual para a equipe Mahindra Racing, onde os usuários podem comprar itens como canecas, camisetas e ingressos usando a moeda virtual Mahindra Coins (MC). 
<br>

```c
from helpers import print_de_opcoes, forca_opcao, limpar_tela, verifica_numero
```
Este trecho importa funções utilitárias de um módulo chamado `helpers`.

<hr>

```c
def desconto_final(number, discount):
    number = number - (number * (discount / 100))
    return number
```
<hr>

Calcula o valor final após a aplicação de um desconto percentual (`discount`) sobre um valor (`number`).

```c
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
```
<hr>
<ul>
    <li>A função principal `loja()` simula a operação da loja.</li>
    <li>Se for a primeira vez que o usuário acessa a loja, uma mensagem de boas-vindas é exibida.</li>
    <li>Define os preços dos produtos e inicializa uma lista de preços e uma lista de itens disponíveis para compra.</li>
    <li>Inicia um loop onde o usuário pode selecionar itens para comprar.</li>
    <li>Mostra as opções de compra utilizando a função `print_de_opcoes()`.</li>
    <li>Solicita a escolha do usuário utilizando a função `forca_opcao()`.</li>
    <li>Solicita a quantidade do item a ser comprado e calcula o subtotal.</li>
    <li>Atualiza o total da compra e exibe o subtotal.</li>
    <li>Pergunta ao usuário se deseja continuar comprando ou finalizar.</li>
    <li>Se o usuário optar por finalizar, aplica um desconto baseado no valor total da compra.</li>
    <li>Exibe o total final após o desconto e uma mensagem de agradecimento.</li>
</ul>
<hr>

<center>Este projeto encontra sob a <a href="path">MIT License.</a></center>
