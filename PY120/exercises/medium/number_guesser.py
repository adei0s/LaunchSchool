import random
import math

class GuessingGame:
    def __init__ (self, low, high):
        self._low = low
        self._high = high
        self._the_number = None
        self._try_remain = None
        self._the_guess = None

    MESSAGE = {
        'high' : "Your guess is too high",
        'low' : "Your guess is too low",
        'win' : "You won!",
        'lose' : "You have no more guesses. You lost!",
    }
    
    def reset(self):
        self._the_number = random.randint(self._low, self._high)
        self._try_remain = int(math.log2(self._high - self._low + 1)) + 1
        self._the_guess = None
        
    def invalid(self):
        while not 0 < self._the_guess < 100:
            print(f"Invalid guess, Enter a nubmer between {self._low} and {self._high}:")
            self._the_guess = int(input())
        
         
    def play(self):
        self.reset()
        while self._try_remain > 0:
            if self.turn():
                print(self.MESSAGE['win'])
                break
            if self._try_remain == 0:
                print(self.MESSAGE['lose'])
            else:
                self._try_remain -= 1
            
    def turn(self):
        print(f"You have {self._try_remain} guesses remaining.")
        print(f"Enter a number between {self._low} and {self._high}:")
        self._the_guess = int(input())
        self.invalid()
        if self._the_guess == self._the_number:
            return True
        else:
            if self._the_guess > self._the_number:
                print(self.MESSAGE['high'])
            elif self._the_guess < self._the_number:
                print(self.MESSAGE['low'])

game = GuessingGame(501, 1500)
game.play()