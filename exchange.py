import requests
import json
keys = requests.get('https://api.exchangeratesapi.io/latest')
keys = json.loads(keys.text)
key_list = []
for key in keys['rates']:
    key_list.append(key)
print(f'Kullanılabilecek döviz kurları : {key_list}')
bozulan_doviz = input('bozulacak döviz türünü girin: ').upper()
alinan_doviz  = input('alinacak döviz türünü girin: ').upper()
bozulan_doviz_degeri=input(f'kaç {bozulan_doviz} bozduracaksınız ? : ')
result = requests.get(f'https://api.exchangeratesapi.io/latest?base={bozulan_doviz}')

result = json.loads(result.text)
alinan_doviz_degeri = result['rates'][f'{alinan_doviz}']

print(f'bozdurulan :{int(bozulan_doviz_degeri)} {bozulan_doviz}')
print(f'alınabilecek :{round(float(alinan_doviz_degeri),5)} {alinan_doviz}')