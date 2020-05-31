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

    # pencere konumu ve boyutunu ayarlar
    win.setGeometry(400,200,500,500)

    #pencereyi gösterir
    win.show()

    # pencre üzerinde x butonuna basınca çıkılsın
    sys.exit(app.exec_())

# fonksiyon call
window()
