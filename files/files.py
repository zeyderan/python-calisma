# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
# Kullanımı : open(dosya_adi, dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir

# "w": (Write) yazma modu. Dosyayı konumda oluşturur.
#   **dosya içeriğini siler ve yeniden yazar
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# "r": (Read) okuma. varsayılan. Dosya konumda yoksa hata verir.

# file = open('newfile.txt','w',encoding='utf-8')
# file.write('merhaba dünya')
# file.close()

# file = open('newfile.txt','a',encoding='utf-8')
# file.write('\nbu yazı "a" modu ile eklendi')
# file.close()

#dosya önceden varsa hata verir
# file = open('newfile.txt','x',encoding='utf-8')
# file.write('\nbu yazı "x" modu ile eklendi')
# file.close()

# file = open('newfile.txt','r',encoding='utf-8')
# icerik = file.readlines()
# for line in icerik:
#     print(line,end='')
# file.close()