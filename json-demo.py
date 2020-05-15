import json
import os
# Model
# Kullıcı oluştururken kullanılacak kalıp
class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

#Kullanıcı ile veritabanı (şu anda .json dosyasına yazıyoruz) üzerinde işlemler yapmamızı sağlayan sınıf
class UserRepository:
    # Cunstructor
    def __init__(self):
        self.users = [] # belleğe yüklü kulanıcı listesi boş set ediliyor
        self.isLoggedIn = False # anlık kullanıcı login mi
        self.currentUser = {} # anlık kullanıcı listesi
        #load users from .json file
        self.loadUser()
    def loadUser(self):
        if os.path.exists('users.json'):# user.json dosyası dizinde mevcut ise
          with open('users.json','r',encoding='utf-8') as file:# dosyayı okuma modunda açar
              users = json.load(file)
              for user in users:# kullanıcılar listesi içinde döner (kullanıcılar json objeleridir)
                  user = json.loads(user)# json to dictionary dönüşümü yapar

                  #bilgiler ile yeni bir user nesnesi oluşturur
                  newUser = User(username=user['username'],password=user['password'],email=user['email'])
                  self.users.append(newUser)# bellekte bulunan users listesine ekler
                  print(self.users) # bellekteki kullanıcıları ekrana yazar (user obje liste elemanları bellek adresi yazılır)
    def register(self,user: User):#kullanıcı kayıt işlemi yapar user nesnesi bekler
        self.users.append(user)#bellekte yüklü kullanıcı listesine ekleme yapar
        self.saveToFile()# dosya kayıt metodunu çağırı
        print('Kullanıcı Oluşturuldu.')
    def login(self,username,password):# login işlemi yapar
        for user in self.users:# bellekteki kullanıcılar üzerinde döner
            if user.username == username and user.password == password:#kullanıcı adı ve şifre doğru ise
                self.isLoggedIn = True # login bilgisi true olur
                self.currentUser = user # anlık kullanıcı set edilir
                print('login yapıldı')
                break # kullanıcı adı şifre eşleşirse döngüden çıkar
    def logout(self):# log out işlemi yapar
        self.isLoggedIn = False # login bayrağını false yapar
        self.currentUser = {}# anlık kullanıcı listesini temizler
        print('çıkış yapıldı.')
    def identity(self):# aktif kullanıcının bilgilerini döner
        if self.isLoggedIn:#kullanıcı login olmuş mu ?
            print(f'username: {self.currentUser.username}')# kullanıcı adını yaıdr
        else:
            print('giriş yapılmadı')# hata fırlat
    def saveToFile(self):
        list = [] # kaydedilecek bilgilerin listesi 

        for user in self.users:# bellekte bulunanan kullanıcı listesi üzerinde döner
            list.append(json.dumps(user.__dict__))# user objesini dictionar yapar, json a çevirir ve listeye ekler
        
        with open ('users.json','w') as file:# users.json dosyasını yazma modunda aç. içerik varsa silinir ('w')
            json.dump(list, file)# json bilgiyi dosyaya aktar

respository = UserRepository() # kullanıcı veri crud işlemleri için arayüz

while True:
    print('Menü'.center(50,'*'))#başlık yazar
    secim = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz: ')#kullanıcıdan işlem bilgisi alır
    if secim =='5':# 5 ise çık
        break
    else:
        if secim =='1':
            #register
            username = input('username: ')
            password = input('password: ')
            email    = input('email   : ')

            user = User(username=username, password=password, email=email)#user objesi oluştur

            respository.register(user)# user kaydet
        elif secim =='2':
            if respository.isLoggedIn:# kullanıcı login mi ?
                print('zaten login oldunuz')# hata ver
            else:# login değil ise giriş bilgilerini iste
                username = input('username: ')
                password = input('password: ')
                respository.login(username,password)# login işlemini yap
        elif secim =='3':
            respository.logout()# çıkış işlemini yap
        elif secim =='4':
            #displasy username
            respository.identity()# aktif kullanıcı bilgisini ekrana yazdır
        else:# seçim seçenekler arasıda yoksa hata fırlat döngüyü tekrar başlat
            print('yanlış seçim')
