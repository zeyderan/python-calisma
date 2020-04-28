sayılar = [1,3,5,7,9,12,19,21]

# 1- Sayılar listesindeki hangi sayılar 3'ün katıdır ?
# resultList = []
# for i in sayılar:
#     if (i % 3) == 0:
#         resultList.append(i)

# print(resultList)

# 2- Sayılar listesinde sayıların toplamı kaçtır ?
# toplam = 0
# for i in sayılar:
#     toplam +=i
# print(toplam)

# 3- Sayılar listesindeki tek sayıların karesini alınız.
# resultList = []
# for i in sayılar:
#     if (i % 2) != 0:
#         resultList.append(i**2)
# print(resultList)


sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# 4- şehirlerden hangileri en fazla 5 karakterlidir ?
# resutList = []
# for i in sehirler:
#     if len(i)<=5:
#         resutList.append(i)
# print(resutList)

urunler = [
    {'name':'samsung S6','price':'3000'},
    {'name':'samsung S7','price':'4000'},
    {'name':'samsung S8','price':'5000'},
    {'name':'samsung S9','price':'6000'},
    {'name':'samsung S10','price':'7000'}
]

# 5- Ürünlerin fiyatları toplamı nedir ?
# toplam = 0
# for i in urunler:
#     toplam += int(i['price'])
# print(toplam)


# 6- Ürünlerin fiyatı en fazla 5000 olan ürünleri gösteriniz.
resultList = []
for i in urunler:
    if int(i['price']) <= 5000:
        resultList.append(i)

print(resultList)


