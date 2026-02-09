def general_search_algorithm(puzzle_state, heuristic_function):
    frontier = [] #I tried to use the heapq method but failed, so I chose to use a easier list to implement.
    visited = [] #record the visited states to avoid repeated states.
    nodes_expanded = 0
    start_node = Node(puzzle_state, parent=None, g_n=0, h_n=heuristic_function)
    frontier.append(start_node)
    

