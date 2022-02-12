# WEEK 4
# PROJECT: KICKBALL TEAMS

import random

# AVAILABLE PLAYERS

available_players = ['Anastasia', 'Eli', 'Jamal', 'Jada', 'Theo', 'Michelle', 'Adam', 'Rhea', 'Charlie', 'Jasmine', 'Marley', 'Kenji', 'Sydney', 'Cooper']

# LIST OF TEAM CAPTAINS

jaleesas_team = ['Jaleesa']
rahims_team = ['Rahim']

while len(jaleesas_team) < 8:
    player_selected = random.choice(available_players)
    jaleesas_team.append(player_selected)
    available_players.remove(player_selected)

# FOR-LOOP THAT ADDS THE REMAINING PLYAER TO RAHIM'S TEAM

rahims_team.extend(available_players)

# PRINTS THE PLAYERS ON EACH TEAM

print("\nJaleesa's Team")
print(*jaleesas_team, sep = ", ")

print("\nRahim's Team")
print(*rahims_team, sep = ", ")
