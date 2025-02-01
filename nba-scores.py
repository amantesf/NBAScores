from requests import get
from pprint import PrettyPrinter
from datetime import datetime

BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"

printer = PrettyPrinter()

today_date = datetime.today().strftime("%Y%m%d")

response = get(f"{BASE_URL}?dates={today_date}").json()

games = response.get("events", [])

if not games:
    print("No NBA games today.")
else:
    print(f"NBA Games for {datetime.today().strftime('%B %d, %Y')}\n")
    
    for game in games:
        competitors = game["competitions"][0]["competitors"]
        team_1 = competitors[0]["team"]["displayName"]
        team_1_score = competitors[0].get("score", "0")
        
        team_2 = competitors[1]["team"]["displayName"]
        team_2_score = competitors[1].get("score", "0")

        status = game["status"]["type"]["description"]  # e.g., "Final" or "In Progress"

        print(f"{team_1} ({team_1_score}) vs {team_2} ({team_2_score}) - {status}")

