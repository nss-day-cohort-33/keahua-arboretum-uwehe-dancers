import os
from arboretum import Arboretum
from actions import annex_biome
from actions import cultivate_plant
from actions import feed_animal
from actions import release_animal
from actions import build_facility_report


keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n  +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n \033[1;31;m | \033[1;0;m K  e  a  h  u  a    A  r  b  o  r  e  t  u  m \033[1;31;m | \033[1;0;m \n  +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n")
    print("1. Annex Biome")
    print("2. Release New Animal")
    print("3. Feed Animal")
    print("4. Cultivate New Plant")
    print("5. Show Arboretum Report")
    print("6. Exit")

def first_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n  +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n \033[1;31;m | \033[1;0;m K  e  a  h  u  a    A  r  b  o  r  e  t  u  m \033[1;31;m | \033[1;0;m \n  +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n")
    print("1. Annex Biome")


def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    if len(keahua.mountains) is not 0 or len(keahua.grasslands) is not 0 or len(keahua.forests) is not 0 or len(keahua.swamps) is not 0 or len(keahua.rivers) is not 0:
        build_menu()
    else:
        first_menu()

    choice = input("\n Choose a KILLER option. \n \033[1;31;m> \033[1;0;m ")

    if choice == "1":
        annex_biome(keahua)

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        feed_animal(keahua)

    if choice == "4":
        cultivate_plant(keahua)

    if choice == "5":
        build_facility_report(keahua)

    if choice != "6":
        main_menu()

main_menu()
