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
