#Part1
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

pet1 = Pet("Max","dog",1)
pet2 = Pet("Bella","cat",2,True)
pet3 = Pet("Chiki","bird",10)\

pet1.mark_adopted()
pet1.birthday()
pet2.birthday()
pet3.mark_adopted()
pet3.birthday()
pet1.display_info()
pet2.display_info()
pet3.display_info()

#Part2
pets = [pet1, pet2, pet3]
def get_non_Adopted():
    non_adopted = []
    for pet in pets:
        if pet.adopted == False:
            non_adopted.append(pet)
    return non_adopted
