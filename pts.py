class Pet:
    def __init__(self, name, species,age,adopted=False):
        self.name = name
        self.species = species
        self.age = age
        self.adopted = adopted
    def display_info(self):
        if self.adopted == True:
            print(f"{self.name} is a {self.age}-year-old {self.species} who has been adopted.")
        else:
            print(f"{self.name} is a {self.age}-year-old {self.species} who is not adopted yet.")
    def mark_adopted(self):
        self.adopted = True
    def birthday(self):
        self.age += 1


