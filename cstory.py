"""Chat story module.
"""

import curses
import sys


class ChatStory:
    def __init__(self, title, desc):
        """Initialize self. See help(type(self)) for accurate signature.
        """

        self._title = title
        self._desc = desc

        self._stdscr = None
        self._pmtscr = None

        self._scrbuf = []   # screen buffer

        self.__elems__ = []

    def _prestart(self, stdscr):
        """Set up screen properties.
        """

        self._stdscr = stdscr
        a = ''
        curses.curs_set(0)

        y, x = self._stdscr.getmaxyx()
        # create a prompt screen
        self._pmtscr = self._stdscr.derwin(1, x, y - 1, 0)
        self._pmtscr.keypad(True)

        self.__start__()

    def __getscr__(self):
        """Return the screen used to display contents.
        """

        return self._stdscr

    def __update__(self, buffer):
        """Update the chat story screen.
        """

        line = ''

        length = len(buffer)
        y, _ = self._stdscr.getyx()

        for i in range(length):
            y += 1
            self._scrbuf += [buffer[i]]
            self._stdscr.addstr(y, 0, buffer[i][0], buffer[i][1])
            self._stdscr.refresh()

            self._pmtscr.addstr('$ ', curses.A_BOLD)
            flag = self._getline(line)
            self._pmtscr.erase()

            if flag == -1:
                sys.exit()

    def _getline(self, buffer):
        """Get line of input from a prompt panel.
        """

        i = 0
        curses.curs_set(1)

        while True:
            ch = self._pmtscr.getch()
            s = chr(ch)

            if ch == ord('\n'):
                break
            elif ch == ord('\b'):
                y, x = self._pmtscr.getyx()
                if x > 2:
                    self._pmtscr.move(y, x - 1)
                    self._pmtscr.clrtoeol()

                    buffer = buffer[:-1]
            elif ch == 4:
                return -1
            else:
                self._pmtscr.addstr(s)
                self._pmtscr.refresh()
                buffer += s
                i += 1

        curses.curs_set(0)

        return i

    def __start__(self):
        """Entry point for a user program, called by _prestart method.
        """

    def get_title(self):
        """Return the title of the chat story.
        """

        return (self._title)

    def get_desc(self):
        """Return the description of the chat story.
        """

        return self._desc

    def get_elems(self):
        """Get the elements of the chat story.
        """

        return self._elems

    def run(self):
        """Run the Chat story application.
        """

        curses.wrapper(self._prestart)
