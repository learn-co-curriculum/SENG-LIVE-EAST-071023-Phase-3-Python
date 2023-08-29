from classes.result import Result


class Game:
    all = [] 

    def __init__(self, title):
        self.title = title

        Game.all.append(self)

    def __repr__(self):
        return f"{{title:{self.title}}}"
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not hasattr(self, 'title') and type(title) is str and len(title) > 0:
            #attribute has not been defined
            #and our string title, is valid
            self._title = title
        else:
            raise Exception

    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        from statistics import mean
        this_players_results = [result.score for result in self.results() if result.player is player]
        if len(this_players_results) == 0:
            return -1
        return round(mean(this_players_results), 2)

