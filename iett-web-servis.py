from zeep import Client
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
client = Client('https://api.ibb.gov.tr/iett/ibb/ibb.asmx?wsdl')
result = client.service.DurakDetay_GYY('1')
table = result.find('Table')
print(  table.find('HATKODU').text,
        table.find('YON').text,
        table.find('SIRANO').text,
        table.find('DURAKKODU').text,
        table.find('DURAKADI').text,
        table.find('XKOORDINATI').text,
        table.find('YKOORDINATI').text,
        table.find('DURAKTIPI').text,
        table.find('ISLETMEBOLGE').text,
        table.find('ISLETMEALTBOLGE').text,
        table.find('ILCEADI').text,
        )
