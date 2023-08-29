#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    ttt = Game("Tic Tac Toe")
    csgo = Game("Counter Strike Global Offensive")

    animal_crossing = Game("Animal Crossing")

    thomas = Player("Smart Dog")
    curtis = Player("Sad Cow")
    breelle = Player("braillejord")

    # rand_nums = [ 3, 2, 3, 4, 2.0, 3.2]
    # num_player = Player(rand_nums) # this throws Exception now

    r1 = Result(thomas, ttt, 5000)
    r2 = Result(thomas, csgo, 50)
    r3 = Result(breelle, animal_crossing, 3020)
    r4 = Result(thomas, csgo, 60)
    r5 = Result(thomas, csgo, 48)
    
    ipdb.set_trace()
