'''
Following Dr. Keogh's pseudocode structure[1], with some variable name variations:

function general-search(problem, QUEUEING-FUNCTION)
nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
loop do
    if EMPTY(nodes) then return "failure"
        node = REMOVE-FRONT(nodes)
    if problem.GOAL-TEST(node.STATE) succeeds then return node
        nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
end

[1]: https://www.dropbox.com/scl/fo/blbkjaf1eyl94lij5wl2b/AAvNKn0YrnaX0oGPQn7ueFo?dl=0&e=2&rlkey=alq2gb2ftsw73hcar4lk897r0  Dr. Keogh's slide 2-Blind Search_part2.ppt, page 3
In my code:
- 'nodes' is implemented as 'frontier' (a list of nodes to be explored)
- 'node' is implemented as 'best' (the node with lowest f(n) value)
- 'problem.GOAL-TEST(node.STATE)' is implemented as 'check_is_goal()'
The core algorithm logic matches the pseudocode exactly.
'''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from node import Node
from puzzle import Puzzle
from heuristics import count_misplaced_tile, manhattan_distance

def general_search_algorithm(puzzle_state, heuristic_function):
    frontier = [] #I tried to use the heapq method but failed, so I chose to use a easier list to implement.
    visited = [] #record the visited states, to avoid repeated states.
    nodes_expanded = 0
    start_node = Node(puzzle_state, parent=None, g_n=0, h_n=heuristic_function(puzzle_state.state)) #initialize the start node, and calculate its h_n value.
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
            child.h_n = heuristic_function(child.state.state)
            child.f_n = child.g_n + child.h_n  #update the fn value.
            if child.tuple() not in visited:
                frontier.append(child)

    print("No solution is founded.")
    return None, nodes_expanded, max_queue_size #if we cannot find the solution, return None and the number of nodes expanded and the max queue size.

def uniform_cost_search(puzzle_state):
    return general_search_algorithm(puzzle_state, heuristic_function=lambda state: 0)
def a_star_with_manhattan(puzzle_state):
    return general_search_algorithm(puzzle_state, heuristic_function=manhattan_distance)
def a_star_with_misplaced_tile(puzzle_state):
    return general_search_algorithm(puzzle_state, heuristic_function=count_misplaced_tile)
#call the heuristics functions from the heuristics.py file.
'''

#test

test_state = [  [1,2,3],
                [5,0,6],
                [4,7,8]]#depth=4, using Dr. Keogh's test case.
puzzle = Puzzle(test_state)
result_node, nodes_expanded, max_queue_size = a_star_with_manhattan(puzzle)
print("Nodes Expanded:", nodes_expanded)
print("Max Queue Size:", max_queue_size)
#Output: Nodes Expanded: 4, Max Queue Size: 6

'''