#ERROR IN LINES 60 & 40

# Define the board size (rows, columns)
rows = 6
cols = 7

# Create an empty board
board = [[" " for _ in range(cols)] for _ in range(rows)]

# Function to print the board
def print_board(board):
    for row in board:
        print("|", end="")
        for cell in row:
            print(cell + "|", end="")
        print()

# Function to check if a column is full
def is_column_full(board, col):
    return board[0][col] != " "

# Function to place a piece in the board
def place_piece(board, col, player):
    for row in range(rows-1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player
            break

# Function to check for a winner
def check_winner(board, player):

    # Initialize row if necessary (assuming it should be an integer)
    row = 0  # Add this line if row might not be initialized elsewhere

    # Check horizontal wins
    for row in board:
        for col in range(cols-3):
            if row[col] == player and row[col+1] == player and row[col+2] == player and row[col+3] == player:
                return True

    # Check vertical wins
    if row < rows - 3:  # Check if enough rows below (corrected)
        if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
            return True

    # Check diagonal wins (more complex logic, not included here)
    return False

# Main game loop
current_player = "X"
while True:
    print_board(board)
    col_choice = int(input(f"Player {current_player}, choose a column (1-{cols})")) - 1

    if is_column_full(board, col_choice):
        print("Column is full, try again!")
        continue

    place_piece(board, col_choice, current_player)

    # Check for winner
    if check_winner(board, current_player):
        print_board(board)
        print
