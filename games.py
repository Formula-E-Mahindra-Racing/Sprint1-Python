import random
from helpers import meu_index, limpar_tela
from game_dictionaries import dict_game_forca, dict_game_complete_frase
from cadastro_login import usuarios

def game_forca():
    word = random.choice(dict_game_forca['words'])
    index = meu_index(dict_game_forca['words'], word)
    guessed = ["_"] * len(word)
    tries = 10
    print("\nBem vindo a Formula Forca!\nComo jogar: digite letras individualmente até alguma dela aparecer no display,\nfaça isso até formar a palavra completa.\nAtenção!\nHá palavras com mais de uma palavra, essas não possuirão espaço entre elas\nAs palavras não possuem assento ou 'ç'\n")
    while tries > 0:
        print(" ".join(guessed))
        print(f"Dica: {dict_game_forca['tips'][index]}")
        guess = input(f"Você tem {tries} tentativas\nDigite uma letra:\n--> ").upper()
        limpar_tela()
        if guess in word:
            print("Bom trabalho!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            print("Oops, tente de novo!")
            tries -= 1
        if "_" not in guessed:
            print("Você conseguiu! A palavra era", word)
            return True
    print("Fim de jogo! A palavra era", word)
    return False

def game_adivinhe_numero():
    number = random.randint(1, 100)
    tries = 10
    print("\nBem vindo ao Formula Adivinha!\nRegras: você terá que adivinhar um número entre 1 e 100 e nós te diremos se está muito alto ou muito baixo")
    while tries > 0:
        guess = int(input(f"Você tem {tries} tentativas\nDiga um número entre 1 e 100:\n--> "))
        if guess == number:
            print("Parabéns! O número era", number)
            return True
        elif guess < number:
            print("Muito baixo! Tente de novo.")
            tries -= 1
        else:
            print("Muito alto! Tente de novo.")
            tries -= 1
    print(f"Fim de jogo! O número era {number}")
    return False

def game_complete_frase():
    palavra = random.choice(dict_game_complete_frase['words'])
    index = meu_index(dict_game_complete_frase['words'], palavra)
    frase = dict_game_complete_frase['phrases'][index]
    dica = dict_game_complete_frase['tips'][index]
    print("\nBem vindo ao Formula Frase!\nNesse jogo será mostrado uma frase incompleta e o jogador deverá completa-la com uma palavra\nSomente uma dica sobre a palavra será mostrada\n")
    while True:
        print(f"Dica para a palavra: {dica}")
        guess = input(f"Complete a frase: {frase}\n--> ").lower()
        if guess == palavra:
            print(f"Parabéns! A frase era {frase.replace('...', palavra)}")
            return True
        else:
            limpar_tela()
            print("Oops, tente de novo!")

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

games = {
    "1": {"name": "Formula Forca", "game": game_forca},
    "2": {"name": "Formula Adivinha", "game": game_adivinhe_numero},
    "3": {"name": "Formula Frase", "game": game_complete_frase},
}