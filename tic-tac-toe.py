from tkinter import messagebox
from tkinter import *

# Create window
window = Tk()
window.title("Tic-Tac-Toe")

# Create Board
def game_board():
    for i in range(3):
        for j in range(3):
            btn = Button(window, text="", font=("Arial", 50), width=6, height=2, bg="lightblue", command=lambda row=i, col=j: handle_click(row, col))
            btn.grid(row=i, column=j, sticky="nesw")

game_board()

# Initialize variables
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# letter = input('Chose your letter ("O" or "X")': )
current_player = 1

# Handle button click
def handle_click(row, col):
    global current_player

    if board[row][col] == 0:
        if current_player == 1:
            board[row][col] = 'X'
            current_player = 2
        else:
            board[row][col] = 'O'
            current_player = 1

        button = window.grid_slaves(row=row, column=col)[0]
        button.config(text=board[row][col])

    check_for_winner()

# Check the winner
def check_for_winner():
    winner = None

    # Check in rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != 0:
            winner = row[0]
            break
    
    # Check in columns
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col] and board[0][col]!=0:
            winner = board[0][col]
            break

    # Check in diagonals
    if (board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0]) and board[1][1] != 0:
        winner = board[1][1]

    if all([all(row) for row in board]) and winner is None:
        winner = "Tie"
    
    if winner:
        declare_winner(winner)
        
# Declare the winner and ask for play again
def declare_winner(winner):
    if winner == "Tie":
        message = "It's a Tie!"
    else:
        message = f"Player {winner} wins!"

    answer = messagebox.askyesno("Game over!", message + " Play Again!")

    if answer:
        global current_player
        global board
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        current_player = 1

        for i in range(3):
            for j in range(3):
                button = window.grid_slaves(row=i, column=j)[0]
                button.config(text = '')
    else:
        window.quit()  

window.mainloop()