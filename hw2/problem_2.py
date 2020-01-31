class Node(object):
    def __init__(self, data, depth):
        self.data = data
        self.depth = depth
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


def parentheses_balance(input):
    s = []
    balanced = True
    i = 0
    while i < len(input) and balanced:
        if input[i] == "(":
            s.append(input[i])
        elif input[i] == ")":
            if len(s) == 0:
                balanced = False
            else:
                s.pop()
        i += 1
    if balanced and len(s) == 0:
        return True
    return False




def construct_tree(arr):
    print("To check for validity, we negate the last premise and then look to see if all paths are closed, \nmeaning both an atomic statement and its negation are in the tree")
    negate = []
    depth = 0
    statements = [Node(str(x), depth) for x in arr]
    statements[-1].data = "!("+statements[-1].data+")"
    tree = []
    types_of_discharge = []
    while len(statements) != 0:
        s = statements.pop(0)
        # print("statement: " + s.data)
        if parentheses_balance(s.data) == False:
            print("INVALID-INPUT")
            return
        # check depth to determine when to iterate depth
        tree.append(s)
        character = 0
        while character < len(s.data):
            # print("testing character", s.data[character])
            if "(" == s.data[character]:
                if s.data[-1] == ")" and parentheses_balance(s.data[1:-1]):
                    s.data = s.data[1:-1]
            if ">" == s.data[character]:
                before = s.data[:character].strip()
                after = s.data[character+ 1:].strip()
                if parentheses_balance(before) and parentheses_balance(after):
                    depth += 1
                    types_of_discharge.append("disjunct")
                    statements.append(Node("!" + before, depth))
                    statements.append(Node(after, depth))
                # otherwise, if unbalanced, leave the string as is
                    character = len(s.data)
                else:
                    character += 1
            elif "|" == s.data[character]:
                before = s.data[:character].strip()
                after = s.data[character+1:].strip()
                if parentheses_balance(before) and parentheses_balance(after):
                    depth += 1
                    types_of_discharge.append("disjunct")
                    statements.append(Node(before, depth))
                    statements.append(Node(after, depth))
                # otherwise, if unbalanced, leave the string as is
                    character = len(s.data)
                else:
                    character += 1
            elif "&" == s.data[character]:
                # print("and")
                before = s.data[:character].strip()
                after = s.data[character + 1:].strip()
                if parentheses_balance(before) and parentheses_balance(after):
                    depth += 1
                    types_of_discharge.append("conjunct")
                    statements.append(Node(before, depth))
                    statements.append(Node(after, depth))
                # otherwise, if unbalanced, leave the string as is
                    character = len(s.data)
                else:
                    character += 1
            elif "!" == s.data[character]:
                depth += 1
                negate.clear()
                if "!" == s.data[character+1]:  # if double negation "!!"
                    types_of_discharge.append("conjunct")
                    statements.append(Node(s.data.replace("!!", ""), depth))
                elif "(" == s.data[character+1]:      # if "!(" in the string
                    start = character+1
                    end = start+1
                    snippet = s.data[start:end]
                    while parentheses_balance(snippet) == False:        # iterates until finding balanced statement to negate
                        end += 1
                        snippet = s.data[start:end]
                    # now, negate the parts of the snippet
                    if (parentheses_balance(snippet[1:-1])):            # if the snippet is encased in parentheses, remove them before decomposing statement
                        snippet = snippet[1:-1]
                    # print("snippet is " + snippet)
                    delimiter = 0
                    before = snippet[:delimiter]
                    after = snippet[delimiter + 1:]
                    while snippet[delimiter] not in ">|&" or parentheses_balance(before) == False or parentheses_balance(after) == False:
                        before = snippet[:delimiter]
                        after = snippet[delimiter+1:]
                        delimiter += 1
                    # find the delimiter of the snippet
                    before = snippet[:delimiter].strip()
                    after = snippet[delimiter+1:].strip()
                    if "|" == snippet[delimiter]:
                        negate.append(Node("!" + before + " & !" + after, depth))
                    elif "&" == snippet[delimiter]:
                        negate.append(Node("!" + before + " | !" + after, depth))
                    elif ">" == snippet[delimiter]:
                        negate.append(Node("!(!" + before + " | " + after + ")", depth))
                    # print("before", before, "and after", after)
                    # now, deal with the remainder
                    remainder = s.data[end+1:]
                    # print("remainder", remainder)
                    other_delimiter = 0
                    if remainder != "":
                        while remainder[other_delimiter] not in ">|&":
                            other_delimiter += 1                        # finds other delimiter in the rest of the statement if it exists
                        if "|" == remainder[other_delimiter]:
                            other_statement = remainder[other_delimiter+1:].strip()
                            negate.append(Node(other_statement, depth))
                        elif "&" == remainder[other_delimiter]:
                            other_statement = remainder[other_delimiter+1:].strip()
                            negate.append(Node(other_statement, depth))
                        elif ">" == remainder[other_delimiter]:
                            other_statement = remainder[other_delimiter + 1:].strip()
                            negate[0] = Node("!" + negate[0].data, depth)
                            negate.append(Node(other_statement, depth))
                    for n in negate:
                        # print("negate info", n.data)
                        statements.append(n)
                # otherwise, if "!" is followed by a character, leave the string as is
                else:
                    character +=1
                    continue
                # print("len negate", len(negate))
                character = len(s.data)
            else:
                character +=1
                # is either an atomic statement or negated atomic statement
        # print(len(statements))
    for t in tree:
        print(t.depth, "\t", t.data)
    return tree


# construct_tree(["!A | B", "A", "B"])
construct_tree(["A | B", "!A > B"])
