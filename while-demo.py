sayılar = [1,3,5,7,9,12,19,21]

# 1: sayılar listesini while ile ekrana yazdırın
# x = 0
# while x < len(sayılar):
#     print(sayılar[x])
#     x +=1

# 2: başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
# ilk = int(input('ilk sayıyı girin: '))
# son = int(input('ikinci sayıyı girin: '))
# while son <= ilk:
#     print('ikinci sayı ilk sayıdan büyük olmalı !')
#     son = int(input('ikinci sayıyı girin: '))

# while ilk < son:
#     if (ilk % 2) == 1:
#         print(ilk)
#     ilk += 1


# 3: 1-100 arası sayıları azalarak ekrana yazdırın
# x = 100
# while x > 0:
#     print(x)
#     x -=1

# 4: kullanıcıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın
# x = 1
# resutList = []
# while x < 6:
#     resutList.append(int(input(f'{x}. sayıyı girin : ')))
#     x +=1

# print(sorted(resutList))

# 5: kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayın
#   **ürün sayısını kullanıcıya sorun
#   **dictionary listesi yapısı (name,price) şeklinde olsun
#   ** ürün ekleme işlemi bittiğinde ürünleri ekrana while ile listeleyin

ürünSayı = int(input('Kaç adet ürün gireceksiniz : '))
ürünListesi = []

x = 1
while x < (ürünSayı + 1):
    name = input(f'{x}.ürün ismi girin : ')
    price = input(f'{name} için fiyat bilgisi girin : ')
    ürünListesi.append({
        'name':name,
        'price':price
    })
    x +=1
for urun in ürünListesi:
    print (f"{urun['name']} isimi ürünün fiyatı {urun['price']} dır.")