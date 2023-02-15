from utils import randcell
import os
from map import TREE_BONUS

class Helicopter:
    def __init__(self, w, h):
        rc= randcell(w, h)
        rx, ry= rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.mxtank = 1
        self.tank = 0
        self.score = 0
        self.totalscore = 0
        self.total_score = 0
        self.lives = 20

    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if(nx >= 0 and ny >=0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

    def print_stats(self):
        print("💧 ", self.tank, "/", self.mxtank, sep="", end = "|")
        print("🏆", self.score,"/", self.total_score, end=" | ")
        print("💛", self.lives)

    def game_over(self):
        os.system("cls")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print()
        print("  GAME OWER, YOUR SCORE IS", self.total_score)
        print("        TREES SAVED -",int(self.total_score/TREE_BONUS))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        exit(0)

    def export_data(self):
        return {"score":self.score, "totalscore":self.total_score,
                "lives":self.lives,
                "x":self.x, "y":self.y,
                "tank":self.tank, "mxtank":self.mxtank}

    def import_data(self, data):
        self.x = data["x"] or 0
        self.y = data["y"] or 0
        self.tank = data["tank"] or 0
        self.mxtank = data["mxtank"] or 1
        self.lives = data["lives"] or 20
        self.score = data["score"] or 0
        self.total_score = data["totalscore"] or 0