import os
from fauna import RiverDolphin

def release_animal(arboretum):
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
        pass

    if choice == "2":
        animal = RiverDolphin()

    if choice == "3":
        pass

    if choice == "4":
        pass

    if choice == "5":
        pass

    if choice == "6":
        pass

    if choice == "7":
        pass

    if choice == "8":
        pass

    biome_choice = []

    try:
        if animal.brackish_water:
            for river in arboretum.rivers:
                biome_choice.append(river)
    except AttributeError:
        pass

    try:
        if animal.saltwater:
            for coastline in arboretum.coastlines:
                biome_choice.append(coastline)
    except AttributeError:
        pass

    os.system('cls' if os.name == 'nt' else 'clear')

    for index, river in enumerate(biome_choice):
        print(f'{index + 1}. {river.type} ({river.list_length()} animals)')

    print("Where would you like to place the animal\033[1;31;m? \033[1;0;m ")
    choice = input("\033[1;31;m> \033[1;0;m ")

    biome_choice[int(choice) - 1].add_animal(animal)


