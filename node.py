#In the node file, we want to define the Node class for the search tree,
# and it is quite different from the state of the puzzle. But in the search tree,
# it contains the way for us to reach a puzzle state.
class Node:
    def __init__(self, state, parent=None, g_n=0, h_n=0):
        self.state = state
        self.parent = parent
        self.g_n = g_n                          # Cost to reach this node
        self.h_n = h_n                          # Heuristic cost to goal(estimate cost to reach goal)
        self.f_n = g_n + h_n                    # Total estimated cost
    def expand(self):
        # We want to expand the node to generate its children nodes.
        children = []
        row, col = self.state.find_blank()
        #try to move the blank in all four directions.
        try_right = self.state.move_right()
        if try_right is not None:
            right_node = Node(try_right, parent=self, g_n=self.g_n + 1)
            children.append(right_node)

        try_left = self.state.move_left()
        if try_left is not None:
            left_node = Node(try_left, parent=self, g_n=self.g_n + 1)
            children.append(left_node)

        try_up = self.state.move_up()
        if try_up is not None:
            up_node = Node(try_up, parent=self, g_n=self.g_n + 1)
            children.append(up_node)

        try_down = self.state.move_down()
        if try_down is not None:
            down_node = Node(try_down, parent=self, g_n=self.g_n + 1)
            children.append(down_node)

        #After trying all four directions, return the children list, so that we can pass it to the search algorithm.
        return children
    
    #Dr.eamonn mentioned in the flie that repeated states should be avoided.
    #So we need to define the comparation method to compare two nodes.
    #I try to change the matrix state into a tuple, so that we can easily compare two states.
    def tuple(self):
        flat_state = []
        for row in self.state.state: #Sorry for the confusion, here self.state is a Puzzle object.
            for tile in row:
                flat_state.append(tile)
        return tuple(flat_state)
    

    