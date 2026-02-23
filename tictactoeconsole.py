board = [" " for _ in range(9)]

def p_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def c_winner(p):
    win = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    
    for pos in win:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == p:
            return True
    return False

def draw():
    return " " not in board

def play_game():
    cp = "X"
    
    while True:
        p_board()
        try:
            move = int(input(f"Player {cp}, choose position (1-9): ")) - 1
            
            if move < 0 or move > 8:
                print("Invalid position! Choose 1-9.")
                continue
                
            if board[move] != " ":
                print("Spot already taken! Try again.")
                continue
            
            board[move] = cp
            
            if c_winner(cp):
                p_board()
                print(f"🎉 Player {cp} wins!")
                break
            
            if draw():
                p_board()
                print("It's a draw!")
                break
            
            cp = "O" if cp == "X" else "X"
        
        except ValueError:
            print("Please enter a valid number.")

play_game()
