# try: # hata yakalamaya başla
#     x = int(input('x :'))
#     y = int(input('y :'))
#     print(x/y)
# except ZeroDivisionError: #sıfıra bölünme hatası
#     print('y için 0 girilemez')
# except ValueError:#değer hatası
#     print('x ve y için sayısal değer girmelisiniz')
# else:#hiçbir hata yok ise çalışacak blok
#     print('herşey yolunda')


while True: #kullanıcı doğru bilgi girene kadar sorar
    try: # hata yakalamaya başla
        x = int(input('x :'))
        y = int(input('y :'))
        print(x/y)
    except ZeroDivisionError: #sıfıra bölünme hatası
        print('y için 0 girilemez')
    except ValueError:#değer hatası
        print('x ve y için sayısal değer girmelisiniz')
    else:#hiçbir hata yok ise çalışacak blok
        break #kullanıcı doğru bilgi girdiğinde while dan çıkar
    finally: # her zaman çalışır.
        print('try except bloğu sonlandı')