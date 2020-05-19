from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r"C:\\python-calisma\\python-calisma\\selenium\\geckodriver.exe")

url = 'http://github.com'
driver.get(url) # ziyarete başla . sayfa tam yüklenmeden diğer işleme geçmez
time.sleep(2) # 2 sn bekle
print(driver.title) # sayfa başlığını consola yazdır
time.sleep(2) # iki saniye bekle
driver.close() # browser ı kapat

