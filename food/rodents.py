class Rodent:
   def __init__(self):
      """
      list of rodents that animals will eat
      """
      self.__food = ["Mongoose", "Roof Rat", "House Mouse", "Polynesian Rat"]

   @property
   def food(self):
      return self.__food