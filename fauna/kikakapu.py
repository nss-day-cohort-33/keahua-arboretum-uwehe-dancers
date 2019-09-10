from fauna import Fauna
from interfaces import IBrackish
from interfaces import IStagnant
from interfaces import Identifiable

class Kikakapu(Fauna, IBrackish, IStagnant, Identifiable):

    def __init__(self):
        Fauna.__init__(self, "Kikakapu", 1)
        IBrackish.__init__(self)
        IStagnant.__init__(self)
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
        return f"Kikakapu {self.id}. Eeee EeeEEeeeeEE!"