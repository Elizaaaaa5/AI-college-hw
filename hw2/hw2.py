import random, math, json
import numpy as np

class Node:
    def __init__(self, data, level, fval)
def generate():
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    puzzle_state = []
    while len(values) > 0:
        val = random.randrange(0, 9)
        if val not in puzzle_state:
            puzzle_state.append(val)
            values.remove(val)
    fin_puz_state = []
    partOne = puzzle_state[0:3]
    partTwo = puzzle_state[3:6]
    partThree = puzzle_state[6:9]
    fin_puz_state.append(partOne)
    fin_puz_state.append(partTwo)
    fin_puz_state.append(partThree)
    return fin_puz_state


def isGoalState(arr):
    goal_state = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]
    return arr == goal_state


def hScore(curr):
    goal_state = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]
    score = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if curr[i][j] != goal_state[i][j] and goal_state[i][j] != 0:
                score += 1
    return score


def fScore(curr, gScore):
    return hScore(curr) + gScore


def findZero(curr):
    for i in range(0, 3):
        for j in range(0, 3):
            if curr[i][j] == 0:
                return i, j


def generateMoves(curr):
    x, y = findZero(curr)
    val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
    children = []
    for i in val_list:
        if (0 <= i[0] <= 2) and (0 <= i[1] <= 2):
            child = np.copy(curr).tolist()
            child[x][y] = child[i[0]][i[1]]
            child[i[0]][i[1]] = 0
            children.append(child)
    return children


allMoves = []


def solve(input):
    current_state = json.loads(str(input))
    allMoves.append(current_state)
    gScore = 0
    while isGoalState(current_state) == False:
        moves = generateMoves(current_state)
    fScores = []
    if all(m in allMoves for m in moves):
        return ("Not solvable")
    else:
        novelMoves = []
        for m in moves:
            if m not in allMoves:
                novelMoves.append(m)
        for n in novelMoves:
            fScores.append(fScore(n, gScore))
        index = fScores.index(min(fScores))  # return index of the move with the minimum fScore
        current_state = novelMoves[index]
        allMoves.append(current_state)
        print(current_state)
        gScore += 1


d = generate()
print(solve(d))