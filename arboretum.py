class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__rivers = []
        self.__grasslands = []
        self.__mountains = []
        self.__swamps = []
        self.__forests = []
        self.__coastlines = []

    @property
    def rivers(self):
        return self.__rivers

    def add_river(self, new_river):
        self.__rivers.append(new_river)

    def __str__(self):
        return f"rivers : {self.__rivers}"
