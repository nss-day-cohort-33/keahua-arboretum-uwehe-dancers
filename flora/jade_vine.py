from interfaces import ISilt
from interfaces import IMarsh
from flora import Flora

class Jade_Vine(Flora, ISilt, IMarsh):

    def __init__(self):
        Flora.__init__(self, "Blue Jade Vine", 0)
        ISilt.__init__(self)
        IMarsh.__init__(self)