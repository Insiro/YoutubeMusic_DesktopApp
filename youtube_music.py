import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5 import QtWidgets


class MyApp(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        hbox = QtWidgets.QHBoxLayout()
        
        self.setWindowTitle("Youtube Music")
        web = QWebEngineView()
        web.setUrl(QUrl("https://music.youtube.com"))
        
        hbox.addWidget(web)
        self.setLayout(hbox)
        self.show()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())