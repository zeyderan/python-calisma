'''
    ogreniler = {
        '120' : {
            'ad' : 'Ali',
            'soyad' : 'Yılmaz',
            'telefon' : '532 000 00 01'
        },
        '125' : {
            'ad' : 'Can',
            'soyad' : 'Korkmaz',
            'telefon' : '532 000 00 02'
        },
        '128' : {
            'ad' : 'Volkan',
            'soyad' : 'Yükselen',
            'telefon' : '532 000 00 01'
        },
    }

'''
# 1- Bilgileri verilen öğrencileri kulanıcıdan aldığınız bilgilerler dictionary içinde saklayın
ogrenciler = {}

number = input('öğrenci no :')
ad = input('öğrenci ad :')
soyad = input('öğrenci soyad :')
telefon = input('öğrenci telefon :')

# ogrenciler[number] = {
#         'ad' : ad,
#         'soyad' : soyad,
#         'telefon' : telefon
#     }

#update kullanarak birden fazla veriyi aynı anda işleme sokabiliriz
ogrenciler.update({
    number : {
        'ad' : ad,
        'soyad' : soyad,
        'telefon' : telefon
    }
})
number = input('öğrenci no :')
ad = input('öğrenci ad :')
soyad = input('öğrenci soyad :')
telefon = input('öğrenci telefon :')
ogrenciler.update({
    number : {
        'ad' : ad,
        'soyad' : soyad,
        'telefon' : telefon
    }
})
number = input('öğrenci no :')
ad = input('öğrenci ad :')
soyad = input('öğrenci soyad :')
telefon = input('öğrenci telefon :')
ogrenciler.update({
    number : {
        'ad' : ad,
        'soyad' : soyad,
        'telefon' : telefon
    }
})
print(ogrenciler)

# 2- Öğrenci bilgisini kullanıcıdan alıp ilgili öğrencinin bilgisini gösterin

ogrenci = input('aranan öğrenci no')

print(ogrenciler[ogrenci])

