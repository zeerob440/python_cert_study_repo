# demonstrate difference between class an instance vars

class Team:

    team_type: str = 'Hockey Team' # class var


    def __init__(self, team_name):
        self.team_name = team_name

team1 = Team('Florida Panthers')
team2 = Team('Chicago Blackhawks')

print(team1.team_type)
print(team2.team_type)

print (f'The Class Scope Variable for Instance Vars:{team1.team_name, team2.team_name} is: {Team.team_type}\n')

