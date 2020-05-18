import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '2a0cebe35888589a756953098fb345a5c26fc79b'
    
    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()
    def getRepositories(self, username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()
    def createRepository(self, name):
        requests.post(self.api_url+'/user/repos?access_token'+self.token,json={
            "name":name,
            "description":"bu repo otomatik oluşturuldu",
            "homepage":"https://github.com",
            "private":False,
            "has_issues":True,
            "has_projects":True,
            "has_wiki":True
        })
github = Github()

while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ')

    if secim == '4':
        break
    else:
        if secim == '1':
            username = input('username: ')
            result = github.getUser(username)
            print(f'name: {result["name"]}\nrepos: {result["public_repos"]}\nfollowers: {result["followers"]}')

        elif secim =='2':
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo["name"])

        elif secim == '3':
        #2a0cebe35888589a756953098fb345a5c26fc79b
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print('Yanlış Seçim...')
