import random
from Skeleton import Enemy


class KeyEnemy(Enemy):
    def __init__(self, game):
        super().__init__(game)
        self.imgcode = self.game.KeyskeletonInMap

    def place_enemy_on_map(self):
        while True:
            x, y = [random.randint(5, 9), random.randint(0, 5)]
            if self.move_validity(x, y):
                self.actor_current_position = [x, y]
                self.game.board_map[x][y] = self.game.KeyskeletonInMap
                break
        return self.actor_current_position

    def conditionfunc(self, x, y):
        if not self.game.board_map[x][y] in [self.game.HeroInMap, self.game.BossInMap]:
            return True
