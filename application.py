import game_results_class
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
    QFrame,
)

results = game_results_class.GameResultsForWeek(1)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Example")
        # Create a QGridLayout instance
        outer_layout = QGridLayout()

        # Create a grid for each game result
        # Probably a better way to do this, but not sure how
        game_counter = 0
        while game_counter < len(results):
        	# left_game_frame = QFrame()
        	# left_game_frame.setStyleSheet('border:1px solid rgb(0, 255, 0)')
        	left_game = QGridLayout()
        	left_game.setContentsMargins(20, 20, 20, 20)
        	left_game.addWidget(QPushButton('Date'), 0, 0)
        	left_game.addWidget(QPushButton('Winning Team'), 1, 0)
        	left_game.addWidget(QPushButton('Winning Score'), 1, 1)
        	left_game.addWidget(QPushButton('Losing Team'), 2, 0)
        	left_game.addWidget(QPushButton('Losing Score'), 2, 1)
        	outer_layout.addLayout(left_game, game_counter, 0)
        	game_counter += 1

        	right_game = QGridLayout()
        	right_game.addWidget(QPushButton('Date'), 0, 0)
        	right_game.addWidget(QPushButton('Winning Team'), 1, 0)
        	right_game.addWidget(QPushButton('Winning Score'), 1, 1)
        	right_game.addWidget(QPushButton('Losing Team'), 2, 0)
        	right_game.addWidget(QPushButton('Losing Score'), 2, 1)
        	outer_layout.addLayout(right_game, game_counter - 1, 1)
        	game_counter += 1

        # Set the layout on the application's window
        self.setLayout(outer_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())