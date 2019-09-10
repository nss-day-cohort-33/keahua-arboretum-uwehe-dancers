from interfaces import ISilt
from flora import Flora

class Silversword(Flora, ISilt):

    def __init__(self):
        Flora.__init__(self, "Silversword", 22)
        ISilt.__init__(self)
