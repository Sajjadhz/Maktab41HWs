import random
#########################
# Toss a coin to see who plays first
if random.choice(["You","Computer"]) == "You":
    first_player = "You"
else:
    first_player = "Computer"
##########################
#initialize game state
state = ["-","-","-","-","-","-","-","-","-"]
state_int = [0,0,0,0,0,0,0,0,0]
all_positions = [1,2,3,4,5,6,7,8,9]
remaining_positions = all_positions
print("position pattern:")
print("1 | 2 | 3")
print("4 | 5 | 6")
print("7 | 8 | 9")
print("----------")
winner = None
is_someone_won = False
##########################
def get_users_choice():
    print("Enter a position as given pattern from remainig positions:" + str(remaining_positions))
    p = int(input())
    if p not in remaining_positions:
        print("Sorry, The entered position already is filled or wrong. Enter a valid position.")
    else:
        state[p - 1] = 'X'
        state_int[p - 1] = 1
        remaining_positions.remove(p)
        print(state[0] + " | " + state[1] + " | " + state[2])
        print(state[3] + " | " + state[4] + " | " + state[5])
        print(state[6] + " | " + state[7] + " | " + state[8])
        print("----------")
        print("Compurer\'s turn")
##########################        
def get_computers_choice():
    p = random.choice(remaining_positions)
    state[p - 1] = 'O'
    state_int[p - 1] = -1
    remaining_positions.remove(p)
    print(state[0] + " | " + state[1] + " | " + state[2])
    print(state[3] + " | " + state[4] + " | " + state[5])
    print(state[6] + " | " + state[7] + " | " + state[8])
    print("----------")
    print("Your turn")
   
##########################
def check_winner():
    is_someone_won = True
    if state[0] == state[1] == state[2] == 'X' or \
       state[3] == state[4] == state[5] == 'X' or \
       state[6] == state[7] == state[8] == 'X' or \
       state[0] == state[3] == state[6] == 'X' or \
       state[1] == state[4] == state[7] == 'X' or \
       state[2] == state[5] == state[8] == 'X' or \
       state[0] == state[4] == state[8] == 'X' or \
       state[2] == state[4] == state[6] == 'X':
        print("Congratulation! You won.")
        winner = "X"
        is_someone_won = True
        return is_someone_won
    elif state[0] == state[1] == state[2] == 'O' or \
       state[3] == state[4] == state[5] == 'O' or \
       state[6] == state[7] == state[8] == 'O' or \
       state[0] == state[3] == state[6] == 'O' or \
       state[1] == state[4] == state[7] == 'O' or \
       state[2] == state[5] == state[8] == 'O' or \
       state[0] == state[4] == state[8] == 'O' or \
       state[2] == state[4] == state[6] == 'O':
        print("Sorry, Game Over.")
        winner = "O"
        is_someone_won = True
        return is_someone_won
##########################
# part 1
def run_part1():
    for turn in range(5):
        if first_player == "You":
            get_users_choice()
            is_someone_won = check_winner()
            if not is_someone_won:
                get_computers_choice()
                is_someone_won = check_winner()
        else:
            get_computers_choice()
            is_someone_won = check_winner()
            if not is_someone_won:
                get_users_choice()
                is_someone_won = check_winner()   
        if is_someone_won or (len(remaining_positions) == 0):
            break

##########################
# Part 2

urgent_positions = []
def which_to_fill():
    urgent_positions = []
    if state_int[0] + state_int[1] + state_int[2] == 2:urgent_positions.append([1,2,3][[state_int[0] , state_int[1] , state_int[2]].index(0)])
    if state_int[3] + state_int[4] + state_int[5] == 2:urgent_positions.append([4,5,6][[state_int[3] , state_int[4] , state_int[5]].index(0)])
    if state_int[6] + state_int[7] + state_int[8] == 2:urgent_positions.append([7,8,9][[state_int[6] , state_int[7] , state_int[8]].index(0)])
    if state_int[0] + state_int[3] + state_int[6] == 2:urgent_positions.append([1,4,7][[state_int[0] , state_int[3] , state_int[6]].index(0)])
    if state_int[1] + state_int[4] + state_int[7] == 2:urgent_positions.append([2,5,8][[state_int[1] , state_int[4] , state_int[7]].index(0)])
    if state_int[2] + state_int[5] + state_int[8] == 2:urgent_positions.append([3,6,9][[state_int[2] , state_int[5] , state_int[8]].index(0)])
    if state_int[0] + state_int[4] + state_int[8] == 2:urgent_positions.append([1,5,9][[state_int[0] , state_int[4] , state_int[8]].index(0)])
    if state_int[2] + state_int[4] + state_int[6] == 2:urgent_positions.append([3,5,7][[state_int[2] , state_int[4] , state_int[6]].index(0)])
    urgent_positions = list(set(urgent_positions))
    return urgent_positions
    
##########################
def get_intelligent_choice(urgent_positions):    
    if len(urgent_positions) > 0:
        print(urgent_positions)
        urgent_positions = list(set(urgent_positions).intersection(set(remaining_positions)))
        p = random.choice(urgent_positions)
    else:
        p = random.choice(remaining_positions)
    print(p)
    state[p - 1] = 'O'
    state_int[p - 1] = -1
    remaining_positions.remove(p)
    print(state[0] + " | " + state[1] + " | " + state[2])
    print(state[3] + " | " + state[4] + " | " + state[5])
    print(state[6] + " | " + state[7] + " | " + state[8])
    print("----------")
    print("Your turn")
##########################
def run_part2():
    for turn in range(5):
        if first_player == "You":
            get_users_choice()
            is_someone_won = check_winner()
            if not is_someone_won:
                urgent_positions = which_to_fill()
                get_intelligent_choice(urgent_positions)
                is_someone_won = check_winner()
        else:
            urgent_positions = which_to_fill()
            get_intelligent_choice(urgent_positions)
            is_someone_won = check_winner()
            if not is_someone_won:
                get_users_choice()
                is_someone_won = check_winner()   
        if is_someone_won or (len(remaining_positions) == 0):
            break
'''
To run part1 uncomment run_part1()
To run part2 uncomment run_part2()
but not both of them in same time.
'''
#run_part1()
run_part2()
