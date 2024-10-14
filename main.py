
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Stig's App")
        
        button = QPushButton("Press Me! :)")
        
        self.setMinimumSize(QSize(480, 320))
        self.setMaximumSize(QSize(1280, 820))
        
        self.setCentralWidget(button)
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()