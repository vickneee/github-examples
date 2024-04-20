def print_board(board):
    for row in board:
        print(" ".join(row))

def check_win(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        print("Player", player, "turn")
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        if board[row][col] != ' ':
            print("Invalid move, try again.")
            continue
        board[row][col] = player
        if check_win(board):
            print("Player", player, "wins!")
            break
        player = 'O' if player == 'X' else 'X'

tic_tac_toe()