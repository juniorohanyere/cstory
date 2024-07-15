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

    def _prestart(self, screen):
        """Set up screen properties.
        """

        self._screen = screen

        curses.curs_set(0)

        self.__start__()

    def __start__(self):
        """Entry point for a user program, called by _prestart method.
        """

    def title(self):
        """Return the title of the chat story.
        """

        return (self._title)

    def description(self):
        """Return the description of the chat story.
        """

        return self._desc

    def run(self):
        """Run the Chat story application.
        """

        curses.wrapper(self._prestart)
