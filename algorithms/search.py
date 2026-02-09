def general_search_algorithm(puzzle_state, heuristic_function):
    frontier = [] #I tried to use the heapq method but failed, so I chose to use a easier list to implement.
    visited = [] #record the visited states, to avoiding repeated states.
    nodes_expanded = 0
    start_node = Node(puzzle_state, parent=None, g_n=0, h_n=heuristic_function)
    frontier.append(start_node)
    max_queue_size = -1
    while len(frontier) > 0:
        if len(frontier) > max_queue_size:
            max_queue_size = len(frontier)#if update the max queue size.
        best = frontier[0]
        for node in frontier:
            if node.f_n < best.f_n:
                best = node         #update the best node in the frontier(has the lowest f_n value).
        frontier.remove(best)       #remove the best node from the frontier, and expand it.
        if best.state.check_is_goal():
            #we found it! return the best node, the number of nodes expanded and the max queue size. And in the report, we can trace back the path and compare.
            return best, nodes_expanded, max_queue_size
        #now mark it as visited.
        visited.append(best.tuple())
        nodes_expanded += 1

        children = best.expand() #Continue to expand the best node, and add its children to the frontier.

        for child in children:
            if child.tuple() not in visited:
                frontier.append(child)

    print("No solution is founded.")
    return None, nodes_expanded, max_queue_size #if we cannot find the solution, return None and the number of nodes expanded and the max queue size.