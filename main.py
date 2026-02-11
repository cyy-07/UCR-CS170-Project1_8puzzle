from puzzle import Puzzle
from algorithms.search import uniform_cost_search, a_star_with_misplaced_tile, a_star_with_manhattan
from algorithms.heuristics import uniform_cost, count_misplaced_tile, manhattan_distance

def main():
    print("Welcome to Yiyang's 8-puzzle solver!")
    print("It is your choice now! If you choose \"1\", it will be a default test puzzle, if you choose \"2\", you can create your own puzzle!")
    user_choice = input("Please enter 1 or 2: ")
    if user_choice == "1":
        print("\n Default puzzles:(1-8, with increasing difficulty, which means the depth increasing)")
        print("choose '1' -> depth=0")
        print("choose '2' -> depth=2")
        print("choose '3' -> depth=4")
        print("choose '4' -> depth=8")
        print("choose '5' -> depth=12")
        print("choose '6' -> depth=16")
        print("choose '7' -> depth=20")
        print("choose '8' -> depth=24")
        difficulty_choice = input("Please enter a number from 1 to 8: ")    
        # Dr. Keogh mentioned in the report that we can use his test cases.
        if difficulty_choice == "1":
            test_state = [  [1,2,3], [4,5,6], [7,8,0]]#depth=0
        elif difficulty_choice == "2":
            test_state = [  [1,2,3], [4,5,6], [0,7,8]]#depth=2
        elif difficulty_choice == "3":
            test_state = [  [1,2,3], [5,0,6], [4,7,8]]#depth=4
        elif difficulty_choice == "4":
            test_state = [  [1,3,6], [5,0,2], [4,7,8]]#depth=8
        elif difficulty_choice == "5":
            test_state = [  [1,3,6], [5,0,7], [4,8,2]]#depth=12
        elif difficulty_choice == "6":
            test_state = [  [1,6,7], [5,0,3], [4,8,2]]#depth=16
        elif difficulty_choice == "7":
            test_state = [  [7,1,2], [4,8,5], [6,3,0]]#depth=20
        elif difficulty_choice == "8":
            test_state = [  [0,7,2], [4,6,1], [3,5,8]]#depth=24
        else:
            print("Invalid choice! Please enter a number from 1 to 8.")
            return
        select_algorithm(Puzzle(test_state))#Debug: I first tried select_algorithm(test_state), but error.
    elif user_choice == "2":
        print("\n It is your choice now! Please enter your own puzzle state, using 0 to represent the blank tile. Please only enter valid 8-puzzles!")
        own_puzzle_row_one = input("Enter the first row: ")
        own_puzzle_row_two = input("Enter the second row: ")
        own_puzzle_row_three = input("Enter the third row: ")
        for i in range(3):
            own_puzzle_row_one[i] = int(own_puzzle_row_one[i])
            own_puzzle_row_two[i] = int(own_puzzle_row_two[i])
            own_puzzle_row_three[i] = int(own_puzzle_row_three[i])
        user_input_state = [own_puzzle_row_one, own_puzzle_row_two, own_puzzle_row_three]
        select_algorithm(Puzzle(user_input_state)) #Debug: I first tried select_algorithm(user_input_state), but error.
        # Fixed by wrapping the list into a Puzzle object so the search algorithm so that we can use .display()
    else:
        print("Invalid choice! Please enter 1 or 2.")
        return
def select_algorithm(puzzle_state):
    print("\n Now, please select the algorithm you want to use to solve the puzzle.")
    print("choose '1' -> Uniform Cost Search")
    print("choose '2' -> A* with Misplaced Tile Heuristic")
    print("choose '3' -> A* with Manhattan Distance Heuristic")
    algorithm_choice = input("Please enter a number from 1 to 3: ")
    if algorithm_choice == "1":
        result_node, nodes_expanded, max_queue_size = uniform_cost_search(puzzle_state)
    elif algorithm_choice == "2":
        result_node, nodes_expanded, max_queue_size = a_star_with_misplaced_tile(puzzle_state)
    elif algorithm_choice == "3":
        result_node, nodes_expanded, max_queue_size = a_star_with_manhattan(puzzle_state)
    else:
        print("Invalid choice! Please enter a number from 1 to 3.")
        return
    
if __name__ == "__main__":
        main()