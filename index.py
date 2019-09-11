import os
from arboretum import Arboretum
from actions import annex_biome
from actions import cultivate_plant
from actions import feed_animal
from actions import release_animal
from actions import build_facility_report


keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

def first_menu():
    #Starting menu if there are no biomes annexed
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"  +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n \033[1;31;m | \033[1;0;m K  e  a  h  u  a    A  r  b  o  r  e  t  u  m \033[1;31;m | \033[1;0;m \n  +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n")
    print("1. Annex Biome")
    print("6. Exit")

def build_menu():
    #Once user has annexed a biome
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"  +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n \033[1;31;m | \033[1;0;m K  e  a  h  u  a    A  r  b  o  r  e  t  u  m \033[1;31;m | \033[1;0;m \n  +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n")
    print("1. Annex Biome")
    print("2. Release New Animal")
    print("3. Feed Animal")
    print("4. Cultivate New Plant")
    print("5. Show Arboretum Report")
    print("6. Exit")

def check_biomes():
    # If there are any biomes annexed, return true
    if len(keahua.mountains) is not 0 or len(keahua.grasslands) is not 0 or len(keahua.forests) is not 0 or len(keahua.swamps) is not 0 or len(keahua.rivers) is not 0:
        return True
    else:
        return False

def main_menu():
    if check_biomes():
        build_menu()
        choice = input("\n Choose a KILLER option. \n \033[1;31;m> \033[1;0;m ")
    else:
        first_menu()
        choice = input("\n Start by annexing a biome, or exiting. \n \033[1;31;m> \033[1;0;m ")


    if choice == "1":
        annex_biome(keahua)

    if choice == "2" and check_biomes():
        release_animal(keahua)

    if choice == "3" and check_biomes():
        feed_animal(keahua)

    if choice == "4" and check_biomes():
        cultivate_plant(keahua)

    if choice == "5" and check_biomes():
        build_facility_report(keahua)

    if choice != "6":
        main_menu()

main_menu()
