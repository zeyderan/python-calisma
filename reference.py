#value types -> string , numbers
x = 5
y = 25
# y bilgisini x e atalım
x = y
#y üzerinde değişiklik yapalım
y = 10
#değişiklik x'e aktarılmadı
# print(x,y)

#reference types

a = ['apple','banana']
b = ['apple','banana']

a = b
# a üzerinde de 0. eleman grape olarak değişir.
b[0] = 'grape'

print(a,b)