import sqlite3 as db

#mydb = db.connect(':memory:') # in memory db kod çalışınca var olur kod son bulunca hafızadan silinir

mydb = db.connect('test.sqlite')
my_cursor = mydb.cursor() # imleç

# yeni bir tablo oluştur
my_cursor.execute('''\
                CREATE TABLE isim_soyisim (isim, soyisim)\
''')
# işlemi uygula (her seferinde commit etmeye gerek yok)
mydb.commit()

# tabloya veri ekle
my_cursor.execute('''\
                INSERT INTO isim_soyisim VALUES ('AYKUT','BAYRAKTAR')\
''')

mydb.commit()

# eklediğin verileri tablodan çek
data = my_cursor.execute('''\
                SELECT * FROM isim_soyisim\
''').fetchall()

print(data)

