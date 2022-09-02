
import os
import time
import datetime



#create sample board 9x9 
board1 = [[3,0,0,2,0,1,0,0,0],
          [7,4,0,0,0,0,0,1,9],
          [0,2,0,0,6,0,5,0,0],
          [0,3,0,7,4,0,0,0,1],
          [0,0,8,0,0,0,9,0,0],
          [6,0,0,0,9,2,0,5,0],
          [0,0,2,0,8,0,0,4,0],
          [1,5,0,0,0,0,0,9,7],
          [6,0,0,0,9,2,0,5,0]]

board2 = [[0, 4, 3, 0, 8, 0, 2, 5, 0],
          [6, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 9, 4],
          [9, 0, 0, 0, 0, 4, 0, 7, 0],
          [0, 0, 0, 6, 0, 8, 0, 0, 0],
          [0, 1, 0, 2, 0, 0, 0, 0, 3],
          [8, 2, 0, 5, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 5],
          [0, 3, 4, 0, 9, 0, 7, 1, 0]]

start_time = time.time()

def display_board(matrix):

    #if matrix is None, print No Solution 
    if matrix == None:
        print("No Solution")
        return
    
    #this line will create border line to help shape it like a board
    grid_line = "-"*25 #Output = "-------------------------"
    
    #if matrix doesn't have any containing numbers, print Empty Matrix
    if matrix == []: 
        print("Empty Matrix")

    num_rows = len(matrix) #len(matrix) or 9
    num_cols = len(matrix[0]) #len(matrix[0]) or 9

    for i in range(num_rows): #Iterate
        if i % 3 == 0:
            print(grid_line)
        print_row = "" #This is a container for picked up values from the board
        for j in range(num_cols):
            if j % 3 == 0:
                print_row += "| "
            
            # value variable below will have the value of picked-up number from the 
            #     matrix IF matrix[i][j] is greater than 0
            #     else, place a space/blank
            value = str(matrix[i][j]) if matrix[i][j] > 0 else " "
            print_row += value + " " # append the value of "value" variable to print_row with 1 space
        
        # once the column iteration is done, add "|" to print_row (it will be placed in the last character of print_row)
        print_row += "|"
        

        # print row (line per column iteration)
        print(print_row)

    #enclose the grid after 3 printed row
    print(grid_line)

# Display 
# display_board(board1)

def isValid(matrix, row, col, value):
    for j in range(9):
        if matrix[row][j] == value:
            # print("Duplicate value for row detected")
            return False
    for i in range(9):
        if matrix[i][col] == value:
            # print("Duplicate value for column detected")            
            return False
    
    grid_row = row // 3
    grid_col = col // 3

    for i in range(3):
        for j in range(3):
            if matrix[3*grid_row + i][3*grid_col + j] == value:
                # print("Duplicate value for grid detected")
                return False
    return True

calls = 0
def find_empty_cell(board):
    global calls
    calls += 1
    cursor_pos = [0, 0]
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                cursor_pos[0] = row
                cursor_pos[1] = col
                return cursor_pos


def solve_board(board):
    cell = find_empty_cell(board)

    if cell is None:
        return board
    row = cell[0]
    col = cell[1]

    for value in range(1, 10):
        if(isValid(board, row, col, value)):
            board[row][col] = value
            # os.system('cls')
            # print("Start Time: " + str(start_time))
            # real_time = time.time()
            # print("Real Time: " + str(real_time))
            display_board(board)
            
            solution = solve_board(board)
            if solution is not None:
                return solution

            # Backtrack code
            board[row][col] = 0
    return None


def main():
    print(solve_board(board3))
    print("============ DONE ==============")
    print("Total Calls: %d"%(calls))
    end_time = time.time()
    time_taken = (end_time - start_time) 
    ss = datetime.timedelta(seconds=int('%d'%(time_taken)))
    print("Time taken: " + str(ss)) 



if __name__ == "__main__":
    main()

