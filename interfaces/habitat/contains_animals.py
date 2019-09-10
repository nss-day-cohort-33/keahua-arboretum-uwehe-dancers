import os
class IContainsAnimals():

    def __init__(self, max):
        self.animals = []
        self.max_animals = max

    def list_length(self):
        return len(self.animals)

    def add_animal(self, new_animal):
        if len(self.animals) < self.max_animals:
            self.animals.append(new_animal)

