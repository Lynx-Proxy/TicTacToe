board = ["-", "-", "-","-", "-", "-","-", "-", "-"]

currentplayer = "X"
winner = None
gamerunning = True
inp = None

def printboard(board):
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board):
    global inp
    _inp = input("\nEnter a number from 1-9: ")
    if _inp != '':
        inp = int(_inp)
    else:
        print("\nDon't leave the field blank")
        playerInput(board)

    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentplayer
    elif inp > 9 or inp < 1:
            print("\nGive a number from 1 to 9")
            playerInput(board)
    else:
        print("\nOoops! spot taken")
        playerInput(board)

def switchPlayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
        print("\nIt's O's turn")
    elif currentplayer == "O":
        currentplayer = "X"
        print("\nIt's X's turn")

def runChecks(board):
    global gamerunning
    if (board[0]==board[1]==board[2] and board[2] != "-") or \
       (board[3]==board[4]==board[5] and board[5] != "-") or \
       (board[6]==board[7]==board[8] and board[7] != "-") or \
       (board[0]==board[3]==board[6] and board[3] != "-") or \
       (board[1]==board[4]==board[7] and board[4] != "-") or \
       (board[2]==board[5]==board[8] and board[2] != "-") or \
       (board[0]==board[4]==board[8] and board[4] != "-") or \
       (board[2]==board[4]==board[6] and board[4] != "-"):
        printboard(board)
        print(f"\n{currentplayer} wins!")
        gamerunning = False
    elif "-" not in board:
        printboard(board)
        print("\nIt's a tie!")
        gamerunning = False

def startGame():
    global gamerunning

    while gamerunning:
        printboard(board)
        playerInput(board)
        runChecks(board)
        if gamerunning:
            switchPlayer()

    playAgain = input("\nWill you play again [y/N]? ")

    if playAgain.lower() == "y":
        gamerunning = True
        startGame()
    elif playAgain.lower() == "n":
        quit()
    else:
        print("\nEnter either y or n")
        startGame()

startGame()


