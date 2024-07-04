"""
time : 40 min
"""
import random as r

class Game():
    def generating_number(self):
        number = r.randint(0, 100)
        return number
    def game(self):
        player_guess = input("Try to guess the number: ")
        number = self.generating_number()
        for counter in range(10):
            try:
                if int(player_guess) < number:
                    player_guess = input("The number you gave me is below the secret number, try again: ")
                elif int(player_guess) > number:
                    player_guess = input("The number you gave me is above the secret number, try again: ")
            except:
                player_guess = input("You didn't typed a number, thus you lose a chance. Try again: ")
        if player_guess != number:
            try_again = input(f"Sorry mate, you lost. The number was {number}. Do you want to try again? (y/n)\n")
            if try_again == "y":
                self.game()
            elif try_again == "n":
                print("K bye !")
            else:
                try_again = input("The answer you gave me is invalid, try again: (y/n)\n")
    def main(self):
        print("Welcome to a number guesser game. You have 10 tries to guess the secret number and if you try to put anything else than a number, you lose a try.\n")
        self.game()

guess = Game()
guess.main()