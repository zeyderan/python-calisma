import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip

# mainwindowdan türeyen window sınıfı
class MyWindow(QMainWindow):
    #constructor
    def __init__(self):
        #parent yapılandırıcı
        super(MyWindow,self).__init__()
        #window title
        self.setWindowTitle('Sınıftan İlk Uygulama')

        #pencere pozisyonu ve ölçüleri
        self.setGeometry(200,200,700,700)
        self.setToolTip('ToolTip')

        #pencere içersine eklenecek widget vb bileşenleri ekleyen metod
        self.initUI()
    
    # pencere içi bileşenleri ekleyen metod
    def initUI(self):
        #label eklendi ve pencere içine konumlandırıldı
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText('Adınız: ')
        self.lbl_name.move(50,30)

        #label eklendi ve pencere içine konumlandırıldı
        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText('Soyadınız: ')
        self.lbl_surname.move(50,70)


        #text box ekleme işlemi
        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150,30)
        self.txt_name.resize(200,32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,70)
        self.txt_surname.resize(200,32)

        # buton eklendi
        self.btn_save = QtWidgets.QPushButton(self)
        #buton üzerindeki yazı
        self.btn_save.setText('Kaydet')
        #butonun pencere içindeki konumu
        self.btn_save.move(150,110)
        #butonunun clicked sinyali ile clicked slotu bağlandı.
        self.btn_save.clicked.connect(self.clicked)
        
    #clicked slot.
    def clicked(self):
        print('butona tıklandı ' + self.txt_name.text()+ ' '+ self.txt_surname.text())

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())

window()