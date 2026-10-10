class Animal:
    def __init__(self, animal_id, name, species):
        self.animal_id = animal_id
        self.name = name
        self.species = species
        self.hunger = 5

    def feed(self, amount):
        if amount <= 0:
            return False

        if amount >= self.hunger:
            self.hunger = 0
        else:
            self.hunger -= amount
        return True

    def show_status(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nHunger: {self.hunger}/10"
