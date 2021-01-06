from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QGroupBox, QGridLayout)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QFont, QColor
import sys
import game_results_class

# TODO: Use this format to fill in results in window
results = game_results_class.GameResultsForWeek(1)
print(results[0].get_winning_team())

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Grid layout
        self.grid = QGridLayout()              # The Grid that contains the Grids of game results

        for row in range(1, 12):

            # LEFT SCOREBUG STUFF
            self.LSBgroupbox = QGroupBox()
            self.LSBgroupbox.setStyleSheet("QGroupBox { border: 6px solid black;}")

            self.LSBGrid = QGridLayout()
            self.LSBGrid.addWidget(self.LSBgroupbox, 0, 0, 3, 3)
            self.LSBGrid.setSpacing(0)
            
            LSBdateLabel = QLabel('Date')
            LSBdateLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            LSBdateLabel.setFont(QFont('Arial', 14)) 
            
            LSBteam1Label = QLabel('Pittsburgh Steelers')
            LSBteam1Label.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            LSBteam1Label.setFont(QFont('Arial', 14)) 
            
            LSBteam2Label = QLabel('Green Bay Packers')
            LSBteam2Label.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            LSBteam2Label.setFont(QFont('Arial', 14)) 
            
            LSBteam1ScoreLabel = QLabel('10')
            LSBteam1ScoreLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            LSBteam1ScoreLabel.setFont(QFont('Arial', 14))
            LSBteam1ScoreLabel.setAlignment(Qt.AlignRight) 
            
            LSBteam2ScoreLabel = QLabel('12')
            LSBteam2ScoreLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            LSBteam2ScoreLabel.setFont(QFont('Arial', 14))
            LSBteam2ScoreLabel.setAlignment(Qt.AlignRight) 

            self.LSBGrid.addWidget(LSBdateLabel, 0, 0, 1, 3)
            self.LSBGrid.addWidget(LSBteam1Label, 1, 0, 1, 2)
            self.LSBGrid.addWidget(LSBteam1ScoreLabel, 1, 2, 1, 1)
            self.LSBGrid.addWidget(LSBteam2Label, 2, 0, 1, 2)
            self.LSBGrid.addWidget(LSBteam2ScoreLabel, 2, 2, 1, 1)


            # RIGHT SCOREBUG STUFF
            self.RSBgroupbox = QGroupBox()
            self.RSBgroupbox.setStyleSheet("QGroupBox { border: 6px solid black;}")

            self.RSBGrid = QGridLayout()
            self.RSBGrid.addWidget(self.RSBgroupbox, 0, 0, 3, 3)
            self.RSBGrid.setSpacing(0)
            
            RSBdateLabel = QLabel('Date')
            RSBdateLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            RSBdateLabel.setFont(QFont('Arial', 14)) 
            
            RSBteam1Label = QLabel('Team 1')
            RSBteam1Label.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            RSBteam1Label.setFont(QFont('Arial', 14)) 
            
            RSBteam2Label = QLabel('Team 2')
            RSBteam2Label.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            RSBteam2Label.setFont(QFont('Arial', 14))

            RSBteam1ScoreLabel = QLabel('10')
            RSBteam1ScoreLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            RSBteam1ScoreLabel.setFont(QFont('Arial', 14))
            RSBteam1ScoreLabel.setAlignment(Qt.AlignRight)

            RSBteam2ScoreLabel = QLabel('12')
            RSBteam2ScoreLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            RSBteam2ScoreLabel.setFont(QFont('Arial', 14))
            RSBteam2ScoreLabel.setAlignment(Qt.AlignRight) 

            self.RSBGrid.addWidget(RSBdateLabel, 0, 0, 1, 3)
            self.RSBGrid.addWidget(RSBteam1Label, 1, 0, 1, 2)
            self.RSBGrid.addWidget(RSBteam1ScoreLabel, 1, 2, 1, 1)
            self.RSBGrid.addWidget(RSBteam2Label, 2, 0, 1, 2)
            self.RSBGrid.addWidget(RSBteam2ScoreLabel, 2, 2, 1, 1)


            # ADD LEFT AND RIGHT SCOREBUG TO MAIN GRID LAYOUT
            self.grid.addLayout(self.LSBGrid, row, 0)
            self.grid.addLayout(self.RSBGrid, row, 1)

        self.widget.setLayout(self.grid)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1400, 900)
        self.setWindowTitle('NFL Game Results 2020 Season')
        self.show()

        return

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())