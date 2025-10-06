from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QCalendarWidget, QMessageBox, QFileDialog, QLabel
from PyQt5 import uic

class UI(QMainWindow):
    def __init__(self, controller):
        super(UI,self).__init__()
        uic.loadUi("vue.ui",self)
        self.setWindowTitle("Traccar API")
        self.controller = controller#Définition du controller
        self.leUsager = self.findChild(QLineEdit,"leUsager")
        self.leMotPasse = self.findChild(QLineEdit,"leMotPasse")
        self.leDeviceId = self.findChild(QLineEdit,"leDeviceId")
        self.calDe = self.findChild(QCalendarWidget,"calDe")
        self.calA = self.findChild(QCalendarWidget,"calA")
        self.btnFichierOut = self.findChild(QPushButton,"btnFichierOut")
        self.laPath = self.findChild(QLabel,"laPath")
        self.btnSauvegarde = self.findChild(QPushButton,"btnSauvegarde")

    def ouvertureFichierOutut(self):
        save_file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "my_document.txt",
                                                        "Text Files (*.txt);;All Files (*)")
