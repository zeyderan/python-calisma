import pandas as pd

#data

numbers = [20,30,40,50]
letters = ['a','b','c','d']

pandas_series = pd.Series(numbers)
pandas_series = pd.Series(letters,['c','d','e','f']) # ikinci parametre ile index bilgisini biz verebiliriz

dict = {'a':10,'b':20,'c':30}

pandas_series = pd.Series(dict)

print(pandas_series)