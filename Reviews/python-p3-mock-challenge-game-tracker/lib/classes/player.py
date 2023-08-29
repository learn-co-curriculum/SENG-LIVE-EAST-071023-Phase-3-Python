from classes.result import Result


class Player:
    all = []

    def __init__(self, username):
        self.username = username

        Player.all.append(self)
    
    def __repr__(self):
        return f"{{username:{self.username}}}"

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if type(username) is str:
            if 2 <= len(username) <= 16:
                self._username = username
            else:
                raise Exception("Username must be between 2 and 16 characters.")
        else:
            raise TypeError("Username must be string")

    def results(self):
        #Returns a list of Result instances 
        # associated with the Player instance.
        # Single Source of Truth
        return [result for result in Result.all if result.player is self]

    def games_played(self):
        return list(set([result.game for result in self.results()]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        all_games_i_have_played = [result.game for result in self.results()]
        return all_games_i_have_played.count(game)

    @classmethod
    def highest_scored(cls, game):
        if len(cls.all) == 0:
            return None
        best_player = cls.all[0]
        #start off assuming player 0 is the best

        for player in cls.all:
            #if this player has a better score
            if game.average_score(player) > game.average_score(best_player):
                #make them the new best player
                best_player = player
        
        return best_player
        

