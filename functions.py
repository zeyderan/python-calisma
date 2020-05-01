# def sayHello(user = 'User'): # parametreye başta bir atama yapılırsa
#                              # fonksiyon parametresizde çağrılsa hata vermez ve varsayılan değeri yazar
#     print(f'Hello {user}')

# sayHello('Aykut')
# sayHello('Ömer')
# sayHello()

# def sayHello(user = 'User'):
#     return f'Hello {user}'

# msg = sayHello('Ömer')
# print(msg)


# def total(num1 = 0, num2 = 0):
#     return num1 + num2

# toplam = total(15,62)

# print(toplam)

def yasHesapla(dogumYili):
    '''
    DOCSTRING: Dogum yilina gore yasi hesaplar
    INPUT: Dogum yili
    OUTPUT: Yas
    '''
    return 2020 - dogumYili

ageOmer = yasHesapla(2018)
print(ageOmer)

print(help(yasHesapla))