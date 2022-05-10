import random
import time
from GameActors import GameCharecters


class Enemy(GameCharecters):
    def __init__(self, game):
        super().__init__(game)
        self.actor_previous_position = [None, None]
        self.enemy_level()
        self.health = 2*self.elevel*random.randint(1, 6)
        self.defence = self.elevel/2*random.randint(1, 6)
        self.strike = self.elevel*random.randint(1, 6)
        self.place_enemy_on_map()
        self.imgcode = self.game.SkeletonInMap

    def enemy_level(self):
        level = random.choices([self.game.level, self.game.level+1,
                                self.game.level+2], cum_weights=(50, 40, 10), k=1)
        self.elevel = int(level[0])
        return self.elevel

    def place_enemy_on_map(self):
        while True:
            x, y = [random.randint(0, 5), random.randint(0, 9)]
            if self.move_validity(x, y):
                self.actor_current_position = [x, y]
                self.game.board_map[x][y] = self.game.SkeletonInMap
                break
        return self.actor_current_position

    def find_avilable_moving_options(self):
        self.avl_crd = []
        x, y = self.actor_current_position
        self.crd = [[x+1, y], [x-1, y],
                    [x, y+1], [x, y-1]]
        for crd in self.crd:
            if self.move_validity(crd[0], crd[1]):
                self.avl_crd.append(crd)
        return self.avl_crd

    def find_next_move_cordinaation(self):
        self.find_avilable_moving_options()
        choicenum = random.randint(0, 100)
        if self.actor_previous_position == [None, None]:
            self.actor_next_position = random.choice(self.avl_crd)
        else:
            self.avl_crd.remove(self.actor_previous_position)
            if choicenum < 20 or len(self.avl_crd) == 0:
                self.actor_next_position = self.actor_previous_position
            else:
                self.actor_next_position = random.choice(self.avl_crd)
        return self.actor_next_position

    def conditionfunc(self, x, y):
        if not self.game.board_map[x][y] in [self.game.HeroInMap, self.game.BossInMap, self.game.KeyskeletonInMap]:
            return True

    def move_enemy(self):

        if time.time() - self.last_move > 0.8:
            self.find_next_move_cordinaation()
            x, y = self.actor_current_position
            if self.conditionfunc(x, y):
                self.game.board_map[x][y] = self.game.FloorInMap
            x, y = self.actor_next_position
            if self.conditionfunc(x, y):
                self.game.board_map[x][y] = self.imgcode
            self.actor_previous_position = self.actor_current_position
            self.actor_current_position = self.actor_next_position
            self.last_move = time.time()
