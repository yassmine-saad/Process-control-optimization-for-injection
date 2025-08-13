import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap
from datetime import datetime

class HomePage(QWidget):
    BG_COLOR = "#FFFFFF"
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 480
    BACKGROUND_IMAGE_PATH = "page1.jpg"
    SECOND_PAGE_IMAGE_PATH = "page2.jpg"
    PASSWORD = "0000"  # Définir le mot de passe ici

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Page")
        self.setGeometry(100, 100, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setStyleSheet("background-color: " + self.BG_COLOR)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # Afficher l'image de fond
        pixmap = QPixmap(self.BACKGROUND_IMAGE_PATH)
        label = QLabel(self)
        label.setPixmap(pixmap)
        vbox.addWidget(label)

        # Afficher la date actuelle
        current_date = datetime.now().strftime("%d/%m/%Y")
        date_label = QLabel(current_date)
        vbox.addWidget(date_label)

        # Bouton pour la détection
        detection_button = QPushButton("DETECTION", self)
        detection_button.setStyleSheet("background-color: #008000")
        detection_button.clicked.connect(self.start_detection)
        vbox.addWidget(detection_button)

        self.setLayout(vbox)

    def start_detection(self):
        # Lancer le script de détection en temps réel
        command = '& C:/Users/Houssem/AppData/Local/Microsoft/WindowsApps/python3.12.exe "c:/Users/Houssem/Desktop/test houssem/TFLite_detection_webcam.py" --modeldir "C:\\Users\\Houssem\\Desktop\\test houssem"'
        subprocess.Popen(command, shell=True)
        print("Détection en cours...")
        # Une fois la détection terminée, ouvrir la deuxième page
        self.open_second_page()

    def open_second_page(self):
        self.hide()  # Masquer la fenêtre principale
        self.new_window = SecondPage()
        self.new_window.show()

class SecondPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Deuxième Page")
        self.setGeometry(100, 100, 800, 480)
        self.setStyleSheet("background-color: " + HomePage.BG_COLOR)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # Afficher l'image de fond de la deuxième page
        pixmap = QPixmap(HomePage.SECOND_PAGE_IMAGE_PATH)
        label = QLabel(self)
        label.setPixmap(pixmap)
        vbox.addWidget(label)

        # Afficher la date actuelle sur la deuxième page
        current_date = datetime.now().strftime("%d/%m/%Y")
        date_label = QLabel(current_date)
        vbox.addWidget(date_label)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    homepage = HomePage()
    homepage.show()
    sys.exit(app.exec_())

