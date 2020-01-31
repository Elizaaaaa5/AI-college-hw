


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
    return (arr == goal_state)



def findZero(curr):
    for i in range(3):
        for j in range(3):
            if curr[i][j] == 0:
                return i, j


def generateMoves(curr):
    x, y = findZero(curr.data)
    val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
    children = []
    for i in val_list:
        if (0 <= i[0] <= 2) and (0 <= i[1] <= 2):
            child = np.copy(curr.data).tolist()
            child[x][y] = child[i[0]][i[1]]
            child[i[0]][i[1]] = 0
            newNode = Node(child, curr)
            children.append(newNode)
    return children



def solve(input):
    input = json.loads(str(input))
    current_state = Node(input, None)

    moves = []
    visited_states= []

    moves.append(current_state)
    visited_states.append(str(current_state.data))
    while len(moves) != 0:
        check = moves.pop(0)
        # print(check.data)
        if isGoalState(check.data):
            print("the optimal path:")
            printSequence(check)
            break
        else:
            check_children = generateMoves(check)
            for c in check_children:
                if str(c.data) not in visited_states:
                    moves.append(c)
                    visited_states.append(str(c.data))


def printSequence(check):
    sequence = []
    while check.parent != None:
        sequence.append(str(check.data))
        check = check.parent
    print('\n'.join(map(str, sequence[::-1])))

