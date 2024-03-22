"""Who is playing whom in Brad's pick16 thing"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

PlayerName = str
TeamName = str
Seed = int
Channel = str

teams_by_player = {
    "Brad": [
        "UNC",
        "Houston",
        "Purdue",
        "Auburn",
        "Duke",
        "Gonzaga",
        "Wisconsin",
        "BYU",
        "Michigan State",
        "Colorado",
        "Virginia",
        "New Mexico",
        "Oregon",
        "James Madison",
        "McNeese State",
        "Samford",
    ],
    "John": [
        "Colorado",
        "Colorado State",
        "Drake",
        "Nevada",
        "Duquesne",
        "NC State",
        "New Mexico",
        "Oregon",
        "Grand Canyon",
        "James Madison",
        "McNeese State",
        "UAB",
        "Charleston",
        "Samford",
        "Vermont",
        "Yale",
    ],
    "Jon": [
        "UNC",
        "Houston",
        "Purdue",
        "Marquette",
        "Tennessee",
        "Iowa State",
        "Baylor",
        "Creighton",
        "Illinois",
        "Alabama",
        "Kansas",
        "Texas A&M",
        "Drake",
        "New Mexico",
        "Grand Canyon",
        "McNeese State",
    ],
    "Micah": [
        "Arizona",
        "Tennessee",
        "Iowa State",
        "Kansas",
        "Saint Mary's",
        "San Diego State",
        "BYU",
        "Texas",
        "Michigan State",
        "Colorado",
        "Drake",
        "New Mexico",
        "Grand Canyon",
        "James Madison",
        "Vermont",
        "Colgate",
    ],
    "Aaron": [
        "UNC",
        "Houston",
        "Marquette",
        "Iowa State",
        "Baylor",
        "Illinois",
        "Auburn",
        "Wisconsin",
        "Texas",
        "Mississippi State",
        "Michigan State",
        "Colorado",
        "Colorado State",
        "Drake",
        "McNeese State",
        "Samford",
    ],
}

seed_by_teamname: dict[Seed, TeamName] = {
    "UNC": 1,
    "Houston": 1,
    "Purdue": 1,
    "Arizona": 2,
    "Marquette": 2,
    "Tennessee": 2,
    "Iowa State": 2,
    "Baylor": 3,
    "Creighton": 3,
    "Illinois": 3,
    "Auburn": 4,
    "Duke": 4,
    "Alabama": 4,
    "Kansas": 4,
    "Gonzaga": 5,
    "Wisconsin": 5,
    "Saint Mary's": 5,
    "San Diego State": 5,
    "BYU": 6,
    "Clemson": 6,
    "Dayton": 7,
    "Texas": 7,
    "Florida": 7,
    "WA State": 7,
    "Mississippi State": 8,
    "FL Atlantic": 8,
    "Nebraska": 8,
    "Utah State": 8,
    "Michigan State": 9,
    "Texas A&M": 9,
    "Northwestern": 9,
    "TCU": 9,
    "Colorado": 10,
    "Colorado State": 10,
    "Drake": 10,
    "Nevada": 10,
    "Virginia": 10,
    "Duquesne": 11,
    "NC State": 11,
    "New Mexico": 11,
    "Oregon": 11,
    "Grand Canyon": 12,
    "James Madison": 12,
    "McNeese State": 12,
    "UAB": 12,
    "Charleston": 13,
    "Samford": 13,
    "Vermont": 13,
    "Yale": 13,
    "Colgate": 14,
    "Oakland": 14,
    "Western KY": 15,
    "Stetson": 16,
    "Grambling St": 16,
    "Longwood": 16,
    "Wagner":16,
    "Montana State":16
}


@dataclass
class Game:
    """A Game"""

    time: datetime
    teams: list[TeamName]
    winner: Optional[TeamName] = None
    channel: Optional[Channel] = None


games = [
    Game(time=datetime(2024, 3, 19), teams=["Wagner", "Howard"], winner="Wagner"),
    Game(
        time=datetime(2024, 3, 19),
        teams=["Colorado State", "Virginia"],
        winner="Colorado State",
    ),
    Game(
        time=datetime(2024, 3, 20),
        teams=["Grambling St", "Montana State"],
        winner="Montana State",
    ),
    Game(
        time=datetime(2024, 3, 20), teams=["Colorado", "Boise State"], winner="Colorado"
    ),
    Game(
        time=datetime(2024, 3, 21),
        teams=["Michigan State", "MS State"],
        winner="Michigan State",
    ),
    Game(time=datetime(2024, 3, 21), teams=["Duquesne", "BYU"], winner="Duquesne"),
    Game(time=datetime(2024, 3, 21), teams=["Arkon", "Creighton"], winner="Creighton"),
    Game(
        time=datetime(2024, 3, 21),
        teams=["Long Beach St", "Arizona"],
        winner="Arizona",
    ),
    Game(time=datetime(2024, 3, 21), teams=["Wagner", "UNC"], winner="UNC"),
    Game(
        time=datetime(2024, 3, 21),
        teams=["Morehead St", "Illinois"],
        winner="Illinois",
    ),
    Game(
        time=datetime(2024, 3, 21),
        teams=["Oregon", "South Carolina"],
        winner="Oregon",
    ),
    Game(time=datetime(2024, 3, 21), teams=["Nevada", "Dayton"], winner="Dayton"),
    Game(time=datetime(2024, 3, 21), teams=["Colorado State", "Texas"], winner="Texas"),
    Game(time=datetime(2024, 3, 21), teams=["Oakland", "Kentucky"], winner="Oakland"),
    Game(
        time=datetime(2024, 3, 21),
        teams=["McNeese State", "Gonzaga"],
        winner="Gonzaga",
    ),
    Game(
        time=datetime(2024, 3, 21),
        teams=["SD State", "Iowa State"],
        winner="Iowa State",
    ),
    Game(
        time=datetime(2024, 3, 21),
        teams=["Saint Peter's", "Tennessee"],
        winner="Tennessee",
    ),
    Game(
        time=datetime(2024, 3, 21),
        teams=["NC State", "Texas Tech"],
        winner="NC State",
    ),
    Game(time=datetime(2024, 3, 21), teams=["Drake", "WA State"], winner="WA State"),
    Game(time=datetime(2024, 3, 21), teams=["Samford", "Kansas"], winner="Kansas"),
    Game(time=datetime(2024, 3, 22, 12, 15), teams=["Northwestern", "FL Atlantic"]),
    Game(time=datetime(2024, 3, 22, 12, 40), teams=["Colgate", "Baylor"]),
    Game(time=datetime(2024, 3, 22, 13, 45), teams=["UAB", "San Diego State"]),
    Game(time=datetime(2024, 3, 22, 14, 00), teams=["Western KY", "Marquette"]),
    Game(time=datetime(2024, 3, 22, 14, 45), teams=["Stetson", "UNC"]),
    Game(time=datetime(2024, 3, 22, 15, 10), teams=["New Mexico", "Clemson"]),
    Game(time=datetime(2024, 3, 22, 16, 15), teams=["Yale", "Auburn"]),
    Game(time=datetime(2024, 3, 22, 16, 30), teams=["Colorado", "Florida"]),
    Game(time=datetime(2024, 3, 22, 18, 50), teams=["Texas A&M", "Nebraska"]),
    Game(time=datetime(2024, 3, 22, 19, 10), teams=["Vermont", "Duke"]),
    Game(time=datetime(2024, 3, 22, 19, 25), teams=["Grambling St", "Purdue"]),
    Game(time=datetime(2024, 3, 22, 19, 35), teams=["Charleston", "Alabama"]),
    Game(time=datetime(2024, 3, 22, 21, 20), teams=["Longwood", "Houston"]),
    Game(time=datetime(2024, 3, 22, 21, 40), teams=["James Madison", "Wisconsin"]),
    Game(time=datetime(2024, 3, 22, 21, 55), teams=["TCU", "Utah State"]),
    Game(time=datetime(2024, 3, 22, 22, 5), teams=["Grand Canyon", "Saint Mary's"]),
]

score_by_player = {player: 0 for player, _ in teams_by_player.items()}

for game in games:
    if game.winner:
        if game.winner not in game.teams:
            raise RuntimeError(f"MICAH FIX YOUR DATABASE {game.winner}")
        if game.winner not in seed_by_teamname:
            raise RuntimeError(f"MICAH FIX YOUR DATABASE {game.winner}")
        for player, teams in teams_by_player.items():
            for team in teams:
                if game.winner is team:
                    worth = seed_by_teamname[team]
                    if game.time.month == 3 and game.time.day < 21:
                        worth /= 2
                    score_by_player[player] += int(worth)
        for team in game.teams:
            if team != game.winner:
                for player,teams in teams_by_player.items():
                    if team in teams:
                        teams.remove(team)
    if game.time.day == 22 and game.winner is None:
        team_0_holders = [
            player
            for player, teams in teams_by_player.items()
            if game.teams[0] in teams
        ]
        team_1_holders = [
            player
            for player, teams in teams_by_player.items()
            if game.teams[1] in teams
        ]
        if team_0_holders or team_1_holders:
            print(
                f"{game.time.strftime('%-I:%M')} - {game.teams[0]} ({seed_by_teamname[game.teams[0]]}) vs {game.teams[1]} ({seed_by_teamname[game.teams[1]]})"
            )
            print(f"    {game.teams[0]}: {', '.join(map(str, team_0_holders))}")
            print(f"    {game.teams[1]}: {', '.join(map(str, team_1_holders))}")

for player,score in score_by_player.items():
    print(f"{player}: {score}")

for player,teams in teams_by_player.items():
    print(f"{player}: {', '.join(map(str, teams))}")