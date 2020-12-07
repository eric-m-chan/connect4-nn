import random
import copy
from const import *

def get_next_row(board, col):
        for i in range(NUM_ROW):
            if board[i][col] == EMPTY_VAL:
                return i
class Player:

    def __init__(self, value, strategy, model=None):
        self.value      = value
        self.strategy   = strategy
        self.model      = model

    def get_move(self, availableMoves, board):
        #pick a random move out of available moves
        if self.strategy == "random":
            return random.choice(availableMoves)

        elif self.strategy == "showstopper":
            boardCopy = copy.deepcopy(board)

            #checks if there is a column of 3
            for move in availableMoves:
                #check if height at least 3
                nextRow = get_next_row(boardCopy, move)
                if nextRow > 2:
                    #if 3 in a col of yours, place it
                    if boardCopy[nextRow-1][move] == self.value and boardCopy[nextRow-2][move] == self.value and boardCopy[nextRow-3][move] == self.value:
                        return move
                    #if 3 in a col of opponent, block it
                    elif boardCopy[nextRow-1][move] != self.value and boardCopy[nextRow-2][move] != self.value and boardCopy[nextRow-2][move] != self.value:
                        return move

            #check if there is a row of 3
            for move in availableMoves:
                if move > 2:
                    nextRow = get_next_row(boardCopy, move)
                    #if 3 in a row of yours, place it 
                    if boardCopy[nextRow-3][move] == self.value and boardCopy[nextRow-2][move] == self.value and boardCopy[nextRow-1][move] == self.value:
                        return move
                    #if 3 in a row of opponent, block it
                    elif boardCopy[nextRow-3][move] != self.value and boardCopy[nextRow-2][move] != self.value and boardCopy[nextRow-1][move] != self.value:
                        return move  

            #flips a coin - if 0, pick random
            #if 1 - pick highest column
            coin = random.randint(0, 1)
            if (coin == 0):
                return random.choice(availableMoves)
            
            else:
                #find highest column
                #highestColumn stores the move (column)
                #height stores the actual height
                highestColumn = availableMoves[0]
                height = get_next_row(boardCopy, availableMoves[0])
                
                for move in availableMoves:
                    tempHeight = get_next_row(boardCopy, move)
                    
                    if tempHeight > height:
                        highestColumn = move
                        height = tempHeight

                return highestColumn

        else:
            #use the keras neural network
            maxValue = 0
            bestMove = availableMoves[0]

            for move in availableMoves:
                boardCopy = copy.deepcopy(board)
                
                nextRow = get_next_row(boardCopy, move)
                boardCopy[nextRow][move] = self.value

                if self.value == PLAYER_1_VAL:
                    value = self.model.predict(boardCopy, 2)
                else:
                    value = self.model.predict(boardCopy, 0)

                if value > maxValue:
                    maxValue = value
                    bestMove = move
                
                return bestMove
    
    def get_player(self):
        return self.value

