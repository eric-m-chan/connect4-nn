from game import Game
from player import Player
from controller import Controller
from model import Model
from const import *

if __name__ == "__main__":
    firstGame = Game()
    p1Random = Player(PLAYER_1_VAL, strategy='random')
    p2Random = Player(PLAYER_2_VAL, strategy='random')
    p1ShowStopper = Player(PLAYER_1_VAL, strategy='showstopper')
    p2ShowStopper = Player(PLAYER_2_VAL, strategy='showstopper')

    control = Controller(firstGame, p1Random, p2Random)
    print("Playing with two random players")
    control.simulate_games(2000)

    model = Model(NUM_ROW * NUM_COL, 3, 21, 100)
    model.train(control.get_training_history())
    
    p1Neural = Player(PLAYER_1_VAL, strategy='model', model=model)
    p2Neural = Player(PLAYER_2_VAL, strategy='model', model=model)

    '''
    secondGame = Game()
    p2Neural = Player(PLAYER_2_VAL, strategy='model', model=model)
    control = Controller(secondGame, p1Random, p2Neural)
    print("Playing with one neural player and one random player")
    control.simulate_games(1000)
    
    thirdGame = Game()
    p1Neural = Player(PLAYER_1_VAL, strategy='model', model=model)
    p2Neural = Player(PLAYER_2_VAL, strategy='model', model=model)
    control = Controller(thirdGame, p1Neural, p2Neural)
    print("Playing with two neural players")
    control.simulate_games(1000)
    '''

    fourthGame = Game()
    control = Controller(fourthGame, p1Neural, p2Random)
    print("Playing with Player 1 as Neural and Player 2 as Random")
    control.simulate_games(1000)
