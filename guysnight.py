"""Who is playing whom in Brad's pick16 thing"""

from datetime import datetime, date
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

score_by_player = {player: 0 for player, _ in teams_by_player.items()}
seed_by_team = {}

tournament_dates = [
    date(2024, 3, 19),
    date(2024, 3, 20),
    date(2024, 3, 21),
    date(2024, 3, 22),
    date(2024, 3, 23),
    date(2024, 3, 24),
    date(2024, 3, 28),
    date(2024, 3, 29),
    date(2024, 3, 30),
    date(2024, 3, 31),
    date(2024, 4, 6),
    date(2024, 4, 8),
]

next_tournament_date = (
    today
    if today in tournament_dates
    else next((date for date in tournament_dates if date > today), None)
)

for date in tournament_dates:
    if next_tournament_date and date > next_tournament_date:
        break
    response = requests.get(
        f"{BASE_URL}/{date.year}/{date.month:02}/{date.day:02}/scoreboard.json",
        timeout=5,
    )
    results = response.json()

    if "games" not in results:
        continue

    if date == next_tournament_date and today != date:
        print(f"Upcoming games on {next_tournament_date}:")

    for game in [
        game["game"] for game in results["games"] if game["game"]["bracketId"]
    ]:
        state = game["gameState"]
        home = game["home"]["names"]["short"]
        away = game["away"]["names"]["short"]
        if date == next_tournament_date:
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

if next_tournament_date:
    print()
for player, score in score_by_player.items():
    print(f"{player}: {score}")

# To see teams remaining per player:
# for player, teams in teams_by_player.items():
#     print()
#     print(f"{player}:")
#     for team in teams:
#         print(f"{team} ({seed_by_team[team]})")
