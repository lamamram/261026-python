## modèle pour chaque UI
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from gui_MainWindow import Ui_MainWindow
from PySide6.QtCore import Slot
from text_analyser import Counter

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.resize(600, 400)
        self.setupUi(self)

        # gestion d'évènement sur un widget: click sur le bouton
        # connecter == chercher une méthode qui exécute la logique métier
        # slot == gestionnaire d'évènement (eventhandler)
        # self.okBtn.clicked.connect(self.on_okBtn_clicked)

    @Slot()
    def on_okBtn_clicked(self):
        """
        connexion automatique des gestionnaires d'évènements
        1/ décorer la méthode avec Sllot()
        2/ nommer la méthode selon on_<widget_name>_<event_name>
        """
        self.listWidget.clear()

        text = self.textEdit.toPlainText()
        min_len = self.signWords.value()
        counter = Counter(text,min_len=min_len)
        for k, v in counter.get_occurences().items():
            self.listWidget.addItem(f"{k}: {v}")
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
