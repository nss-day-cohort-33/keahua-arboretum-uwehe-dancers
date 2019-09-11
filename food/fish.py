class Fish:
    def __init__(self):
        """
        list of fish that animals will eat
        """
        self.__food = ["Trout", "Mackarel", "Salmon", "Sardine"]

    @property
    def food(self):
        return self.__food


    def list_food(self):
        for index, snack in enumerate(self.__food):
                print(f'{index + 1}. {snack}')





