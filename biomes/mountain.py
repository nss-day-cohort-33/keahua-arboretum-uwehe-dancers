from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from biomes import Biome

class Mountain(IContainsAnimals, IContainsPlants, Identifiable, Biome):
    def __init__(self):
        """
        Initialize max occupancy of plants and animals
        """
        IContainsAnimals.__init__(self, 6)
        IContainsPlants.__init__(self, 4)
        Identifiable.__init__(self)
        Biome.__init__(self, "Mountain")

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

    def add_plant(self, plant):
        """
        In the mountains, soil is clay; plants must be able to live in clay soil;
        otherwise raise error
        This
        """
        try:
            if plant.clay_soil:
                IContainsPlants.add_plant(self, plant)
        except AttributeError:
            raise AttributeError("plant Is Incompatible With Biome")

