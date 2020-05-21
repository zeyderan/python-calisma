import pandas as pd

df = pd.read_csv('C:\\python-calisma\\python-calisma\\pandas\\all_seasons.csv')

result = df.columns

result = df.head(5) # ilk beş satırı getir
result = df.tail(5) # son beş satırı getir

#sütun ismi ts_pct olanlardan değeri 0.48 den büyük olan için 
#true küçük için false döner her satır için
result = df['ts_pct'].head(20) > 0.48

#sütun ismi ts_pct olanlardan değeri 0.48 den büyük olan için 
# ilk 10 tanesinin player_name ve age bilgilerini yazar
result = df[df['ts_pct'] > 0.48].head(10)[['player_name','age']]
print(result)