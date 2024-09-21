# Formula-themed games
import random
from helpers import meu_index, limpar_tela
from game_dictionaries import dict_game_forca, dict_game_complete_frase


def game_forca():
    word = random.choice(dict_game_forca['words'])
    index = meu_index(dict_game_forca['words'], word)
    guessed = ["_"] * len(word)
    tries = 10
    print("Bem vindo a Formula Forca!\nComo jogar: digite letras individualmente até alguma dela aparecer no display,\nfaça isso até formar a palavra completa.\nAtenção!\nHá adivinhações com duas palavras nas quais elas não possuirão espaço\nAs palavras não possuem assento ou 'ç'\n")
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
    number = random.randint(1, 100)  # a random number
    tries = 10
    print("Bem vindo ao Formula Adivinha!\nRegras: você terá que adivinhar um número entre 1 e 100 e nós te diremos se está muito alto ou muito baixo")
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
    print("Bem vindo ao Formula Frase!\nNesse jogo será mostrado uma frase incompleta e o jogador deverá completa-la com uma palavra\nSomente uma dica sobre a palavra será mostrada\n")
    while True:
        print(f"Dica para a palavra: {dica}")
        guess = input(f"Complete a frase: {frase}\n--> ").lower()
        if guess == palavra:
            print(f"Parabéns! A frase era {frase.replace('...', palavra)}")
            return True
        else:
            limpar_tela()
            print("Oops, tente de novo!")


games = {
    "1": {"name": "Formula Forca", "game": game_forca},
    "2": {"name": "Formula Adivinha", "game": game_adivinhe_numero},
    "3": {"name": "Formula Frase", "game": game_complete_frase},
}


def games_menu():
    while True:
        print("Escolha um jogo:")
        for key, game in games.items():
            print(f"{key}. {game['name']}")
        choice = input("Digite o número da escolha: ")
        if choice in games:
            if games[choice]["game"]():
                play_again = input("Deseja jogar novamente? (y/n): ")
                if play_again.lower() == "y":
                    limpar_tela()
                    continue
                else:
                    break
            else:
                play_again = input("Deseja jogar novamente? (y/n): ")
                if play_again.lower() == "y":
                    limpar_tela()
                    continue
                else:
                    break
        else:
            print("Opção inválida. Tente novamente!")
    return
game_complete_frase()
