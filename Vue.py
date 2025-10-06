from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QCalendarWidget, QMessageBox, QFileDialog, QLabel
from PyQt5 import uic

class UI(QMainWindow):
    def __init__(self, controller):
        super(UI,self).__init__()
        uic.loadUi("vue.ui",self)
        self.setWindowTitle("Traccar API")
        self.controller = controller#Définition du controller
        self.leURL = self.findChild(QLineEdit,"leURL")
        self.leUsager = self.findChild(QLineEdit,"leUsager")
        self.leMotPasse = self.findChild(QLineEdit,"leMotPasse")
        self.leDeviceId = self.findChild(QLineEdit,"leDeviceId")
        self.calDe = self.findChild(QCalendarWidget,"calDe")
        self.calA = self.findChild(QCalendarWidget,"calA")
        self.btnFichierOut = self.findChild(QPushButton,"btnFichierOut")
        self.btnFichierOut.clicked.connect(self.ouvertureFichierOutut)
        self.laPath = self.findChild(QLabel,"laPath")
        self.btnSauvegarde = self.findChild(QPushButton,"btnSauvegarde")

    def ouvertureFichierOutut(self):
        fichier = QFileDialog.getSaveFileName(self, "Sauvegarde GEOJSON", "position.geojson",
                                                        "Fichier geojson (*.geojson)")
        if fichier:
            self.laPath.setText( fichier[0])