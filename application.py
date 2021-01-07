from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QGroupBox, QGridLayout)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QFont, QColor
import sys
import game_results_class

# TODO: Use this format to fill in results in window
results = game_results_class.GameResultsForWeek(1)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Grid layout
        self.grid = QGridLayout()              # The Grid that contains the Grids of game results

        row = 0
        for game_no in range(0, len(results) - 1):
            print(game_no)

            # LEFT SCOREBUG STUFF
            self.LSBgroupbox = QGroupBox()
            self.LSBgroupbox.setStyleSheet("QGroupBox { border: 6px solid black;}")

            self.LSBGrid = QGridLayout()
            self.LSBGrid.addWidget(self.LSBgroupbox, 0, 0, 3, 3)
            self.LSBGrid.setSpacing(0)
            
            LSBdateLabel = QLabel(results[game_no].get_date())
            LSBdateLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            LSBdateLabel.setFont(QFont('Arial', 14)) 
            
            LSBteam1Label = QLabel(results[game_no].get_losing_team())
            LSBteam1Label.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            LSBteam1Label.setFont(QFont('Arial', 14)) 
            
            LSBteam2Label = QLabel(results[game_no].get_winning_team())
            LSBteam2Label.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            LSBteam2Label.setFont(QFont('Arial', 14)) 
            
            LSBteam1ScoreLabel = QLabel(results[game_no].get_losing_score())
            LSBteam1ScoreLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            LSBteam1ScoreLabel.setFont(QFont('Arial', 14))
            LSBteam1ScoreLabel.setAlignment(Qt.AlignRight) 
            
            LSBteam2ScoreLabel = QLabel(results[game_no].get_winning_score())
            LSBteam2ScoreLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            LSBteam2ScoreLabel.setFont(QFont('Arial', 14))
            LSBteam2ScoreLabel.setAlignment(Qt.AlignRight) 

            self.LSBGrid.addWidget(LSBdateLabel, 0, 0, 1, 3)
            self.LSBGrid.addWidget(LSBteam1Label, 1, 0, 1, 2)
            self.LSBGrid.addWidget(LSBteam1ScoreLabel, 1, 2, 1, 1)
            self.LSBGrid.addWidget(LSBteam2Label, 2, 0, 1, 2)
            self.LSBGrid.addWidget(LSBteam2ScoreLabel, 2, 2, 1, 1)

            # ADD LEFT SCOREBUG TO MAIN GRID LAYOUT
            self.grid.addLayout(self.LSBGrid, row, 0)

            # Increase game number to get number
            game_no += 1

            # Add game ro right if there are games left
            if game_no <= len(results):
            # RIGHT SCOREBUG STUFF
                self.RSBgroupbox = QGroupBox()
                self.RSBgroupbox.setStyleSheet("QGroupBox { border: 6px solid black;}")

                self.RSBGrid = QGridLayout()
                self.RSBGrid.addWidget(self.RSBgroupbox, 0, 0, 3, 3)
                self.RSBGrid.setSpacing(0)
                
                RSBdateLabel = QLabel(results[game_no].get_date())
                RSBdateLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
                RSBdateLabel.setFont(QFont('Arial', 14)) 
                
                RSBteam1Label = QLabel(results[game_no].get_losing_team())
                RSBteam1Label.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
                RSBteam1Label.setFont(QFont('Arial', 14)) 
                
                RSBteam2Label = QLabel(results[game_no].get_winning_team())
                RSBteam2Label.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
                RSBteam2Label.setFont(QFont('Arial', 14))

                RSBteam1ScoreLabel = QLabel(results[game_no].get_losing_score())
                RSBteam1ScoreLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
                RSBteam1ScoreLabel.setFont(QFont('Arial', 14))
                RSBteam1ScoreLabel.setAlignment(Qt.AlignRight)

                RSBteam2ScoreLabel = QLabel(results[game_no].get_winning_score())
                RSBteam2ScoreLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
                RSBteam2ScoreLabel.setFont(QFont('Arial', 14))
                RSBteam2ScoreLabel.setAlignment(Qt.AlignRight) 

                self.RSBGrid.addWidget(RSBdateLabel, 0, 0, 1, 3)
                self.RSBGrid.addWidget(RSBteam1Label, 1, 0, 1, 2)
                self.RSBGrid.addWidget(RSBteam1ScoreLabel, 1, 2, 1, 1)
                self.RSBGrid.addWidget(RSBteam2Label, 2, 0, 1, 2)
                self.RSBGrid.addWidget(RSBteam2ScoreLabel, 2, 2, 1, 1)

                # ADD RIGHT SCOREBUG TO GRID
                self.grid.addLayout(self.RSBGrid, row, 1)


            row += 1

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