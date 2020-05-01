# 1- Gönerilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın
# kelime = str(input('Ekrana yazılacak kelimeyi girin: '))
# adet = int(input('Kaç kere yazılsın: '))

# def ekranaDefacaYaz(kelime, adet):
#     for item in range(adet):
#         print(kelime)

# ekranaDefacaYaz(kelime,adet)
# 2- Kendine gönderilen sınırsız sayıda parametreyi bir listeye çeviren fonksiyonu yazın

# def listeyeCevir(*params):
#     liste=[]
#     for param in params:
#         liste.append(param)
#     return liste

# print(listeyeCevir(10,50,64,98))

# 3- Gönerilen 2 sayı arasıdaki tüm asal sayıları bulun

# def asalBul(num1, num2):
#     listeAsal=[]
#     if num1 == num2:
#         print('girdiğiniz sayılar eşit')
#         return []

#     for sayi in range(min(num1,num2),max(num1,num2)+1):
#         if sayi > 1:
#             for i in range(2,sayi):
#                 if(sayi % i == 0):
#                     break
#             else: #python 3.x ile gelen özellik for için else kullaılabilir
#                   # eğer for döngüsü normal olarak sonlanacaksa else bloğu çalışır
#                   # eğer for döngüsü break ile bitecekse çalışmaz.
#                 listeAsal.append(sayi)
#     return listeAsal
    
# sayi1 = int(input('1. sayıyı giriniz: '))
# sayi2 = int(input('2. sayıyı giriniz: '))

# print(asalBul(sayi1,sayi2))
# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün

def tamBolenler(num):
    tamBolenList = []

    for bolen in range(2,num):
        if(num % bolen) == 0:
            tamBolenList.append(bolen)

    return tamBolenList

print(tamBolenler(596))