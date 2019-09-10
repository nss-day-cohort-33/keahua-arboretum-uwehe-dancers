class Fauna:

    def __init__(self, species, age):
        """
        assigning a species, age / minimum release age
        """
        self.species = species
        self.age = age
        self.min_age = age

    def move(self, propulsion, speed):
        return f"{self. species} moves at {speed} meters/sec by {propulsion}"
