from termin import Termin
from datetime import datetime
from typing import List

class Terminverwaltung:
    '''
    Diese Klasse verwaltet eine Liste von Termin-Objekten. 
    Sie kann neue Termine hinzufügen, anzeigen und anstehende Termine filter.
    '''

    def __init__(self):
        self.termine: List[Termin] = []

    def add_termin(self, termin: Termin) -> None:
        '''Fügt einen neuen Termin zur Liste hinzu'''
        self.termine.append(termin)
    
    def get_all_termine(self) -> List[Termin]:
        '''Gibt alle gespeicherten Termine zurück'''
        return self.termine
    
    def get_upcoming_termine(self) -> List[Termin]:
        ''''
        Gibt alle Termine zurück, deren Datum in der Zukunft liegt.
        Die Methode nutzt das aktuelle Datum, um zu filtern.
        '''
        heute = datetime.now()
        upcoming = []
    
        for termin in self.termine:
            try: 
                termmin_datum = datetime.strptime(termin.date, "%d.%m.%Y").date()
                if termmin_datum >= heute:
                    upcoming.append(termin)
            except ValueError:
                print(f"Ungültiges Datum: {termin.date}")
        return upcoming

    def display_termine(self) -> None: 
        '''Gibt alle Termine formatiert in der Konsole aus.'''
        if not self.termine:
            print("Es sind keine Termine vorhanden.")
            return 
        
        for termin in self.termine:
            print(termin)

    def remove_termin_by_index(self, index: int) -> bool:
        '''Entfernt einen Termin anhand seines Index. Gibt True zurück, wenn erfolgreich'''
        if 0 <= index < len(self.termine):
            del self.termine[index]
            return True 
        return False
    
    def to_dict_list(self) -> List[dict]:
        '''Gibt alle Termine als Liste von Dictionaries zurück'''
        return [termin.__dict__ for termin in self.termine]
    
    def load_from_dict_list(self, data: List[dict]) -> None:
        '''Lädt Termine aus einer Liste von Dictionaries'''
        self.termine = [Termin(**termin) for termin in data]

    
    @classmethod
    def with_default_termine(cls) -> 'Terminverwaltung':
        '''Erstellt eine Terminverwaltung mit vorgegebenen Terminen'''
        instance = cls()
        instance.add_termin(Termin("Klausur Informatik (Voreingestellt)", "24.02.2025", "9:00", "Raum 123"))
        instance.add_termin(Termin("Probeklausur Mathematik (Voreingestellt)", "01.05.2025", "10:30", "Raum 456"))
        return instance
    
    def __str__(self) -> str:
        '''Gibt alle Termine als formatierten String zurück.'''
        if not self.termine:
            return "Es sind keine Termine vorhanden."
        return "\n".join(str(termin) for termin in self.termine)