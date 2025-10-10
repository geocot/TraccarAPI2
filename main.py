#Martin Couture
#Octobre 2025
#Une classe qui permet de se connecter sur un serveur Traccar via la méthode "login".
#La méthode "Logout" permet de se déconnecter.
#Pour recevoir les informations en format JSON de Traccar, utliser la méthode getPositionsJSON.
#Pour enregistrer les informations de Traccar en format GEOJSON : getPositionsGEOJSON

try:
    __import__("PyQt5")
except ModuleNotFoundError:
    print(f"Le module 'PyQt5' n'existe pas, veuillez l'installer")

import TraccarAPIGeoJSON as tr2
import Controller, sys
from PyQt5.QtWidgets import QApplication, QCalendarWidget

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = tr2.Traccar()
        self.vue = Vue.UI(self.model)
        self.vue.show()


if __name__ == "__main__":
    app = App(sys.argv)
    app.exec_()