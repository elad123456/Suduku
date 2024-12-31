def board_is_not_empty(options:list)->bool:
    for i in range(9):
        for j in range(9):
            if len(options[i][j])!=0:
                return True
    return False
def minimize_length_optional_list(optional_list:list)->int:
    min_list=9
    for i in range(9):
        for j in range(9):
            if len(optional_list[i][j])<min_list and len(optional_list[i][j])>1 :
                min_list=len(optional_list[i][j])
    return min_list

def board_not_includes_none(options:list)->bool:
    for i in range(9):
        for j in range(9):
            if len(options[i][j])!=0:
                if options[i][j][0]==None:
                    return False
    return True



def check_if_the_board_not_full(suduku_board:list)->bool:
    for i in range(9):
        for j in range(9):
            if suduku_board[i][j]==-1:
                return True
    return False



#return the list without a specific number
def remove_number_from_list(list1:list,num:int)->list:
    if num in list1:
        list1.remove(num)
    return list1



#input(suduku board,location), return the optional values if the location is empty,otherwise return [0]
def options_of_index(suduku_board:list,loc:tuple)->list:
    if suduku_board[loc[0]][loc[1]]!=-1:
        return [0]
    else:
        suduku_row=suduku_board[loc[0]]
        suduku_column=[]
        suduku_square=[]
        for i in range(9):
            suduku_column.append(suduku_board[i][loc[1]])
        start_point_for_square=[]
        start_point_for_square.append(loc[0]//3*3)
        start_point_for_square.append(loc[1] // 3 * 3)
        for i in range(3):
            for k in range(3):
                suduku_square.append(suduku_board [start_point_for_square[0]+i][start_point_for_square[1]+k])
        check_list=suduku_square+suduku_row+suduku_column
        suduku_square_no_duplicates = []
        for num in check_list:
            if num not in suduku_square_no_duplicates:
                suduku_square_no_duplicates.append(num)
        list_of_options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for num in suduku_square_no_duplicates:
            list_of_options=remove_number_from_list(list_of_options,num)
        return list_of_options



#input(suduku coard) return the optins for each location. if there is no option for any number the list includ NONE
def posible_digits(suduku_board:list)->list:
    return_suduku_options=[]
    for i in range(9):
        options_row=[]
        for j in range(9):
            check_number=suduku_board[i][j]
            if check_number==-1:
                indexes=(i,j)
                optins_for_number= options_of_index(suduku_board,indexes)
                if len(optins_for_number)==0:
                    optins_for_number=[None]
            else:
                optins_for_number=[]
            options_row.append(optins_for_number)
        return_suduku_options.append(options_row)
    return return_suduku_options



def one_stage(suduku_board:list,posible_options:list)->tuple:
    while check_if_the_board_not_full(suduku_board) and board_not_includes_none(posible_options) and board_is_not_empty(posible_options):

sudoku_board = [
    [-1, 3, 4, 6, 7, 8, 9, 1, 2],  # Row 1
    [6, 7, 2, 1, 9, 5, 3, 4, 8],  # Row 2
    [1, 9, 8, -1, 4, -1, 5, 6, 7],  # Row 3
    [-1,5, 9, 7, 6, 1, 4, 2, 3],  # Row 4
    [4, 2, 6, 8, -1, 3, 7, 9, 1],  # Row 5
    [7, 1, 3, 9, 2, 4, 8, 5, 6],  # Row 6
    [9, 6, 1, 5, 3, -1, 2, 8, 4],  # Row 7
    [2, 8, 7, 4, 1, 9, 6, 3, 5],  # Row 8
    [3, 4, 5, -1, 8, -1, 1, 7, 9]   # Row 9
]
sudoku_board1 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],  # Row 1
    [6, 7, 2, 1, 9, 5, 3, 4, 8],  # Row 2
    [1, 9, 8, 3, 4, 2, 5, 6, 7],  # Row 3
    [8, 5, 9, 7, 6, 1, 4, 2, 3],  # Row 4
    [4, 2, 6, 8, 5, 3, 7, 9, 1],  # Row 5
    [7, 1, 3, 9, 2, 4, 8, 5, 6],  # Row 6
    [9, 6, 1, 5, 3, 7, 2, 8, 4],  # Row 7
    [2, 8, 7, 4, 1, 9, 6, 3, 5],  # Row 8
    [3, 4, 5, 2, 8, 6, 1, 7, 9]   # Row 9
]
options=[
    [[5], [None], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[],[], [], [2, 3], [], [2], [], [], []],
    [[8], [], [], [], [], [], [], [], []],
    [[], [], [], [], [5], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [7], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [2], [], [2, 6], [], [], []]]
#check_if_the_board_is_full test
"""print(check_if_the_board_is_full(sudoku_board1))
print(check_if_the_board_is_full(sudoku_board))"""
#one_stage(sudoku_board,posible_digits(sudoku_board))
#print(posible_digits(sudoku_board1))
#print(board_includes_none(posible_digits(sudoku_board1)))
#op=[[[], [], [], [], [], [], [], [4,5], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[8,3,4], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []]]
#print(minimize_length_optional_list(op))
option=posible_digits(sudoku_board1)
print(option)
one_stage(sudoku_board,option)
