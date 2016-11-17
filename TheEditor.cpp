#include <string.h>
#include <stdio.h>
#include <ncurses.h>


/* writelineno () {	
   }
*/

int main ()
{
	int lineno = 1;
	char* lineno_str = new char[4];
	int c;
	initscr();			/* Start curses mode 		  */
	printw("This is the SINGLE USEFUL EDITOR. ");
	printw("When you're here, you can't go back\n");
	refresh();			/* Print it on to the real screen */
	keypad(stdscr, TRUE);
	noecho();
	sprintf(lineno_str, "%3d ", lineno++);
	printw(lineno_str);
	while (1) {
		c=getch();
		// Catch Ctrl-D
		if (c == 4) {
			break;
		// Catch return
		} else if (c == 10 || c == 13 || c == 343) {
			printw("\n");
			sprintf(lineno_str, "%3d ", lineno++);
			printw(lineno_str);
		// Catch printable characters
		} else if (64 < c < 256) {
			addch(c);
		}
		//refresh();
	}
	endwin();			/* End curses mode		  */

	return 0;
}
