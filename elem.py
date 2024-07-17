"""Create a new element.
"""

import curses


class Element:
    """Create a new element for sending messages to the chat story screen.
    """

    def __init__(self, cs, dname=None, fname=None, lname=None):
        """Initialize self. See help(type(self)) for accurate signature.

        Args:
            cs (obj): a ChatStory object.
            dname (str): the display name of the element.
            fname (str): the first name of the element.
            lname (str): the last name of the element.
        """

        self._cs = cs

        self._dname = dname
        self._fname = fname
        self._lname = lname

        # add the new element to the list of elements
        self._cs.__elems__ += [self]

    def getnames(self):
        """Return the names of the element as a tuple object.
        """

        return (self._dname, self._fname, self._lname)

    def echo(self, tag=None, msg=''):
        """Post a message to the screen.
        """

        buffer = [(self._dname, curses.A_BOLD)]
        buffer += [(msg, curses.A_NORMAL)]
        buffer += [('', curses.A_NORMAL)]

        self._cs.__update__(buffer)
