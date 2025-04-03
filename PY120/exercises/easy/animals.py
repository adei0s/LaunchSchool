class Animal:
    def __init__(self, name, age, legs, species, status):
        self.name = name
        self.age = age
        self.legs = legs
        self.species = species
        self.status = status

    def introduce(self):
        return (f"Hello, my name is {self.name} and I am "
                f"{self.age} years old and {self.status}.")
                
class Cat(Animal):
    def __init__(self, name, age, status):
        super().__init__(name, age, 4, "cat", status)

    def introduce(self):
        return f"{super().introduce()} meow meow!"
    
class Dog(Animal):
    def __init__ (self, name, age, status, owner):
        super().__init__(name, age, 4, "dog", status)
        self._owner = owner
        
    def introduce(self):
        return f"{super().introduce()} woof woof"
        
    def greet_owner(self):
        print(f"Hi {self._owner}! woof woof")
        
cat = Cat("pepe", 4, "happy")
dog = Dog("bobo", 9, "huntry", "daddy")
        
print(cat.introduce())
print(dog.introduce())
