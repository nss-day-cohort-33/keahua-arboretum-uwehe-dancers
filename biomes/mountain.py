from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants

class Mountain(IContainsAnimals, IContainsPlants, Identifiable):
    def __init__(self):
        """
        Initialize max occupancy of plants and animals
        """
        IContainsAnimals.__init__(self, 6)
        IContainsPlants.__init__(self, 4)
        Identifiable.__init__(self)
        self.type = "Mountain"

    def add_animal(self, animal):
        """
        Mountain is highly elevated; animals must be able to live in high elevation;
        otherwise raise error
        """
        try:
            if animal.elevation:
                super().add_animal(animal)
        except AttributeError:
            raise AttributeError("Animal Is Incompatible With Biome")