from fauna import Fauna
from interfaces import IStagnant
from interfaces import Identifiable

class Spider(Fauna, IStagnant, Identifiable):

    def __init__(self):
        Fauna.__init__(self, "Hawaiian Happy-Face Spider", .5)
        IStagnant.__init__(self)
        Identifiable.__init__(self)

    # @property
    # def prey(self):
    #     return self.__prey

    # def feed(self, prey):
    #     if prey in self.__prey:
    #         print(f"The Hawaiian Happy-Face Spider ate {prey} for a meal")
    #     else:
    #         print(f"The Hawaiian Happy-Face Spider rejects the {prey}")


    def __str__(self):
        return f"Hawaiian Happy-Face Spider {self.id}. Eeee EeeEEeeeeEE!"