import random
from Skeleton import Enemy


class BossEnemy(Enemy):
    def __init__(self, game):
        super().__init__(game)
        self.health = 2*self.enemy_level()*random.randint(1, 6) + random.randint(1, 6)
        self.defence = self.enemy_level()/2*random.randint(1, 6) + random.randint(1, 6)
        self.strike = self.enemy_level()*random.randint(1, 6) + + random.randint(1, 6)
        self.imgcode = self.game.BossInMap

    def place_enemy_on_map(self):
        while True:
            x, y = [random.randint(5, 9), random.randint(5, 9)]
            if self.move_validity(x, y):
                self.actor_current_position = [x, y]
                self.game.board_map[x][y] = self.game.BossInMap
                break
        return self.actor_current_position

    def conditionfunc(self, x, y):
        if self.game.board_map[x][y] != self.game.HeroInMap:
            return True
