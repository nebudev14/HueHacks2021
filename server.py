import socket 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

s = socket.socket() 
host = socket.gethostname() 
port = 32654 
s.bind(("",port)) 
s.listen(5)

# GUI
class App(QWidget):
    messageSending = ""
    def __init__(self):
        super().__init__()
        self.title = 'Simple Messenger'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # text box
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # send button
        button = QPushButton("Send", self)
        button.setToolTip("Button that sends a message")
        button.move(20, 80)
        button.clicked.connect(self.on_click)

        self.show()

    # sends message to client when clicked
    @pyqtSlot()
    def on_click(self):
        message_sent = self.textbox.text()
        c,addr = s.accept() 
        c.send(bytes(message_sent, "utf-8"))
        c.close()
        self.textbox.setText("")
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

