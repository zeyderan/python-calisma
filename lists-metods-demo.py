names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998,2000,1998,1987]

# 1- 'Cenk' ismini listenin sonuna ekleyin
names.append('Cenk')
result = names
# 2- 'Sena' değerini listenin başına ekleyin
names.insert(0,'Sena')
result = names
# 3- 'Deniz' ismini listeden silin
denizIndex = names.remove('Deniz')
result = names
# 4- 'Deniz' isminin indexi nedir
#print(denizIndex)
# 5- 'Ali' listenin bir elemanı mıdır ?
result = 'Ali' in names
# 6- Liste elemanlarını ters çevirin
result = names[::-1]
# 7- Liste elemanlarını alfabetik sıralayınız
result = sorted(names)
# 8- years listesini rakamsal büyüklüğe göre sıralayınız
result = sorted(years)
# 9- str = 'Chevrolet,Dacia' karakter dizisini listeye çevirin
result = 'Chevrolet,Dacia'.split(',')

# 10- years dizisinin en büyük ve en küçük elemanı nedir
enkucuk = sorted(years)[0]
enbuyuk = sorted(years)[len(years)-1]

result = f'years dizisinin en büyük elemnı {enbuyuk} ve en küçük elemanı {enkucuk}'

# 11- years dizisinde kaç tane 1998 değeri vardır
result = years.count(1998)

# 12- years dizisinin tüm elemanlarını silin
years = []
result = years
# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
marka1 = input('Marka girin : ')
marka2 = input('Marka girin : ')
marka3 = input('Marka girin : ')
result = [marka1,marka2,marka3]
print(result)