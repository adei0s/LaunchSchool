class Person:
    def __init__ (self, first_name):
        self._first_name = first_name # attribute for first name
        self._last_name = '' # attribute for last name, default empty

    def __str__ (self):
        return self.name

    @property
    def name (self):
        return f'{self._first_name} {self._last_name}'

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @name.setter
    def name(self, new_name):
        new_name = new_name.split()
        self._first_name = new_name[0]
        if len(new_name) > 1:
            self._last_name = new_name[1]
        else:
            self._last_name = ''

    @first_name.setter 
    def first_name(self, new_name):
        self._first_name = new_name

    @last_name.setter
    def last_name(self, new_name):
        self._last_name = new_name



bob = Person('Robert Smith')
print(f"The person's name is: {bob}")