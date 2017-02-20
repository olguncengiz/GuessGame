import random

class GuessGame:
    def __init__(self, length, difficulty):
        self.length = length
        self.passcode = ''
        self.steps = 1
        self.generate()
        self.easy = difficulty

    def generate(self):
        numbers = '0123456789'
        for i in range(self.length):
            f = random.randrange(len(numbers))
            self.passcode = self.passcode + numbers[f]

    def play(self):
        print 'Try To Crack The Code...'
        while True:
            guess = raw_input()
            if guess == self.passcode:
                print 'You Cracked The Code In %s Tries.' % self.steps
                break
            elif len(guess) != len(self.passcode):
                print 'N/A'
            else:
                result = self.mask(guess)
                self.steps = self.steps + 1
                print result

    def mask(self, guess):
        result = ''

        if self.easy:
            numbers = dict()
            for i in range(len(self.passcode)):
                if guess[i] == self.passcode[i]:
                    result = result + guess[i]
                else:
                    result = result + ' '
                    if self.passcode[i] in numbers:
                        numbers[self.passcode[i]] = numbers[self.passcode[i]] + 1
                    else:
                        numbers[self.passcode[i]] = 1

            for i in range(len(result)):
                if result[i] == ' ' and guess[i] in numbers and numbers[guess[i]] > 0:
                    result = result[:i] + '*' + result[i + 1:]
                    numbers[guess[i]] = numbers[guess[i]] - 1
        else:
            correct = 0
            misplaced = 0

            numbers = dict()
            for i in range(len(self.passcode)):
                if guess[i] == self.passcode[i]:
                    correct += 1
                    result = result + guess[i]
                else:
                    result = result + ' '
                    if self.passcode[i] in numbers:
                        numbers[self.passcode[i]] = numbers[self.passcode[i]] + 1
                    else:
                        numbers[self.passcode[i]] = 1

            for i in range(len(result)):
                if result[i] == ' ' and guess[i] in numbers and numbers[guess[i]] > 0:
                    misplaced += 1
                    numbers[guess[i]] = numbers[guess[i]] - 1

            result = 'Correct = %s\nMisplaced = %s\n' % (correct, misplaced)

        return result



                