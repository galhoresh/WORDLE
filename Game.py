from WORDLE.Printer import printValues
from WORDLE.WordArray import valid_word_array


class Game():

    def __init__(self, print_choice, word):
        self.word = word
        self.print = print_choice
        self.word_array = []
        self.word_result = []

    def Play(self):
        while (len(self.word_array) < 5):
            self.getWord()
            self.calculateWordResult()
            printValues(self.word_array, self.word_result, self.print)
            if self.word_array[-1] == self.word:
                print("CONGRATULATIONS YOU WIN!")
                return
        print("LOSER!")
        print("THE WORD IS: " + self.word)

    def getWord(self):
        input_test = False
        while (input_test == False):
            word_input = input("Enter a 5 letter word\n")
            word_input = word_input.lower()
            try:
                assert len(word_input) == 5
                assert (word_input in valid_word_array)
                input_test = True
            except:
                if (len(word_input) == 5):
                    print("Not a valid word")
                else:
                    print("Must be a 5 letter word")
        self.word_array.append(word_input)

    def calculateWordResult(self):
        word = self.word_array[-1]
        result = ["", "", "", "", ""]
        for i in range(5):
            if word[i] == self.word[i]:
                result[i] = "T"
            else:
                result[i] = "F"
        for i in range(5):
            if result[i] == "F":
                for x in range(5):
                    if word[i] == self.word[x]:
                        if result[x] == "F":
                            result[i] = "P"
        self.word_result.append(result)
