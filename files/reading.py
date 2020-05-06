# try:
#     file = open('newfile2.txt','r')
#     print(file)
# except FileNotFoundError:
#     print('dosya okuma hatası')
# finally:
#     file.close()
#     print('dosya kapandı')

file = open('newfile.txt','r',encoding='utf-8')

# for döngüsü ile okuma
# for i in file:
#     print(i,end='')
# file.close()

# ******************read() fonkiyonu

# content1 = file.read()
# print('içerik 1')
# print(content1)

# content2 = file.read()
# print('içerik 2')
# print(content2) #imleç en sonda olduğu için bişi okuyamaz

# contet = file.read(5)#ilk 5 karakteri okur
# print(contet)

# contet = file.read(3)#sonraki 3 karakteri okur
# print(contet)

# ******************readline() fonkiyonu her seferinde 1 satır okur

# print(file.readline(),end='')

# ******************readlines() fonkiyonu tüm satırları liste içine atar

# print(file.readlines())

file.close()