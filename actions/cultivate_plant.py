import os
from enum import Enum
from flora import Apple_Tree
from flora import Eucalyptus
from flora import Silversword
from flora import Jade_Vine

def cultivate_plant(arboretum):
    """
    Set plant variable to nothing
    User input is save as 'choice'
    Checks how many plants can go in each biome and
    only allows plants to be added to biomes with occupancy
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    plant = None

    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")


    choice = input("\n Choose plant.\n \033[1;31;m> \033[1;0;m ")

    if choice == "1":
        plant = Apple_Tree()

    if choice == "2":
        plant = Silversword()

    if choice == "3":
        plant = Eucalyptus()

    if choice == "4":
        plant = Jade_Vine()

    biome_choice = list()

    class biome_attr_enum(Enum):
        swamps = "marsh_soil"
        mountains = "clay_soil"
        grasslands = "silt_soil"
        forests = "loamy_soil"

    for biome_type in biome_attr_enum:
        try:
            if getattr(plant, biome_type.value):
                for biome in getattr(arboretum, biome_type.name):
                    biome_choice.append(biome)
        except AttributeError:
            pass

    os.system('cls' if os.name == 'nt' else 'clear')

    for index, biome in enumerate(biome_choice):
        print(f'{index + 1}. {biome.type} ({biome.plant_list_length()} plants)')

    print("Where would you like to place the plant\033[1;31;m? \033[1;0;m ")
    choice = input("\033[1;31;m> \033[1;0;m ")

    #compares length of plant list to max amount
    #int converts input string to number, -1 to get array index
    if len(biome_choice[int(choice) - 1].plants) < biome_choice[int(choice) - 1].max_plants:
        biome_choice[int(choice) - 1].add_plant(plant)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print error if amount of plants is maxed
        print(f"\n****  That biome is not large enough  ****\n****    Please choose another one     ****\n")


        for index, biome in enumerate(biome_choice):
            print(f'{index + 1}. {biome.type} ({biome.plant_list_length()} plants)')

        print(f"Where would you like to release the {plant.species}\033[1;31;m? \033[1;0;m ")
        choice = input("\033[1;31;m> \033[1;0;m ")

        biome_choice[int(choice) - 1].add_plant(plant)


