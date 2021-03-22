import random

random.seed(0)


class Die:
    def __init__(self):
        self.roll()

    def roll(self):
        self.face = random.randint(1, 6)
        return self.face


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.die = Die()

    def decide(self):
        turn_score = 0
        decision = "r"

        while decision == "r":
            self.die.roll()
            roll = self.die.face
            if roll == 1:
                turn_score = 0
                current_total_score = self.score + turn_score
                print("{} rolled a 1. Your score for this turn is 0. Your total score for the game is {}".format(self.name, current_total_score))
                decision = "h"
            else:
                turn_score = turn_score + roll
                current_total_score = self.score + turn_score
                print("{} rolled a {}. Your current score for this turn is {}.  Your total score for the game is {}.".format(self.name, roll, turn_score, current_total_score))
                if current_total_score >= 100:
                    break
                else:
                    decision = input("Roll again or hold? Please enter r for roll again or h to hold.")
        self.score += turn_score

class Game:
    def __init__(self, player_one, player_two):
        self.die = Die()
        self.player_one = Player("Player One")
        self.player_two = Player("Player Two")

    def play(self):
        while self.player_one.score < 100 and self.player_two.score < 100:
            self.player_one.decide()
            if self.player_one.score < 100:
                self.player_two.decide()
        if self.player_one.score >= 100:
            print("Player 1 wins! Game over.")
        elif self.player_two.score >= 100:
            print("Player 2 wins! Game over.")


def main():
    game = Game("Player 1", "Player 2")
    game.play()


if __name__ == "__main__":
    main()
    
