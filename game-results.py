import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.pro-football-reference.com/years/2020/week_1.htm")
soup = BeautifulSoup(page.content, 'html.parser')



game_dates_list = []
game_winners_list = []
game_losers_list = []
GameCounter = 1
WeekOneGames = {}

# Each game contains the following info:
    # Winning and Losing team names
    # Date of the game
    # Each team's score
# For each game result, find the date, winner, and loser and append to their respective lists
for game in soup.find_all('table', class_ = 'teams'):
    game_date = game.find('tr', class_ = 'date') # Grabs unformatted date
    game_loser = game.find('tr', class_ = 'loser') # Grabs unformatted losing team info
    game_winner = game.find('tr', class_ = 'winner') # Grabs unformatted winning team info

    # Use this to grab team info we want
    game_loser_tname = game_loser.text.split('\n')[1]
    game_loser_score = game_loser.text.split('\n')[2]

    game_winner_tname = game_winner.text.split('\n')[1]
    game_winner_score = game_winner.text.split('\n')[2]

    # Group the game's info into a dictionary
    GameInfo = {'Winner' : game_winner_tname, 'Winning Score' : game_winner_score, 
                'Loser' : game_loser_tname, 'Losing Score' : game_loser_score,
                'Date' : game_date.text}

    # Add the specific game to a dictionary with all other games
    WeekOneGames['Game %s' % GameCounter] = GameInfo

    # Increase GameCounter to separate games in our dictionary
    GameCounter += 1

print(WeekOneGames['Game 6'])
        