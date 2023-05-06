import random

valid_word_array = []

def getWord():
    f = open(r"C:\Users\Gal\Documents\WORDLE\words.txt", 'r')
    i = 0
    for line in f:
        valid_word_array.append(line.strip())
        i+=1
    word = str(random.choice(valid_word_array))
    f.close()
    return word
