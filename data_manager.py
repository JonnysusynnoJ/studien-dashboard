import json
from terminverwaltung import Terminverwaltung
from termin import Termin

class DataManager:
    '''
    Diese Klasse übernimmt das Speicher und Laden von Daren im JSON-Format.
    '''

    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def save_data(self, data: dict) -> None:
        '''Speicheert ein Dictionary als JSON-Datei'''
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def load_data(self) -> dict:
        '''Lädt Daten aus der JSON-Datie und gibt sie als Dictionary zurück.'''
        try: 
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Datei nicht gefunden - starte mit leeren Daten.")
            return {}
        except json.JSONDecodeError:
            print(f"Fehler beim Einlesen der Datei - ungültiges JSON.")
            return {}
        except Exception as e:
            print(f"Unbekannter Fehler beim Laden: {e}")
            return {}

    def save_termine(self, terminverwaltung: list) -> None:
        '''Speichert die Terminliste in einer JSON-Datei'''
        data = {"termine": terminverwaltung.to_dict_list()}
        self.save_data(data)

    def load_termine(self, terminverwaltung) -> Terminverwaltung:
        '''Lädt die Terminliste aus einer JSON-Datei in ein Terminverwaltung-Objekt'''
        data = self.load_data()
        if "termine" in data:
            terminverwaltung.load_from_dict_list(data["termine"])