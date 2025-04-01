from datetime import date 

class Dashboard:
    '''
    Repräsentiert das zentrale Dashboard, das alle Komponenten (Terminverwaltung, 
    Chatbot, Studienfortschritt, Notdendurchschnitt, DataManger) zusammenführt
    '''

    def __init__(self, title: str, user_name: str, current_date: str = None, termin_verwaltung=None, chatbot=None, studienfortschritt=None, notendurschnitt=None, data_manager=None):
        self.title = title
        self.user_name = user_name
        self.current_date = current_date or date.today().strftime("%d.%m.%Y")
        self.termin_verwaltung = termin_verwaltung
        self.chatbot = chatbot
        self.studienfortschritt = studienfortschritt
        self.notendurschnitt = notendurschnitt
        self.data_manager = data_manager
    