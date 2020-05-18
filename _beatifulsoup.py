from bs4 import BeautifulSoup

html_source = '''
<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<div>
<h1>My Second Heading</h1>
</div>
<div>
<h1>My Third Heading</h1>
</div>
<p>My first paragraph.</p>
<a href='www.google.com'></a>
<a href='www.moogle.com'></a>
<a href='www.poogle.com'></a>
</body>
</html>
'''
soup = BeautifulSoup(html_source, 'html.parser')

result = soup.prettify() # dağınık gelen html yapısını düzgün halde basar

result = soup.body.div.h1.string
result = soup.find_all('div')# liste seklinde bütün divleri döner
result = soup.div.findNextSibling().h1.string

result = soup.find_all('a')

for href in result:
    print(href.get('href'))

