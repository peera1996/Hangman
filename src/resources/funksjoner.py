import json
from random import randint

# Creates a two dimensional list of hangman. Takes the number of wrong guesses as
# a parameter, and fills in the figure appropriately.
def create_figure(attempt=0):
    if attempt < 0 or attempt > 6:
        raise ValueError("Minimum er 0 og maksimum er 6")

    figure = [['+', '-', '-', '-', '-', '+', ' '],
              ['|', '/', ' ', ' ', ' ', '|', ' '],
              ['|', ' ', ' ', ' ', ' ', '', ' '],
              ['|', ' ', ' ', ' ', '', ' ', ''],
              ['|', ' ', ' ', ' ', '', ' ', ''],
              ['-', '+', '-', ' ', ' ', ' ', ' ']]

    replace_array = {"array": [{
        'index_x': 2,
        'index_y': 6,
        'character': 'o'
    },
        {
            'index_x': 3,
            'index_y': 4,
            'character': '/'
        },
        {
            'index_x': 3,
            'index_y': 6,
            'character': '\\'
        },
        {
            'index_x': 3,
            'index_y': 5,
            'character': '|'
        },
        {
            'index_x': 4,
            'index_y': 4,
            'character': '/'
        },
        {
            'index_x': 4,
            'index_y': 6,
            'character': '\\'
        }]}

    for i in range(0, attempt):
        replace_char = replace_array['array'][i]['character']
        figure[replace_array['array'][i]['index_x']][replace_array['array'][i]['index_y']] = replace_char

    return figure


# Prints a pretty representation of the two dimensional list returned from create_figure()
def print_figure(figure):
    for rad in figure:
        print(''.join(rad), end='')
        print('')


# Check to see if a string consists of a single alphabetical letter.
def is_letter(user_input):
    return user_input.isalpha() and len(user_input) == 1


# Gives a visual representation of which letters of a word are correctly guessed.
# The parameter 'word' is the word to check against.
# The parameter 'guessed_letters' is a list of the letters a player has guessed (both right and wrong guesses).
# If e.g. the word is 'giraffe', and the user has guessed the letters 't', 'p', 'g', 'f', and 'e', the
# string returned will be "g _ _ _ f f e'
def reveal_correct_letters(word, guessed_letters):
    vizualisation_as_list = list('_' * len(word))
    word_as_list = list(word)
    for guessed_letter in guessed_letters:
        for idx, letter_in_word in enumerate(word_as_list):
            if guessed_letter == letter_in_word:
                vizualisation_as_list[idx] = guessed_letter

    return " ".join(vizualisation_as_list)


def sjekk_om_vunnet(losning):
    if not losning.__contains__("_"):
        print("Gratulerer! Du har gjettet ordet :D")
        return True
    else:
        return False


def sjekk_om_tapt(i):
    if i == 6:
        print("Du tapte spillet :(")
        return True
    else:
        return False


def hent_ord(vanskelighetsgrad):
    with open('resources/ordliste.json') as fp:
        ordliste = []
        data = json.load(fp)
        ord = data['ordliste']
        for enkeltOrd in ord:
            if vanskelighetsgrad == enkeltOrd['vanskelighetsgrad']:
                ordliste.append(enkeltOrd['ord'])
        random_index = randint(0, len(ordliste)-1)
        return ordliste[random_index]
