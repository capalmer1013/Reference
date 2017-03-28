import curses
import time
import random

class character:
    def __init__(self, x, y, icon="O"):
        self.x = x
        self.y = y
        self.nextX = 0
        self.nextY = 0
        self.icon = icon

    def moveX(self, magnitude):
        self.nextX += magnitude

    def moveY(self, magnitude):
        self.nextY += magnitude

    def draw(self, scr):
        scr.addch(self.y, self.x, " ")
        scr.addch(self.nextY, self.nextX, self.icon)
        self.x = self.nextX
        self.y = self.nextY

    def collision(self, listOfObjects):
        if (self.nextX, self.nextY) in listOfObjects:
            return True
        else:
            return False
    def undoMove(self):
        self.nextX = self.x
        self.nextY = self.y

class wall:
    def __init__(self, x, y, icon="X"):
        self.x = x
        self.y = y
        self.icon = icon

    def draw(self, scr):
        scr.addch(self.y, self.x, self.icon, curses.color_pair(1))

    def moved(self):
        return False

def main(scr):
    listOfObjects = []
    objectPos = []
    running = True
    scr.nodelay(1)
    scr.border()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
    max_y, max_x = scr.getmaxyx()
    player = character(2, 2, curses.ACS_DIAMOND)
    for _ in range(100):
        listOfObjects.append(wall(random.randint(2, max_x-1), random.randint(2, max_y-1),curses.ACS_BLOCK))

    for each in listOfObjects:
        each.draw(scr)
        objectPos.append((each.x, each.y))

    while running:
        c = scr.getch()
        if c == ord('q'):
            running = False
        elif c == curses.KEY_UP:
            player.moveY(-1)

        elif c == curses.KEY_DOWN:
            player.moveY(1)

        elif c == curses.KEY_RIGHT:
            player.moveX(1)

        elif c == curses.KEY_LEFT:
            player.moveX(-1)

        if player.collision(objectPos):
            player.undoMove()

        #time.sleep(.05)
        player.draw(scr)

        for each in listOfObjects:
            if each.moved():
                each.draw(scr)
                objectPos.remove((each.previousX, each.previousY))
                objectPos.append((each.x, each.y))

if __name__ == "__main__":
    curses.wrapper(main)
