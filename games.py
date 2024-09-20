# Formula-themed games
import random
from helpers import meu_index, limpar_tela

dict_game_forca = {
    "words": ["EPRIX", "CAMPEONATO", "CORRIDA", "ELETRICO", "CARROS", "PILOTOS", "EQUIPES", "TEMPORADA", "CLASSIFICACAO", "PONTOS", "POLEPOSITION", "VOLTAMAISRAPIDA", "PODIUM", "CAMPEAO", "FIA", "MAHINDRA", "GEN2", "GEN3", "ATTACKMODE", "FANBOOST", "SAFETYCAR", "VIRTUALSAFETYCAR", "DRS", "REGENERACAO", "ENERGIA", "BATERIA", "RECARGA", "CIDADE", "CIRCUITO", "URBANO", "SUSTENTABILIDADE", "MOBILIDADEELETRICA"],
    
    "tips": ["Cada corrida da Fórmula E", "Campeonato mundial de carros elétricos", "Prova de velocidade em um circuito", "Movido a eletricidade", "Veículos de competição", "Condutores dos carros", "Grupos que competem", "Período de corridas", "Ordem dos pilotos", "Sistema de pontuação", "Primeiro lugar na classificação", "Melhor tempo em uma volta", "Os três primeiros colocados", "Vencedor do campeonato", "Federação Internacional do Automóvel", "Nome da principal empresa de Formula E", "Segunda geração de carros", "Terceira geração de carros", "Modo de potência extra", "Votos dos fãs para potência extra", "Carro de segurança para neutralizar a corrida", "Sistema de segurança virtual", "Sistema de redução de arrasto", "Recuperação de energia na frenagem", "Fonte de potência dos carros", "Armazenamento de energia", "Abastecimento de energia", "Localização das corridas", "Local onde a corrida acontece", "Corrida em ambiente urbano", "Compromisso com o meio ambiente", "Transporte elétrico"]
}


def game_forca():
    word = random.choice(dict_game_forca['words'])
    index = meu_index(dict_game_forca['words'], word)
    guessed = ["_"] * len(word)
    tries = 10
    print("Bem vindo a Formula Forca!\nComo jogar: digite letras individualmente até alguma dela aparecer no display,\nfaça isso até formar a palavra completa.\nAtenção!\nHá adivinhações com duas palavras nas quais elas não possuirão espaço\nAs palavras não possuem assento ou 'ç'")
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
    frase = "CHECKED"
    print("Bem vindo ao Formula Frase!")
    while True:
        guess = input(
            "Complete a frase: 'In the final lap, the ... flag waves'\n--> ").upper()
        if guess == frase:
            print("Parabéns! A frase era 'In the final lap, the checked flag waves'")
            return True
        else:
            print("Oops, tente de novo!")


games = {
    "1": {"name": "Formula Forca", "game": game_forca},
    "2": {"name": "Formula Guess", "game": game_adivinhe_numero},
    "3": {"name": "Formula Phrase", "game": game_complete_frase},
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
game_forca()
