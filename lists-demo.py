# 1- "Bmw,Mercedes,Opel,Mazda" elemanlarına sahip bir liste oluşturunuz
markalar = ['Bmw','Mercedes','Opel','Mazda']
result = markalar

# 2- Liste kaç elemanlıdır ?
result = len(markalar)

# 3- Listenin ilk ve son elemanı nedir ?
result = markalar[0]
result = markalar[-1]

# 4- Mazda değerini Toyota ile değiştirin
result = markalar[-1]='Toyota'

# 5- Mercedes listenin bir elemanımıdır ?
result = 'Mercedes' in markalar

# 6- Listenin -2 indexindeki değer nedir ?
result = markalar[-2]

# 7- Listenin ilk 3 elemanını alın
result = markalar[:3]

# 8- Listenin son iki elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin
markalar[-2] = 'Toyota'
markalar[-1] = 'Renault'
result = markalar

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin
markalar = markalar + ['Audi','Nissan']
result = markalar

# 10- Listenin son elemanını silin
markalar.pop()
result = markalar

# 11- Liste elemanlarını tersten yazdırın

result = markalar[::-1]
# 12- Aşağıdaki verileri bir liste içinde saklayın

        # studentA : Ömer Bayraktar 2018,(100,100,100)
        # studentB : Ömer Eymen 2023,(90,10,50)
        # studentC : Eymen Bayraktar 2020,(15,20,30)
# 13- Liste elemanlarını ekrana yazdırın
print(result)