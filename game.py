import os
import copy

#values that will be printed
PLAYER_1_PIECE  = '1'
PLAYER_2_PIECE  = '2'
#encoding of board values
EMPTY_VAL       = 0
PLAYER_1_VAL    = 1
PLAYER_2_VAL    = 2

GAME_STATE_DRAW = 3
GAME_NOT_OVER   = 4

#standard connect 4 board size
NUM_ROW = 6
NUM_COL = 7
EMPTY = ' '


class Game:
    def __init__(self):
        self.reset_board()

    def reset_board(self):
        #empty 2D array with size Row by Col
        self.board =[ [EMPTY_VAL for i in range(NUM_COL)] for j in range(NUM_ROW) ]

        self.boardHistory = []

    def print_board(self):
        for i in range(NUM_ROW):
            for j in range(NUM_COL):
                print("__", end='')
            
            print(os.linesep)

            for j in range(NUM_COL):
                if self.board[i][j] == PLAYER_1_VAL:
                    print(PLAYER_1_PIECE, end='')
                elif self.board[i][j] == PLAYER_2_VAL:
                    print(PLAYER_2_PIECE, end='')
                elif self.board[i][j] == EMPTY_VAL:
                    print(EMPTY, end='')
                print(" | ", end='')

            print(os.linesep)

            for j in range(NUM_COL):
                print("__", end='')

        print(os.linesep)

    #get remaining legal moves
    #moves are defined by columns - player selects column, piece automatically drops to next row
    def get_available_moves(self):
        availableMoves = []

        for j in range(NUM_COL):
            #if the topmost slot is empty, then it is a legal column
            if self.board[NUM_ROW-1][j] == EMPTY_VAL:
                availableMoves.append(j)
        
        return availableMoves

    def get_game_result(self):
        #Check horizontal locations for a win
        for i in range(NUM_ROW):
            for j in range(NUM_COL-3):
                if self.board[i][j] != EMPTY_VAL and self.board[i][j] == self.board[i][j+1] and self.board[i][j] == self.board[i][j+2] and self.board[i][j] == self.board[i][j+3]:
                    return self.board[i][j]
        #Check vertical locations for a win
        for i in range(NUM_ROW-3):
            for j in range(NUM_COL):
                if self.board[i][j] != EMPTY_VAL and self.board[i][j] == self.board[i+1][j] and self.board[i][j] == self.board[i+2][j] and self.board[i][j] == self.board[i+3][j]:
                    return self.board[i][j]
        #Check up-diagonals for a win
        for i in range(NUM_ROW-3):
            for j in range(NUM_COL-3):
                if self.board[i][j] != EMPTY_VAL and self.board[i][j] == self.board[i+1][j+1] and self.board[i][j] == self.board[i+2][j+2] and self.board[i][j] == self.board[i+3][j+3]:
                    return self.board[i][j]
        #Check down-diagonals for a win
        for i in range(3, NUM_ROW):
            for j in range(NUM_COL-3):
                if self.board[i][j] != EMPTY_VAL and self.board[i][j] == self.board[i-1][j+1] and self.board[i][j] == self.board[i-2][j+2] and self.board[i][j] == self.board[i-3][j+3]:
                    return self.board[i][j]

        #if no win, check if its a draw
        drawFound = True

        for j in range(NUM_COL):
            if self.board[NUM_ROW-1][j] == EMPTY_VAL:
                drawFound = False

        if drawFound:
            return GAME_STATE_DRAW
        else:
            return GAME_NOT_OVER

    def move(self, move, player):
        #drop piece
        for i in range(NUM_ROW):
            if self.board[i][move] == 0:
                nextRow = i
                break

        self.board[nextRow][move] = player
        self.boardHistory.append( copy.deepcopy(self.board) )

    def get_board_history(self):
        return self.boardHistory

    def get_board(self):
        return self.board

