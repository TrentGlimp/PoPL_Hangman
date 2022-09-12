class Board(object):
    def __init__(self):
        self.man = "   \n   \n   \n"
        self.word = charList
        self.board = emptyList

    def __str__(self):
        return self.man + self.board


word = input("Enter a word: ")
charList = []
guessedList = []
for each in word:
    charList.append(each)
print(charList)
emptyList = ["_" if char != " " else char for char in charList]
print(emptyList)

letter = input("Guess a letter: ")


# make sure letter is in the list of letters(for the word) and the input is not a special char or number
# if letter is correct replace underscores with letter ex: word = hello, guess: = e result: _e___
def check_guess(letter):
    for i in range(len(charList)):
        if charList[i] == letter:
            emptyList[i] = letter
            print("Correct guess!")
    else:
        guessedList.append(letter)
        print("Not quite, try another letter.")


check_guess(letter)
'''
capitalList = [char.upper() for char in charList]

print(capitalList)

'''
