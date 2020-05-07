def ortalamalari_oku():
    while open ()

def not_gir():
    ad = input('Öğrenci Adı: ')
    soyad = input('Öğrenci Soyadı: ')
    not1 = input('not 1: ')
    not2 = input('not 2: ')
    not3 = input('not 3: ')

    with open('sinav_notlari.txt','a',encoding='utf-8') as file:
        file.write(f'{ad} {soyad} : {not1},{not2},{not3}\n')
def notlari_kaydet():
    pass

while True:
    islem = input('1- Notları Oku\n2- Not gir\n3- Notları Kayıt Et\n4- Çıkış\n')

    if islem =='1':
        ortalamalari_oku()
    elif islem =='2':
        not_gir()
    elif islem =='3':
        notlari_kaydet()
    else:
        break