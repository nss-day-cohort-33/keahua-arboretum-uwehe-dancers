from fauna import Fauna
from interfaces import ISaltwater
from interfaces import Identifiable

class Ulae(Fauna, ISaltwater, Identifiable):

    def __init__(self):
        Fauna.__init__(self, "'Ulae", 1)
        ISaltwater.__init__(self)
        Identifiable.__init__(self)

    # @property
    # def prey(self):
    #     return self.__prey

    # def feed(self, prey):
    #     if prey in self.__prey:
    #         print(f"The Ope'ape'a ate {prey} for a meal")
    #     else:
    #         print(f"The Ope'ape'a rejects the {prey}")


    def __str__(self):
        return f"'Ulae {self.id}. Eeee EeeEEeeeeEE!"
