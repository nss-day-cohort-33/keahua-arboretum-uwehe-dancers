from interfaces import ILoamy
from flora import Flora

class Eucalyptus(Flora, ILoamy):

    def __init__(self):
        Flora.__init__(self, "Rainbow Eucalyptus Tree", 8)
        ILoamy.__init__(self)