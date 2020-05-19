import pandas as pd

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1, oranges = s2)

data = [['ahmet',50],['ali',40],['ömer',100],['çınar',10]]

df = pd.DataFrame(data,columns=['Name','Grade'])

print(df)