class Vegetation:
   def __init__(self):
      """
      list of vegetation that animals will eat
      """
      self.__food = ["Shrubs", "Flowers", "Weeds", "Fruit"]

   @property
   def food(self):
      return self.__food


