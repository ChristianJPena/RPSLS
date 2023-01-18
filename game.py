from human import Human
from AI import Ai


class Game:
        def __init__(self):
            self.rpsls_one = input("What is your name?")

    def run_game(self):
        self.display_welcome()
        self.display_steps()
        # self.battle_phase()
        # self.display_winner()

    def display_welcome(self):
        print('!BAZINGA!\nWelcome to\nRock, Paper, Scissors, Lizard, Spock!')
    
    def display_steps(self):
        print('Rules to this game are fairly simple\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\n\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock')
    
    # def battle_phase(self):
    #     while self.dinosaur1.health > 0 and self.robot1.health > 0:
    #         self.robot1.attack(self.dinosaur1)
    #         if self.dinosaur1.health > 0:
    #             self.dinosaur1.attack(self.robot1)
        
    # def display_winner(self):
    #     if self.robot1.health <= 0:
    #         print(f'{self.dinosaur1.name} deactivated {self.robot1.name}\n🦖')
    #     elif self.dinosaur1.health <= 0:
    #         print(f'{self.robot1.name} mauled {self.dinosaur1.name}\n🤖')