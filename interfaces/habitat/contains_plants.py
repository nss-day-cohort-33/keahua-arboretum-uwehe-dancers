class IContainsPlants():

    def __init__(self, max):
        self.plants = []
        self.max_plants = max

    def plant_list_length(self):
        """
        returns a number of plants
        in the biome
        """
        return len(self.plants)

    def add_plant(self, new_plant):
        """
        checks length of list of plants
        if less than max occupancy - add; if not, don't add
        does not display error
        """
        if len(self.plants) < self.max_plants:
            self.plants.append(new_plant)

    def give_plant(self):
        plant_list = list()
        plant_count = list()
        for plant in self.plants:
            plant_list.append(plant.species)
        for plant_species in set(plant_list):
            plant_count.append(f"{str(plant_list.count(plant_species))} {plant_species}")
        return f'{", ".join(plant_count)}'
