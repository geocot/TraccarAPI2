#Martin Couture
#Octobre 2025
#Une classe qui permet de se connecter sur un serveur Traccar via la méthode "login".
#La méthode "Logout" permet de se déconnecter.
#Pour recevoir les informations en format JSON de Traccar, utliser la méthode getPositionsJSON.
#Pour enregistrer les informations de Traccar en format GEOJSON : getPositionsGEOJSON

#Vérification si le module existe.
try:
    __import__("geojson")
except ModuleNotFoundError:
    print(f"Le module 'geojson' n'existe pas, veuillez l'installer")

import datetime, requests
from geojson import Feature, FeatureCollection, Point
from requests.auth import HTTPBasicAuth

class Traccar:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.token = None


    def setUrl(self, url:str) -> None:
        self.url = url
        self.sessionUrl = f"{self.url}/api/session"
    def setUsername(self, username:str) -> None:
        self.username = username
    def setPassword(self, password:str) -> None:
        self.password = password
    def setPath(self, path:str) -> None:
        self.path = path
    def setDeviceId(self, deviceId:int) -> None:
        self.deviceId = deviceId
    def setDateDebut(self, date:datetime) -> None:
        self.dateDebut = date
    def setDateFin(self, date:datetime) -> None:
        self.dateFin = date


    def _login(self)->bool:
        self.session.auth = HTTPBasicAuth(self.username, self.password)
        try:
            response = self.session.post(self.sessionUrl, data={'email': self.username, 'password': self.password})

            if response.status_code == 200:
                cookies = self.session.cookies.get_dict()
                self.token = cookies['JSESSIONID']
                print("Connecté!")
                return True
            else:
                print("Erreur de l'authentification")
                print(response.status_code)
                return False

        except requests.exceptions.RequestException as e:
                print(f"Request failed: {str(e)}")
                return False

    def _logout(self)->bool:
        try:
            self.session.delete(self.sessionUrl)
            self.session.close()
            print('Déconnexion!')
            return True
        except requests.exceptions.RequestException as e:
            print(f"Requête avec problème: {str(e)}")
            return False

    def _getPositionsJSON(self):
        "Retourne un élément JSON"
        if self._login():
            url = f"{self.url}/api/positions"
            params = {}
            if self.deviceId:
                params['deviceId'] = self.deviceId
            if self.dateDebut:
                params['from'] = self.dateDebut.isoformat() + 'Z'
            if self.dateFin:
                params['to'] = self.dateFin.isoformat() + 'Z'

            if self.session:
                try:
                    response = self.session.get(url, params=params)
                    return response.json()

                except requests.exceptions.RequestException as e:
                    print(f"Requête avec problème: {str(e)}")
            self._logout()

    def getPositionsGEOJSON(self):
        "Enregistre un GEOJSON dans un fichier : c:/temp/positions.geojson"
        if self._login():
            JSON = self._getPositionsJSON(self.deviceId, self.dateDebut, self.dateFin)

            listePoints =  []
            for position in JSON:
                listePoints.append(Feature(geometry=Point((position['longitude'], position['latitude'])), properties={"deviceId":position["deviceId"], "deviceTime": position["deviceTime"], "id":position["id"]}))
            fc = FeatureCollection(listePoints)

            file = open(self.path, 'w')
            file.write(str(fc))
            file.close()
            self._logout()

    def blablbar(self):
        print("blablbar")

if __name__ == "__main__":
    import TraccarAPI2 as tr2
    import datetime

    t = tr2.Traccar("https://url.xyz", "votre courriel", "votre mot de passe")
    t.login()
    t.getPositionsGEOJSON(4, datetime.datetime(2025, 10, 4), datetime.datetime.now())
    t.logout()