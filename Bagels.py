"""
In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. The game offers one of
the following hints in response to your guess:
“Pico” when your guess has a correct digit in the wrong place,
“Fermi” when your guess has a correct digit in the correct place, and
“Bagels” if your guess has no correct digits. You have 10 tries to guess the secret number.
Reference: https://inventwithpython.com/bigbookpython/project1.html
"""
import random

num_digits = 3
max_guesses = 10

def main():
    while True:
        secretNum = getSecretNum()
        print("I have thought of a number")
        print("You have {} guesses to get that number".format(max_guesses))
        numGuesses = 1
        while numGuesses <= max_guesses:
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print("Guess:{}".format(numGuesses))
                guess = input('> ')
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > max_guesses:
                print("You ran out of guesses!!")
                print("The answer was:{}".format(secretNum))

        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair"""
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range (len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')   # A correct digit is in the correct place
        elif guess[i] in secretNum:
            clues.append('Pico')    # A correct digit is in the incorrect place
    if len(clues) == 0:
        return 'Bagels'             # There are no correct digits at all
    else:
        clues.sort()                #Sort the clues into alphabetical order so their original order doesn't give information away.
        return ''.join(clues)       # Make a single string from the list of string clues

if __name__ == "__main__":
    main()


