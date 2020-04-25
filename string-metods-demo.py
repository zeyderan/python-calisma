website = "http://www.google.com"
course = "Python Kursu : Baştan Sona Python Programlama Rehberi (40 Saat)"

# 1- '  Hello World  ' karakter dizisinin baş ve sondali boşluk karakterlerini silin
result = '  Hello World  '.strip()    #iki yandeki boşluğu kaldır
result = '  Hello World  '.lstrip()   #soldaki boşluğu kaldır
result = '  Hello World  '.rstrip()   #sağdaki boşluğu kaldır

result = website.lstrip('htp:/')    #soldan hangi karakteri sileceğimizi belirtebiliriz

# 2- 'www.sadikturan.com' içindeki google bilgisi dışındakileri silin
result='www.sadikturan.com'.strip('w.com')

# 3- 'course' içerisinde tüm karakterleri küçük harf yapın
result = course.lower()
result = course.upper()
result = course.title()

# 4- 'website' içerisinde kaç tane 'o' karakteri vardır
result = website.count('o')

# 5- 'website' www ile başlayıp com ile bitiyormu ?
result = website.startswith('www')
result = website.endswith('com')

# 6- 'website' içinde .com ifadesi var mı ?
result = website.find('.com',0,10)

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi ?
result = course.isalpha()
result = "Hello".isalpha()

# 8- 'contends' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz
result = "Contends".center(50,'*')
result = "Contends".ljust(50,'*')
result = "Contends".rjust(50,'*')

# 9- 'course' içindeki tüm boşluk karakterlerini '-' ile değiştirin
result = course.replace(' ','-')

# 10-'Hello World' içerisinde World ifadesini I here ile değiştirin
result = 'Hello World'.replace('World','I here')

# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın
result = course.split(' ')

print(result)