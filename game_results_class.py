import requests
from bs4 import BeautifulSoup

# Only for games that do not end in a tie
class GameResult():

	def __init__(self, winning_team, losing_team, date, winning_score, losing_score):
		self.winning_team = winning_team
		self.losing_team = losing_team
		self.date = date
		self.winning_score = winning_score
		self.losing_score = losing_score

	# Return the winning team of a game
	def get_winning_team(self):
		return self.winning_team

	# Return the losing team of a game
	def get_losing_team(self):
		return self.losing_team

	# Return the date of a game
	def get_date(self):
		return self.date

	# Return the winning score of a game
	def get_winning_score(self):
		return self.winning_score

	# Return the losing score of a game
	def get_losing_score(self):
		return self.losing_score

	# Display the game result
	def display_game_result(self):
		print(f'{self.get_date()}\n{self.get_winning_team()}  {self.get_winning_score()}\n{self.get_losing_team()}  {self.get_losing_score()}')

# For games which end in a tie
# Ability to show home and away team comes from structure of website HTML code
# TODO: Can I use abstraction here to simplify this class?
class TieGameResult():

	def __init__(self, away_team, home_team, date, tie_score):
		self.away_team = away_team
		self.home_team = home_team
		self.date = date
		self.tie_score = tie_score

	# Return the away team of the tie game
	def get_away_team(self):
		return self.away_team

	# Return the home team of the tie game
	def get_home_team(self):
		return self.home_team

	# Return the date of the game
	def get_date(self):
		return self.date

	# Return the tie score of the game
	def get_score(self):
		return self.tie_score

	# Display the tie game result
	def display_game_result(self):
		print(f'{self.get_date()}\n{self.get_away_team()}  {self.get_score()}\n{self.get_home_team()}  {self.get_score()}')
