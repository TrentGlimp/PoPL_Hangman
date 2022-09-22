import getpass
# make conditional to prevent double guessing
class Game(object):
    def __init__(self):
        self.man = "   \n   \n   \n"
        self.word = charList
        self.board = emptyList

    def __str__(self):
        return self.man + self.board

def form_phrase():
    phrase = input("Enter a phrase: ")
    for i in range(20):print("")
    global charList
    charList = []
    global guessedList
    guessedList = []
    for each in phrase:
        charList.append(each)
    global emptyList
    emptyList = ["_" if char != " " else char for char in charList]


# make sure letter is in the list of letters(for the word) and the input is not a special char or number
# if letter is correct replace underscores with letter ex: word = hello, guess: = e result: _e___
strikes = 0
def check_letter(strikes):
    letter = input("Guess a letter: ")
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

def check_phrase(strikes):
    global phrase
    phrase = input("Guess the phrase: ")
    for letter in phrase:
        if letter in guessedList:
            print("\nA letter in the phrase has already been guessed.")
    if phrase == ''.join(charList):
        print("Congratulations you win!")
        quit()
    else:
        print("Not quite, try another phrase or letter.")
        strikes += 1
    print(f"You have {strikes} strikes.\n")
    return strikes


form_phrase()
game = Game()

while 6 >= strikes:
    valid = False
    while not valid:
        letter_or_phrase = input("Would you like to guess a single letter or the whole phrase\n[l, p]\n")
        if letter_or_phrase == "l" or letter_or_phrase == "p":
            valid = True
            if letter_or_phrase == "l":strikes = check_letter(strikes)
            else:strikes = check_phrase(strikes)

    print(''.join(emptyList) + "\n")
    if game.board == game.word:
        print("Congratulations you win!")
        quit()
print("L better luck next time pal.")
'''
capitalList = [char.upper() for char in charList]

print(capitalList)

'''
