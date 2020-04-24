import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor, QPalette, QIcon


class MyApp(QtWidgets.QWidget):
    titleName: str = "Youtube Music"
    webURL: str = "https://music.youtube.com"

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon("./icon.png"))
        self.setStyleSheet("background:black")
        hbox = QtWidgets.QHBoxLayout()
        self.web = QWebEngineView()
        self.web.back
        self.setWindowTitle(self.titleName)
        self.web.setUrl(QUrl(self.webURL))

        hbox.addWidget(self.web)
        self.setLayout(hbox)
        self.show()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
