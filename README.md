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

## Explicando o <a href="path">Código</a> 🧑‍💻
 
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

## Explicando o <a href="path">Código</a> 🧑‍💻

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

## Explicando o <a href="path">Código</a> 🧑‍💻

```c
import random
```
<hr>

Esta linha importa o módulo random, que é utilizado para gerar números aleatórios.

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

















<center>Este projeto encontra sob a <a href="path">MIT License.</a></center>
