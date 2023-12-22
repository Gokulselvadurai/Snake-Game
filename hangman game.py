import random
import string
from words import words
from hangman_visual import lives_visual_dict
def get_word(words):
    word= random.choice(words)
    while "-" in word or " " in word:
        word= random.choice(words)
    return word
life=6
word=get_word(words).upper()
letters_in_the_word=set(word)
used_letters=set()
while len(letters_in_the_word)>0 and life>0:
    print("You have",life,"life left and You used words are",",".join(used_letters)) # I want to remember the words used by the guy who playing the game
    word_list=[letter if letter in used_letters else "-" for letter in word]
    print("Till you find "," ".join(word_list))
    letter=input("Type your guessed word ").upper()
    alphabet = set(string.ascii_uppercase) #which contain all uppercase alphabets
    if letter not in used_letters:
        used_letters.add(letter)
        if letter in letters_in_the_word:
            letters_in_the_word.remove(letter)
        else:
            life=life-1
            print("letter is not in the word.")
            print(lives_visual_dict[life])
    elif letter in used_letters:
        print("You have already used that character.\n\tTRY AGAIN")
    else:
        print("Invalid character.\n\tTRYAGAIN")
if life==0:
    print(lives_visual_dict[life])
    print("You died :( .The word is",word)
else:
    print("You guessed the word :)",word,"correctly")