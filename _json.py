# person = {'name':'Ali','languages':['python','C#']}

# result = person['name'] + ' ' + str(person['languages'])

import json
# burada json key value lar çift tırnak değilde tek tırnak ile
#tanımlarsak hata veriyor
#json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes
person_string = '{"name":"Ali","languages":["python","C#"]}'

# JSON string to Dict
result = json.loads(person_string)

with open('newfile.txt') as f:
    data = json.load(f)
    print('from file')
    print(data['name'])
print('from person_string variable')  
print(result['name'])