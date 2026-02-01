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
    
    def copy(self):
        # We want to create a copy of the current puzzle state, to better compare states.
        state_copy = []
        for row in self.state:
            state_copy.append(row.copy())
        return state_copy
    


    def check_is_goal(self):
        # We want to check if the current state is the same with the goal state.
         goal = [[1,2,3],
                [4,5,6],
                [7,8,0]]
         return self.state == goal
        # Try to display the puzzle 
    def display(self):
        for row in self.state:
            for num in row:
                if num == 0:
                    print("*", end=" ")
                else:
                    print(num, end=" ")
            print()