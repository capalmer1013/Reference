import curses

# global screen object
stdscr = curses.initscr()
curses.start_color()

def initialize():
    # initialize application
    # can also call curses.wrapper() to safely initialize and deinitialize
    global stdscr
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)


def cleanup():
    # end application
    global stdscr
    curses.nocbreak();
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()


def main():
    global stdscr
    running = True
    initialize()
    curses.beep()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_CYAN)
    #stdscr.addstr(0,0,"currentMode: typing mode", curses.A_UNDERLINE)
    #stdscr.addstr(0,1,"Pretty Text", curses.color_pair(1))
    stdscr.addstr(0,0, "RED ALERT!", curses.color_pair(1))
    while running:
        c = stdscr.getch()
        stdscr.refresh()
        if c == ord('p'):
            print "hello"
        elif c == ord('q'):
            running = False

    cleanup()

if __name__ == "__main__":
    main()
