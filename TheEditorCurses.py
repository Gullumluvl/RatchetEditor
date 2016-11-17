#!/usr/bin/env python2.7

# TODO:
# reach the bottom of the window and avoid ERR


import curses

HEADER = ("    This is the ONLY USEFUL EDITOR. "
          "When you're here, you can't go back\n")

def writelineno():
    global lineno
    try:
        lineno += 1
    except NameError:
        lineno = 1
    stdscr.addstr('%3s' % lineno, curses.A_REVERSE)
    stdscr.addch(' ')


#my_return_key = ''

stdscr = curses.initscr()
try:
    stdscr.addstr(0, 0, HEADER,
                  curses.A_REVERSE)
    writelineno()
    stdscr.refresh()
    curses.noecho()
    stdscr.keypad(1)
    while 1:
        ch = stdscr.getch()
        if ch == 4: # Ctrl-D
            break
        elif ch in [curses.KEY_ENTER, 10, 13]:
            stdscr.addch('\n')
            #my_return_key = ch
            writelineno()
        elif ch < 256:
            stdscr.addch(ch)

    # Terminate ncurse application
finally:
    curses.nocbreak(); stdscr.keypad(0); curses.echo()
    curses.endwin()
    #print "Return key: %r" % my_return_key  ### It's 10.
