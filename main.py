from dashboard import Dashboard
from terminverwaltung import Terminverwaltung
from termin import Termin
from chatbot import Chatbot
from notendurchschnitt import Notendurchschnitt
from data_manager import DataManager
from grade import Grade
from studienfortschritt import Studienfortschritt

def setup_dashboard_data():
       
    # Initilisiert den DataManager mit dem Pfad zur JSON-Datei
    data_manager = DataManager("data.json")
    saved_data = data_manager.load_data()

    # Erstellt die Terminverwaltung und fügt Termine hinzu
    termin_verwaltung = Terminverwaltung.with_default_termine()
    
    # Erstellt die Instanz für Studienfortschritt
    studienfortschritt = Studienfortschritt.default_progress()

    # Erstellt den Chatbot mit einer Knowledge-Base
    chatbot = Chatbot.with_default_knowledge(termin_verwaltung, studienfortschritt)

    

    # Erstellt die Noten
    grades = Grade.default_grades()

    # Erstellt den Notendurchschnitt
    notendurschnitt = Notendurchschnitt.with_default_data()

    return termin_verwaltung, studienfortschritt, notendurschnitt, chatbot, data_manager