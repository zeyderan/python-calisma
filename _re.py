import re

result = dir(re)

# regular expression

str = 'Python Kursu: Python Programlama Rehberiniz | 40 saat'

# re.findall()

result = re.findall('Python',str)

result = str.count('Python') # re ile alternatif result = len(re.findall('Python',str))

result = str.split()

result = re.split(' ',str) is str.split() #false , == -> true

result = re.sub(' ','-',str) # değiştirme işlemi yapara boşluk yerine \s de kullanılabilir

result = re.search('Python', str) # match object döner span ve match özellikleri vardır

result = re.findall('[abc]',str) # a b ve c karakterlerini string içinde arar

result = re.findall('[a-zA-Z]', str) # büyük küçük tüm karakterler

result = re.findall('[^abc]',str) # abc dışıkdaki tüm karakterler

result = re.findall('[^0-9]',str) # rakamlar dışıkdaki tüm karakterler


# . - herhangi tek bir karakterin yerini alır

result = re.findall('...',str) # her 3 karakteri döndürür

result = re.findall('Py..on',str)

# ^ belirilen string ile başlıyor mu ? ifadenin tamamı !

result = re.findall('^P',str)

# $ belirtilen string ile bitiyor mu ? ifadenin tamamı !

result = re.findall('t$',str)

# * bir karakterin sıfır ya da daha fazla sayıda olup olmamasına bakar

result = re.findall('sa*t',str)

# + bir karakterin 1 ya da daha fazla olması

result = re.findall('sa+t',str)

# ? bir karakterin 0 ya da 1 kez olması olması

result = re.findall('sa?t',str)

# {} karakter sayısını kontrol eder

result = re.findall('[0-9]{1}',str) # bu şekilde 40 rakamını 4 ve 0 olarak alır

result = re.findall('[0-9]{1,2}',str) # bu şekilde 40 rakamının tamamını alır

# | alternatif seçeneklerden birinin gerçekleşmesi gerekir


# () gruplamak için kullanılır

result = re.findall('(P|C)ython',str)

# \ özel karakterleri aramamızı sağlar
result = re.findall('\|',str) # | karakterini ara varsa getirir

# \A belirtilen karakter string in başında mı 

result = re.findall('\APyt',str)

# \Z belirtilen karakter string in sonunda mı 

result = re.findall('\ZPyt',str)

# \b belirtilen karakter kelimenin in sonunda mı başında mı

result = re.findall('Pyt\b',str)

print(result)