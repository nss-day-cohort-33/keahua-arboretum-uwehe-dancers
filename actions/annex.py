import os
from biomes import River
from biomes import Coastline
from biomes import Forest
from biomes import Grassland
from biomes import Mountain
from biomes import Swamp


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
        mountain = Mountain()
        arboretum.mountains.append(mountain)
    if choice == "2":
        swamp = Swamp("froggy")
        arboretum.swamps.append(swamp)
    if choice == "3":
        grassland = Grassland()
        arboretum.grassland.append(grassland)
    if choice == "4":
        forest = Forest()
        arboretum.forest.append(forest)
    if choice == "5":
        river = River()
        arboretum.add_river(river)
    if choice == "6":
        coastline = Coastline()
        arboretum.add_coastline(coastline)
