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
   
    #Instead of defining all 8 number's moves, 
    #I noticed that we can just define the blank's move
    #(Because every move can be seen as the number swop with the blank).

    def move_up(self):
        blank_position = self.find_blank()
        row = blank_position[0]
        col = blank_position[1]
        #check whether we can move up or not, if not, return None.
        if row == 0:
            return None
        updated_state = self.copy()
        updated_state[row][col]= updated_state[row-1][col]
        updated_state[row-1][col]=0
        return Puzzle(updated_state)
    #define move in other directions in the same way.
    def move_down(self):
        blank_position = self.find_blank()
        row = blank_position[0]
        col = blank_position[1]
        if row == self.size - 1:
            return None
        updated_state = self.copy()
        updated_state[row][col] = updated_state[row + 1][col]
        updated_state[row + 1][col] = 0
        return Puzzle(updated_state)
    def move_right(self):
        blank_position = self.find_blank()
        row = blank_position[0]
        col = blank_position[1]
        if col == self.size - 1:
            return None
        updated_state = self.copy()
        updated_state[row][col] = updated_state[row][col + 1]
        updated_state[row][col + 1] = 0
        return Puzzle(updated_state)
    def move_left(self):
        blank_position = self.find_blank()
        row = blank_position[0]
        col = blank_position[1]
        if col == 0:
            return None
        updated_state = self.copy()
        updated_state[row][col] = updated_state[row][col - 1]
        updated_state[row][col - 1] = 0
        return Puzzle(updated_state)
    

