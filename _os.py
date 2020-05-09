import os #işletim sistemi ile igli işlem ve bilgi sağlar
import datetime
result = os.name #işletim sistemi adı

result = os.getcwd()#dosyanın olduğu konum

#os.mkdir('klasoryolu') # klasör oluşturur

#os.chdir() dizin değiştiri
result = os.listdir('c:\\')
result = [x for x in result if x.endswith('.sys')] # .sys ile bitenleri filtreler
result = list(filter(lambda x: x.endswith('.sys'),result)) #lambda ile aynı işi yapabiliriz.

result = os.stat('newfile.txt')
result = datetime.datetime.fromtimestamp(result.st_atime)
print(result)

