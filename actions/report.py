from enum import Enum
import os

def build_facility_report(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    biome_list = ("coastlines", "mountains", "rivers", "forests", "grasslands", "swamps")

    for biome_type in biome_list:
        for biome in getattr(arboretum, biome_type):
            print(f'\n\n{biome.type} [%.8s]' % biome.id)
            for animal in getattr(biome, "animals"):
                print(f'    {animal.species} (%.8s)' % animal.id)

    input("\n\nPress any key to continue...")