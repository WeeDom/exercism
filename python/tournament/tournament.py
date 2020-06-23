from collections import namedtuple, defaultdict


def tally(rows):
    team_results = namedtuple('Team', 'name MP W D L P', defaults=(None,))
    table = defaultdict(dict)
    for res in rows:
        home, away, result = res.split(';')
        homewin, awaywin, draw, homeloss, awayloss = 0, 0, 0, 0, 0
        if result == 'win':
            homewin, awaywin, draw, homeloss, awayloss = 3, 0, 0, 0, 1
        elif result == 'loss':
            homewin, awaywin, draw, homeloss, awayloss = 0, 3, 0, 1, 0
        else:  # draw
            homewin, awaywin, draw, homeloss, awayloss = 0, 0, 1, 0, 0

        if table[home]:
            table[home] = table[home]._replace(
                MP=table[home].MP + 1,
                W=table[home].W + (1 if homewin else 0),
                D=table[home].D + draw,
                L=table[home].L + homeloss,
                P=table[home].P + (homewin if homewin else draw if draw else 0)
            )
        else:
            table[home] = team_results(
                name=home,
                MP=1,
                W=1 if homewin else 0,
                D=1 if draw else 0,
                L=1 if homeloss else 0,
                P=homewin if homewin else draw if draw else 0
            )

        if table[away]:
            table[away] = table[away]._replace(
                MP=table[away].MP + 1,
                W=table[away].W + (1 if awaywin else 0),
                D=table[away].D + draw,
                L=table[away].L + awayloss,
                P=table[away].P + (awaywin if awaywin else draw if draw else 0)
            )
        else:
            table[away] = team_results(
                name=away,
                MP=1,
                W=1 if awaywin else 0,
                D=1 if draw else 0,
                L=1 if awayloss else 0,
                P=awaywin if awaywin else draw if draw else 0
            )
    header = ["Team                           | MP |  W |  D |  L |  P"]
    res = []
    for team in sorted(
                        sorted(
                                table.values(),
                                reverse=True,
                                key=lambda x: x.name),
                        key=lambda x: x.P
                    ):
        res.append(
            f'{team.name.ljust(31)}| {str(team.MP).rjust(2)} | ' +
            f'{str(team.W).rjust(2)} | {str(team.D).rjust(2)} | ' +
            f'{str(team.L).rjust(2)} |  {str(team.P)}')
    return header + res[::-1]
