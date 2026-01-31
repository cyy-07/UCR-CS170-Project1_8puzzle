class Puzzle:
    def __init__(self, state):
        # We want to initialize the puzzle, with a given state.
        self.state = state
        self.size = len(state)
    def find_blank(self):
        # We want to find the position of the 0(blank) in the puzzle.
        for i in range(self.size):
            for j in range(self.size):
                if self.state[i][j] == 0:
                    return (i, j)
        return None