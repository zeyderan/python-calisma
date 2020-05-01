# def changeName(n):
#     n = 'Ömer'

# name = 'Aykut'

# changeName(name)
'''
changeName(name) ile name değişkeni değiştirilemez.
n ve name iki farklı değişken olduğu için name değişmez.
valuetype.
'''
# print(name)

# def change(n):
#     n[0] = 'istabul'
'''
change ile gelen dizinin ilk elemanı değiştirilir.
cünkü dizi değişkenlerinde dizinin referansı(adresi tutulur)
change fonksiyonuna bir dizi gönderince n ve gelen dizi
aynı adrese refere eder !
eğer change fonksiyonun sehirler[:] gibi kopyalama yapan bir 
parametre gönderirsek yine valuetype da olduğu gibi
orjinal dizi üzerinde değişiklik olmaz
'''
# sehirler = ['ankara','izmir']

# change(sehirler)

# print(sehirler) #['istanbul','izmir']

# def add(a, b):
#     return sum((a,b))

# print(add(10,20)) #sadece iki parametre alır

# def add(*params): # parametre olarak tuple listesi alır
#     return sum((params))

# print(add(10,20)) #istenilen sayıda parametre alır
# print(add(10,20,30,40,50,60,70)) #istenilen sayıda parametre alır


def displayUser(**params):# parametre olarak dictionary alır
    print(type(params))
    for key, value in params.items():
        print(f'{key} is {value}')

displayUser(name = 'Aykut', Yas = 15)
displayUser(name = 'Ömer', Yas = 1, city = 'İstanbul')
displayUser(name = 'Sibel', Yas = 10, city = 'Giresun', gender = 'Female')
















