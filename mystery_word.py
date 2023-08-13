import random
import time
import json
from anipage import start_screen
import pyfiglet
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

very_easy_pics = {
    0: "  +---+\n      |\n      |\n      |\n      |\n      |\n      |\n      |\n      |\n      |\n=========",

    1: "  +---+\n  |   |\n      |\n      |\n      |\n      |\n      |\n      |\n      |\n      |\n=========",

    2: "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n      |\n      |\n      |\n      |\n=========",

    3: "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n      |\n      |\n      |\n      |\n=========",

    4: "  +---+\n  |   |\n  O   |\n  |   |\n /    |\n      |\n      |\n      |\n      |\n      |\n=========",

    5: "  +---+\n  |   |\n  O   |\n  |   |\n /|   |\n      |\n      |\n      |\n      |\n      |\n=========",

    6: "  +---+\n  |   |\n  O   |\n  |   |\n /|\  |\n      |\n      |\n      |\n      |\n      |\n=========",

    7: "  +---+\n  |   |\n  O   |\n  |   |\n /|\  |\n|     |\n      |\n      |\n      |\n      |\n=========",

    8: "  +---+\n  |   |\n  O   |\n  |   |\n /|\  |\n| |   |\n      |\n      |\n      |\n      |\n=========",

    9: "  +---+\n  |   |\n  O   |\n  |   |\n /|\  |\n| | | |\n      |\n      |\n      |\n      |\n=========",

    10: "  +---+\n  |   |\n  O   |\n  |   |\n /|\  |\n| | | |\n  |   |\n      |\n      |\n      |\n=========",

    11: "  +---+\n  |   |\n  O   |\n  |   |\n /|\  |\n| | | |\n  |   |\n /    |\n      |\n      |\n=========",

    12: "  +---+\n  |   |\n  O   |\n  |   |\n /|\  |\n| | | |\n  |   |\n / \  |\n|     |\n      |\n=========",

    13: "  +---+\n  |   |\n  O   |\n  |   |\n /|\  |\n| | | |\n  |   |\n / \  |\n|   | |\n      |\n=========",

    14: "  +---+\n  |   |\n  O   |\n  |   |\n /|\  |\n| | | |\n  |   |\n / \  |\n|   | |\n      |\n========="
}

easy_pics = {
    0: "  +---+\n      |\n      |\n      |\n      |\n      |\n      |\n=========",

    1: "  +---+\n  O   |\n      |\n      |\n      |\n      |\n      |\n=========",

    2: "  +---+\n  O   |\n /    |\n      |\n      |\n      |\n      |\n=========",

    3: "  +---+\n  O   |\n /|   |\n      |\n      |\n      |\n      |\n=========",

    4: "  +---+\n  O   |\n /|\  |\n      |\n      |\n      |\n      |\n=========",

    5: "  +---+\n  O   |\n /|\  |\n|     |\n      |\n      |\n      |\n=========",

    6: "  +---+\n  O   |\n /|\  |\n| |   |\n      |\n      |\n      |\n=========",

    7: "  +---+\n  O   |\n /|\  |\n| | | |\n      |\n      |\n      |\n=========",

    8: "  +---+\n  O   |\n /|\  |\n| | | |\n /    |\n      |\n      |\n=========",

    9: "  +---+\n  O   |\n /|\  |\n| | | |\n / \  |\n|     |\n      |\n=========",

    10: "  +---+\n  O   |\n /|\  |\n| | | |\n / \  |\n|   | |\n      |\n=========",

    11: "  +---+\n  O   |\n /|\  |\n| | | |\n / \  |\n|   | |\n      |\n========="
}

medium_pics = {
    0: "  +---+\n      |\n      |\n      |\n      |\n      |\n=========",

    1: "  +---+\n  O   |\n      |\n      |\n      |\n      |\n=========",

    2: "  +---+\n  O   |\n /    |\n      |\n      |\n      |\n=========",

    3: "  +---+\n  O   |\n /|   |\n      |\n      |\n      |\n=========",

    4: "  +---+\n  O   |\n /|\  |\n      |\n      |\n      |\n=========",

    5: "  +---+\n  O   |\n /|\  |\n|     |\n      |\n      |\n=========",

    6: "  +---+\n  O   |\n /|\  |\n| |   |\n      |\n      |\n=========",

    7: "  +---+\n  O   |\n /|\  |\n| | | |\n      |\n      |\n=========",

    8: "  +---+\n  O   |\n /|\  |\n| | | |\n /    |\n      |\n=========",

    9: "  +---+\n  O   |\n /|\  |\n| | | |\n /    |\n      |\n========="

}

regular_pics = {
    0: "  +---+\n      |\n      |\n      |\n      |\n      |\n=========\n",

    1: "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========\n",

    2: "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========\n",

    3: "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========\n",

    4: "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========\n",

    5: "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========\n",

    6: "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========\n",

    7: "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n",

    8: "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n"
}

hard_pics = {
    0: "  +---+\n      |\n      |\n      |\n      |\n      |\n=========\n",

    1: "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========\n",

    2: "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========\n",

    3: "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========\n",

    4: "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========\n",

    5: "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n",

    6: "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n"
}

xtra_hard_pics = {
    0: "  +---+\n      |\n      |\n      |\n      |\n      |\n=========\n",

    1: "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========\n",

    2: "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========\n",

    3: "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========\n",

    4: "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n",

    5: "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n"
}

impossible_pics = {
    0: "  +---+\n      |\n      |\n      |\n      |\n      |\n=========\n",

    1: "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========\n",

    2: "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========\n",

    3: "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n"
}

difficulty_lives = {
    'very easy': 15,
    'easy': 12,
    'medium': 10,
    'regular': 8,
    'hard': 6,
    'xtra hard': 5,
    'impossible': 3
}


def sleep(text=None):
    if text is None:
        time.sleep(.5)
        print()
    else:
        time.sleep(.2)
        print(f'\n{text}\n')
        time.sleep(.3)


def format_time(seconds):
    minutes = int(seconds // 60)
    remaining_seconds = int(seconds % 60)
    formatted_time = f"{minutes} minutes and {remaining_seconds} seconds"
    return formatted_time


def select_word(filename, word_length_setting):
    length_ranges = {
        'Xtreme': (20, 22),
        'Greater': (17, 19),
        'Longer': (13, 16),
        'Regular': (9, 12),
        'Small': (5, 8),
        'Mini': (2, 4)
    }
    min_length, max_length = length_ranges[word_length_setting]
    with open(filename, 'r') as file:
        file = file.read()
    words_list = file.split()
    filtered_words = [
        word for word in words_list if min_length <= len(word) <= max_length]  # list comprehension, very cool!
    random_word = random.choice(filtered_words)
    return random_word


def load_game_number():
    with open('game_number.txt', 'r') as file:
        return int(file.read().strip())


def save_game_number(game_number):
    with open('game_number.txt', 'w') as file:
        file.write(str(game_number) + '\n')


def load_game_difficulty():
    with open('game_difficulty.txt', 'r') as file:
        return str(file.read().strip())


def save_game_difficulty(game_difficulty):
    with open('game_difficulty.txt', 'w') as file:
        file.write(str(game_difficulty) + '\n')


def load_word_length():
    with open('word_length.txt', 'r') as file:
        return str(file.read().strip())


def save_word_length(word_length):
    with open('word_length.txt', 'w') as file:
        file.write(str(word_length) + '\n')


def load_score_history():
    with open("score_history.txt", 'r') as score_history:
        return json.load(score_history)


def save_score_history(score_history):
    with open('score_history.txt', 'w') as file:
        json.dump(score_history, file)


def load_high_score():
    with open('high_score.txt', 'r') as file:
        return float(file.read().strip())


def save_high_score(high_score):
    with open('high_score.txt', 'w') as file:
        file.write(str(high_score) + '\n')


def count_words_by_length(filename):
    word_counts = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip()
                length = len(word)
                if length not in word_counts:
                    word_counts[length] = 0
                word_counts[length] += 1
    except FileNotFoundError:
        print("File not found.")
        return []

    sorted_counts = sorted(word_counts.items(), reverse=True)
    result = [f"{length} letter words: {count}" for length,
              count in sorted_counts]
    return result


def display_letters(word, guessed_letters, game_difficulty, wrong_guesses):
    if game_difficulty == 'Very Easy':
        print(very_easy_pics[wrong_guesses])
    elif game_difficulty == 'Easy':
        print(easy_pics[wrong_guesses])
    elif game_difficulty == 'Medium':
        print(medium_pics[wrong_guesses])
    elif game_difficulty == 'Regular':
        print(regular_pics[wrong_guesses])
    elif game_difficulty == 'Hard':
        print(hard_pics[wrong_guesses])
    elif game_difficulty == 'Xtra Hard':
        print(xtra_hard_pics[wrong_guesses])
    elif game_difficulty == 'Impossible':
        print(impossible_pics[wrong_guesses])
    print()
    chosen_word = ''
    for letter in word:
        if letter.upper() in guessed_letters:
            chosen_word += letter.lower() + ' '
        else:
            chosen_word += '_ '
    if chosen_word:
        chosen_word = chosen_word[0].upper() + chosen_word[1:]
    return chosen_word


def user_guess(counter, guessed_letters, random_word, display, game_difficulty):
    while counter > 0:
        if counter == difficulty_lives[game_difficulty.lower()] and len(guessed_letters) == 0:
            print(f'You have {counter} guesses remaining!!')
        if counter < difficulty_lives[game_difficulty.lower()] and counter > 1:
            print(f'You only have {counter} wrong attempts remaining!!')
        if counter == 1:
            print(
                f'Last chance!! You have {counter} wrong attempts remaining!!')
        if counter == difficulty_lives[game_difficulty.lower()] and len(guessed_letters) > 0:
            print(f'You still have {counter} wrong attempts remaining!!')

        formatted_multi_guesses = ', '.join(
            guessed_letters[:-1]) + ' & ' + guessed_letters[-1] if len(guessed_letters) > 1 else ''
        formatted_guesses = ', '.join(guessed_letters) if len(
            guessed_letters) == 1 else ''

        if formatted_guesses:
            print(f'So far you have guessed: {formatted_guesses}')
        if formatted_multi_guesses:
            print(f'So far you have guessed: {formatted_multi_guesses}')

        print()  # aesthetic empty line

        guess = input('Guess a letter: > ').lower().strip()
        sleep('...')
        if guess.lower() == 'ex':
            exiting_game_text = pyfiglet.figlet_format(
                text="//EXITING GAME//", font='smslant')
            print(exiting_game_text)
            print('//EXITING CURRENT GAME//')
            sleep('...')
            return None
        if guess.lower() == random_word.lower():
            sleep('...')
            return guess
        elif len(guess) > 1:
            print('Please enter only (1) letter at a time!')
            sleep('...')
            print(f'\n{display}\n')
        if not guess.isalpha():
            print('Please enter only a letter!')
            sleep('...')
            print(f'\n{display}\n')
        elif guess.upper() in guessed_letters and guess.upper() != 'F':
            print(f'You have already guessed: {guess}\n')
            sleep('...')
            print(f'\n{display}\n')
        elif guess.upper() == 'F' and guess.upper() in guessed_letters:
            f_pressed_text = pyfiglet.figlet_format(
                text="'F' PRESSED", font="standard", width=50)
            print(f_pressed_text)
            print("\nYou have paid respects.\nPlease guess again.")
            sleep('...')
        elif guess in random_word and guess not in guessed_letters:
            return guess

        else:
            return guess[0]


def play_game(filename, score_history, high_score, word_length_setting, game_difficulty):
    play = True
    game_number = load_game_number()
    high_score = load_high_score()
    wrong_guesses = 0

    congrats_statements = [
        "Great job!",
        "Well done!",
        "You're a genius!",
        "You're on fire!",
        "Fantastic guess!",
        "Incredible!",
        "Impressive work!",
        "You nailed it!",
        "You're a word wizard!",
        "You're unstoppable!",
        "Bravo!",
        "You're amazing!",
        "You've got this down!",
        "Outstanding!",
        "You're a pro!",
        "Spectacular!",
        "You're on a roll!",
        "You're killing it!",
        "You're a master of this!",
        "You're the word detective!",
        "You're rocking it!",
        "Terrific job!",
        "You're a word expert!",
        "You're making it look easy!",
        "Way to go!",
        "You're getting closer!",
        "You're spot on!",
        "Excellent guess!",
        "You're on the mark!",
        "You're a word champion!"
    ]

    dissapoint_statements = [
        "Oh No!",
        "I'm so sorry!",
        "Ooops, wrong guess!",
        "Better luck next time!",
        "Oh no, that's not correct!",
        "Keep trying!",
        "Don't worry, you'll get one soon enough!",
        "Not quite right.",
        "Almost there, but not quite.",
        "You're on the right track!",
        "Not the letter we're looking for.",
        "Try a different letter.",
        "You're so close!",
        "The secret word isn't that one.",
        "That's not the missing piece.",
        "It's not that letter.",
        "Keep searching, you'll find it!"
    ]

    win_statements = [
        "You're literally the smartest person ever!!",
        "OMG how'd you do that?! You're amazing!!",
        "You made this game look so easy!!",
        "You've cracked the code like a master detective!",
        "Congratulations, word wizard! You've triumphed!",
        "Bravo! You've emerged victorious as the word master!",
        "Incredible job! You've conquered the word challenge!",
        "You've shown unparalleled skill in solving mysteries of words!"
    ]

    record_statements = [
        "Excellent Job!",
        "You've made it look easy!",
        "You're amazing!",
        "You're unstoppable!",
        "What a beast!",
        "You're a word guessing god!",
        "All hail the word master!",
    ]

    length_ranges = {
        'Xtreme': (20, 22),
        'Greater': (17, 19),
        'Longer': (13, 16),
        'Regular': (9, 12),
        'Small': (5, 8),
        'Mini': (2, 4)
    }

    print('\nHey there! Try to guess all the letters in the secret word before your guesses run out!\n \n')
    score_time = format_time(high_score)
    print(
        f"Out of {game_number} games played, your high score is \n \n~~ {score_time} ~~\n \nCan you set a new record??\nYour current settings are: \n \nWord Length: {word_length_setting}\nGame Difficulty: {game_difficulty}\n \n{word_length_setting} length will generate words with {length_ranges[word_length_setting][0]} to {length_ranges[word_length_setting][1]} letters.\n{game_difficulty} difficulty allows {difficulty_lives[game_difficulty.lower()]} wrong guesses before GAME OVER.\nReturn to the main menu to change settings.\n \n[EX]it to return to the main menu or reset the game.")
    sleep('...')

    while play:
        game_number += 1
        save_game_number(game_number)
        random_word = select_word(filename, word_length_setting)
        guessed_letters = []
        counter = difficulty_lives[game_difficulty.lower()]

        start_time = time.time()  # record the start time

        print(random_word)
        print()

        while counter > 0:
            display = display_letters(
                random_word, guessed_letters, game_difficulty, wrong_guesses)
            print(f'\n{display}\n')

            if '_ ' not in display:
                # displays victory screen, press 'Q' to quit
                start_screen()
                end_time = time.time()  # Record the end time
                duration = end_time - start_time
                formatted_time = format_time(duration)
                formatted_word = random_word[0].upper(
                ) + random_word[1:].lower()
                win_message = random.choice(win_statements)
                print(
                    f"{win_message}\nYou guessed the secret word, '{formatted_word}'!")
                print(
                    f'It only took you {formatted_time}!')
                print('...')

                if high_score is None:
                    high_score = duration
                    record_message = random.choice(record_statements)
                    print(
                        f"{record_message} You've just set your first record!\nCheck out 'High Score' to view your fastest time!")
                elif high_score is not None and duration < high_score:
                    high_score = duration
                    save_high_score(high_score)
                    record_message = random.choice(record_statements)
                    print(
                        f"{record_message} You just set a *NEW* record!\n'High Score' has been updated with your latest time!")

                # adding to score history dictionary
                score_history[f'Game {game_number}'] = f'WIN: {formatted_time}'
                with open('score_history.txt', 'w') as file:
                    json.dump(score_history, file)

                sleep('...')
                break

            guess = user_guess(counter, guessed_letters,
                               random_word, display, game_difficulty)

            if guess is None:
                end_time = time.time()  # Record the end time
                duration = end_time - start_time
                formatted_time = format_time(duration)
                score_history[f'Game {game_number}'] = f'EXIT - {formatted_time}'
                with open('score_history.txt', 'w') as file:
                    json.dump(score_history, file)
                play = False
                break

            if guess in random_word and guess.upper() not in guessed_letters:
                congrats_message = random.choice(congrats_statements)
                print(f'{congrats_message} You guessed "{guess.upper()}" correctly!')
                sleep('...')
                guessed_letters.append(guess.upper())

            if guess not in random_word and guess not in guessed_letters:
                dissapoint_message = random.choice(dissapoint_statements)
                print(
                    f"{dissapoint_message} '{guess.upper()}' is not in the secret word :(")
                sleep('...')
                guessed_letters.append(guess.upper())
                counter -= 1
                wrong_guesses += 1

        else:
            end_time = time.time()  # Record the end time
            duration = end_time - start_time
            formatted_time = format_time(duration)

            display = display_letters(
                random_word, guessed_letters, game_difficulty, wrong_guesses)
            formatted_word = random_word[0].upper(
            ) + random_word[1:].lower()
            print(
                f'\n{display}\n \n[GAME OVER]\n \nThe correct word was: {formatted_word} :(')
            print(f'You played for: {formatted_time}')
            sleep('...')
            # adding to score history dictionary
            score_history[f'Game {game_number}'] = f'LOSS: {formatted_time}'
            with open('score_history.txt', 'w') as file:
                json.dump(score_history, file)

        while True:
            play_again = input(
                'Do you want to play again? (y/n) > ').lower().strip()
            sleep('...')
            if play_again.lower() == 'n':
                print('Thanks for playing!')
                play = False
                break
            if play_again.upper() == 'F':
                f_pressed_text = pyfiglet.figlet_format(
                    text="'F' PRESSED", font="standard", width=50)
                print(f_pressed_text)
                print(
                    "\nYou have paid respects.\nPlease enter 'yes' or 'no'.")
                sleep('...')
            elif play_again.lower() == 'y':
                play = True
                resetting_game_text = pyfiglet.figlet_format(
                    text="//RESETTING GAME//", font='smslant')
                print(resetting_game_text)
                # print('//RESETTING GAME//')
                sleep('...')
                print('Guessed Letters = 0\nCounter = 8\n \nReady to go!!')
                sleep('...')
                counter = difficulty_lives[game_difficulty.lower()]
                guessed_letters = []
                wrong_guesses = 0
                break
            else:
                print("Please enter either 'yes' or 'no'")
                sleep('...')
        if not play:
            return high_score


def main_menu():
    filename = 'words.txt'
    score_history = load_score_history()
    high_score = load_high_score()
    word_length_setting = load_word_length()
    game_difficulty = load_game_difficulty()
    # print('\nWelcome to Hangman!\n')
    welcome_to_text = pyfiglet.figlet_format(
        text='Welcome to', font='rectangles', width=50)
    print(welcome_to_text)
    game_name_text = pyfiglet.figlet_format(text="Hangman",
                                            font="ogre",)
    print(game_name_text)
    while True:
        print(
            "\n~~ MAIN MENU ~~\n \nOptions:\n[P]lay the game\n[C]heck high score\n[V]iew score history\n[S]ettings\n[T]ools\n[E]xit the game\n")

        choice = input('Choose an option: > ').lower().strip()

        if choice == 'p':
            sleep('...')
            initializing_game_text = pyfiglet.figlet_format(
                text="STARTING GAME!", font='smslant')
            print(initializing_game_text)
            sleep('...')
            new_high_score = play_game(
                filename, score_history, high_score, word_length_setting, game_difficulty)
            save_high_score(new_high_score)
            sleep('...')

        elif choice == 'c':
            sleep('...')
            if high_score is None:
                print('No record has been set yet.')
            else:
                formatted_time = format_time(high_score)
                # print(high_score)
                print(f'The current record is: \n{formatted_time}')
            sleep('...')

        elif choice == 'v':
            sleep('...')
            initializing_score_history = pyfiglet.figlet_format(
                text="--SCORE HISTORY--", font='smslant')
            print(initializing_score_history)
            for game, duration in score_history.items():
                print(f"{game}: {duration}")
            print("\n--- End of Score History ---")
            sleep('...')

        elif choice == 's':
            game_setting_flag = True
            sleep('...')
            game_settings_text = pyfiglet.figlet_format(
                text="GAME SETTINGS", font='smslant')
            print(game_settings_text)
            # print('//GAME SETTINGS//')
            sleep('...')
            print(
                'Options:\n[L]ength setting\n[D]ifficulty setting\n[E]xit\n')
            while game_setting_flag:
                setting_choice = input('Select an option: > ').lower().strip()

                if setting_choice == 'l':
                    choice_flag = True
                    sleep('...')
                    length_settings_text = pyfiglet.figlet_format(
                        text="LENGTH SETTINGS", font='smslant')
                    print(length_settings_text)
                    # print('//WORD LENGTH SETTINGS//')
                    sleep('...')
                    print(
                        f'Word Lengths:\n[X]treme  | (20-22 letters)\n[G]reater | (17-19 letters)\n[L]onger  | (13-16 letters)\n[R]egular | (9-12 letters)\n[S]mall   | (5-8 letters)\n[M]ini    | (2-4 letters)\n \n \nThe word length is currently set to: \n \n~~ {word_length_setting} ~~\n')
                    while choice_flag:
                        maybe_change = input(
                            'Would you like to change the word length? (y/n) > ').lower().strip()
                        if maybe_change == 'y':
                            sleep('...')
                            while True:
                                len_change = input(
                                    'Select new word length: > ').lower().strip()

                                if len_change == 'x':
                                    sleep('...')
                                    word_length_setting = 'Xtreme'
                                    save_word_length(word_length_setting)
                                    choice_flag = False
                                    print(
                                        f'The Word Length Setting has been set to: {word_length_setting}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif len_change == 'g':
                                    sleep('...')
                                    word_length_setting = 'Greater'
                                    save_word_length(word_length_setting)
                                    choice_flag = False
                                    print(
                                        f'The Word Length Setting has been set to: {word_length_setting}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif len_change == 'l':
                                    sleep('...')
                                    word_length_setting = 'Longer'
                                    save_word_length(word_length_setting)
                                    choice_flag = False
                                    print(
                                        f'The Word Length Setting has been set to: {word_length_setting}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif len_change == 'r':
                                    sleep('...')
                                    word_length_setting = 'Regular'
                                    save_word_length(word_length_setting)
                                    choice_flag = False
                                    print(
                                        f'The Word Length Setting has been set to: {word_length_setting}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif len_change == 's':
                                    sleep('...')
                                    word_length_setting = 'Small'
                                    save_word_length(word_length_setting)
                                    choice_flag = False
                                    print(
                                        f'The Word Length Setting has been set to: {word_length_setting}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif len_change == 'm':
                                    sleep('...')
                                    word_length_setting = 'Mini'
                                    save_word_length(word_length_setting)
                                    choice_flag = False
                                    print(
                                        f'The Word Length Setting has been set to: \n \n~~ {word_length_setting} ~~')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                        elif maybe_change == 'n':
                            sleep('...')
                            return_menu_text = pyfiglet.figlet_format(
                                text="BACK TO MENU", font='rectangles')
                            print(return_menu_text)
                            # print('//RETURNING TO MENU//')
                            sleep('...')
                            game_setting_flag = False
                            break

                        elif maybe_change == 'f':
                            sleep('...')
                            f_pressed_text = pyfiglet.figlet_format(
                                text="'F' PRESSED", font="standard", width=50)
                            print(f_pressed_text)
                            print("\nYou have paid respects.")
                            sleep('...')

                        else:
                            sleep('...')
                            print('Invalid choice. Please choose (y/n)')
                            sleep('...')
                    break

                elif setting_choice == 'd':
                    setting_choice_flag = True
                    sleep('...')
                    difficulty_settings_text = pyfiglet.figlet_format(
                        text="DIFFICULTY SETTINGS", font='smslant')
                    print(difficulty_settings_text)
                    # print('//DIFFICULTY SETTINGS//')
                    sleep('...')
                    print(
                        f'Options:\n[V]ery Easy  | (15 Lives)\n[E]asy       | (12 Lives)\n[M]edium     | (10 Lives)\n[R]egular    | (8 Lives)\n[H]ard       | (6 Lives)\n[X]tra Hard  | (5 Lives)\n[I]mpossible | (3 Lives)\n \n \nThe difficutly is currently set to:\n \n~~ {game_difficulty} ~~\n')
                    while setting_choice_flag:
                        change_maybe = input(
                            'Would you like to change the game difficulty? (y/n) > ')

                        if change_maybe == 'y':
                            sleep('...')
                            while True:
                                change_diff = input(
                                    'Select new game difficulty: > ').lower().strip()

                                if change_diff == 'v':
                                    sleep('...')
                                    game_difficulty = 'Very Easy'
                                    save_game_difficulty(game_difficulty)
                                    setting_choice_flag = False
                                    print(
                                        f'The game difficulty has been set to: {game_difficulty}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif change_diff == 'e':
                                    sleep('...')
                                    game_difficulty = 'Easy'
                                    save_game_difficulty(game_difficulty)
                                    setting_choice_flag = False
                                    print(
                                        f'The game difficulty has been set to: {game_difficulty}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif change_diff == 'm':
                                    sleep('...')
                                    game_difficulty = 'Medium'
                                    save_game_difficulty(game_difficulty)
                                    setting_choice_flag = False
                                    print(
                                        f'The game difficulty has been set to: {game_difficulty}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif change_diff == 'r':
                                    sleep('...')
                                    game_difficulty = 'Regular'
                                    save_game_difficulty(game_difficulty)
                                    setting_choice_flag = False
                                    print(
                                        f'The game difficulty has been set to: {game_difficulty}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif change_diff == 'h':
                                    sleep('...')
                                    game_difficulty = 'Hard'
                                    save_game_difficulty(game_difficulty)
                                    setting_choice_flag = False
                                    print(
                                        f'The game difficulty has been set to: {game_difficulty}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif change_diff == 'x':
                                    sleep('...')
                                    game_difficulty = 'Xtra Hard'
                                    save_game_difficulty(game_difficulty)
                                    setting_choice_flag = False
                                    print(
                                        f'The game difficulty has been set to: {game_difficulty}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif change_diff == 'i':
                                    sleep('...')
                                    game_difficulty = 'Impossible'
                                    save_game_difficulty(game_difficulty)
                                    setting_choice_flag = False
                                    print(
                                        f'The game difficulty has been set to: {game_difficulty}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                else:
                                    sleep('...')
                                    print(
                                        'Invalid choice. Please select an option listed.')
                                    sleep('...')

                        elif change_maybe == 'n':
                            sleep('...')
                            return_menu_text = pyfiglet.figlet_format(
                                text="BACK TO MENU", font='rectangles')
                            print(return_menu_text)
                            # print('//RETURNING TO MENU//')
                            sleep('...')
                            setting_choice_flag = False
                            game_setting_flag = False
                            break

                        else:
                            sleep('...')
                            print('Invalid choice. Please choose (y/n)')
                            sleep('...')
                    break

                elif setting_choice == 'e':
                    sleep('...')
                    # print('//RETURNING TO MENU//')
                    return_menu_text = pyfiglet.figlet_format(
                        text="BACK TO MENU", font='rectangles')
                    print(return_menu_text)
                    sleep('...')
                    break

        elif choice == 'f':
            sleep('...')
            f_pressed_text = pyfiglet.figlet_format(
                text="'F' PRESSED", font="standard", width=50)
            print(f_pressed_text)
            print("\nYou have paid respects.")
            sleep('...')

        elif choice == 'e':
            sleep('...')
            print('\nThanks for playing!\nSee you again soon!\n')
            goodbye_text = pyfiglet.figlet_format(
                text='Goodbye!', font='larry3d')
            print(goodbye_text)
            break

        elif choice == 't':
            sleep('...')
            while True:
                dev_tool_text = pyfiglet.figlet_format(
                    text='DEVELOPER TOOLS', font='Rectangles', width=50)
                print(dev_tool_text)
                print(
                    '\n \nOptions:\n[L]engths of words listed\n[R]andom word generator\n[E]xit\n \n')
                tool_choice = input(
                    'Choose an option: > ').lower().strip()

                if tool_choice == 'l':
                    sleep('...')
                    word_length_counts = count_words_by_length(filename)
                    print(
                        'The lengths of the words in this list & how numerous they are:\n')
                    for length_count in word_length_counts:
                        print(length_count)
                    sleep('...')

                elif tool_choice == 'r':
                    sleep('...')
                    random_word_generator = pyfiglet.figlet_format(
                        text="//RANDOM WORD GENERATOR//", font='smslant')
                    print(random_word_generator)
                    # print('//RANDOM WORD GENERATOR//')
                    random_word = select_word(filename, word_length_setting)
                    sleep('...')
                    print(
                        f'Your current word length is:\n \n~~ {word_length_setting} ~~\n \nRandom word generated:\n \n~~ {random_word} ~~')
                    sleep('...')

                elif tool_choice == 'e':
                    sleep('...')
                    break

                else:
                    sleep('...')
                    print("Invalid choice. Please choose one of the options listed.")
                    sleep('...')

        else:
            sleep('...')
            print("Invalid choice. Please choose one of the options listed.")
            sleep('...')


if __name__ == "__main__":
    main_menu()
