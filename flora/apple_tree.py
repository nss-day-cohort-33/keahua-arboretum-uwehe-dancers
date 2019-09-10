from interfaces import IClay
from flora import Flora

class Apple_Tree(Flora, IClay):

    def __init__(self):
        Flora.__init__(self, "Mountain Apple Tree", 17)
        IClay.__init__(self)