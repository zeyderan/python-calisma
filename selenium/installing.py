from selenium import webdriver #ilgili modulü import et

#hangi browser kullanlacaksa driver indirilip yolu verilmeli
driver = webdriver.Firefox(executable_path=r"C:\\python-calisma\\python-calisma\\selenium\\geckodriver.exe")
url = 'http://www.msn.com'#browserın ziyaret edeceği adres
driver.get(url)#ziyarete başla