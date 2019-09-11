import os
from fauna import Fauna
from interfaces import IGroundNesting
from interfaces import Identifiable
from food import Vegetation
class Nene_Goose(Fauna, IGroundNesting, Identifiable, Vegetation):

    def __init__(self):
        Fauna.__init__(self, "Nene Goose", 7)
        IGroundNesting.__init__(self)
        Identifiable.__init__(self)
        Vegetation.__init__(self)

    def feed(self, food):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'The {self.species} ate {food} for a meal.\n')
            input('Press enter to return to the main menu...')

    def animal_food(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        Vegetation.list_food(self)
        print(f"What is on the menu for the {self.species} today?")
        choice = input(">")
        self.feed(self.food[int(choice)-1])


    def __str__(self):
        return f"Nene Goose {self.id}. Eeee EeeEEeeeeEE!"