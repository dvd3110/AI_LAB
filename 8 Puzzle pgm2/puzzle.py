from queue import Queue

Q = Queue()


def print_grid(src):
    # print the grid state
    state = src.copy()
    state[state.index(-1)] = '_'
    print(f"""
     {state[0]} {state[1]} {state[2]}
     {state[3]} {state[4]} {state[5]}
     {state[6]} {state[7]} {state[8]}
    """)


src = [1, 2, 5, 3, 4, -1, 6, 7, 8]
target = [-1, 1, 2, 3, 4, 5, 6, 7, 8]


Q.put(src)


def runner(src):
    
    visited_states = set()
    visited_states.add(tuple(src))

    while(not Q.empty()):
        state = Q.get()
        # visited_states.add(state)
        Moves = []

        print_grid(state)

        if(state == target):
            print("The Game has been finished!")
            return
        

        Moves += [move for move in possible_moves(state,visited_states) if move not in Moves]     

        for m in Moves:
            if tuple(m) not in visited_states:
                Q.put(m)
                visited_states.add(tuple(m))

    print("Not Solvable")



def possible_moves(state, visited_states):
    b = state.index(-1)
    d = []
    if 9 > b - 3 >= 0:
        d += 'u'
    if 9 > b + 3 >= 0:
        d += 'd'
    if b not in [2, 5, 8]:
        d += 'r'
    if b not in [0, 3, 6]:
        d += 'l'

    pos_moves = []
    for move in d:
        pos_moves.append(gen(state, move, b))
    return [move for move in pos_moves if tuple(move) not in visited_states]



def gen(state, direction, b):
    temp = state.copy()
    if direction == 'u':
        temp[b - 3], temp[b] = temp[b], temp[b - 3]
    if direction == 'd':
        temp[b + 3], temp[b] = temp[b], temp[b + 3]
    if direction == 'r':
        temp[b + 1], temp[b] = temp[b], temp[b + 1]
    if direction == 'l':
        temp[b - 1], temp[b] = temp[b], temp[b - 1]
    return temp



runner(src)

print("Name: Nagalakshman BS")
print("USN: 1BM22Cs410")