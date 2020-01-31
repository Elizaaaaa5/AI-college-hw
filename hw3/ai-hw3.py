import numpy as np
# import json

TEAM_NAME = "a why"
MEMBERS = ["md9bt", "lc3am", "jhr3kd"]
rt = []
num_rounds = 0

"""
state is passed in as a dictionary, examples below: 


state = {
"reaction-time": "1.857",
"team-code": "eef8976e",
"game": "chicken",
"opponent-name": "mighty_ducks"
}

state = {
"game": "connect_more",
"opponent-name": "mighty_ducks",
"columns": 6,
"connect_n": 5,
"your-token": "R",
"board": [
["R","Y"],
["R"],
[],
["R",],
["Y","Y"],
[],
]
}
"""

def new_distribution(hp_loc=1.5, hp_scale=0.25):
    dist_mu = np.random.normal(loc=hp_loc, scale=hp_scale)
    dist_var = np.random.normal(loc=hp_loc, scale=hp_scale)
    dist_mu = max(0, dist_mu)
    dist_var = max(0, dist_var)
    return (dist_mu, dist_var)

rt_loc, rt_scale = new_distribution()

def get_move(state):
    global rt
    global num_rounds
    # code for the chicken game
    if state["game"] == "chicken":
        if float(state["reaction-time"]) == 0:
            rt.clear()
            num_rounds = 0
            return 6
        else:
            rt.append(float(state["reaction-time"]))
            num_rounds += 1
            avg = np.average(rt)
            sd = np.std(rt)
            if num_rounds < 4:
                when_to_swerve = avg + 4
            else:
                when_to_swerve = avg + (2 * sd)
            if when_to_swerve > 10:
                return 10
            return when_to_swerve

    # code for the connect more game
    else:
        return 1

state = {
    "reaction-time": "0",
    "team-code": "eef8976e",
    "game": "chicken",
    "opponent-name": "mighty_ducks",
    "previous-move": "0",
    "outcome": "0"
    }

print(get_move(state))
print(rt)

for i in range(0,9):
    num = np.random.normal(loc=rt_loc, scale=rt_scale)
    num = max(0,num)
    num = min(10,num)
    state["reaction-time"] = num

    print(get_move(state))
    print(rt)