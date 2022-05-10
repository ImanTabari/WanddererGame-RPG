import random
import time
from GameActors import GameCharecters


class Hero(GameCharecters):
    def __init__(self, game):
        super().__init__(game)
        self.actor_current_position = [0, 0]
        self.health = 20 + 3 * random.randint(1, 6)
        self.defence = 2 * random.randint(1, 6)
        self.strike = 5 + random.randint(1, 6)
        self.maxhealth = self.health
        self.game.heroImg = self.game.hero_downImg
        self.level = 1

    def change_BoardMap_Stat(self, X, Y):
        x, y = self.actor_current_position
        if self.move_validity(x+X,  y+Y):
            self.game.board_map[x][y] = self.game.FloorInMap
            self.actor_next_position = [x+X, y+Y]
            x, y = self.actor_next_position
            self.game.board_map[x][y] = self.game.HeroInMap
            self.actor_current_position = self.actor_next_position
            self.last_move = time.time()

    def move_hero(self, event):
        if time.time() - self.last_move > 0.4:
            if event.keysym == 'Left':
                self.game.heroImg = self.game.hero_leftImg
                self.change_BoardMap_Stat(0, -1)
            elif event.keysym == 'Right':
                self.game.heroImg = self.game.hero_rightImg
                self.change_BoardMap_Stat(0, 1)
            elif event.keysym == 'Up':
                self.game.heroImg = self.game.hero_upImg
                self.change_BoardMap_Stat(-1, 0)
            elif event.keysym == 'Down':
                self.game.heroImg = self.game.hero_downImg
                self.change_BoardMap_Stat(1, 0)

    def hero_levelup(self):
        healup = random.randint(1, 6)
        self.health += healup
        self.maxhealth += healup
        self.defence += random.randint(1, 6)
        self.strike += random.randint(1, 6)
        self.level += 1


class HeroNextLevel(Hero):
    def __init__(self, game, level, health, maxhealth, defence, strike):
        super().__init__(game)
        self.level = level
        self.health = health
        self.maxhealth = maxhealth
        self.defence = defence
        self.strike = strike

    # def health_in_new_map(self):

    #     a = random.choices([health, health, health], cum_weights=(50, 40, 10), k=1)
