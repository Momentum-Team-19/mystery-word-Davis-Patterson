import random


def select_word(filename):
    with open(filename, 'r') as file:
        file = file.read()
    words_list = file.split()
    random_word = random.choice(words_list)
    return random_word


def display_word_board(word, guessed_letters):
    chosen_word = ''
    for letter in word:
        if letter in guessed_letters:
            chosen_word += letter + ' '
        else:
            chosen_word += '_ '
    return chosen_word


def user_guess(counter, guessed_letters):
    while counter > 0:

        print(f'You have {counter} guesses remaining!')
        print(f'You have guessed, {guessed_letters}')
        guess = input('Guess a letter: > ').lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print('Please enter only one letter!')
        else:
            guessed_letters.append(guess)
            return guess


def play_game():
    random_word = select_word('test-word.txt')
    guessed_letters = []
    counter = 8

    while True:
        display = display_word_board(random_word, guessed_letters)
        print(display)

        if '_ ' not in display:
            print("Hey, way to go! You guessed the word!", random_word)
            break

        guess = user_guess(counter, guessed_letters)
        guessed_letters.append(guess)


if __name__ == "__main__":
    play_game()
