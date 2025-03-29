class Termin: 
    def __init__(self, title: str, date: str, time: str, description: str):
        self.title = title
        self.date = date
        self.time = time
        self.description = description
    
    def __str__(self):
        return f"{self.title} am {self.date} um {self.time} - {self.description}"