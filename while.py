x = 1

# while x <= 100: # 1 - 100 arası çift sayıları yazdırır.
#     if x % 2 == 0:
#         print(x)
#     x +=1

name = '' # bu şekilde name False olarak algılanır.

while not name.strip():# boşluk karakterlerini kaldırır.
    name = input('isminizi girin :')
print(f'merhaba {name}')