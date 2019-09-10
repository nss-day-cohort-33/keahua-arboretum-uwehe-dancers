from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants



class Grassland(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        """
        Initialize max occupancy of plants and animals
        """
        IContainsAnimals.__init__(self, 12)
        IContainsPlants.__init__(self, 6)
        Identifiable.__init__(self)
        self.type = "Grassland"

    def add_animal(self, animal):
        """
        Grassland is for ground_nesting animals; raise error if animals not ground_nesting
        """
        try:
            if animal.ground_nesting:
                super().add_animal(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")