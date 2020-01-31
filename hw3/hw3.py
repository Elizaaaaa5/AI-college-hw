import numpy as np

TEAM_NAME = "a why"
MEMBERS = ["md9bt", "lc3am", "jhr3kd"]
rt = []
num_rounds = 0
outcomes = []
max_len_vert = 0


def getcol(state):
    global max_len_vert
    max_len_vert = 0
    rtn_col = -1
    for column in range(len(state["board"])):
        len_vert = 0
        for token in range(len(state["board"][column])):
            if state["board"][column][token] != state["your-token"]:
                len_vert = 0
            else:
                len_vert += 1
        if len_vert > max_len_vert:
            max_len_vert = len_vert
            rtn_col = column
        # if multiple columns have the longest vertical distance, pick one at random to build on
        # ha ha suckers just try to block us
        if len_vert == max_len_vert:
            coin_toss = np.random.random_integers(0,1)
            if coin_toss == 1:
                max_len_vert = len_vert
                rtn_col = column
    if rtn_col == -1:        # if there is no vertical to build off of
        rtn_col = np.random.random_integers(0, state["columns"])
    return rtn_col


def getoppcol(state):
    rtn_col = -1
    # try adding opponent's token to each column on the board
    # see if they have connect-n, if they do, put your token where they would need to
    if state["your-token"] == "R":
        oppToken = "Y"
    else:
        oppToken = "R"
    for column in range(len(state["board"])):
        # add opponent token
        state["board"][column].append(oppToken)
        # check for vertical connect-n
        len_vert = 0
        for token in range(len(state["board"][column])):
            if state["board"][column][token] == state["your-token"]:
                len_vert = 0
            else:
                len_vert += 1
        if len_vert >= state["connect_n"]:
            rtn_col = column
        # remove opponent token, last in the list, before considering next scenario
        state["board"][column].pop(-1)

    for column in range(len(state["board"])):
        # add opponent token
        state["board"][column].append(oppToken)
        # check for horizontal connect-n
        len_hor = 0
        for row in range(len(max(state["board"], key=len))):
            for c in range(len(state["board"])):
                try:
                    if state["board"][c][row] == state["your-token"]:
                        len_hor = 0
                    else:
                        len_hor += 1
                except:
                    len_hor = 0
                if len_hor >= state["connect_n"]:
                    rtn_col = column
        # remove opponent token, last in the list, before considering next scenario
        state["board"][column].pop(-1)
    return rtn_col


def get_move(state):
    global rt
    global num_rounds
    global outcomes
    # code for the chicken game
    if state["game"] == "chicken":
        if float(state["reaction-time"]) == 0:                      # indicates new distribution; clear global vars
            rt.clear()
            outcomes.clear()
            num_rounds = 0
            when_to_swerve = 6
        else:                                                       # otherwise, learn about distribution to inform rt
            rt.append(float(state["reaction-time"]))
            outcomes.append(float(state["outcome"]))
            num_rounds += 1
            avg = np.average(rt)
            sd = np.std(rt)
            if num_rounds < 4:
                when_to_swerve = avg + 4
            else:
                multiplier = 2
                if outcomes[-1] == -1 and outcomes[-2] == -1 and outcomes[-3] == -1:
                    multiplier = 1
                if outcomes[-1] == -10:
                    multiplier = 2.5
                when_to_swerve = avg + (multiplier * sd)
            if when_to_swerve > 10:                                 # never return more than 10
                when_to_swerve = 10
        return when_to_swerve

    # code for the connect more game
    else:
        col_defense = getoppcol(state)      # priority: blocks horizontal and vertical connect-ns by the other team
        if col_defense != -1:
            return col_defense

        # some situations for early game play if not in immediate danger of losing
        if np.size(state["board"]) == 0:    # tries center column if board is empty
            return state["columns"] // 2
        if np.size(state["board"]) == 1:
            for column in range(len(state["board"])):
                if len(state["board"][column]) > 0:
                    if (column-1) < 0:
                        return column+1
                    if (column+1) >= len(state["board"]):
                        return column-1     # puts something to left or right of first move
        a = state["board"]
        count = 0
        for list in a:
            for elem in list:
                count += 1
        if count <= 8:                      # in early moves, places in variety of columns
            return np.random.random_integers(0, state["columns"]-1)

        col_offense = getcol(state)
        return col_offense                  # finds column with highest vertical, and builds up on that


state = {
    "game": "connect_more",
    "opponent-name": "mighty_ducks",
    "columns": 6,
    "connect_n": 5,
    "your-token": "R",
    "board": [
    ["Y", "Y"],
    ["Y"],
    ["Y"],
    ["R", "Y"],
    ["R","Y"],
    ["Y"],
    ]
}

print(get_move(state))