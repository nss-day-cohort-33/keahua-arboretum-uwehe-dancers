from fauna import Fauna
from interfaces import IBrackish
from interfaces import ISaltwater
from interfaces import Identifiable
from food import Fish
import os




class RiverDolphin(Fauna, IBrackish, ISaltwater, Identifiable, Fish):

    def __init__(self):
        Fauna.__init__(self, "River Dolphin", 13)
        IBrackish.__init__(self)
        ISaltwater.__init__(self)
        Identifiable.__init__(self)
        Fish.__init__(self)

    def feed(self, food):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'The {self.species} ate {food} for a meal.\n')
            input('Press enter to return to the main menu...')

    def animal_food(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        Fish.list_food(self)
        print(f"What is on the menu for the {self.species} today?")
        choice = input(">")
        self.feed(self.food[int(choice)-1])

    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'





