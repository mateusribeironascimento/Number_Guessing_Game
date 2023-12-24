import art
import random

print(art.logo)
print(f"\033[1m{'THE NUMBER GUESSING GAME':-^104}\033[0m")
print(f"I'm thinking of a number between 1 and 100.")

chances = 0

while True:
    difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficult == 'easy':
        chances = 10
        break
    elif difficult == 'hard':
        chances = 5
        break
    else:
        print("Please, choose a correct difficulty.")


def chosen_number():
    return random.randint(0, 101)


def game(attempts):
    number = chosen_number()
    while True:
        if attempts == 0:
            print('You do not have attempts remaining anymore, you lose! Try again :P')
            break
        else:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input('Make a guess: '))
            if number == guess:
                print(f"You got it! The answer was {number}, you win!")
                break
            elif number > guess:
                print("Too low.")
                attempts -= 1
                if attempts > 0:
                    print("Try again.")
            else:
                print("Too high.")
                attempts -= 1
                if attempts > 0:
                    print("Try again.")


game(chances)
