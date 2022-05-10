import random
import time


class GameCharecters:

    last_move = time.time()

    def __init__(self, game):
        self.game = game
        self.actor_current_position = [None, None]
        self.actor_next_position = [None, None]
        self.health = None
        self.defence = None
        self.strike = None
        self.strikevalue = None

    def move_validity(self, x, y):
        if x in range(0, 10) and y in range(0, 10) and self.game.board_map[x][y] != self.game.WallInMap:
            return True

    def strike_value(self):
        self.strikevalue = self.strike + 2*random.randint(1, 6)
        return self.strikevalue
