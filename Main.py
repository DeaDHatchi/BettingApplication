class Identifier:
    def __init__(self):
        self.identifier = None


class Slip:
    def __init__(self, identifier: Identifier):
        self.identifier = identifier


class Bet(Slip):
    pass


class Team:
    def __init__(self, name: str, identifier: Identifier):
        self.name = name
        self.pool = 0.00
        self.identifier = identifier


class Match:
    def __init__(self, teama: Team, teamb: Team, identifier: Identifier):
        self.teamA = teama
        self.teamB = teamb
        self.identifier = identifier


class Gambler:
    def __init__(self, name: str, balance: float, identifier: Identifier):
        self.name = name
        self.balance = balance
        self.identifier = identifier




def calcPositiveBetting(odds: float, stake: float) -> float:
    return (stake / odds) * 100


def calcNegativeBetting(odds: float, stake: float) -> float:
    return (stake / 100) * odds


print(calcPositiveBetting(odds=300, stake=5.00))
print(calcNegativeBetting(odds=300, stake=5.00))
