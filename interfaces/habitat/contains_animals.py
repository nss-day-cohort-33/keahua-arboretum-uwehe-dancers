import os
class IContainsAnimals():

    def __init__(self, max):
        self.animals = []
        self.max_animals = max

    def list_length(self):
        """
        returns a number of animals
        in the biome
        """
        return len(self.animals)

    def add_animal(self, new_animal):
        """
        checks length of list of animals
        if less than max occupancy - add; if not, don't add
        does not display error
        """
        if len(self.animals) < self.max_animals:
            self.animals.append(new_animal)

