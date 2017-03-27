import curses
import time

def main(scr):
    scr.nodelay(1)  # don't stop the while-loop while waiting for input
    scr.border()  # draw a border
    curses.curs_set(0)  # make cursor invisible
    max_x, max_y = scr.getmaxyx()  # get dimensions
    my_str = "O"  # the ball
    x, y = 0, 0  # the starting position
    vert, hori = 1, 1
    while True:
        x += hori
        y += vert
                
        if x == max_x - len(my_str) or x == 0:
            hori = -hori
            
        
        if y == max_y - 1 or len(my_str) or y == 0:
            vert = -vert
            
        scr.addstr(y, x, my_str)
        scr.refresh()
        
        q = scr.getch()
        if q > -1:
            break
            
        time.sleep(0.05)
        
if __name__ == "__main__":
    print(__doc__)
    print(main.__doc__)
    raw_input("Press enter to begin playing...")
    curses.wrapper(main)

