# Formula-themed games
import random

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

games = {
    "1": {"name": "Formula Forca", "game": game_forca},
    "2": {"name": "Formula Guess", "game": game_adivinhe_numero},
    "3": {"name": "Formula Phrase", "game": game_complete_frase},
}

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