from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QGroupBox, QGridLayout, QComboBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QFont, QColor
import sys
import game_results_class

results = game_results_class.GameResultsForWeek(2020, 1)      # results[0] contains list of game objects, results[1] contains the corresponding year number for the games, results[2] contains the corresponding week number for these games

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI(results)

    def initUI(self, results):
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Grid layout
        self.grid = QGridLayout()              # The Grid that contains the Grids of game results
        self.mainLayout = QVBoxLayout()        # Main layout which contains all other layouts
        self.topLayout = QHBoxLayout()         # Top layout which contains widgets for selecting the year and week

        # Create week combobox and add weeks 1-17 as options
        self.weekSelector = QComboBox()
        for week_num in range(1, 18):
            self.weekSelector.addItem(str(week_num))
        self.weekSelector.setCurrentText(str(results[2]))       # Update the value of the combobox because initUI is called when a week is selected and will always set week to 1 if this line is missing

        # Create year combobox and add years 1970-2020 as options
        self.yearSelector = QComboBox()
        for year_num in range(1970, 2021):
            self.yearSelector.addItem(str(year_num))
        self.yearSelector.setCurrentText(str(results[1]))       # Update the value of the combobox because initUI is called when a year is selected and will always set year to 2020 if this line is missing


        row = 0
        game_no = 0
        # Loop through every game in our results list (Each week/season may have a different number of games due to bye weeks and number of teams in the league)
        while game_no < (len(results[0]) - 1):

            # LEFT SCOREBUG STUFF
            self.LSBgroupbox = QGroupBox()
            self.LSBgroupbox.setStyleSheet("QGroupBox { border: 6px solid gray;}")

            self.LSBGrid = QGridLayout()
            self.LSBGrid.addWidget(self.LSBgroupbox, 0, 0, 3, 3)
            self.LSBGrid.setSpacing(0)

            # Check that the game did not end in a tie
            if results[0][game_no].get_result_type() == 'win/loss':
                self.LSBdateLabel = QLabel(results[0][game_no].get_date())
                self.LSBteam1Label = QLabel(results[0][game_no].get_losing_team())
                self.LSBteam2Label = QLabel(results[0][game_no].get_winning_team())
                self.LSBteam1ScoreLabel = QLabel(results[0][game_no].get_losing_score())
                self.LSBteam2ScoreLabel = QLabel(results[0][game_no].get_winning_score())
                self.LSBteam2Label.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px; font-weight: bold')    # Styling here to help distinguish tie games from win/loss games
                self.LSBteam2ScoreLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 5px; padding-bottom: 0px; font-weight: bold')   # Styling here to help distinguish tie games from win/loss games

            # Game ended in a tie
            else:
                self.LSBdateLabel = QLabel(results[0][game_no].get_date())
                self.LSBteam1Label = QLabel(results[0][game_no].get_away_team())
                self.LSBteam2Label = QLabel(results[0][game_no].get_home_team())
                self.LSBteam1ScoreLabel = QLabel(results[0][game_no].get_score())
                self.LSBteam2ScoreLabel = QLabel(results[0][game_no].get_score())
                self.LSBteam2Label.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')   # Styling here to help distinguish tie games from win/loss games
                self.LSBteam2ScoreLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 5px; padding-bottom: 0px')  # Styling here to help distinguish tie games from win/loss games
                

            self.LSBdateLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            self.LSBdateLabel.setFont(QFont('Arial', 14)) 
                
            self.LSBteam1Label.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
            self.LSBteam1Label.setFont(QFont('Arial', 14)) 
            
            self.LSBteam2Label.setFont(QFont('Arial', 14)) 
            
            self.LSBteam1ScoreLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 5px; padding-bottom: 0px')
            self.LSBteam1ScoreLabel.setFont(QFont('Arial', 14))
            self.LSBteam1ScoreLabel.setAlignment(Qt.AlignRight) 
            
            self.LSBteam2ScoreLabel.setFont(QFont('Arial', 14))
            self.LSBteam2ScoreLabel.setAlignment(Qt.AlignRight) 

            self.LSBGrid.addWidget(self.LSBdateLabel, 0, 0, 1, 3)
            self.LSBGrid.addWidget(self.LSBteam1Label, 1, 0, 1, 2)
            self.LSBGrid.addWidget(self.LSBteam1ScoreLabel, 1, 2, 1, 1)
            self.LSBGrid.addWidget(self.LSBteam2Label, 2, 0, 1, 2)
            self.LSBGrid.addWidget(self.LSBteam2ScoreLabel, 2, 2, 1, 1)

            # ADD LEFT SCOREBUG TO MAIN GRID LAYOUT
            self.grid.addLayout(self.LSBGrid, row, 0)

            # Increase game number to get correct game number
            game_no += 1

            # Add game to right if there are games left
            if game_no <= len(results[0]):
            # RIGHT SCOREBUG STUFF
                self.RSBgroupbox = QGroupBox()
                self.RSBgroupbox.setStyleSheet("QGroupBox { border: 6px solid gray;}")

                self.RSBGrid = QGridLayout()
                self.RSBGrid.addWidget(self.RSBgroupbox, 0, 0, 3, 3)
                self.RSBGrid.setSpacing(0)

                # Check that the game did not end in a tie
                if results[0][game_no].get_result_type() == 'win/loss':
                    self.RSBdateLabel = QLabel(results[0][game_no].get_date())
                    self.RSBteam1Label = QLabel(results[0][game_no].get_losing_team())
                    self.RSBteam2Label = QLabel(results[0][game_no].get_winning_team())
                    self.RSBteam1ScoreLabel = QLabel(results[0][game_no].get_losing_score())
                    self.RSBteam2ScoreLabel = QLabel(results[0][game_no].get_winning_score())
                    self.RSBteam2Label.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px; font-weight: bold')    # Styling here to help distinguish tie games from win/loss games
                    self.RSBteam2ScoreLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 5px; padding-bottom: 0px; font-weight: bold')   # Styling here to help distinguish tie games from win/loss games

                # Game ended in a tie
                else:
                    self.RSBdateLabel = QLabel(results[0][game_no].get_date())
                    self.RSBteam1Label = QLabel(results[0][game_no].get_away_team())
                    self.RSBteam2Label = QLabel(results[0][game_no].get_home_team())
                    self.RSBteam1ScoreLabel = QLabel(results[0][game_no].get_score())
                    self.RSBteam2ScoreLabel = QLabel(results[0][game_no].get_score())
                    self.RSBteam2Label.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')   # Styling here to help distinguish tie games from win/loss games
                    self.RSBteam2ScoreLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 5px; padding-bottom: 0px')  # Styling here to help distinguish tie games from win/loss games
                
                self.RSBdateLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
                self.RSBdateLabel.setFont(QFont('Arial', 14)) 
                
                self.RSBteam1Label.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 0px; padding-bottom: 0px')
                self.RSBteam1Label.setFont(QFont('Arial', 14)) 
                
                self.RSBteam2Label.setFont(QFont('Arial', 14))

                self.RSBteam1ScoreLabel.setStyleSheet('padding-top : 0px; padding-left: 5px; padding-right: 5px; padding-bottom: 0px')
                self.RSBteam1ScoreLabel.setFont(QFont('Arial', 14))
                self.RSBteam1ScoreLabel.setAlignment(Qt.AlignRight)

                self.RSBteam2ScoreLabel.setFont(QFont('Arial', 14))
                self.RSBteam2ScoreLabel.setAlignment(Qt.AlignRight) 

                self.RSBGrid.addWidget(self.RSBdateLabel, 0, 0, 1, 3)
                self.RSBGrid.addWidget(self.RSBteam1Label, 1, 0, 1, 2)
                self.RSBGrid.addWidget(self.RSBteam1ScoreLabel, 1, 2, 1, 1)
                self.RSBGrid.addWidget(self.RSBteam2Label, 2, 0, 1, 2)
                self.RSBGrid.addWidget(self.RSBteam2ScoreLabel, 2, 2, 1, 1)

                # ADD RIGHT SCOREBUG TO GRID
                self.grid.addLayout(self.RSBGrid, row, 1)

            row += 1
            game_no += 1


        self.yearSelector.currentTextChanged.connect(self.updateYearAndWeek) # Check to see if the user selected a different year, if so we update the game results shown
        self.weekSelector.currentTextChanged.connect(self.updateYearAndWeek) # Check to see if the user selected a different week, if so we update the game results shown

        # TOP LAYOUT WIDGETS
        self.yearLabel = QLabel('Year')
        self.yearLabel.setFixedWidth(50)
        self.yearLabel.setFont(QFont('Arial', 14))

        self.weekLabel = QLabel('Week')
        self.weekLabel.setFixedWidth(50)
        self.weekLabel.setFont(QFont('Arial', 14))

        self.topLayout.addWidget(self.yearLabel)
        self.topLayout.addWidget(self.yearSelector)
        self.topLayout.addWidget(self.weekLabel)
        self.topLayout.addWidget(self.weekSelector)

        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.grid)
        self.widget.setLayout(self.mainLayout)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(50, 50, 1600, 900)
        self.setWindowTitle('NFL Game Results %s Season' % str(results[1])) # Changes the title of the window depending on which year is selected
        self.show()

        return

    # Called when the user selects a new week/year
    # Grab results for the week and year and call our initializer method to recreate our window with the new game results
    def updateYearAndWeek(self):
        week = self.weekSelector.currentText()
        self.weekSelector.setCurrentText(week)
        year = self.yearSelector.currentText()
        self.yearSelector.setCurrentText(year)
        results = game_results_class.GameResultsForWeek(year, week)
        self.initUI(results)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())