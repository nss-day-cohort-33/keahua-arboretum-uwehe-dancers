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

    @property
    def grasslands(self):
        return self.__grasslands

    @property
    def mountains(self):
        return self.__mountains

    @property
    def swamps(self):
        return self.__swamps

    @property
    def forests(self):
        return self.__forests

    @property
    def coastlines(self):
        return self.__coastlines

    def add_river(self, new_river):
        self.__rivers.append(new_river)

    def add_coastline(self, new_coastline):
        self.__coastlines.append(new_coastline)

