import os
class IContainsAnimals():

    def __init__(self, max):
        self.animals = []
        self.max_animals = max

    def animal_list_length(self):
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

    def give_animal(self):
        animal_list = list()
        animal_count = list()
        for animal in self.animals:
            animal_list.append(animal.species)
        for animal_species in set(animal_list):
            animal_count.append(f"{str(animal_list.count(animal_species))} {animal_species}")
        return f'{", ".join(animal_count)}'


