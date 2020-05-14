import json
class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        #load users from .json file
        self.loadUser()
    def loadUser(self):
        pass    
    def register(self,user: User):
        self.users.append(user)
        self.saveToFile()
        print('Kullanıcı Oluşturuldu.')
    def login(self):
        pass
    def saveToFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))
        
        with open ('users.json','w') as file:
            json.dump(list, file)

respository = UserRepository()

while True:
    print('Menü'.center(50,'*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz: ')
    if secim =='5':
        break
    else:
        if secim =='1':
            #register
            username = input('username: ')
            password = input('password: ')
            email    = input('email   : ')

            user = User(username=username, password=password, email=email)

            respository.register(user)
        elif secim =='2':
            #login
            pass
        elif secim =='3':
            #logout
            pass
        elif secim =='4':
            #displasy username
            pass
        else:
            print('yanlış seçim')
# 20:06 da kaldın.