import copy
from const import *

class Controller:

    def __init__(self, game, player1, player2):
        self.game               = game
        self.player1            = player1
        self.player2            = player2
        self.trainingHistory    = []

    def simulate_games(self, numGames):
        p1Wins = 0
        p2Wins = 0
        draws  = 0

        for i in range(numGames):
            self.game.reset_board()
            self.play_game()

            if self.game.get_game_result() == PLAYER_1_VAL:
                p1Wins += 1
            elif self.game.get_game_result() == PLAYER_2_VAL:
                p2Wins += 1
            elif self.game.get_game_result() == GAME_STATE_DRAW:
                draws += 1
            
            #print every 200 games
            if i % 200 == 0:
                if self.game.get_game_result() == PLAYER_1_VAL:
                    print("Player 1 wins")
                elif self.game.get_game_result() == PLAYER_2_VAL:
                    print("Player 2 wins")
                elif self.game.get_game_result() == GAME_STATE_DRAW:
                    print("Draw")
                self.game.print_board()

        print("Player 1 Wins: " + str(int(p1Wins * 100 / numGames)) + "%")
        print("Player 2 Wins: " + str(int(p2Wins * 100 / numGames)) + "%")
        print("Draws: " + str(int(draws * 100 / numGames)) + "%")

    def play_game(self):
        playerToMove = self.player1

        #play until someone wins or a draw
        while self.game.get_game_result() == GAME_NOT_OVER:
            availableMoves = self.game.get_available_moves()
            move = playerToMove.get_move(availableMoves, self.game.get_board())
            self.game.move(move, playerToMove.get_player())

            if playerToMove == self.player1:
                playerToMove = self.player2
            else:
                playerToMove = self.player1

        #record who won and a copy of the board
        for item in self.game.get_board_history():
            self.trainingHistory.append( (self.game.get_game_result(), copy.deepcopy(item)) )

    def get_training_history(self):
        return self.trainingHistory
