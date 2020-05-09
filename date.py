from datetime import datetime
# from datetime import time
# from datetime import date

simdi = datetime.now()

result = simdi.year
result = simdi.hour

result = datetime.ctime(simdi) # Sat May  9 11:51:29 2020

result = datetime.strftime(simdi,'%Y') #2020
result = datetime.strftime(simdi,'%D') #05/09/20 - AA/GG/YYYY
result = datetime.strftime(simdi,'%X') #11:53:22
result = datetime.strftime(simdi,'%A') #Saturday
result = datetime.strftime(simdi,'%B') #May
result = datetime.strftime(simdi,'%d') #09 gün
result = datetime.strftime(simdi,'%a') #Sat
result = datetime.strftime(simdi,'%d-%B-%Y') #GG-AA-YYYY  

t = '21 April 2019 hour 10:12:30'

dt = datetime.strptime(t,'%d %B %Y hour %H:%M:%S')

result = dt

print(result)