import curses

# global screen object
stdscr = curses.initscr()

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
    while running:
        c = stdscr.getch()
        if c == ord('p'):
            print "hello"
        elif c == ord('q'):
            running = False

    cleanup()

if __name__ == "__main__":
    main()
