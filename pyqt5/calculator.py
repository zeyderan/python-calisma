import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

#Basit hesap makinesi

class MainForm(QMainWindow):# Ana pencereyi kalıtım yolu ile oluştur
    def __init__(self):#constructor
        super(MainForm,self).__init__()#parent constructor binding child

        self.setWindowTitle('Hesap Makinesi')#pencere başlığı
        self.setGeometry(200,200,500,500)#pecere konum ve boyutu
        self.initUI()#bileşenleri ekrana ekleyecek fonksiyon - aşağıda tanımlandı
    def initUI(self):
        #label ekleme
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('Sayi 1: ')
        self.lbl_sayi1.move(50,30)

        #single line textbox
        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)

        #label ekleme
        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText('Sayi 2: ')
        self.lbl_sayi2.move(50,80)

        #single line textbox
        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2 .move(150,80)
        self.txt_sayi2 .resize(200,32)

        #result label
        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.move(150,180)
        self.lbl_sonuc.resize(300,32)

        #toplama işlemi butonu
        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText('+')
        self.btn_topla.move(50,120)
        self.btn_topla.resize(64,64)

        #çıkarma işlemi butonu
        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText('-')
        self.btn_cikar.move(150,120)
        self.btn_cikar.resize(64,64)

        #çarpma işlemi butonu
        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText('*')
        self.btn_carp.move(250,120)
        self.btn_carp.resize(64,64)

        #bölme işlemi butonu
        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText('/')
        self.btn_bol.move(350,120)
        self.btn_bol.resize(64,64)
        
        # butonlara olay ekleme 
        # butonu slot metoda parametre göndermek içi lambda yapısı kullanıldı
        self.btn_topla.clicked.connect(lambda:self.islemYap(self.btn_topla))
        self.btn_cikar.clicked.connect(lambda:self.islemYap(self.btn_cikar))
        self.btn_carp.clicked.connect(lambda:self.islemYap(self.btn_carp))
        self.btn_bol.clicked.connect(lambda:self.islemYap(self.btn_bol))

        
    # matematiksel işlemi yapan metod
    def islemYap(self,islem):
        #gelen değer sayı ise int yap değilse 0 a eşitle
        a = int(self.txt_sayi1.text() if self.txt_sayi1.text().isdigit() else '0')
        b = int(self.txt_sayi2.text() if self.txt_sayi2.text().isdigit() else '0')
        
        # işlem cinsine göre verilen işlemi yap
        if islem.text() == '+':
            sonuc = a + b
        if islem.text() == '-':
            sonuc = a - b
        if islem.text() == '*':
            sonuc = a * b
        if islem.text() == '/':
            #sıfıra bölünme hatasını önlemek için
            if b != 0:
                #bölmede sonuç tam değilse virgüllü göstermek için float halde bırak ve 2 hane göster
                sonuc = round((a / b),2) if a % b != 0 else int(a / b)
            else:
                #bölen sıfır ise hata ver
                sonuc = 'Sıfıra Bölme İşlemi Mümkün Değildir'
        self.lbl_sonuc.setText(f'Sonuc : {sonuc}')


            

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec())

app()