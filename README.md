
> What's done cannot be undone. -- _Lady Macbeth_

This repository tries to implement the only relevant text editor; a text editor
of many names.  One calls it *The Ultimate Editor*, *The Only Useful Editor* or
modestly *The Editor*.  It has also be named *The Can't-Go-Back Editor*, *The
There-Is-No-Going-Back Editor*, or the
*[Ratchet](https://en.wikipedia.org/wiki/Ratchet_(device)) Editor*.

# This is an editor where you can't go back. 

Each typed letter is engraved forever. As each letter is typed, the cursor
moves forward, as does the inexorable wheel of time. Backspaces, arrows and
other desperate attempts at Escape will miserably fail.

# Currently

DO NOT INSTALL. This is not ready yet. Although this is still experimental,
there is no big risk using it in your console, these versions may lack features
but work.

## Python Implementation

With and without the `curses` library.

## C++ attempt with `ncurses`.

Compile with:

    g++ TheEditor.cpp -o TheEditor -lncurses


# CREDITS

For the python parts, I copied portions of code from:

* This [stackoverflow question](http://stackoverflow.com/a/21659588/4614641)
* Magmax's [python-readchar](https://github.com/magmax/python-readchar) module

# LICENCE

This code is logically licensed under the [WTFPL -- Do What the Fuck You Want to
Public License](http://www.wtfpl.net/).

