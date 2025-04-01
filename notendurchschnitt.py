from typing import List
from grade import Grade

class Notendurchschnitt:
    '''
    Die Klasse berechnet den aktuellen Notendurchschnitt
    und vergleicht ihn mit einem angstrebten Zielwert. 
    '''

    def __init__(self, grades: List[Grade], target_average: float):
        self.grades = grades
        self.target_average = target_average   
        self.current_average = self.calculate_average()

    def calculate_average(self) -> float:
        '''Berechnet den Durchschnitt der vorhandenen Noten.'''
        if not self.grades:
            return 0.0
        total = sum(grade.grade for grade in self.grades)
        return round(total / len(self.grades), 2)

    def compare_with_target(self) -> str:
        '''Vergleicht den Durchschnitt mit dem Zielwert.'''
        if self.current_average <= self.target_average:
            return "Ziel erreicht ☑️"
        else: 
            return "Ziel noch nicht erreich ❌"

    @classmethod
    def with_default_data(cls) -> "Notendurchschnitt":
        '''Erstellt ein Notendurchschnitt-Objekt mit Standardwerten und berechnet den Durchschnitt.'''
        grades = Grade.default_grades()
        return cls(grades=grades, target_average = 2.0) 