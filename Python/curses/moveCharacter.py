import curses
import time


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
        scr.addstr(self.y, self.x, " ")
        scr.addstr(self.nextY, self.nextX, self.icon)
        self.x = self.nextX
        self.y = self.nextY

def main(scr):
    listOfObjects = []
    running = True
    scr.nodelay(1)
    scr.border()
    curses.curs_set(0)
    player = character(2, 2)

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

        #time.sleep(.05)
        player.draw(scr)


if __name__ == "__main__":
    curses.wrapper(main)
