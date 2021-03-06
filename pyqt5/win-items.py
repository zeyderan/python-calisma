import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow



# main window için tanımlanan fonksiyon
def window():
    # komut satırından argüman almak için Qapplication kullanılır
    app = QApplication(sys.argv)

    # Boş ana pencere nesnesi 
    win = QMainWindow()

    # pencere başlığı
    win.setWindowTitle('İlk Uygulama')

    # pencere konumu ve boyutu
    win.setGeometry(400,200,500,500)

 
    #label eklendi ve pencere içine konumlandırıldı
    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText('Adınız: ')
    lbl_name.move(50,30)

    #label eklendi ve pencere içine konumlandırıldı
    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText('Soyadınız: ')
    lbl_surname.move(50,70)

    #label eklendi ve pencere içine konumlandırıldı
    lbl_tel = QtWidgets.QLabel(win)
    lbl_tel.setText('Telefon: ')
    lbl_tel.move(50,110)


    #text box ekleme işlemi
    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(150,30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150,70)

    #clicked slot.
    def clicked(self):
        print('butona tıklandı ' + txt_name.text()+ ' '+ txt_surname.text())

    # buton eklendi
    btn_save = QtWidgets.QPushButton(win)
    #buton üzerindeki yazı
    btn_save.setText('Kaydet')
    #butonun pencere içindeki konumu
    btn_save.move(150,110)

    #butonunun clicked sinyali ile clicked slotu bağlandı.
    btn_save.clicked.connect(clicked)

    #pencereyi gösterir
    win.show()

    # pencre üzerinde x butonuna basınca çıkılsın
    sys.exit(app.exec_())

# fonksiyon call
window()
