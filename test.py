class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other): # greater than: >
        return self.age > other.age

    def __ge__(self, other): # greater than or equal to: >
        return self.age >= other.age

    def __lt__(self, other): # less than: <=
        return self.age < other.age
    
    def __le__(self, other): # less than or equal to: <=
        return self.age <= other.age

    def __eq__(self, other): # equal to: ==
        return self.age < other.age
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"


p01 = Person('ali', 19)
p02 = Person('vali', 16)

print(p01)
