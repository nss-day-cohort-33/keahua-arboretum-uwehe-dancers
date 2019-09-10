from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants

class Forest(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        """
        Initialize max occupancy of plants and animals
        """
        IContainsAnimals.__init__(self, 12)
        IContainsPlants.__init__(self, 6)
        Identifiable.__init__(self)
        self.type = "Forest"

    def add_animal(self, animal):
        """
        Forest has a canopy; animals must live in canopy
        otherwise raise error
        """
        try:
            if animal.canopy:
                super().add_animal(animal)
        except AttributeError:
            raise AttributeError("Cannot add animals that do not live in the canopy")

