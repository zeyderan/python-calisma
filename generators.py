# bellekte yer kaplamayan iterator lar üretir

# bu kod bloğu sayı yükseldikçe bellekte yer kaplar
# def cube():
#     result = []

#     for i in range(5):
#         result.append(i**3)
    
#     return result

# print(cube())

#yield kullanırsak bellekte yer kaplamaz
#oluşturduğumuz elemanı liste içerisinde saklamak gerekmiyorsa
#elemanı sadece o anda kullanıp atıyorsak yield kullanmalıyız
# def cube():
#     for i in range(5):
#         yield i**3

# for i in cube():
#     print(i)

liste = (i**3 for i in range(5)) # [] yerine () ile yazarsak generator objesi döner
print(liste)