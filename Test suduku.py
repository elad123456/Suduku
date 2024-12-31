from Suduku import Suduku:
:
def test_check_board_full(board:list):
    sudoku_board = [
        [-1, 3, 4, 6, 7, 8, 9, 1, 2],  # Row 1
        [6, 7, 2, 1, 9, 5, 3, 4, 8],  # Row 2
        [1, 9, 8, -1, 4, -1, 5, 6, 7],  # Row 3
        [-1, -1, 9, 7, 6, 1, 4, 2, 3],  # Row 4
        [4, 2, 6, 8, -1, 3, 7, 9, 1],  # Row 5
        [7, 1, 3, 9, 2, 4, 8, 5, 6],  # Row 6
        [9, 6, 1, 5, 3, -1, 2, 8, 4],  # Row 7
        [2, 8, 7, 4, 1, 9, 6, 3, 5],  # Row 8
        [3, 4, 5, -1, 8, -1, 1, 7, 9]  # Row 9
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
        [3, 4, 5, 2, 8, 6, 1, 7, 9]  # Row 9
    ]
    assert check_if_the_board_is_full(sudoku_board1)==True
    assert check_if_the_board_is_full(sudoku_board) == False