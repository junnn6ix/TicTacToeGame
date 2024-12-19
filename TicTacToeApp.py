# import gui
import tkinter

def setTile(row, column):
    global currPlayer
    
    if (gameOver):
        return
    
    if board[row][column]["text"] != "":
        # already taken spot
        return
    
    board[row][column]["text"] = currPlayer # mark the board
    
    if currPlayer == playerO: # switch player
        currPlayer = playerX
    else:
        currPlayer = playerO
    
    label["text"] = "Giliran " + currPlayer
    
    # check the winner
    checkWinner()
        
def checkWinner():
    global turns, gameOver
    turns += 1
    
    # check 3 rows (horizontal)
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
        and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " adalah pemenangnya!", foreground=colorYellow)
            for column in range(3):
                board[row][column].config(foreground=colorYellow, background=colorLightGray)
            gameOver = True
            return
    # check 3 column (vertical)
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " adalah pemenangnya", foreground=colorYellow)
            for row in range(3):
                board[row][column].config(foreground=colorYellow, background=colorLightGray)
            gameOver = True
            return
    
    # diagonal
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " adalah pemenangnya", foreground=colorYellow)
        for i in range(3):
            board[i][i].config(foreground=colorYellow, background=colorLightGray)
        gameOver = True
        return
    
    # anti-diagonal
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " adalah pemenangnya", foreground=colorYellow)
        board[0][2].config(foreground=colorYellow, background=colorLightGray)
        board[1][1].config(foreground=colorYellow, background=colorLightGray)
        board[2][0].config(foreground=colorYellow, background=colorLightGray)
        gameOver = True
        return
    
    # tie
    if (turns == 9):
        gameOver = True
        label.config(text="Sama!", foreground=colorYellow)

def newGame():
    global turns, gameOver
    
    turns = 0
    gameOver = False
    
    label.config(text="Giliran " + currPlayer, foreground="white")
        
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=colorBlue, background=colorGray)

# game setup
playerX = "X"
playerO = "O"
currPlayer = playerX
board = [[0, 0, 0,],
         [0, 0, 0],
         [0, 0, 0]]

colorBlue = "#4584b6"
colorYellow = "#ffde57"
colorGray = "#343434"
colorLightGray = "#646464"

turns = 0
gameOver = False

# window setup
window = tkinter.Tk()
window.title("Tic Tac Toe Game by Kel. x")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = "Giliran " + currPlayer, font=("Consolas", 17), background=colorGray,
                      foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"), background=colorGray, foreground=colorBlue, width=4, height=1, command=lambda row=row, column=column: setTile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="Mulai Ulang", font=("Consolas", 17), background=colorGray, foreground="white", command=newGame)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# centering the window
window.update()
windowWidth = window.winfo_width()
windowHeight = window.winfo_height()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

windowX = int((screenWidth/2) - (windowWidth/2))
WindowY = int((screenHeight/2) - (windowHeight/2))

# format "(w)x(h)+(x)+(y)"
window.geometry(f"{windowWidth}x{windowHeight}+{windowX}+{WindowY}")

window.mainloop()