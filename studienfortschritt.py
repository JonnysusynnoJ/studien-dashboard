class Studienfortschritt: 
    '''
    Diese Klasse berechnet und speichert den Fortschritt im Studium 
    anhand von abgeschlossenen Modulen und ECTS-Punkten.
    '''

    def __init__(self, completed_modules: int, total_ects: int, progress_percentage: float = 0.0):
        self.completed_modules = completed_modules
        self.total_ects = total_ects
        self.completed_ects = self.calculate_completed_ects()
        self.progress_percentage = progress_percentage
        
    def calculate_completed_ects(self) -> int:
        '''Geht davon aus, dass ein Modul 5 ECDS hat.'''
        return self.completed_modules * 5

    def calculate_progress(self) -> int:
        '''Berechnet den prozentualen Fortschritt auf Basis der ECTS.'''
        if self.total_ects == 0:
            self.progress_percentage = 0.0
        else: 
            self.progress_percentage = round((self.completed_ects / self.total_ects) * 100)
        return self.progress_percentage

    def __str__(self) -> str:
        return f"{self.progress_percentage}% des Studiums abgeschlossen."
    
    @classmethod
    def default_progress(cls) -> "Studienfortschritt":
        '''Erstellt ein Studienfortschritt-Objekt mit Standardwerten und berechnet den Fortschritt.'''
        instance = cls(completed_modules=6, total_ects=180)
        instance.calculate_progress()
        return instance
