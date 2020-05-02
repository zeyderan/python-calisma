# Bankamatik Uygulaması

hesapA = {
    'ad': 'Aykut Bayraktar',
    'hesapNo': '155457568',
    'bakiye': 3000,
    'ekHesap': 2000
}

hesapB = {
    'ad': 'Sibel Bayraktar',
    'hesapNo': '9944587854',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz.')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/y)')
            if ekHesapKullanimi == 'e':

                ekhesapKullanılacakMiktar = miktar - hesap['bakiye']

                hesap['ekHesap'] -= ekhesapKullanılacakMiktar

                hesap['bakiye']=0


                print('paranızı alabilirsiniz.')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")
        else:
            print('üzgünüz bakiye yetersiz.')

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesabınızda {hesap['ekHesap']} TL limit bulunmaktadır.")

paraCek(hesapA,2500)

paraCek(hesapA,2000)

bakiyeSorgula(hesapA)