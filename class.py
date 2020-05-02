# Object Oriented Programming (OOP)

# Class

class Person: # class ismi büyük harfle başla
    # class attributes
    adress = 'no information'
    # object attributes
    def __init__(self, name, year): # sefl -> classtan üretilen objeyi temsil eder
        self.name = name
        self.year = year
    #methods

# instance (object)
p1 = Person('ali',1990) # classtan obje tanımladık
p2 = Person('yağmur',1995)
# updating
p1.name = 'aykut'
p1.adress = 'istabul'
# accessing object attributes
print(f'name : {p1.name} year : {p1.year} adress : {p1.adress}')
print(f'name : {p2.name} year : {p2.year} adress : {p2.adress}')
#print(p1 == p2) # False