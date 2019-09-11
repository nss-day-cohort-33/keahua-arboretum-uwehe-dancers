import os
from fauna import RiverDolphin
from fauna import Bat
from fauna import Gecko
from fauna import Kikakapu
from fauna import Nene_Goose
from fauna import Pueo
from fauna import Spider
from fauna import Ulae

def feed_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    animal = []

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("\n Choose animal to feed.\n \033[1;31;m> \033[1;0;m ")

    if choice == "1":
        animal = arboretum.animal_feed_list("Gold Dust Day Gecko")

    if choice == "2":
        animal = arboretum.animal_feed_list("River Dolphin")

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

    os.system('cls' if os.name == 'nt' else 'clear')

    for index, animal in enumerate(animal):
        print(f'{index + 1}. {animal.species}')

    animal_choice = input("> ")
    animal[int(animal_choice)-1].animal_food()









