"""Chat story module.
"""

import curses


class ChatStory:
    def __init__(self, title, desc):
        """Initialize self. See help(type(self)) for accurate signature.
        """

        self._title = title
        self._desc = desc

        self._screen = None
        self.__scrbuf__ = {}   # screen buffer

        self.__elems__ = []

    def _prestart(self, screen):
        """Set up screen properties.
        """

        self._screen = screen

        curses.curs_set(0)

        self.__start__()

    def __getscr__(self):
        """Return the screen used to display contents.
        """

        return self._screen

    def __update__(self, buffer):
        """Update the chat story screen.
        """

        strip_buf = buffer.strip()
        buf = strip_buf.split('\n')

        length = len(buf)
        y, _ = self._screen.getyx()

        for i in range(length):
            y += 1
            self._scrbuf += [buf[i]]
            self._screen.addstr(y, 0, buf[i])
            self._getline()

    def _getline(self, buffer):
        """Get line of input from a prompt panel.
        """

        s = ''
        i = 0

        while True:
            ch = self._screen.getch()
            if ch == curses.KEY_ENTER:
                return i
            elif ch == curses.KEY_BACKSPACE:
                pass

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
