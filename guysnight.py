"""Who is playing whom in Brad's pick16 thing"""

from datetime import datetime, date, timedelta
import requests
from pytz import timezone

teams_by_player = {
    "Brad": [
        "UConn",
        "Houston",
        "Purdue",
        "Auburn",
        "Duke",
        "Gonzaga",
        "Wisconsin",
        "BYU",
        "Michigan St.",
        "Colorado",
        "Virginia",
        "New Mexico",
        "Oregon",
        "James Madison",
        "McNeese",
        "Samford",
    ],
    "John": [
        "Colorado",
        "Colorado St.",
        "Drake",
        "Nevada",
        "Duquesne",
        "NC State",
        "New Mexico",
        "Oregon",
        "Grand Canyon",
        "James Madison",
        "McNeese",
        "UAB",
        "Col. of Charleston",
        "Samford",
        "Vermont",
        "Yale",
    ],
    "Jon": [
        "UConn",
        "Houston",
        "Purdue",
        "Marquette",
        "Tennessee",
        "Iowa St.",
        "Baylor",
        "Creighton",
        "Illinois",
        "Alabama",
        "Kansas",
        "Texas A&M",
        "Drake",
        "New Mexico",
        "Grand Canyon",
        "McNeese",
    ],
    "Micah": [
        "Arizona",
        "Tennessee",
        "Iowa St.",
        "Kansas",
        "Saint Mary's (CA)",
        "San Diego St.",
        "BYU",
        "Texas",
        "Michigan St.",
        "Colorado",
        "Drake",
        "New Mexico",
        "Grand Canyon",
        "James Madison",
        "Vermont",
        "Colgate",
    ],
    "Aaron": [
        "UConn",
        "Houston",
        "Marquette",
        "Iowa St.",
        "Baylor",
        "Illinois",
        "Auburn",
        "Wisconsin",
        "Texas",
        "Mississippi St.",
        "Michigan St.",
        "Colorado",
        "Colorado St.",
        "Drake",
        "McNeese",
        "Samford",
    ],
}

BASE_URL = "https://data.ncaa.com/casablanca/scoreboard/basketball-men/d1/"
now = datetime.now(timezone("US/Eastern"))
today = date(now.year, now.month, now.day)
CURRENT_YEAR = today.year
START_DATE = date(CURRENT_YEAR, 3, 19)
FINAL_DATE = min(date(CURRENT_YEAR, 4, 8), today)

score_by_player = {player: 0 for player, _ in teams_by_player.items()}
seed_by_team = {}

for date in [
    START_DATE + timedelta(days=n)
    for n in range(int(1 + (FINAL_DATE - START_DATE).days))
]:
    response = requests.get(
        f"{BASE_URL}/{CURRENT_YEAR}/{date.month:02}/{date.day:02}/scoreboard.json",
        timeout=5,
    )
    results = response.json()

    if "games" not in results:
        continue

    for game in [
        game["game"] for game in results["games"] if game["game"]["bracketId"]
    ]:
        state = game["gameState"]
        home = game["home"]["names"]["short"]
        away = game["away"]["names"]["short"]
        if today.month == date.month and today.day == date.day:
            home_holders = [
                player for player, teams in teams_by_player.items() if home in teams
            ]
            away_holders = [
                player for player, teams in teams_by_player.items() if away in teams
            ]
            if home_holders or away_holders:
                print(
                    f"{game['startTime']} - {home} ({game['home']['seed']}) vs {away} ({game['away']['seed']}) - {game['network']}"
                )
                if state == "live":
                    if not game["currentPeriod"]:
                        print(
                            f"    LIVE: {game['home']['score']}-{game['away']['score']} (HALFTIME)"
                        )
                    else:
                        print(
                            f"    LIVE: {game['home']['score']}-{game['away']['score']} {game['contestClock']} ({game['currentPeriod']})"
                        )
                elif state == "final":
                    print(f"    FINAL: {game['home']['score']}-{game['away']['score']}")
                print(f"    {home}: {', '.join(map(str, home_holders))}")
                print(f"    {away}: {', '.join(map(str, away_holders))}")
        if state == "final":
            if game["home"]["winner"]:
                winner = home
                loser = away
                worth = int(game["home"]["seed"])
                seed_by_team[home] = worth
            else:
                winner = away
                loser = home
                worth = int(game["away"]["seed"])
                seed_by_team[away] = worth
            if game["bracketRound"] == ("First Four&#174;"):
                worth //= 2
            elif game["bracketRound"] == ("Elite Eight&#174;"):
                worth += 1
            elif game["bracketRound"] == ("Final Four&#174;"):
                worth += 3
            elif game["bracketRound"] == ("Championship"):
                worth += 5
            for player, teams in teams_by_player.items():
                for team in teams:
                    if winner == team:
                        score_by_player[player] += worth
                try:
                    teams.remove(loser)
                except ValueError:
                    pass

print()
for player, score in score_by_player.items():
    print(f"{player}: {score}")

# To see teams remaining per player:
# for player, teams in teams_by_player.items():
#     print()
#     print(f"{player}:")
#     for team in teams:
#         print(f"{team} ({seed_by_team[team]})")
