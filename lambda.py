#def square(num): return num ** 2


numbers = [1,3,5,9]

# # map den dönen sonucu listeye çirerek görebiliriz
# # result = list(map(square,numbers))

# result = list(map(lambda num: num ** 2,numbers))

# # alternatif

# for num in result:
#     print(num)

#def check_even(num): return num % 2 ==0

result = list(filter(lambda x:x%2==1,numbers))

print(result)