# code up here runs outside of the class,
# so a cyclic or circular import error occurs
# if both classes try to import each other up here!

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        Result.all.append(self)
    
    def __repr__ (self):
        return f"{{'player':{self.player} 'game':{self.game} 'score':{self.score}}}"

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if type(score) is int:
            if score in range(1, 5001):
                self._score = score
            else:
                raise Exception("Score must be in the range of 1 to 5000")
        else:
            raise TypeError("Score must be integer")


    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        from classes.player import Player
        if type(player) is Player:
            self._player = player
        else:
            raise Exception

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        from classes.game import Game
        if type(game) is Game:
            self._game = game
        else:
            raise Exception