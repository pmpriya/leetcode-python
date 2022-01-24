#   Solving the infamous N-queens leetcode hard problem using Backtracking algorithm

def solveNqueens(n):
    # n indicating the number of queens that need to be placed in the board

    solutions = []
    state = []
    search(state, solutions, n)
    return solutions


def is_valid_state(state, n):
    #   checking if it is a valid solution
    return len(state) == n


def get_candidates(state, n):
    # initial stage where state is empty
    if not state:
        return range(n)

    # finding the next position in the state to place the next queen
    position = len(state)
    candidates = set(range(n))

    # pruning down the candidates that place queen into attacks
    for row, col in enumerate(state):
        # discard column
        candidates.discard(col)
        dist = position - row

        # discarding the diagonals
        candidates.discard(col - dist)
        candidates.discard(col + dist)

    return candidates


def search(state, solutions, n):
    if is_valid_state(state, n):
        state_string = state_to_string(state, n)
        solutions.append(state_string)
        return

    for candidate in get_candidates(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.pop()


def state_to_string(state, n):
    #   [ 1,0,3,2] => [".Q..", "Q...", "...Q", "..Q."]
    ret = []
    for i in state:
        string = '.' * i + "Q" + '.' * (n - i - 1)
        ret.append(string)
    return ret


if __name__ == '__main__':
    output = solveNqueens(4)
    print(output)
