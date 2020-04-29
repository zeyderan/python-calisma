'''
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
    buldurmaya çalışın

    ** random modülünü kullanın
    ** 100 üzerinden puanlama yapın her soru 20 puan
    ** hak bilgisini kullanıcıdan alın ve her soru belirtilen
    can sayısı üzerinden hesaplansın.

'''
import random
hak = int(input('maksimum kaç tahminde bulunacağınızı girin : ')) # max tahmin sayısı

aklimda = random.randint(1,100) # bulunacak sayı random
print(aklimda)
tahmin = 0 # tahmin değişkeni
tahminSayisi = 0 # kullanıcı o ana kadar kaç tahminde bulundu
while tahmin != aklimda: # tahmin doğruysa döngüden çıkar
    tahminSayisi +=1 # her döngüde tahmin sayısı artar
    if tahminSayisi == (hak + 1): # tahminsayısı max tahmin sayısını geçerse döngüden çıkar
        break
    else: # soru bilinmediği sürece hak varsa burası döner
        tahmin = int(input('tahmininizi girin : '))
        if tahmin < aklimda: #kullanıcıyı yönlendir.
            print('yukarı !')
        elif tahmin > aklimda:
            print('aşağı !')
puan = round((100-((tahminSayisi - 1) / hak) * 100)) # kullanıcı puan hesaplama
if puan == 0:# son hakkı dahil bilemedi ise
    print(f'Maalesef! Aklımdaki sayı {aklimda}. Tekrar dene !')
else: #cevabı bildi ise
    print(f'Tebrikler! Aklımdaki sayı {aklimda}. {hak} deneme hakının {tahminSayisi} kadarını kullandın. Puanın : {puan} ')