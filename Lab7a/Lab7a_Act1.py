# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Gavin Lane Phillips
#               Ford Hideo Bennett
#               Noah Quinn Hillis
#               Josh Amgad Botros
#               Ian Robert Wiechers
# Section:      472/572
# Assignment:   Lab 6a
# Date:         10/5/2021
#

# Establish Global Variables
userInput = ""
isWhiteTurn = False
isValid = True
blackCount = 12
whiteCount = 12
grid = [['blank', 'black', 'blank', 'black', 'blank', 'black', 'blank', 'black'],
        ['black', 'blank', 'black', 'blank', 'black', 'blank', 'black', 'blank'],
        ['blank', 'black', 'blank', 'black', 'blank', 'black', 'blank', 'black'],
        ['blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank'],
        ['blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank'],
        ['white', 'blank', 'white', 'blank', 'white', 'blank', 'white', 'blank'],
        ['blank', 'white', 'blank', 'white', 'blank', 'white', 'blank', 'white'],
        ['white', 'blank', 'white', 'blank', 'white', 'blank', 'white', 'blank']]


# Creates the Grid from the List defined above
def establishGrid():
    for i in range(8):
        print("")
        for j in range(8):
            if grid[i][j] == "blank":
                print(".", end="")
            elif grid[i][j] == "black" or grid[i][j] == "kingBlack":
                print(chr(9675), end="")
            elif grid[i][j] == "white" or grid[i][j] == "kingWhite":
                print(chr(9679), end="")
        print(" ", end="")
    print("\n")


# When the user hasn't put stop, or either player has lost, the movement continues
while userInput != "stop" or blackCount <= 0 or whiteCount <= 0:
    # Makes the is valid variable. Used to not draw the grid if the player makes an invalid movement
    if isValid:
        establishGrid()
    isValid = True
    # Tests if the its the White or Black side turn
    if isWhiteTurn:
        print("It's White's turn.")
    else:
        print("It's Black's turn.")
    # Enter the row of the piece that the user wants to move, and stops if they enter stop
    userInput = input("What is the row piece would you like to move? (1-8) ")
    if userInput == "stop":
        break
    # Sets the row to the input - 1 and tests if the integer is out of bounds
    row = int(userInput) - 1
    if 0 > row or 7 < row:
        print("This row is out of range.")
        isValid = False
        continue
    # Enter the column of the piece that the user wants to move, and stops if they enter stop
    userInput = input("What is the column piece would you like to move? (1-8) ")
    if userInput == "stop":
        break
    # Sets the column to the the input - 1 and tests if the integer is out of bounds
    column = int(userInput) - 1
    if 0 > column or 7 < column:
        print("This column is out of range.")
        isValid = False
        continue
    # Checks if the user has has attempted to move a blank space
    if grid[row][column] == 'blank':
        print("There is no piece here. Please enter a valid space.")
        isValid = False
        continue
    # Check if the user selected the piece of an opposing side
    if ((grid[row][column] == 'black' or grid[row][column] == 'kingBlack') and isWhiteTurn) or ((grid[row][column] == 'white' or grid[row][column] == 'kingWhite') and not isWhiteTurn):
        print("It isn't this sides turn. Please enter a valid space.")
        isValid = False
        continue
    # Enter the row of the space the piece wants to move to, and stops if the user enters stop
    userInput = input("On which row is the space you want to move or piece you wish to jump? (1-8) ")
    if userInput == "stop":
        break
    # Sets the movement Row to the input - 1, and checks if the space is out of bounds
    moveRow = int(userInput) - 1
    if 0 > moveRow or 7 < moveRow:
        print("This row is out of range.")
        isValid = False
        continue
    # Enter the column of the space the piece wants to move to, and stops if the user enters stop
    userInput = input("On which column is the space you want to move or piece you wish to jump? (1-8) ")
    if userInput == "stop":
        break
    # Sets the movement column to the input = 1, and checks if the space is out of bounds
    moveColumn = int(userInput) - 1
    if 0 > moveColumn or 7 < moveColumn:
        print("This column is out of range.")
        isValid = False
        continue
    # Checks if the user isn't moving diagonally
    if abs(moveColumn - column) != 1 or abs(moveRow - row) != 1:
        print("This space is too far away.")
        isValid = False
        continue
    # Checks if the piece is moving back towards their sides if they are not kinged
    if (isWhiteTurn and grid[row][column] != "kingWhite" and moveRow - row > 0) or (not isWhiteTurn and grid[row][column] != "kingBlack" and moveRow - row < 0):
        print("You cannot move backwards until you are kinged.")
        isValid = False
        continue
    # Checks if the user is trying to move on the space of their own piece
    if (isWhiteTurn and (grid[moveRow][moveColumn] == "white" or grid[moveRow][moveColumn] == "kingWhite")) or (not isWhiteTurn and (grid[moveRow][moveColumn] == "black" or grid[moveRow][moveColumn] == "kingBlack")):
        print("You cannot move on your own space.")
        isValid = False
        continue
    # Establishes the jump row and column, and gets the piece that the user is moving
    jumpRow = moveRow
    jumpColumn = moveColumn
    pieceID = grid[row][column]
    # Checks if the player isn't moving onto a blank space (They are moving on top of an enemy piece)
    if grid[moveRow][moveColumn] != 'blank':
        # Sets the jump row to the space past the piece, and checks if it is out of bounds
        jumpRow = moveRow + (moveRow - row)
        if 0 > jumpRow or 7 < jumpRow:
            print("You cannot jump this piece.")
            isValid = False
            continue
        # Sets the jump column to the space past the piece, and checks if it is out of bounds
        jumpColumn = moveColumn + (moveColumn - column)
        if 0 > jumpColumn or 7 < jumpColumn:
            print("You cannot jump this piece.")
            isValid = False
            continue
        # Checks if the next jump will cause the player to end up on another piece
        if grid[jumpRow][jumpColumn] != "blank":
            print("You cannot jump this piece.")
            isValid = False
            continue
        # Removes the piece from its original space and moves it to the jump space, and removes the jumped piece
        grid[row][column] = "blank"
        grid[moveRow][moveColumn] = "blank"
        grid[jumpRow][jumpColumn] = pieceID
        # Removes a piece from the count
        if isWhiteTurn:
            blackCount -= 1
        else:
            whiteCount -= 1
        # Checks if the piece moved to the other side of the board
        if grid[jumpRow][jumpColumn] == 'black' and jumpRow == 7:
            grid[jumpRow][jumpColumn] = 'kingBlack'
            print("Your piece has been kinged")
        if grid[jumpRow][jumpColumn] == 'white' and jumpRow == 0:
            grid[jumpRow][jumpColumn] = 'kingWhite'
            print("Your piece has been kinged")
    # Runs if the user is going to a blank space
    else:
        # Removes the piece from its original location, and moves it
        grid[row][column] = "blank"
        grid[moveRow][moveColumn] = pieceID
        # Checks if the piece moved to the other side of the board
        if grid[moveRow][moveColumn] == 'black' and moveRow == 7:
            grid[moveRow][moveColumn] = 'kingBlack'
            print("Your piece has been kinged")
        if grid[moveRow][moveColumn] == 'white' and moveRow == 0:
            grid[moveRow][moveColumn] = 'kingWhite'
            print("Your piece has been kinged")
    # Switches the turn to the other side
    if isWhiteTurn:
        isWhiteTurn = False
    else:
        isWhiteTurn = True

# Checks if the white count is higher, and the black count is 0 or less
if whiteCount > blackCount and blackCount <= 0:
    print("White wins with", whiteCount, "pieces left on the board")
# Checks if the black count is higher, and the white count is 0 or less
elif whiteCount < blackCount and whiteCount <= 0:
    print("Black wins with", blackCount, "pieces left on the board")
else:
    print("The game was stopped with", blackCount, "black pieces left and", whiteCount, "white pieces left.")
