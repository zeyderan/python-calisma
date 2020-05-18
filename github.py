import requests

#github class oluştur
class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com' # github nesnesi yapıcı ile api adresi set et
        self.token = '2a0cebe35888589a756953098fb345a5c26fc79b'# github nesnesi yapıcı ile jeton set et
    
    def getUser(self, username):# kullaıcı bilgilerini getiri
        response = requests.get(self.api_url+'/users/'+username)
        return response.json() # json geri döner
    def getRepositories(self, username):#kullanıcı repolarını json döner
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()
    def createRepository(self, name):#yeni repo oluşturur
        requests.post(self.api_url+'/user/repos?access_token'+self.token,json={
            "name":name,
            "description":"bu repo otomatik oluşturuldu",
            "homepage":"https://github.com",
            "private":False,
            "has_issues":True,
            "has_projects":True,
            "has_wiki":True
        })
github = Github() # sınıftan türeyen nesne işlemler bunu üzeriden yapılacak

while True:#sonsuz döngü
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ')# kullanıcı seçim menüsü

    if secim == '4':
        break # seçim 4 ise döngüden çıkar. program sonlanır
    else:
        if secim == '1':#kullanıcı ismi ile github kullanıcısı arar
            username = input('username: ')
            result = github.getUser(username)
            print(f'name: {result["name"]}\nrepos: {result["public_repos"]}\nfollowers: {result["followers"]}')#kullanıcı bilgileri fstring

        elif secim =='2':#kullanıcı repolarını getirir ve ekrana yazar
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo["name"])

        elif secim == '3':# burada yeni bir repo oluşturma işlemiş olduğu için api token kullanımını zorunlu tutmuştur.
        #2a0cebe35888589a756953098fb345a5c26fc79b
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print('Yanlış Seçim...')# seçenekler dışında bir giriş yapılırsa mesaj veriri. döngüyü başa alır
