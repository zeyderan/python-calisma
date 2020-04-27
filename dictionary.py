# key - value

# 41 => kocaeli 34 => istanbul

# listeler ile yaparsak
# sehirler = ['kocaeli','istanbul']
# plakalar = [41,34]

# print(plakalar[sehirler.index('kocaeli')])
# print(sehirler[plakalar.index(34)])

# plakalar = {'kocaeli': 41, 'istanbul' : 34}

# print(plakalar['kocaeli'])

# plakalar['ankara'] = 6

# print(plakalar)

users = {
    'aykut' : {
        'age' : 31,
        'roles' : ['user'],
        'email' : 'aykut@gmail.com',
        'adres' : 'istabul',
        'phone' :'1234567'
    },
    'ömer' : {
        'age' : 1,
        'roles' : ['admin', 'user'],
        'email' : 'ömer@gmail.com',
        'adres' : 'istabul',
        'phone' :'7654123'
    }
}
# print(users['aykut']['age'])
# print(users['aykut']['email'])
# print(users['aykut']['adres'])
# print(users['aykut']['phone'])

print(users['ömer']['roles'])