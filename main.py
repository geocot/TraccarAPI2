try:
    __import__("PyQt5")
except ModuleNotFoundError:
    print(f"Le module 'PyQt5' n'existe pas, veuillez l'installer")

import TraccarAPIGeoJSON as tr2
import Vue, sys, Controller
from PyQt5.QtWidgets import QApplication, QCalendarWidget


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = tr2.Traccar()
        self.controller = Controller.Controller(self.model)
        self.vue = Vue.UI(self.controller)
        self.controller.setVue(self.vue)
        self.vue.show()



if __name__ == "__main__":
    app = App(sys.argv)
    app.exec_()