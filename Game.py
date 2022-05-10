from tkinter import *


class Game:
    root = Tk()
    root.title('Wanderer Game')
    IMG_SIZE = 36
    WIDTH = 10 * IMG_SIZE
    HEIGHT = 10 * IMG_SIZE
    WallInMap = 'W'
    FloorInMap = 'F'
    SkeletonInMap = 'S'
    KeyskeletonInMap = 'KS'
    BossInMap = 'B'
    HeroInMap = 'H'
    board_map = list()
    canvas = Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()
    status = Label(root, text=None,
                   bd=1, relief=SUNKEN, anchor= CENTER)
    status.pack(side=BOTTOM, fill=X)

    imgdir = "images\\"

    def __init__(self, level):

        self.level = level
        self.load_image()
        self.board_init()

    def load_image(self):
        self.floorImg = PhotoImage(file=self.imgdir + "floor.png").subsample(2)
        self.wallImg = PhotoImage(file=self.imgdir + "wall.png").subsample(2)

        self.hero_downImg = PhotoImage(
            file=self.imgdir + "hero-down.png").subsample(2)
        self.hero_upImg = PhotoImage(
            file=self.imgdir + "hero-up.png").subsample(2)
        self.hero_rightImg = PhotoImage(
            file=self.imgdir + "hero-right.png").subsample(2)
        self.hero_leftImg = PhotoImage(
            file=self.imgdir + "hero-left.png").subsample(2)

        self.skeletonImg = PhotoImage(
            file=self.imgdir + "skeleton.png").subsample(2)
        self.keyskeletonImg = PhotoImage(
            file=self.imgdir + "key_skeleton.png").subsample(2)
        self.bossImg = PhotoImage(file=self.imgdir + "boss.png").subsample(2)

    def board_init(self):
        self.board_map = []
        if self.level < 4:
            map = open('map'+str(self.level)+'.txt')
        else:
            map = open('map1.txt')
        for line in map:
            line = line.split()
            self.board_map.append(line)
        return self.board_map

    def board_display(self):
        self.canvas.delete('all')
        for i in range(10):
            for j in range(10):
                if self.board_map[i][j] == self.FloorInMap:
                    self.canvas.create_image(
                        j * self.IMG_SIZE, i * self.IMG_SIZE, image=self.floorImg, anchor=NW)
                elif self.board_map[i][j] == self.WallInMap:
                    self.canvas.create_image(
                        j * self.IMG_SIZE, i * self.IMG_SIZE, image=self.wallImg, anchor=NW)
                elif self.board_map[i][j] == self.SkeletonInMap:
                    self.canvas.create_image(
                        j * self.IMG_SIZE, i * self.IMG_SIZE, image=self.floorImg, anchor=NW)
                    self.canvas.create_image(
                        j * self.IMG_SIZE, i * self.IMG_SIZE, image=self.skeletonImg, anchor=NW)
                elif self.board_map[i][j] == self.KeyskeletonInMap:
                    self.canvas.create_image(
                        j * self.IMG_SIZE, i * self.IMG_SIZE, image=self.floorImg, anchor=NW)
                    self.canvas.create_image(
                        j * self.IMG_SIZE, i * self.IMG_SIZE, image=self.keyskeletonImg, anchor=NW)
                elif self.board_map[i][j] == self.HeroInMap:
                    self.canvas.create_image(
                        j * self.IMG_SIZE, i * self.IMG_SIZE, image=self.floorImg, anchor=NW)
                    self.canvas.create_image(
                        j * self.IMG_SIZE, i * self.IMG_SIZE, image=self.heroImg, anchor=NW)
                elif self.board_map[i][j] == self.BossInMap:
                    self.canvas.create_image(
                        j * self.IMG_SIZE, i * self.IMG_SIZE, image=self.floorImg, anchor=NW)
                    self.canvas.create_image(
                        j * self.IMG_SIZE, i * self.IMG_SIZE, image=self.bossImg, anchor=NW)
