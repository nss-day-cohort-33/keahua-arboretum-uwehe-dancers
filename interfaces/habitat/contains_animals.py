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
        """
        This loops through the animals list and counts how many animals live in this certain biome. It adds the number of animals and the species name to a list and the list is then joined together and returned.
        """

        # setting an empty list to add all the animal species

        animal_list = list()

        # setting an empty list that will hold the string animal numbers with animal species

        animal_count = list()

        # loops through the animals array and adds every animal species to animal_list.

        for animal in self.animals:
            animal_list.append(animal.species)

        # Then puts animal_list in a set and loops through that to get the count of each animal and adds that string to animal_count

        for animal_species in set(animal_list):
            animal_count.append(f"{str(animal_list.count(animal_species))} {animal_species}")

        # combines animal_count into a string and returns it

        return f'{", ".join(animal_count)}'


