def main():
    print("Welcome to Yiyang's 8-puzzle solver!")
    print("It is your choice now! If you choose "1", it will be a default test puzzle, if you choose "2", you can create your own puzzle!")
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

