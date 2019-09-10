from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants

class Swamp(IContainsAnimals, IContainsPlants, Identifiable):
    def __init__(self):
        """
        Initialize max occupancy of plants and animals
        """
        IContainsAnimals.__init__(self, 8)
        IContainsPlants.__init__(self, 12)
        Identifiable.__init__(self)
        self.type = "Swamp"

    def add_animal(self, animal):
        """
        Swamp has stagnant water; animals must be able to live in stagnant water;
        otherwise raise error
        """
        try:
            if animal.stagnant:
                super().add_animal(animal)
        except AttributeError:
            raise AttributeError("Animal Is Incompatible With Biome")