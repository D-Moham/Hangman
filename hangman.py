import random
from words import words

def get_valid_word(words):
    word = random.choice(words) #randomlychooses something from the list
    while '-' in word or '' in word:
        word = random.choice(words)

    return word

def hangman():
    word  = get_valid_word(words)
    word_leters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    3