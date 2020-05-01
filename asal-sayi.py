'''
Soru : Girilen bir sayının asal olup olmadığını bulun.

'''

print(' asal sayı kontrol programı'.title().center(48,'#'),end='\n') #başlık
cikis = False # prgramdançıkış yapılsın mı 
while not cikis: #çıkış yapılana kadar döner
    print('Çıkış yapmak için Q tuşuna basınız !\n') # çıkış yapmak için
    sayi = input('Kontrol edilecek sayıyı giriniz :\n') # girilen bilgiyi al
    asalmi = True # sayı başta asal kabu edildi
    if sayi == 'Q' or sayi =='q': # girilen değer çıkış değeri ise
        print('Güle Güle !\n')
        break
    else:
        sayi = int(sayi) # girilen değeri integer a çevir
    if sayi == 1: # 1 hem kendisi hem 1 e bölünür ancak asal değildir
        print('1 sayısı asal değildir\n')

    for i in range(2,sayi): # 2 den başlayaral girilen sayıya kadar bölerek dener
        if sayi % i == 0: #bölüm varsa asal değildir. döngüden çıkar
            asalmi = False
            break

    if asalmi: #sonuç yazdırır.
        print(f'{sayi} sayısı asaldır\n')
    else:
        print(f'{sayi} sayısı asal değildir\n')