import pymongo # mongo ile ileşim için modül

# connection string
myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017')

#database seçme - eğer yoksa oluşturur
mydb = myclient['test']

#tablo seçme - eğer yoksa oluşturur
mycol = mydb['products']

#tabloya eklenecek kayıt
product = {'name':'Samsung S5','price':1000}
# result = mycol.insert_one(product)

#tablodan kayıt çekme
#find(filtreleme kriter, seçilecek kolonlar)
result = mycol.find()

#sonuçlar birden fazla ise içerisinde dönmek gerekir
for i in result:
    print(i)
print(myclient.list_database_names())
print(mydb.list_collection_names())
