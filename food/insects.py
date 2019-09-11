class Insect:
    def __init__(self):
        """
        list of insects that animals will eat
        """
        self.__food = ["Centipedes", "Cockroaches", "Cane Spiders", "Assassin Bug"]

    @property
    def food(self):
        return self.__food

    def list_food(self):
        for index, snack in enumerate(self.__food):
                print(f'{index + 1}. {snack}')
