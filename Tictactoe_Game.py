import random

#Variables
#Main game loop
playingGame = 1

#Tictactoe game loop
startingGame = 0

#Tictactoe board array
boardArr = ["1","2","3","4","5","6","7","8","9"]

#Player Turn
playerTurn = 1

#Check if players action is correct
switchPlayer = -1

#Total turns of all players
totalPlayerTurns = 0

#Error checks in choosing human or computer
errorTypeCheck1 = 0

#Functions
def showBoard():
    #Start counting from the first index of the array
    sType = 1
    while sType <= 9:
        print(boardArr[sType-1],"|", end='') #Print the boxes, sType-1 since array starts with 0
        if(sType % 3 == 0): #If the counting is divisible by 3 then add a new line(since the are only 3 boxes per row)
            print("")
            print("---------")
        sType += 1 #proceed to the next index of the array

def placeTurn(loc, player): #Give the function the location of the turn and the player
    if loc.isdigit():
        #check if the numbers are between 1-9
        loc = int(loc)
        if loc > 9 or loc < 1:
            print("Please enter numbers between 1-9")
            global switchPlayer
            switchPlayer = -1
            return
    else:
        #check if the entered value is an integer
        print("Please enter numbers between 1-9")
        switchPlayer = -1
        return
    
    #If the choosen location has already a place
    if boardArr[loc-1] == "X" or boardArr[loc-1] == "O":
        print("Place already set! Please choose another number!")
        switchPlayer = -1
    else:
    #if no errors then place the turn
        switchPlayer = 0
        if player == 1:
            boardArr[loc-1] = "X"
        else:
            boardArr[loc-1] = "O"
    global totalPlayerTurns
    totalPlayerTurns += 1 #add the total player turns

def checkWin():
    #if playerWinner is 0, it is tie
    #if playerWinner is 1, then player 1 wins
    #if 2 then player 2 wins
    
    playerWinner = 0
    
    #Player 1
    shape = "X"
    
    #Horizontal Win Check
    if boardArr[0] == shape and boardArr[1] == shape and boardArr[2] == shape: playerWinner = 1
    if boardArr[3] == shape and boardArr[4] == shape and boardArr[5] == shape: playerWinner = 1
    if boardArr[6] == shape and boardArr[7] == shape and boardArr[8] == shape: playerWinner = 1

    #Vertical Win Check
    if boardArr[0] == shape and boardArr[3] == shape and boardArr[6] == shape: playerWinner = 1
    if boardArr[1] == shape and boardArr[4] == shape and boardArr[7] == shape: playerWinner = 1
    if boardArr[2] == shape and boardArr[5] == shape and boardArr[8] == shape: playerWinner = 1

    #Diagonal Win Check
    if boardArr[0] == shape and boardArr[4] == shape and boardArr[8] == shape: playerWinner = 1
    if boardArr[2] == shape and boardArr[4] == shape and boardArr[6] == shape: playerWinner = 1

    #Player 2
    shape = "O"
    
    #Horizontal Win Check
    if boardArr[0] == shape and boardArr[1] == shape and boardArr[2] == shape: playerWinner = 2
    if boardArr[3] == shape and boardArr[4] == shape and boardArr[5] == shape: playerWinner = 2
    if boardArr[6] == shape and boardArr[7] == shape and boardArr[8] == shape: playerWinner = 2

    #Vertical Win Check
    if boardArr[0] == shape and boardArr[3] == shape and boardArr[6] == shape: playerWinner = 2
    if boardArr[1] == shape and boardArr[4] == shape and boardArr[7] == shape: playerWinner = 2
    if boardArr[2] == shape and boardArr[5] == shape and boardArr[8] == shape: playerWinner = 2

    #Diagonal Win Check
    if boardArr[0] == shape and boardArr[4] == shape and boardArr[8] == shape: playerWinner = 2
    if boardArr[2] == shape and boardArr[4] == shape and boardArr[6] == shape: playerWinner = 2

    global startingGame
    if playerWinner == 1:
        print("PLAYER 1 WINS!")
        showBoard()
        startingGame = 0 #End the game
    if playerWinner == 2:
        print("PLAYER 2 WINS!")
        showBoard()
        startingGame = 0 #End the game
        
    #if all the board is placed and there is no winner, then it is a tie
    if totalPlayerTurns == 9 and playerWinner == 0:
        print("Its a tie!!")
        showBoard()
        startingGame = 0 #End the game

def resetVariables():
    global playingGame, startingGame, boardArr, playerTurn, switchPlayer, totalPlayerTurns, errorTypeCheck1
    playingGame = 1
    startingGame = 0
    boardArr = ["1","2","3","4","5","6","7","8","9"]
    playerTurn = 1
    switchPlayer = -1
    totalPlayerTurns = 0
    errorTypeCheck1 = 0

#Main Loop
while playingGame == 1:

    #if playerType is 0, human vs human
    #if 1, comp vs human
    playerType = -1

    #the selected place turn of the player
    playerChoose = -1
    
    print("Tic-tac-toe Game")
    playerType = input("Enter 0 for human vs human and 1 for Computer vs human: ")
    
    if playerType == "0":
        errorTypeCheck1 = 0
        startingGame = 1
        print("Human vs Human")
        
        while startingGame == 1: #Nested loop
            showBoard()
            print("Player", playerTurn, ": ")
            #Ask for the turn
            playerChoose = input("Please choose a number to place your mark: ")
            placeTurn(playerChoose, playerTurn)

            #If the player is good to switch turn with player 2 or 1, then switch
            if switchPlayer == 0:
                if playerTurn == 1:
                    playerTurn = 2
                elif playerTurn == 2:
                    playerTurn = 1
            checkWin()
            
    elif playerType == "1":
        errorTypeCheck1 = 0
        startingGame = 1
        print("Computer vs Human")
        
        while startingGame == 1: #Nested loop
            showBoard()
            print("Player", playerTurn, ": ", end='')

            if playerTurn == 1:
                playerChoose = input("Please choose a number to place your mark: ")
            else:
                playerChoose = str(random.randint(1,9)) #computer will choose a number between 1-9, convert it to string since there will be a checker and str to int converter
                print(playerChoose)
                #if the random number has already a place, then continue to choose a random number until there is none placed on the selected place
                while boardArr[int(playerChoose)-1] == "X" or boardArr[int(playerChoose)-1] == "O":
                    playerChoose = str(random.randint(1,9))
            
            placeTurn(playerChoose, playerTurn)
            
            #If the player is good to switch turn with player 2 or 1, then switch
            if switchPlayer == 0:
                if playerTurn == 1:
                    playerTurn = 2
                elif playerTurn == 2:
                    playerTurn = 1
            checkWin()
    else:
        print("Please enter 0 or 1.")
        errorTypeCheck1 = 1

    #If no errors
    if errorTypeCheck1 == 0:
        #Game End
        playAgain = input("Do you want to play again? y/n: ")
        
        if playAgain == "n" or playAgain == "N":
            print("Thank you for playing! Goodbye!")
            playingGame = 0 #End the main loop
            
        if playAgain == "y" or playAgain == "Y":
            resetVariables()
            startingGame == 1 #Start again the nested loop
