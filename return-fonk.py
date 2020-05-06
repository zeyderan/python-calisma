# def usalma(number):
#     def inner(power):
#         return number ** power
#     return inner

# two = usalma(2) # buradan bize bir fonsiyon döner
# print(two(3)) # gelen fonksiyona bir daha parametre girip sonuca ulaşırız

# def yetki_sorgula(page):
#     def inner(role):
#         if role == 'Admin':
#             return f'{role} rolü {page} sayfasına ulaşabilir.'
#         else:
#             return f'{role} rolü {page} sayfasına ulaşamaz.'
#     return inner
# user1 = yetki_sorgula('Product Edit')
# print(user1('Admin'))

