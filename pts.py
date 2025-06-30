class Pet:
    def __init__(self, name, species,age,adopted=False):
        self.name = name
        self.species = species
        self.age = age
        self.adopted = adopted
    def print(self):
        if self.adopted == True:
            print(f"{self.name} is a {self.age}-year-old {self.species} who has been adopted.")
        else:
            print(f"{self.name} is a {self.age}-year-old {self.species} who is not adopted yet.")



pet1 = Pet("Rocky", "dog", 2)
pet2 = Pet("Luna", "cat", 5, True)

pet1.print()
pet2.print()