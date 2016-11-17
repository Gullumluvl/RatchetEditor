#!/usr/bin/env python2.7


import sys


def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch

ESC = '\x1b'

USELESS_KEYS = {
    'up'            : '\x1b\x5b\x41',
    'down'          : '\x1b\x5b\x42',
    'left'          : '\x1b\x5b\x44',
    'right'         : '\x1b\x5b\x43',
    'page_up'       : '\x1b\x5b\x35\x7e',
    'page_down'     : '\x1b\x5b\x36\x7e',
    'home'          : '\x1b\x5b\x48',
    'end'           : '\x1b\x5b\x46',
    'cr'            : '\x0a',
    'insert'        : '\x1b\x5b\x32\x7e',
    'suppr'         : '',
    'suppr2'        : '\x1b\x5b\x33\x7e',
    'backspace'     : '\x7f',
#    'esc'           : ESC,
    'ctrl_a'        : '\x01',
    'ctrl_b'        : '\x02',
    'ctrl_c'        : '\x03',
    'ctrl_d'        : '\x04',
    'ctrl_e'        : '\x05',
    'ctrl_f'        : '\x06',
    'ctrl_z'        : '\x1a',
    'alt_a'         : '\x1b\x61',
    'ctrl_alt_a'    : '\x1b\x01',
    'ctrl_alt_supr' : '\x1b\x5b\x33\x5e',
    'F1'            : '\x1b\x4f\x50',
    'F2'            : '\x1b\x4f\x51',
    'F3'            : '\x1b\x4f\x52',
    'F4'            : '\x1b\x4f\x53',
    'F5'            : '\x1b\x4f\x31\x35\x7e',
    'F6'            : '\x1b\x4f\x31\x37\x7e',
    'F7'            : '\x1b\x4f\x31\x38\x7e',
    'F8'            : '\x1b\x4f\x31\x39\x7e',
    'F9'            : '\x1b\x4f\x32\x30\x7e',
    'F10'           : '\x1b\x4f\x32\x31\x7e',
    'F11'           : '\x1b\x4f\x32\x33\x7e',
    'F12'           : '\x1b\x4f\x32\x34\x7e',
}

OTHER_KEYS = ['[A', '[B', '[D', '[C', 'OH', 'OF', '[6~', '[5~', '[3~', '[2~']

#ESCAPE_SEQUENCES = [
#    ESC,
#    ESC + '\x5b',
#    ESC + '\x5b' + '\x31',
#    ESC + '\x5b' + '\x32',
#    ESC + '\x5b' + '\x33',
#    ESC + '\x5b' + '\x35',
#    ESC + '\x5b' + '\x36',
#    ESC + '\x5b' + '\x31' + '\x35',
#    ESC + '\x5b' + '\x31' + '\x36',
#    ESC + '\x5b' + '\x31' + '\x37',
#    ESC + '\x5b' + '\x31' + '\x38',
#    ESC + '\x5b' + '\x31' + '\x39',
#    ESC + '\x5b' + '\x32' + '\x30',
#    ESC + '\x5b' + '\x32' + '\x31',
#    ESC + '\x5b' + '\x32' + '\x32',
#    ESC + '\x5b' + '\x32' + '\x33',
#    ESC + '\x5b' + '\x32' + '\x34',
#    ESC + '\x4f',
#    ESC + ESC,
#    ESC + ESC + '\x5b',
#    ESC + ESC + '\x5b' + '\x32',
#    ESC + ESC + '\x5b' + '\x33',
#]

getch = _find_getch()

print "\033[1;31m\033[40mThis is THE ONLY USEFUL TEXT EDITOR. Enter your text below.\033[0m"

def writelineno():
    global lineno
    try:
        lineno += 1
    except NameError:
        lineno = 1
    sys.stdout.write('\033[40m\033[1;30m%-3s\033[0m\033[0m' % lineno)

writelineno()

while 1:
    ch = getch()
    # catch Ctrl-C, Ctrl-D to quit
    if ch == '\x03':
        sys.stdout.write('^C')
        break
    elif ch == '\x04':
        sys.stdout.write('^D\n')
        break
    
    # catch escapes
    elif ch == ESC:
        while getch() != '\x0d':
            pass
        sys.stdout.write('')

    # catch backspace, suppr and other unneeded keystrokes
    elif ch in USELESS_KEYS.values() + OTHER_KEYS: #ESCAPE_SEQUENCES:
        pass
    # catch newline/return
    elif ch == '\x0d':
        sys.stdout.write('\n')
        writelineno()
        #lineno += 1
    else:
        sys.stdout.write(ch)
