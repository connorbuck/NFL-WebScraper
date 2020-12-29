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
		print(f'{self.get_date()}\n{self.get_winning_team()}  {self.get_winning_score()}\n{self.get_losing_team()}  {self.get_losing_score()}\n')

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
		print(f'{self.get_date()}\n{self.get_away_team()}  {self.get_score()}\n{self.get_home_team()}  {self.get_score()}\n')

# Param: Int for week of season
# Returns the page for the requested week of season
def GetPage(weekNum):
    return requests.get("https://www.pro-football-reference.com/years/2020/week_%s.htm" % weekNum)

# Grabs and returns the result of each NFL game for a given week
# Private method, meant to only be used inside of GameResultsForWeek() method below
def __GrabGameResults(soup):
	games_list = []

	for game in soup.find_all('table', class_ = 'teams'):
		game_date = game.find('tr', class_ = 'date').text # Grabs date

		# Game did not end in a tie
		if game.find('tr', class_ = 'loser') is not None:

			game_loser = game.find('tr', class_ = 'loser') # Grabs unformatted losing team info
			game_winner = game.find('tr', class_ = 'winner') # Grabs unformatted winning team info

			# Use this to grab team info we want
			game_loser_tname = game_loser.text.split('\n')[1]
			game_loser_score = game_loser.text.split('\n')[2]

			game_winner_tname = game_winner.text.split('\n')[1]
			game_winner_score = game_winner.text.split('\n')[2]

			# Add the specific game object to a list with all other games
			games_list.append(GameResult(game_winner_tname, game_loser_tname, game_date, game_winner_score, game_loser_score))

		# Game ended in a tie (no winner or loser)
		else:
			teams = game.find_all('tr', class_ = 'draw') # Grabs unformatted team info

			# Use this to grab team info we want
			away_tname = teams[0].text.split('\n')[1]
			home_tname = teams[1].text.split('\n')[1]
			tie_score = teams[0].text.split('\n')[2]

			# Add the specific game object to a list with all other games
			games_list.append(TieGameResult(away_tname, home_tname, game_date, tie_score))
	return games_list

# Return all game results for a given week
def GameResultsForWeek(week):
	page = GetPage(week) # Grab page for given week
	soup = BeautifulSoup(page.content, 'html.parser')
	return __GrabGameResults(soup) # Call helper method and return games list

# Main Method
if __name__ == '__main__':
	week_one_games = GameResultsForWeek(3)
	for game in week_one_games:
		game.display_game_result()