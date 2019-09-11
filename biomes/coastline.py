from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from biomes import Biome

class Coastline(IContainsAnimals, IContainsPlants, Identifiable, Biome):
    def __init__(self):
        """
        Initialize max occupancy of plants and animals
        """
        IContainsAnimals.__init__(self, 15)
        IContainsPlants.__init__(self, 3)
        Identifiable.__init__(self)
        Biome.__init__(self, "Coastline")

    def add_animal(self, animal):
        """
        Coast is saltwater; animals must be able to live in saltwater;
        otherwise raise error
        """
        try:
            if animal.saltwater:
                super().add_animal(animal)
        except AttributeError:
            raise AttributeError("Animal Is Incompatible With Biome")

    # def add_plant(self, plant):
    #     try:
    #         if plant.freshwater and plant.requires_current:
    #             self.plants.append(plant)
    #     except AttributeError:
    #         raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")
