class IContainsAnimals():

    def __init__(self, max):
        self.animals = []
        self.max_animals = max

    def list_length(self):
        return len(self.animals)