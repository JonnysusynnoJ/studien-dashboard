from typing import Dict, List

from anyio import key

class Chatbot:
    '''
    Ein einfacher regelbasierte Chatbot für das Studien-Dashboard. 
    Er kann einfache Fragen beantworten, die in seiner Knowledge-Base gespeichert sind.
    '''

    def __init__(self, knowledge_base: Dict[str, str], tags: List[str]=[]):
        self.knowledge_base = knowledge_base
        self.tags = tags
    
    def get_response(self, question: str) -> str:
        '''
        Gibt eine Antwort auf eine Frage zurück. 
        Die Frage wird in Kleinbuchstaben umgewandelt und auf Schlüsselwörter geprüft.
        '''
        question = question.lower().strip()

        for keyword in self.knowledge_base:
            if keyword.lower() in question:
                return self.knowledge_base[keyword]

        return "Das habe ich leider nicht verstanden. Bitte stelle eine andere Frage."
    
    def get_all_keywords(self) -> List[str]:
        '''Gibt eine Liste aller verfügbaren Schlüsselwörter zurück.'''
        return list(self.knowledge_base.keys())
    
    def get_tags(self) -> List[str]:
        '''Gibt die dem Chatbot zurgeordneten Tags zurück.'''
        return self.tags
    
    @classmethod
    def with_default_knowledge(cls, termin_verwaltung, studienfortschritt) -> "Chatbot":
        '''Erstelllt einen Chatbot mit vordefinierter Knowledge-Base'''

        knowledge_base = {}
        # Begrüßung
        for keyword in ["hallo", "servus", "hi", "hey"]:
            knowledge_base[keyword] = "Willkommen im Studien Dashboard! Wie kann ich dir helfen?"

        # Termine
        for keyword in ["termin", "termine", "veranstallungen"]:
            termine = "\n".join(f"⚪️ {t}" for t in termin_verwaltung.termine)
            knowledge_base[keyword] = "Hier sind deine Termine:\n" + termine

        # Fortschritt    
        for keyword in ["fortschritt", "stand", "ects"]:
            knowledge_base[keyword] = "Dein Studienfortschritt ist: " + str(studienfortschritt)
        
        # Hilfe
        for keyword in ["hilfe", "was kannst du", "was machst du"]:
            knowledge_base[keyword] = "Ich beantworte Fragen zu deinem Studium. Probiere z.B: 'Was sind meine Termine?'"

        
        return cls(knowledge_base, tags=["Begrüßung", "Termine", "Hilfe"])
    

            



    



