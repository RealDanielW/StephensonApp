import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPixmap

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stephensons Tank Overview")
        self.resize(1920, 1080)
        self.setStyleSheet("background-color: #363c56;")

        titleBackground = QLabel("", self)
        titleBackground.setStyleSheet("background-color: #242839;")
        titleBackground.setGeometry(0, 0, 1920, 80)
        titleLabel = QLabel("Upper Tank Farm (UTF)", self)
        titleLabel.setStyleSheet("background: transparent; color: #00a9e0; font-size: 26px; font: bold;")
        titleLabel.setGeometry(300, 12, 370, 50)

        menuLabel = QLabel("", self)
        menuLabel.setStyleSheet("background-color: #2a2f45;")
        menuLabel.setGeometry(0, 0, 280, 1080)

        stephensonsLogo = QPixmap("StephensonLogo.png")
        stephensonsLogo2 = QLabel("", self)
        stephensonsLogo2.setStyleSheet("background-color: #2a2f45")
        stephensonsLogo2.setGeometry(5, 13, 50, 50)
        stephensonsLogo2.setPixmap(stephensonsLogo)
        stephensonsLogo2.setScaledContents(True)
        
        stephensonsLabel = QLabel("Stephenson", self)
        stephensonsLabel.setStyleSheet("color: #00a9e0; background: transparent; font-size: 24px;")
        stephensonsLabel.setGeometry(70, 12, 370, 50)

        seperateLine1 = QLabel("", self)
        seperateLine1.setStyleSheet("background-color: #242839; border: none; border-radius: 3px;")
        seperateLine1.setGeometry(17, 79, 243, 3)

        upperMenuButton = QPushButton("", self)
        upperMenuButton.setStyleSheet("""
            QPushButton {
                background-color: #242839;
                border: none;
            }
            QPushButton:hover {
                background-color: #575969;
            }
            QPushButton:pressed {
                background-color: #131728;
                padding-top: 2px;
                padding-left: 1px;
            }
        """)
        upperMenuButton.setGeometry(5, 90, 274, 90)

        whitelineUPP = QLabel("", self)
        whitelineUPP.setStyleSheet("background-color: #00a9e0;")
        whitelineUPP.setGeometry(0, 90, 5, 90)

        upperMenuImage = QPixmap("ArrowUp.png")
        upperMenuImage2 = QLabel("", self)
        upperMenuImage2.setStyleSheet("background: transparent;")
        upperMenuImage2.setGeometry(20, 110, 40, 40)
        upperMenuImage2.setPixmap(upperMenuImage)
        upperMenuImage2.setScaledContents(True)

        upperMenuText = QLabel("Upper Tank Farm", self)
        upperMenuText.setStyleSheet("background: transparent; color: #00a9e0; font-size: 18px; font: bold;")
        upperMenuText.setGeometry(80, 110, 400, 40)

        lowerMenuButton = QPushButton("", self)
        lowerMenuButton.setStyleSheet("""
            QPushButton {
                background-color: #2a2f45;
                border: none;
            }
            QPushButton:hover {
                background-color: #575969;
            }
            QPushButton:pressed {
                background-color: #131728;
                padding-top: 2px;
                padding-left: 1px;
            }
        """)
        lowerMenuButton.setGeometry(5, 185, 274, 90)

        lowerMenuImage = QPixmap("ArrowDown.png")
        lowerMenuImage2 = QLabel("", self)
        lowerMenuImage2.setStyleSheet("background: transparent;")
        lowerMenuImage2.setGeometry(20, 207, 40, 40)
        lowerMenuImage2.setPixmap(lowerMenuImage)
        lowerMenuImage2.setScaledContents(True)

        lowerMenuText = QLabel("Lower Tank Farm", self)
        lowerMenuText.setStyleSheet("background: transparent; color: #00a9e0; font-size: 18px; font: bold;")
        lowerMenuText.setGeometry(80, 207, 400, 40)

        loggedInUser = QLabel("FirstN LastN", self)
        loggedInUser.setStyleSheet("background: transparent; color: #00a9e0; font-size: 18px")
        loggedInUser.setGeometry(80, 880, 400, 40)

        LoggedInImage = QPixmap("UserPFP.png")
        LoggedInImage2 = QLabel("", self)
        LoggedInImage2.setStyleSheet("background: transparent;")
        LoggedInImage2.setGeometry(20, 880, 40, 40)
        LoggedInImage2.setPixmap(LoggedInImage)
        LoggedInImage2.setScaledContents(True)

        seperateLine2 = QLabel("", self)
        seperateLine2.setStyleSheet("background-color: #242839; border: none; border-radius: 3px;")
        seperateLine2.setGeometry(17, 930, 243, 3)

        roundedOval = QLabel("", self)
        roundedOval.setStyleSheet("background-color: #363c56; border: none; border-radius: 15px;")
        roundedOval.setGeometry(150, 950, 100, 40)

        roundedOval2 = QLabel("", self)
        roundedOval2.setStyleSheet("background-color: #2a2f45; border: none; border-radius: 15px;")
        roundedOval2.setGeometry(200, 952, 40, 37)

        DarkModeImage = QPixmap("DarkMode.png")
        DarkModeImage2 = QLabel("", self)
        DarkModeImage2.setStyleSheet("background: transparent;")
        DarkModeImage2.setGeometry(200, 950, 40, 40)
        DarkModeImage2.setPixmap(DarkModeImage)
        DarkModeImage2.setScaledContents(True)

        LightModeImage = QPixmap("LightMode.png")
        LightModeImage2 = QLabel("", self)
        LightModeImage2.setStyleSheet("background: transparent;")
        LightModeImage2.setGeometry(155, 950, 40, 40)
        LightModeImage2.setPixmap(LightModeImage)
        LightModeImage2.setScaledContents(True)

        modeStatusLabel = QLabel("Dark Mode", self)
        modeStatusLabel.setStyleSheet("background: transparent; color: #00a9e0; font-size: 15px;")
        modeStatusLabel.setGeometry(50, 950, 90, 40)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
