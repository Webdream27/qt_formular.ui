"""************************************************
Einbinden eines erzeugten Formulars
************************************************""" 

# die Module importieren
from PyQt5.QtWidgets import QApplication, QMainWindow

# das Formular importieren
from meingui import Ui_Hauptfenster

# eine Klasse für das Hauptfenster
# sie erbt von QMainWindow und Ui_Formular
class Hauptfenster(QMainWindow, Ui_Hauptfenster):
    
    # die magische Methode __init__()
    def __init__(self):
        
        # die magische Methode __init__() der übergeordneten Klasse aufrufen
        super().__init__()
        
        # die Methode setupUi() aufrufen
        self.setupUi(self)
        
        # das Widget anzeigen
        self.show()      

# eine Instanz der Klasse QApplication erzeugen
app = QApplication([])
# eine Instanz unseres Fensters erzeugen
fenster = Hauptfenster()

# die Anwendung ausführen
app.exec()
