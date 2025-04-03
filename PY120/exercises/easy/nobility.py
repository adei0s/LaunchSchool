class WalkMixin:
    def walk(self):
        return f"{self.name} {self.gait()} forward"
        
class Person(WalkMixin):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name

    def gait(self):
        return "strolls"
        
class Noble(Person):
    def __init__(self, name, title):
        super().__init__(name)
        self.title = title
        
    def gait(self):
        return "struts"


class Cat(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"
        
        
mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())