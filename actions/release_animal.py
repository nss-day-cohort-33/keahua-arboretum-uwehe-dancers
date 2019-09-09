from fauna import RiverDolphin

def release_animal(arboretum):
    animal = None

    print("1. River Dolphin")
    print("2. Dragonfly")

    choice = input("\n Choose animal.\n \033[1;31;m> \033[1;0;m ")

    if choice == "1":
        animal = RiverDolphin()
        # print(arboretum)
    if choice == "2":
        pass

    biome_choice = []
    
    try:
        if animal.brackish_water:
            for river in arboretum.rivers:
                biome_choice.append(river)
    except AttributeError:
        pass

    for index, river in enumerate(biome_choice):
        print(f'{index + 1}. {river.type} ({river.list_length()} animals)')

    print("Where would you like to place the animal\033[1;31;m? \033[1;0;m ")
    choice = input("\033[1;31;m> \033[1;0;m ")

    arboretum.rivers[int(choice) - 1].add_animal(animal)


