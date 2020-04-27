meyveler = {'portakal','elma','muz'}

#index bilgisi ile elemana ulaşılamaz
#print(meyveler[0]) - hata verir

#setler sıralanamazlar
for x in meyveler:
    print(x)

meyveler.add('çilek')

# var olan elemanı tekrar eklemez

meyveler.add('elma')
print(meyveler)

liste = [1,1,2,3,44,4,4,4]
print(set(liste))

meyveler.remove('çilek')
print(meyveler)