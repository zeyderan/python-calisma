# x = 5
# y = 10
# z = 20

x, y, z = 5, 16, 20

# swap işlemi
#x, y = y, x

x +=5 #x = x + 5
x -=5 #x = x + 5
x *=5 #x = x * 5
x /=5 #x = x / 5
x %=5 #x = x % 5
y //=5 #y = y / 5
y **=5 # y = y ** 5
print(x,y,z)

values = 1, 2, 3,5,6
# burada * ifadesi ile fazla değişken varsa kalanların hepsi z ye liste olarak aktarılır
x, y, *z= values
print(x,y,z,)