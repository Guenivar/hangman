import random
import ascii
import sys

#Basic game of hangman
with open("words.txt") as file:
    words = file.read().splitlines()

def main():
    #track attempts
    attempts = 0
    #pick out a word
    word = random.choice(words).upper()
    #censor
    code_word = "_" * len(word)
    #store used letters
    used_letters = []
    #Play
    while attempts < 6:
        #Information
        print(ascii.HANGMANPICS[attempts])
        print(f"Word: {code_word}")
        print(f"Used letters: {used_letters}")
        #get a letter from the player and add it to the used letters
        while True:
            letter = input("Guess: ").upper()
            if guess(letter, used_letters):
                break
        used_letters.append(letter)
        #check if letter is in word and update code word
        if letter in word:
            code_word = decode(letter, word, code_word)
            if word == code_word:
                sys.exit(f"You win! The word was {word.capitalize()}")
        else:
            attempts += 1
    #If failed to guess word
    print(ascii.HANGMANPICS[attempts])
    print("GAME OVER")
    print(f"The word was: {word.capitalize()}")

def guess(letter, used_letters):
    if len(letter) == 1 and letter.isalpha():
        if letter in used_letters:
            print("You have already tried this letter")
            return False
        else:
            return True
    else:
        print("Guess must be a single letter.")
        return False

def decode(letter, word, code_word):
    for i in range(len(word)):
        if word[i] == letter:
            lst = list(code_word)
            lst[i] = letter
            code_word = ''.join(lst)
    return code_word

if __name__ == "__main__":
    main()
