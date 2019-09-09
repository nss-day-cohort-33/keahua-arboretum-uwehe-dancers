import os
from biomes import River


def build_annex_options():
    """
    This will print out the options for the biomes that you can annex
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain")
    print("2. Swamp")
    print("3. Grassland")
    print("4. Forest")
    print("5. River")
    print("6. Coastline")

def annex_biome(arboretum):
    """
    This gives functionality for the options and calls build_annex_options
    """
    build_annex_options()
    choice = input("Choose what you want to annex. \n \033[1;31;m > \033[1;0;m")

    if choice == "1":
        river = River()
        arboretum.rivers.append(river)
    if choice == "2":
        pass
