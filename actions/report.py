from enum import Enum
import os

def build_facility_report(arboretum):
    """
      This gives each biome and the animals that they contain.
      The biome_tuple tuple contains all biome list types in arboretum
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    # This tuple contains the names of lists in arboretum

    biome_tuple = ("coastlines", "mountains", "rivers", "forests", "grasslands", "swamps")

    # This loops through tuple and the gets attribute of the arboretum and then loops through animals within the biome to print out biome and the animals within that the biome.

    for biome_type in biome_tuple:
        for biome in getattr(arboretum, biome_type):
            print(f'\n\n{biome.type} [%.8s]' % biome.id)
            for animal in getattr(biome, "animals"):
                print(f'    {animal.species} (%.8s)' % animal.id)

    input("\n\nPress return to continue...")