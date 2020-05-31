import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import schedule
import time

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

    #pencereyi gösterir
    win.show()

    # pencre üzerinde x butonuna basınca çıkılsın
    sys.exit(app.exec_())

# fonksiyon call
window()
