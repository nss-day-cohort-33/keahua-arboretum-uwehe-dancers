import os
from enum import Enum
from fauna import RiverDolphin
from fauna import Bat
from fauna import Gecko
from fauna import Kikakapu
from fauna import Nene_Goose
from fauna import Pueo
from fauna import Spider
from fauna import Ulae

def release_animal(arboretum):
    """
    Set animal variable to nothing
    User input is save as 'choice'
    Checks how many animals can go in each biome and
    only allows animals to be added to biomes with occupancy
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    animal = None

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("\n Choose animal.\n \033[1;31;m> \033[1;0;m ")

    if choice == "1":
        animal = Gecko()

    if choice == "2":
        animal = RiverDolphin()

    if choice == "3":
        animal = Nene_Goose()

    if choice == "4":
        animal = Kikakapu()

    if choice == "5":
        animal = Pueo()

    if choice == "6":
        animal = Ulae()

    if choice == "7":
        animal = Bat()

    if choice == "8":
        animal = Spider()

    # Create empty list that will contain the available biomes for the chosen animal. This list will be used to print out the biomes to release the made animal.

    biome_choice = list()

    # This is an enum that stores all the different types of biomes. Allows us to dynamically check for attributes so we can add biomes to biome_choice

    class biome_attr_enum(Enum):
        coastlines = "saltwater"
        rivers = "brackish_water"
        swamps = "stagnant_water"
        mountains = "elevation"
        grasslands = "ground_nesting"
        forests = "canopy"

    # This uses the enum to check for each type of attribute on an animal, if a key is there, than the equivalant list in arboretum is looped through to add those biomes to biome_choice. Only biomes that have room for more animals are added to the biome_choice.

    for biome_type in biome_attr_enum:
        try:
            if getattr(animal, biome_type.value):
                for biome in getattr(arboretum, biome_type.name):
                    if len(biome.animals) < biome.max_animals:
                        biome_choice.append(biome)
        except AttributeError:
            pass

    os.system('cls' if os.name == 'nt' else 'clear')

    # biome_choice is enumorated in order to get index value with each biome, so we can list out the biomes to the user with according numbers. If there are no animals then the comprehension will return 0 animals, if there are animals then the give_animal method, which is found on IContainsAnimals is ran which returns the string of animal number and species of each species of animal.

    for index, biome in enumerate(biome_choice):
        print(f'{index + 1}. {biome.type} ({biome.give_animal() if len(biome.animals) > 0 else "0 animals"})')

    print("Where would you like to place the animal\033[1;31;m? \033[1;0;m ")
    choice = input("\033[1;31;m> \033[1;0;m ")

    #compares length of animal list to max amount
    #int converts input string to number, -1 to get array index
    if len(biome_choice[int(choice) - 1].animals) < biome_choice[int(choice) - 1].max_animals:
        biome_choice[int(choice) - 1].add_animal(animal)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print error if amount of animals is maxed
        print(f"\n****  That biome is not large enough  ****\n****    Please choose another one     ****\n")


        for index, biome in enumerate(biome_choice):
            print(f'{index + 1}. {biome.type} ({biome.animal_list_length()} animals)')

        print(f"Where would you like to release the {animal.species}\033[1;31;m? \033[1;0;m ")
        choice = input("\033[1;31;m> \033[1;0;m ")

        biome_choice[int(choice) - 1].add_animal(animal)





