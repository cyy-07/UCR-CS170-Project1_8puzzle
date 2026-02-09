#In this heuristics.py file, we define different heuristic functions for the 8-puzzle problem.
#Let's start with the uniform cost search. It is quite simple because h_n is always 0.
#Therefore, f_n=g_n so we only care about how far we need to reach the node.
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from puzzle import Puzzle
from node import Node
def uniform_cost(state):
    return 0

#Now we define the misplaced tile heuristic search. It is also simple because we only count the number of misplaces tiles.
def count_misplaced_tile(state):
    goal = [[1,2,3],
            [4,5,6],
            [7,8,0]]
    count = 0
    for i in range(3):
        for j in range(3):    #count how many tiles are wrong placed.
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

#Finally, we define the Manhattan distance search. 
#Manhattan distance is the sum of the vertical and horizontal distances(absolute value) from current position to the goal for all tiles.
def manhattan_distance(state):
    goal = [[1,2,3],
            [4,5,6],
            [7,8,0]]
    manhattan_dist = 0
    goal_pos={}
    for i in range(3):
        for j in range(3):
            tile = goal[i][j]
            #We create a dictionary,in order to store the goal position of each tile to look up.
            if tile != 0:
                goal_pos[tile] = (i,j)  #Dr. Keogh mentioned that we should not count the blank.

    #Calculate the Manhattan distance.
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                goal_i, goal_j = goal_pos[tile]
                manhattan_dist += abs(i - goal_i) + abs(j - goal_j) #In both vertical and horizontal direction, we calculate the distance and add both up.
    return manhattan_dist


    '''
    #test

test = [        [1,2,3],
                [5,0,6],
                [4,7,8]]        #depth=4, using Dr. Keogh's test case. Misplaced tile =4, manhattan distance =4.
print("Misplaced Tile Heuristic:", count_misplaced_tile(test))
print("Manhattan Distance Heuristic:", manhattan_distance(test))
test_2 = [          [1,2,3],
                    [4,5,6],
                    [0,7,8]]    #depth=2, using Dr. Keogh's test case. Misplaced tile =2, manhattan distance =2.
print("Misplaced Tile Heuristic:", count_misplaced_tile(test_2))
print("Manhattan Distance Heuristic:", manhattan_distance(test_2))
'''