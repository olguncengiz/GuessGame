from guess_game import GuessGame
import os

def clearScreen():
    os.system('cls')

def printMenu():
    clearScreen()
    print 'Menu'
    print '1-New Game'
    print '2-Exit'

# Main Application Flow:
if __name__ == '__main__':    
    while True:
        printMenu()
        choice = raw_input()
        if choice == '2':
            clearScreen()
            break
        elif choice == '1':
            clearScreen()
            length = int(raw_input('Please Enter The Passcode Length: '))
            guessGame = GuessGame(length)
            #print guessGame.passcode
            guessGame.play()
            raw_input('Press "Enter" To Continue...')