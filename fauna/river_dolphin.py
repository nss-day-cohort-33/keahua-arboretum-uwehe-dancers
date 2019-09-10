from fauna import Fauna
from interfaces import IBrackish
from interfaces import ISaltwater
from interfaces import Identifiable

class RiverDolphin(Fauna, IBrackish, ISaltwater, Identifiable):

    def __init__(self):
        Fauna.__init__(self, "River Dolphin", 13)
        IBrackish.__init__(self)
        ISaltwater.__init__(self)
        Identifiable.__init__(self)

    # @property
    # def prey(self):
    #     return self.__prey

    # def feed(self, prey):
    #     if prey in self.__prey:
    #         print(f'The dolphin ate {prey} for a meal')
    #     else:
    #         print(f'The dolphin rejects the {prey}')


    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'
