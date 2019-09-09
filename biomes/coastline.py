from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants



class Coastline(IContainsAnimals, IContainsPlants, Identifiable):
    def __init__(self):
        IContainsAnimals.__init__(self, 15)
        IContainsPlants.__init__(self, 3)
        Identifiable.__init__(self)
        self.type = "Coastline"

    def add_animal(self, animal):
        try:
            if animal.saltwater:
                super().add_animal(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")

    # def add_plant(self, plant):
    #     try:
    #         if plant.freshwater and plant.requires_current:
    #             self.plants.append(plant)
    #     except AttributeError:
    #         raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")
