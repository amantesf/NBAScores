from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20250131"

response = get(BASE_URL).json()
print(response)