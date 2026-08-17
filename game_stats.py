class GameStats:
    def __init__(self,ai_game):
        self.setting = ai_game.setting
        self.reset_stats()
        self.high_score = self.read_high_score()
    def reset_stats(self):
        self.ships_left = self.setting.ship_limit
        self.score = 0
        self.level = 1
    def read_high_score(self):
        try:
            with open('the_best_achievement.txt','r') as f:
                contents = f.read().strip()
                if contents:
                    return int(contents)
                else:
                    return 0
        except FileNotFoundError:
            return 0
        except ValueError:
           return 0