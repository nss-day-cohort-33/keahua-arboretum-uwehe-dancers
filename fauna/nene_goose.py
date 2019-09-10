from fauna import Fauna
from interfaces import IGroundNesting
from interfaces import Identifiable

class Nene_Goose(Fauna, IGroundNesting, Identifiable):

    def __init__(self):
        Fauna.__init__(self, "Nene Goose", 7)
        IGroundNesting.__init__(self)
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
        return f"Nene Goose {self.id}. Eeee EeeEEeeeeEE!"