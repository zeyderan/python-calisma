from selenium import webdriver
driver = webdriver.Firefox(executable_path=r"C:\\python-calisma\\python-calisma\\selenium\\geckodriver.exe")
url = 'http://www.msn.com'
driver.get(url)