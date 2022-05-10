from tkinter import *
from GameActors import *
from Game import *
from Skeleton import *
from Keyskeleton import *
from Boss import *
from Hero import *


game = Game(1)
hero = Hero(game)
skeleton1 = Enemy(game)
skeleton2 = Enemy(game)
keyskeleton = KeyEnemy(game)
boss = BossEnemy(game)

enemys = [skeleton1, skeleton2, keyskeleton, boss]


def battle(event):
    for enemy in enemys:
        if hero.actor_current_position == enemy.actor_current_position:
            if hero.health > 0 and enemy.health > 0:
                hero.strike_value()
                enemy.strike_value()
                if hero.strikevalue > enemy.defence:
                    enemy.health -= (hero.strikevalue -
                                     enemy.defence)
                if enemy.health > 0 and enemy.strikevalue > hero.defence:
                    hero.health -= (enemy.strikevalue - hero.defence)
                if enemy.health <= 0:
                    hero.hero_levelup()
                    enemys.remove(enemy)


game.root.bind('<space>', battle)


def update_stt_lable():
    game.status['text'] = f'Hero (Level {hero.level}) HP:{hero.health}/{hero.maxhealth} | DP:{hero.defence} | SP{hero.strike} \nBoss (Level {boss.elevel}) HP:{boss.health} | DP:{boss.defence} | SP{boss.strike} \nKeyskeleton (Level {keyskeleton.elevel}) HP:{keyskeleton.health} | DP:{keyskeleton.defence} | SP{boss.strike} \nSkeleton1 (Level {skeleton1.elevel}) HP:{skeleton1.health} | DP:{skeleton1.defence} | SP{skeleton1.strike} \nSkeleton2 (Level {skeleton2.elevel}) HP:{skeleton2.health} | DP:{skeleton2.defence} | SP{skeleton2.strike}'


while True:
    game.board_display()
    update_stt_lable()
    game.root.bind('<Key>', hero.move_hero)
    for enemy in enemys:
        enemy.move_enemy()
    if keyskeleton.health <= 0 and boss.health <= 0:
        newlevel = game.level + 1
        game = Game(newlevel)
        skeleton1 = Enemy(game)
        skeleton2 = Enemy(game)
        keyskeleton = KeyEnemy(game)
        boss = BossEnemy(game)
        enemys = [skeleton1, skeleton2, keyskeleton, boss]
        hero = HeroNextLevel(game, hero.level, hero.health, hero.maxhealth,
                             hero.defence, hero.strike)
    game.root.update_idletasks()
    game.root.update()
