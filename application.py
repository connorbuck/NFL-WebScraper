import game_results_class
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
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
        x = 0
        while x < len(results):
        	f = QGridLayout()
        	f.addWidget(QPushButton("Game %s" % x), 0, 0)
        	outer_layout.addLayout(f, x, 0)
        	x += 1

        	g = QGridLayout()
        	g.addWidget(QPushButton("Game %s" % x), 0, 0)
        	outer_layout.addLayout(g, x - 1, 1)
        	x += 1

        # Set the layout on the application's window
        self.setLayout(outer_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())