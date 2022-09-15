import getpass
# make conditional to prevent double guessing
class Game(object):
    def __init__(self):
        self.man = "   \n   \n   \n"
        self.word = charList
        self.board = emptyList

    def __str__(self):
        return self.man + self.board


word = input("Enter a word: ")
for i in range(20):print("")
charList = []
guessedList = []
for each in word:
    charList.append(each)
emptyList = ["_" if char != " " else char for char in charList]


# make sure letter is in the list of letters(for the word) and the input is not a special char or number
# if letter is correct replace underscores with letter ex: word = hello, guess: = e result: _e___
strikes = 0
def check_guess(letter, strikes):
    global guessedList
    found = False
    for i in range(len(charList)):
        if charList[i] == letter:
            emptyList[i] = letter
            found = True
    if found:
        print("\nCorrect guess!")
    else:
        print("\nNot quite, try another guess.")
        if letter not in guessedList:    
            strikes += 1
            guessedList.append(letter)
    print(f"You have {strikes} strikes.\n")
    return strikes

game = Game()

while 6 >= strikes:
    letter = input("Guess a letter: ")
    strikes = check_guess(letter, strikes)
    print(''.join(emptyList) + "\n")
    if game.board == game.word:
        print("Congratulations you win!")
        quit()
print("L better luck next time pal.")
'''
capitalList = [char.upper() for char in charList]

print(capitalList)

'''
