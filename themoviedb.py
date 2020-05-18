# themoviedb.org => film ve dizi arşivi
# themoviedb' nin sunduğu apiyi uygulamanızda kullanınız.
# Anahtar kelimeye göre arama
# En popüler film listesi
# Vizyondaki film listesi

#e8a9d5f82d78ca210c8076d648685c12

import requests

class theMovieDb:# movidb için sınıf oluştur
    def __init__(self):# gerekli bilgileri yapılandırıcı ile set et
        self.api_url = 'https://api.themoviedb.org/3'
        self.api_key = 'e8a9d5f82d78ca210c8076d648685c12'

    def getPopulars(self):# popular filmler içi apinin verdiği adrese göre değişkenleri yerleştir
        response = requests.get(f'{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1')
        return response.json()# json döner

moviaApi = theMovieDb()

while True:
    secim = input('1- Popular Movies\n2- Exit\nSeçim: ')

    if secim == '2':
        break
    else:
        if secim == '1':
           result = moviaApi.getPopulars()
           for movie in result["results"]:
               print(movie['title']) # popular filmlerin başlık bilgilerini yazdırır.