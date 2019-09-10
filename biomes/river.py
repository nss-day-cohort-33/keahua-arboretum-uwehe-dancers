from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from biomes import Biome

class River(IContainsAnimals, IContainsPlants, Identifiable, Biome):

    def __init__(self):
        """
        Initialize max occupancy of plants and animals
        """
        IContainsAnimals.__init__(self, 12)
        IContainsPlants.__init__(self, 6)
        Identifiable.__init__(self)
        Biome.__init__(self, "River")

    def add_animal(self, animal):
        """
        River is Brackish water; animals must be brackish
        otherwise raise error
        """
        try:
            if animal.brackish_water:
                super().add_animal(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")

    # def add_plant(self, plant):
    #     try:
    #         if plant.freshwater and plant.requires_current:
    #             self.plants.append(plant)
    #     except AttributeError:
    #         raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")
