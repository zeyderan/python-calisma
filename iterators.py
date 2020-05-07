# liste = [1,2,3,4,5] # __iter__ özelliğine sahiptir

# # for i in liste: #liste bir iterable objedir
# #     print(i)

# iterator = iter(liste)

# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))

# while True: # for döngüsünün aslında yaptığı iş budur
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

class MyNumbers:
    def __init__(self,start,stop):# başlangıç ve bitiş değerlerini alır
         self.start=start
         self.stop=stop
    def __iter__(self):# iter kendisini döner
        return self
    def __next__(self):#start<=stop ise bir arttırarak ekran yazdırır
        if self.start <= self.stop:
            x = self.start
            self.start +=1
            return x
        else:#start > stop hata fırlatır
            raise StopIteration

list = MyNumbers(10,20) # obje oluşur

for x in list:#obje içerisinde döner
    print(x)
    






















