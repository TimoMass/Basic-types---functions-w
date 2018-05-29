import random

#make a list of words
words = ['apple',
         'grape',
         'orange',
         'fig',
         'banana']
while True:
    start = input("Press enter/return to start, or enter Q to quit")
    if start.lower() == 'q':
#pick a random word
secret_word =random.choice(words)
bad_guesses = []
good_guesses = []

while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
#draw spaces

#take a guess

#draw guessed letters and strikes

#print out win or lose
