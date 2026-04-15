# Tic Tac Toe with Alpha-Beta Pruning

board = [" " for _ in range(9)]

# ---------- DISPLAY BOARD ----------
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# ---------- CHECK WIN ----------
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # cols
        [0,4,8], [2,4,6]             # diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# ---------- CHECK DRAW ----------
def is_draw():
    return " " not in board

# ---------- ALPHA-BETA FUNCTION ----------
def alpha_beta(is_max, alpha, beta):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_max:  # Computer (O)
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = alpha_beta(False, alpha, beta)
                board[i] = " "
                best = max(best, score)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break   # PRUNING
        return best
    else:  # Player (X)
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = alpha_beta(True, alpha, beta)
                board[i] = " "
                best = min(best, score)
                beta = min(beta, best)
                if beta <= alpha:
                    break   # PRUNING
        return best

# ---------- BEST MOVE ----------
def best_move():
    best_score = -100
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = alpha_beta(False, -100, 100)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# ---------- GAME LOOP ----------
while True:
    print_board()

    # Player move
    pos = int(input("Enter position (0-8): "))
    if board[pos] != " ":
        print("Invalid move!")
        continue
    board[pos] = "X"

    if check_winner("X"):
        print_board()
        print("You win!")
        break
    if is_draw():
        print_board()
        print("Draw!")
        break

    # Computer move
    comp = best_move()
    board[comp] = "O"

    if check_winner("O"):
        print_board()
        print("Computer wins!")
        break
    if is_draw():
        print_board()
        print("Draw!")
        break