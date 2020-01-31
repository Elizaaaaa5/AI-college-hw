
bottom_of_tree = []
statements = []

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

def negate(input):


def construct_tree(arr):
    global bottom_of_tree
    global statements
    statements = [Node(str(x)) for x in arr]
    build_tree()

def build_tree():
    global statements
    global bottom_of_tree
    for s in range(0,len(statements)-1):
        statements[s].children.append(statements[s+1])
    for s in statements:
        print(s.data)
        if "&" in s.data:
            for b in bottom_of_tree:
                b.children.append(Node(s[:s.data.find("&")-1]))
                second = Node(s[s.data.find("&")+1:])
                b.children.append(second)
                bottom_of_tree = [second]
        if "|" in s.data:
            for b in bottom_of_tree:
                first = Node(s[:s.data.find("&")-1])
                second = Node(s[s.data.find("&") + 1:])
                b.children.append(first)
                b.children.append(second)
                bottom_of_tree = [first, second]
