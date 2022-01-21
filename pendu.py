# Jeu du pendu avec 100 mots courants de la langue française. Vous avez 7 vies pour trouver le mot !

import random
from words import words
from pendu_visuel import vies_visuel_dict
import string

# python pendu.py


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Vous avez encore', lives, 'vies et vous avez déjà utilisé ces lettres : ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(vies_visuel_dict[lives])
        print('Mot actuel: ', ' '.join(word_list))

        user_letter = input('Choississez une lettre : ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nVotre lettre,', user_letter, 'n\'est pas dans le mot recherché.')

        elif user_letter in used_letters:
            print('\nVous avez déjà utilisé cette lettre, utilisez en une autre.')

        else:
            print('\nCe n\'est pas une lettre valide.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(vies_visuel_dict[lives])
        print('Vous êtes mort, désolé. Le mot était : ', word)
    else:
        print('Bravo ! Vous avez trouvé le mot : ', word, '!!')


if __name__ == '__main__':
    hangman()
