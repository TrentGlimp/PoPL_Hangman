class Game(object):
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


# make sure letter is in the list of letters(for the word) and the input is not a special char or number
# if letter is correct replace underscores with letter ex: word = hello, guess: = e result: _e___
strikes = 0
def check_guess(letter, strikes):
    for i in range(len(charList)):
        if charList[i] == letter:
            emptyList[i] = letter
            print("Correct guess!")
        else:
            guessedList.append(letter)
            strikes += 1  # change to own elif so
            print("Not quite, try another letter.")
    return strikes

game = Game()

while 6 >= strikes:
    letter = input("Guess a letter: ")
    check_guess(input("Guess a letter: "), strikes)
    if game.board == game.word:
        print("Congratulations you win!")
        quit()
print("L better luck next time pal.")
'''
capitalList = [char.upper() for char in charList]

print(capitalList)

'''
