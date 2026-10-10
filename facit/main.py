from animal import Animal


def can_add_animal(animals, animal_id):
    return animal_id != "" and animal_id not in animals


def add_animal(animals):
    animal_id = input("Animal ID: ")
    if not can_add_animal(animals, animal_id):
        print("ID saknas eller används redan.")
        return False

    name = input("Name: ")
    species = input("Species: ")
    animal = Animal(animal_id, name, species)
    animals[animal_id] = animal
    print("Djuret lades till.")
    return True


def list_animals(animals):
    if not animals:
        print("Inga djur registrerade ännu.")
        return

    for animal_id in animals:
        animal = animals[animal_id]
        print(animal_id, "-", animal.name, "-", animal.species, "- hunger:", animal.hunger)


def animal_menu(animal):
    while True:
        print("\n1. Visa status")
        print("2. Mata djuret")
        print("3. Tillbaka")
        choice = input("Välj: ")

        if choice == "1":
            print(animal.show_status())
        elif choice == "2":
            amount = int(input("Mängd mat (heltal): "))
            if animal.feed(amount):
                print("Djuret har matats.")
            else:
                print("Mängden måste vara större än 0. Hunger ändrades inte.")
        elif choice == "3":
            return
        else:
            print("Välj 1, 2 eller 3.")


def main():
    animals = {}
    running = True

    while running:
        print("\n1. Lägg till djur")
        print("2. Lista djur")
        print("3. Välj djur")
        print("4. Avsluta")
        choice = input("Välj: ")

        if choice == "1":
            add_animal(animals)
        elif choice == "2":
            list_animals(animals)
        elif choice == "3":
            animal_id = input("Vilket ID? ")
            if animal_id in animals:
                animal_menu(animals[animal_id])
            else:
                print("Inget djur har det ID:t.")
        elif choice == "4":
            running = False
        else:
            print("Välj 1, 2, 3 eller 4.")

    print("Hej då!")


main()
