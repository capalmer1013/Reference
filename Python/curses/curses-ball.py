import curses
import time
import random


class ball:
    def __init__(self, x, y):
        self.x =  random.randint(2, x-2)
        self.y =  random.randint(2, y-2)
        self.vert = 1
        self.hori = 1
        self.lastX = 1
        self.lastY = 1

def main(scr):
    scr.nodelay(1)  # don't stop the while-loop while waiting for input
    scr.border()  # draw a border
    curses.curs_set(0)  # make cursor invisible
    max_y, max_x = scr.getmaxyx()  # get dimensions
    my_str = "O"  # the ball
    listOfBalls = []
    temp = ball(max_x, max_y)
    listOfBalls.append(temp)

    while True:
        listOfBallPos = []
        for each in listOfBalls:
            each.lastX = each.x
            each.lastY = each.y
            each.x += each.hori
            each.y += each.vert

            if each.x == max_x - 2 or each.x == 1:
                each.hori = -each.hori
                listOfBalls.append(ball(max_x, max_y))


            if each.y == max_y - 2 or each.y == 1:
                each.vert = -each.vert
                listOfBalls.append(ball(max_x, max_y))

            scr.addstr(each.y, each.x, my_str)
            scr.refresh()


        q = scr.getch()
        if q > -1:
            break
        time.sleep(0.01)

        for each in listOfBalls:
            scr.addstr(each.lastY, each.lastX, " ")

if __name__ == "__main__":
    curses.wrapper(main)

