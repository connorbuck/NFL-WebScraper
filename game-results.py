import requests
from bs4 import BeautifulSoup

# Separate code into methods, create loop to go through each week using %s in following string

# Param: Int for week of season
# Returns the page for the requested week of season
def GetPage(weekNum):
    return requests.get("https://www.pro-football-reference.com/years/2020/week_%s.htm" % weekNum)

# Returns the result of each NFL game for a given week

#TODO: Add check for ties, if scores are equal, winner and loser class do not exist
# instead, check for 'draw' class (Use Week 3 Game 5 as an example)
def GameResults(soup):
    game_dates_list = []
    game_winners_list = []
    game_losers_list = []
    WeekOneGames = {}
    GameCounter = 1

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

    return WeekOneGames

# Display the result of the game
#TODO: Use printf to format output cleanly
#TODO: Make sure the Home team is shown second
def DisplayGameResult(gameResult):
    print(gameResult['Date'])
    print(gameResult['Winner'] + '   ' + gameResult['Winning Score'])
    print(gameResult['Loser'] + '   ' + gameResult['Losing Score'])

# Main Method
if __name__ == '__main__':
    page = GetPage(1)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = GameResults(soup)
    DisplayGameResult(result['Game 1'])
   
