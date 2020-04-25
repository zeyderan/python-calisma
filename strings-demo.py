website = "http://www.google.com"
course = "Python Kursu : Baştan Sona Python Programlama Rehberi (40 Saat)"

# 1- 'course' karakter dizesinde kaç karakter bulunmaktadır ?
# 2- 'website' içinden www karaterini alın
# 3- 'website' içinden com karakterini alın
# 4- 'course' içinden ilk 15 ve son 15 karakteri alın
# 5- 'course' ifadesideki karakterleri tesrten yazdırın

name, surname , age, job = 'Ömer','Bayraktar',1.5,'başkan'

# 6- Yukarıda verilen değişkeler ile ekrana aşağıdakii ifadeyi yazdırın
# 'Benim adım Ömer Bayraktar, Yaşım 1.5 ve mesleğim başkan'
# 7- 'Hello world' ifadesindeli w harfini 'W' ile değiştirin
# 8- 'abc' ifadesini yan yana 3 defa yazdırın

# Cevap 1
print(f"'course' karakter dizisinde {len(course)} karakter bulunmaktadır.")

# Cevap 2
ilkIndex=website.find('w',0)
www=website[ilkIndex:(ilkIndex+3)]
print(www)

# Cevap 3
print(website[-3:])

# Cevap 4
ilkOnBesKarakter=website[:15]
sonOnBesKarakter=website[-15:]
print(f"'website' içerisindeki ilk 15 karakter '{ilkOnBesKarakter}' ve son 15 karakter '{sonOnBesKarakter}'")

# Cevap 5
tersten=course[::-1]
print(tersten)

# Cevap 6
print(f'Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}')

# Cevap 7
hello = "Hello world"
hello = hello.replace('w','W')
print(hello)

# Cevap 8
print('abc'*3)