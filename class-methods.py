# # Object Oriented Programming (OOP)

# # Class

# class Person: # class ismi büyük harfle başla
#     # class attributes
#     adress = 'no information'
#     # object attributes
#     def __init__(self, name, year): # sefl -> classtan üretilen objeyi temsil eder
#         self.name = name
#         self.year = year
#     #methods
#     def intro(self):
#         print('Hello There I am '+self.name)
    
#     def calculateAge(self):
#         return 2020 - self.year

# # instance (object)
# p1 = Person('ali',1990) # classtan obje tanımladık
# p2 = Person('yağmur',1995)

# # updating
# p1.name = 'aykut'
# p1.adress = 'istabul'


# # accessing object attributes
# print(f'name : {p1.name} year : {p1.year} adress : {p1.adress}')
# print(f'name : {p2.name} year : {p2.year} adress : {p2.adress}')

# p1.intro()
# p2.intro()

# print(f'Yaşım {p1.calculateAge()}')

class Circle:
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap
    
    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap

    def alanHesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle(10)

print(c1.cevreHesapla())
print(c1.alanHesapla())