from fauna import Fauna
from interfaces import ICanopy
from interfaces import Identifiable

class Gecko(Fauna, ICanopy, Identifiable):

    def __init__(self):
        Fauna.__init__(self, "Gold Dust Day Gecko", 2)
        ICanopy.__init__(self)
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
        return f"Gold Dust Day Gecko {self.id}. Eeee EeeEEeeeeEE!"