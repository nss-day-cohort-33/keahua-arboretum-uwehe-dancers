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

    def add_river(self, new_river):
        self.__rivers.append(new_river)
