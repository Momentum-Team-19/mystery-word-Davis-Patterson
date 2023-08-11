import random
import time
from anipage import start_screen

hangman_pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",

                "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

                "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

                "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",

                "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

                "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

                "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]


def sleep(text=None):
    if text is None:
        time.sleep(.6)
        print()
    else:
        time.sleep(.2)
        print(f'\n{text}\n')
        time.sleep(.6)


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


def display_letters(word, guessed_letters):
    chosen_word = ''
    for letter in word:
        if letter.upper() in guessed_letters:
            chosen_word += letter.lower() + ' '
        else:
            chosen_word += '_ '
    if chosen_word:
        chosen_word = chosen_word[0].upper() + chosen_word[1:]
    return chosen_word


def user_guess(counter, guessed_letters, random_word, display):
    while counter > 0:
        if counter == 8 and len(guessed_letters) == 0:
            print(f'You have {counter} guesses remaining!!')
        if counter < 8 and counter > 0:
            print(f'You only have {counter} guesses remaining!!')
        if counter == 8 and len(guessed_letters) > 0:
            print(f'You still have {counter} guesses remaining!!')

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
            print('//EXITING CURRENT GAME//')
            sleep('...')
            return None
        if guess.lower() == random_word.lower():
            sleep('...')
            return guess
        if len(guess) > 1:
            print('Please enter only (1) letter at a time!\n')
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
            print("'F' pressed.\nYou have paid respects.\nPlease guess again.")
            sleep('...')
        elif guess in random_word and guess not in guessed_letters:
            return guess

        else:
            return guess


def play_game(filename, score_history, high_score, word_length_setting):
    play = True
    game_number = 0

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

    print('\nHey there! Try to guess all the letters in the secret word before your guesses run out!\n')
    print(
        f"The word length setting is currently set to: \n \n~~ {word_length_setting} ~~\n \nThis setting will have words with {length_ranges[word_length_setting][0]} to {length_ranges[word_length_setting][1]} letters.\nReturn to the main menu to change the word length setting.\n \n[EX]it to return to the main menu or reset the game.")
    sleep('...')

    while play:
        game_number += 1
        random_word = select_word(filename, word_length_setting)
        guessed_letters = []
        counter = 8

        start_time = time.time()  # record the start time

        print(random_word)
        print()

        while counter > 0:
            display = display_letters(random_word, guessed_letters)
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
                    record_message = random.choice(record_statements)
                    print(
                        f"{record_message} You just set a *NEW* record!\n'High Score' has been updated with your latest time!")

                # adding to score history dictionary
                score_history[f'Game {game_number}'] = f'WIN: {formatted_time}'

                sleep('...')
                break

            guess = user_guess(counter, guessed_letters, random_word, display)

            if guess is None:
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

        else:
            end_time = time.time()  # Record the end time
            duration = end_time - start_time
            formatted_time = format_time(duration)
            print(f'Game Over :(\n \nThe correct word was: {random_word}')
            print(f'You played for: {formatted_time}')
            sleep('...')
            # adding to score history dictionary
            score_history[f'Game {game_number}'] = f'LOSS: {formatted_time}'

        while True:
            play_again = input(
                'Do you want to play again? (y/n) > ').lower().strip()
            sleep('...')
            if play_again.lower() == 'n':
                print('Thanks for playing!')
                play = False
                break
            if play_again.upper() == 'F':
                print(
                    "'F' pressed.\nYou have paid respects.\nPlease enter 'yes' or 'no'.")
                sleep('...')
            elif play_again.lower() == 'y':
                play = True
                print('//RESETTING GAME//')
                sleep('...')
                print('Guessed Letters = 0\nCounter = 8\n \nReady to go!!')
                sleep('...')
                counter = 8
                guessed_letters = []
                break
            else:
                print("Please enter either 'yes' or 'no'")
                sleep('...')
        if not play:
            return high_score


def main_menu():
    filename = 'words.txt'
    score_history = {}
    high_score = None
    word_length_setting = 'Regular'
    while True:
        print(
            "\n~~ MAIN MENU ~~\n \nOptions:\n[P]lay the game\n[C]heck high score\n[V]iew score history\n[L]ength setting\n[T]ools\n[E]xit the game\n")

        choice = input('Choose an option: > ').lower().strip()

        if choice == 'p':
            sleep('...')
            print('//Initializing game//')
            sleep('...')
            high_score = play_game(
                filename, score_history, high_score, word_length_setting)
            sleep('...')

        elif choice == 'c':
            sleep('...')
            if high_score is None:
                print('No record has been set yet.')
            else:
                formatted_time = format_time(high_score)
                print(f'The current record is: \n{formatted_time}')
            sleep('...')

        elif choice == 'v':
            sleep('...')
            print("--- SCORE HISTORY ---\n")
            for game, duration in score_history.items():
                print(f"{game}: {duration}")
            print("\n--- End of Score History ---")
            sleep('...')

        elif choice == 'l':
            choice_flag = True
            sleep('...')
            print('//WORD LENGTH SETTINGS//')
            sleep('...')
            print(
                f'The word length is currently set to: \n \n~~ {word_length_setting} ~~\n \n')
            while choice_flag:
                maybe_change = input(
                    'Would you like to change the word length? (y/n) > ').lower().strip()
                if maybe_change == 'y':
                    sleep('...')
                    while True:
                        print(
                            'Word Lengths:\n[X]treme  | (20-22 letters)\n[G]reater | (17-19 letters)\n[L]onger  | (13-16 letters)\n[R]egular | (9-12 letters)\n[S]mall   | (5-8 letters)\n[M]ini    | (2-4 letters)\n \nOr:\n[C]ancel\n')
                        len_change = input(
                            'Select word length: > ').lower().strip()

                        if len_change == 'x':
                            sleep('...')
                            word_length_setting = 'Xtreme'
                            choice_flag = False
                            print(
                                f'The Word Length Setting has been set to: {word_length_setting}')
                            sleep('...')
                            break

                        elif len_change == 'g':
                            sleep('...')
                            word_length_setting = 'Greater'
                            choice_flag = False
                            print(
                                f'The Word Length Setting has been set to: {word_length_setting}')
                            sleep('...')
                            break

                        elif len_change == 'l':
                            sleep('...')
                            word_length_setting = 'Longer'
                            choice_flag = False
                            print(
                                f'The Word Length Setting has been set to: {word_length_setting}')
                            sleep('...')
                            break

                        elif len_change == 'r':
                            sleep('...')
                            word_length_setting = 'Regular'
                            choice_flag = False
                            print(
                                f'The Word Length Setting has been set to: {word_length_setting}')
                            sleep('...')
                            break

                        elif len_change == 's':
                            sleep('...')
                            word_length_setting = 'Small'
                            choice_flag = False
                            print(
                                f'The Word Length Setting has been set to: {word_length_setting}')
                            sleep('...')
                            break

                        elif len_change == 'm':
                            sleep('...')
                            word_length_setting = 'Mini'
                            choice_flag = False
                            print(
                                f'The Word Length Setting has been set to: \n \n~~ {word_length_setting} ~~')
                            sleep('...')
                            break

                        elif len_change == 'c':
                            sleep('...')
                            choice_flag = False
                            print('//RETURNING TO MAIN MENU//')
                            sleep('...')
                            break

                elif maybe_change == 'n':
                    sleep('...')
                    print('//RETURNING TO MENU//')
                    sleep('...')
                    break

                elif maybe_change == 'f':
                    sleep('...')
                    print("'F' pressed.\nYou have paid respects.")
                    sleep('...')

                else:
                    sleep('...')
                    print('Invalid choice. Please choose (y/n)')
                    sleep('...')

        elif choice == 'f':
            sleep('...')
            print("'F' pressed.\nYou have paid respects.")
            sleep('...')

        elif choice == 'e':
            print('\nThanks for playing!\nSee you again soon!\nGoodbye!')
            break

        elif choice == 't':
            sleep('...')
            while True:
                print(
                    '//DEVELOPER TOOLS//\n \n[L]engths of words listed\n[R]andom word generator\n[E]xit\n \n')
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
                    print('//RANDOM WORD GENERATOR//')
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
