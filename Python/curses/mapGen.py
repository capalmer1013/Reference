import curses
import random
import math

seedSize = 32
seed = '{0:032b}'.format(random.getrandbits(64))


def generateColor(x, y, colors):
    # pretty reasonable
    # need to make the
    if x:
        x = x % math.sqrt(x)
    if y:
        y = y % math.sqrt(y)

    center = (x*y) % seedSize
    top = x * -y
    left = -x * y
    right = ((x+1)*y) % seedSize
    bottom = (x*(y+1)) % seedSize

    dirList = [int(center), int(top), int(left), int(right), int(bottom)]
    minN = 0
    maxN = curses.COLORS

    for i in dirList:
        if seed[i % seedSize] == '1':
            minN = int((maxN + minN)/2)
        else:
            max = int((maxN + minN)/2)

    return int((maxN + minN)/2)

def main(scr):
    scr.nodelay(1)
    scr.border()
    scr.timeout(1)
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)

    for i in range(0, curses.COLORS):
        curses.init_pair(i+1, i, -1)

    max_y, max_x = scr.getmaxyx()
    print "max", max_x, max_y
    for i in range(max_y-1):
        for j in range(max_x):
            scr.addstr(i, j, '+', curses.color_pair(generateColor(j, i, curses.COLORS)))

    running = True
    while running:
        c = scr.getch()
        if c == ord('q'):
            running = False

if __name__ == "__main__":
    curses.wrapper(main)
