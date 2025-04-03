class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name
    
    def info(self):
        return f"a {self.species} named {self.name}"
        
class Owner:
    def __init__(self, name):
        self.name = name
        self.pet_list = []
        
    def add_pet(self, pet):
        self.pet_list.append(pet)
        
    def number_of_pets(self):
        return len(self.pet_list)
        
    def print_pets(self):
        for pet in self.pet_list:
            print(pet.info())
        
        
class Shelter:
    def __init__(self):
        self.human_list = []
        
    def adopt(self, owner, pet):
        if owner not in self.human_list:
            self.human_list.append(owner)
        owner.add_pet(pet)
    
    def print_adoptions(self):
        for human in self.human_list:
            print(f"{human.name} has adopted the following pets:")
            human.print_pets()


cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")