# Shopping list

shopping_list = []


def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")


def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)


def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))


while True:
    new_item = input("> ")
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)

# Number game

import random


def game():
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("My number is higher than {}".format(guess))
            else:
                print("My number is lower than {}".format(guess))
            guesses.append(guess)
    else:
        print("You didn't get it! My number was {}".format(secret_num))
    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")


# Letter game

import os
import random
import sys

words = [
    'apple',
    'banana',
    'coconut',
    'orange',
    'grape',
    'strawberry',
    'lime',
    'lemon',
    'kumquat',
    'blueberry'
]


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def draw(bad_guesses, good_guesses, secret_word):
    clear()

    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter, end='')
        print('\n\n')

        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
                else:
                print('_', end='')

                print('')

            def get_guess(bad_guesses, good_guesses):
                guess = input("Guess a letter: ").lower()

                if len(guess) != 1:
                    print("You can only guess a single letter!")
                elif guess in bad_guesses or guess in good_guesses:
                    print("You've already guessed that letter!")
                elif not guess.isalpha():
                    print("You can only guess letters!")
                else:
                    return guess

            def play(done):
                clear()
                secret_word = random.choice(words)
                bad_guesses = []
                good_guesses = []

                while True:
                    draw(bad_guesses, good_guesses, secret_word)
                    guess = get_guess(bad_guesses, good_guesses)

                    if guess in secret_word:
                        good_guesses.append(guess)
                        found = True
                        for letter in secret_word:
                            if letter not in good_guesses:
                                found = False
                        if found:
                            print("You win!")
                            print("The secret word was {}".format(secret_word))
                            done = True
                    else:
                        bad_guesses.append(guess)
                        if len(bad_guesses) == 7:
                            draw(bad_guesses, good_guesses, secret_word)
                            print("You lost!")
                            print("The secret word was {}".format(secret_word))
                            done = True

                    if done:
                        play_again = input("Play again? y/n").lower()
                        if play_again != 'n':
                            return play(done=False)
                        else:
                            sys.exit()

            def welcome():
                start = input("Press enter/return to start or Q to quit").lower()
                if start == 'q':
                    print("Bye!")
                    sys.exit()
                else:
                    return True

            print("Welcome to Letter Guess!")

            done = False

            while True:
                clear()
                welcome()
                play(done)
