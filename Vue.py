#Martin Couture
#Octobre 2025
#Une classe qui permet de se connecter sur un serveur Traccar via la méthode "login".
#La méthode "Logout" permet de se déconnecter.
#Pour recevoir les informations en format JSON de Traccar, utliser la méthode getPositionsJSON.
#Pour enregistrer les informations de Traccar en format GEOJSON : getPositionsGEOJSON

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QCalendarWidget, QMessageBox, QFileDialog, QLabel
from PyQt5 import uic
import datetime

class UI(QMainWindow):
    def __init__(self, model):
        super(UI,self).__init__()
        uic.loadUi("vue.ui",self)
        self.setWindowTitle("Traccar API")
        self.model = model #Définition du model
        self.leURL = self.findChild(QLineEdit,"leURL")
        self.leUsager = self.findChild(QLineEdit,"leUsager")
        self.leMotPasse = self.findChild(QLineEdit,"leMotPasse")
        self.leDeviceId = self.findChild(QLineEdit,"leDeviceId")
        self.calDebut = self.findChild(QCalendarWidget, "calDebut")
        self.calDebut.clicked.connect(self.calDebutClicked)
        self.calFin = self.findChild(QCalendarWidget, "calFin")
        self.calFin.clicked.connect(self.calFinClicked)
        self.btnFichierOut = self.findChild(QPushButton,"btnFichierOut")
        self.btnFichierOut.clicked.connect(self.ouvertureFichierOutut)
        self.laPath = self.findChild(QLabel,"laPath")
        self.btnSauvegarde = self.findChild(QPushButton,"btnSauvegarde")
        self.btnSauvegarde.clicked.connect(self.sauvegardeGeoJson)

    def ouvertureFichierOutut(self):
        fichier = QFileDialog.getSaveFileName(self, "Sauvegarde GEOJSON", "position.geojson",
                                                        "Fichier geojson (*.geojson)")
        if fichier:
            self.laPath.setText(fichier[0])
            self.model.setPath(fichier[0])

    def calDebutClicked(self):
        self.dateDebut = datetime.datetime(self.calDebut.selectedDate().year(), self.calDebut.selectedDate().month(), self.calDebut.selectedDate().day())

    def calFinClicked(self):
        self.dateFin = datetime.datetime(self.calFin.selectedDate().year(), self.calFin.selectedDate().month(), self.calFin.selectedDate().day())

    def sauvegardeGeoJson(self):
            if self.dateDebut < self.dateFin:
                self.model.setDateDebut(self.dateDebut)
                self.model.setDateFin(self.dateFin)
                self.model.setUrl(self.leURL.text())
                self.model.setUsername(self.leUsager.text())
                self.model.setPassword(self.leMotPasse.text())
                self.model.setDeviceId(self.leDeviceId.text())
                self.model.getPositionsGEOJSON()
