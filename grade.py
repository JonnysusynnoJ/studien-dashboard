from datetime import datetime

class Grade:
    '''
    Repräsentiert eine einzelen Prfüfungsleistung (Note) für ein Modul.
    '''

    def __init__(self, module_name: str, grade: float, date: str):
        self.module_name = module_name
        self.grade = grade
        self.date = date
    
    @classmethod 
    def default_grades(cls):
        '''Erzeugt eine Liste von vordefinierten Prüfungsleistungen'''
        return [
            cls("Mathematik 1", 1.5, "2025-01-01"),
            cls("Programieren", 2.4, "2025-02-015"),
            cls("Informatik", 1.9, "2025-03-01")
        ]

    def __str__(self):
        return f"Modul: {self.module_name}, Note: {self.grade}, Datum: {self.date}"