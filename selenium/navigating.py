from selenium import webdriver #ilgili modulü import et
import time # bekleme işlemi için sleep kullanılacak
from selenium.webdriver.common.keys import Keys # tuşa basma eylemleri göndermek için
#hangi browser kullanlacaksa driver indirilip yolu verilmeli
driver = webdriver.Firefox(executable_path=r"C:\\python-calisma\\python-calisma\\selenium\\geckodriver.exe")
url = 'https://semantic-ui.com/examples/login.html?email=gidamuh1%40ugrascatering.com&password=12e12e12e'#browserın ziyaret edeceği adres
driver.get(url)#ziyarete başla
email = driver.find_element_by_name('email') # sayfada email isimli elemente ulaşır
password = driver.find_element_by_name('password')# sayfada password isimli elemente ulaşır
time.sleep(1) # 1 saniye bekler
email.send_keys('aykut@aykut.com')# email isimli elemente string değeri yazar
time.sleep(3)# 3 saniye bekler
password.send_keys('1234')# password isimli elemente string değeri yazar
time.sleep(3)# 3 saniye bekler
password.send_keys(Keys.ENTER)# enter tuşuna basar. burada imleç password üzerinde iken enter'a basar
driver.close()# tarayıcıyı kapatır

