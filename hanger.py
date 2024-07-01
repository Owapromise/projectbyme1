"""
creat a list of secret words and then randomly select a word from the collection  
only the first and last letters of the secret word is displayed
the player guess the word
"""

import random

secret_words=['color', 'book', 'ramp', 'group']

secret_word = random.choice(secret_words)
print(secret_word[0],"___", "___", secret_word[-1])
user_guess = input("guess the secret word: ")

if user_guess == secret_word:
    print("you win. word is ", secret_word)
else:
    print("try again")